var latest_version_directory = "data/v18.3",
	prev_version_directory = "data/v17.3";
/* Standard ACIS data acquisition
----------------------------------------------------------*/
function postSuccess(results, cbf) {
	$("#progressbar").hide();
	if (!results) {
		("No results for request");alert
	} else if (results.error) {
		alert(results.error);
	} else {
		cbf(results);
	}
}
function postError() {
	$("#progressbar").hide();
	alert("Error processing request; please try again");
}
function postResults(input_params, process, cbf) {
	var xdr, args, results,
		url = "https://data.rcc-acis.org" + process;
	if (window.XDomainRequest) {
		xdr = new XDomainRequest();
		xdr.open("GET", url + "?params=" + JSON.stringify(input_params));
		xdr.onload = function () {
			results = JSON.parse(xdr.responseText);
			postSuccess(results, cbf);
		};
		xdr.onerror = postError;
		xdr.onprogress = function () { };
		xdr.ontimeout = function () { };
		setTimeout(function () {
			xdr.send();
		}, 0);
	} else {
		args = {params: JSON.stringify(input_params), output: "json"};
		$.ajax(url, {
			type: 'POST',
			data: args,
			dataType: 'json',
			crossDamain: true,
			success: function (results) { postSuccess(results, cbf); },
			error: postError
		});
	}
}
/* End of data acquisition
----------------------------------------------------------*/
function urlopts() {
	var i, sa, pobj = {},
		validVariables = [
			"himaxt", "lomaxt", "himint", "lomint", "hipcpn",
			"archivehimaxt", "archivelomaxt", "archivehimint",
			"archivelomint", "archivehipcpn","changes",
			"covmaxt", "covmint", "covpcpn", "thread"
		],
		params = window.location.search.slice(1),
		arr = params.split('&');
	for (i = 0; i < arr.length; i += 1) {
		sa = arr[i].split('=');
		if ((sa[0] === 'thr_id' && (sa[1].length === 6 || sa[1].length === 8)) ||
			(sa[0] === 'variable' && $.inArray(sa[1].toLowerCase(), validVariables) >= 0)) {
			pobj[sa[0]] = sa[1];
		}
	}
	return pobj;
}

function fixTraces(results) {
	var i, data, ymd, syr, eyr, input_params,
		sr = $("#selected_report").text(),
		vdr = results.meta.valid_daterange[0],
		isLeap = function(yr) {
			return ((yr % 4 === 0) && (yr % 100 !== 0)) || (yr % 400 === 0);
		},
		processDay = function(dly_results) {
			var j, rn, date, prcp, ymd, newval, newText, nxtval,
				flgyr = [],
				zeroyr = [],
				rest = [],
				// Create an array containing just the results for February 29, if any.
				feb29s = $.grep(dly_results.data, function(v, i) {
    				return v[0].search('-02-29') > 0;
				});
			//When requesting Feb 29 from ACIS WS, we get back the last day of February every year.
			// To get around this, first check to see if there were any Feb 29ths in the results. 
			// If there were, then Feb 29 must have been requested and the grep'd array will be used.
			if (feb29s.length) {
				dly_results.data = feb29s;
			}				
			// save all years with zero/trace/nonzero separately, then merge
			for (j = dly_results.data.length - 1; j >= 0; j -= 1) {
				date = dly_results.data[j][0];
				prcp = dly_results.data[j][1];
				if (prcp === "T") {
					flgyr.push([prcp, date]);
				} else if (prcp === "0.00") {
					zeroyr.push([prcp, date]);
				} else if (prcp != "M") {
					rest.push([prcp, date]); //order of these is irrelevant; just need to know number of nono-zero
				}
			}
			$.merge($.merge(rest, flgyr), zeroyr);
			for (rn = 0; rn <= 2; rn +=1) {
				newval = rest.shift();
				if (newval[0] === "0.00" || newval[0] === "T") {
					newText = (newval[0] === 'T' ? 'Trace' : newval[0]) + ' in ' + newval[1].slice(0, 4);
					ymd = newval[1].split("-");
					if (rn === 2) {
						nxtval = rest.shift();
						if (nxtval[0] === newval[0]) {
							newText += "+";
						}
					}
					$("#results_table tbody tr td").filter(function() {
						return $(this).text() === parseInt(ymd[1]) + "/" + parseInt(ymd[2]);
					}).closest("tr").find("td").eq(rn + 1).text(newText);
				}
			}
		};
	if (sr.search("precipitation") >= 0) {
		for (i = 0; i < 366; i += 1) {
			data = results.smry[0][i];
			if (data[2][0] === "0.00" || data[2][0] === "T") {
				ymd = data[0][1].split("-");
				syr = parseInt(vdr[0].split("-")[0]);
				eyr = parseInt(vdr[1].split("-")[0]);
				if (parseInt(ymd[1]) === 2 && parseInt(ymd[2]) === 29) {
					while (!isLeap(syr)) {
						syr -= 1;
					}
					while (!isLeap(eyr)) {
						eyr += 1;
					}
				}
				input_params = {
					sid: $("#thr_id").val(),
					sdate: syr.toString() + "-" + ymd[1] + "-" + ymd[2],
					edate: eyr.toString() + "-" + ymd[1] + "-" + ymd[2],
					elems: [{
						name: "pcpn",
						interval: [1, 0, 0],
						duration: 1
					}],
					meta: []
				};
				postResults(input_params, "/StnData", processDay);
			}
		}
	}
}

function addGraph(grfdata, ytitle) {
	$("#results_area").append('<div id="chart-container"></div>');
	Highcharts.chart('chart-container', {
        chart: {
            type: 'columnrange',
            inverted: true,
            zoomType: 'xy',
            spacingBottom: 20,
            borderWidth: 1
        },
        title: {
            text: 'Range Between 1st and 3rd Record Values',
            style: {"fontSize": "14px"}
        },
        subtitle: {
            text: 'Click and drag to zoom in'
        },
		credits: {
			text: "Powered by ACIS",
			href: "https://www.rcc-acis.org"
		},
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: {
				day: "%b %e",
				week: "%b %e",
				month: "%b %e"
            },
            gridLineWidth: 1,
            showLastLabel: false
        },
        yAxis: {
            title: {
                text: ytitle
            },
            floor: ytitle.search("precipitation") >= 0 ? 0 : null
        },
        legend: {
            enabled: false
        },
        tooltip: {
        	dateTimeLabelFormats: {
				day: "%b %e",
				week: "%b %e",
				month: "%b %e"
            },
            valueDecimals: ytitle.search("precipitation") >= 0 ? 2 : 0,
            formatter: function () {
				var low = ytitle.search("temperature") >= 0 ? Math.round(this.point.low) : this.point.low, 
					high = ytitle.search("temperature") >= 0 ? Math.round(this.point.high) : this.point.high;
//				return 'Range of records for ' + Highcharts.dateFormat('%b %e', new Date(this.x)) + ': ' + (this.point.low === 0.001 ? "Trace" : this.point.low) + ' to ' + (this.point.high === 0.001 ? "Trace" : this.point.high);
				return 'Range of records for ' + Highcharts.dateFormat('%b %e', new Date(this.x)) + ': ' + low + ' to ' + high;
            }
        },
        series: [{
            name: 'Range of records',
            data: grfdata,
            pointStart: Date.UTC(2016, 0, 1),
            pointInterval: 24 * 3600 * 1000 // one day
        }]
    });
}

function addToGraphSeries(data, graphSeriesData, varhead) {
	var data0 = data.length > 0 ? data[0][0] : null,
		data1 = data.length > 1 ? data[1][0] : null,
		data2 = data.length > 2 ? data[2][0] : null,
		startval = data0,
		endval = data2 || data1 || data0;
	if (!startval) {
		graphSeriesData.push([null,null]);
	} else if (startval === endval && varhead.search("temperature") >= 0) {
		if (varhead.search("Highest") >= 0) {
			graphSeriesData.push([parseFloat(startval) + 0.2, parseFloat(endval) - 0.2]);
		} else {
			graphSeriesData.push([parseFloat(startval) - 0.2, parseFloat(endval) + 0.2]);
		}
	} else {
		// plot traces as zero
		startval = varhead.search("precipitation") >= 0 && (startval === "T" || startval === "Trace") ? 0.00 : parseFloat(startval);
		endval = varhead.search("precipitation") >= 0 && (endval === "T" || endval === "Trace") ? 0.00 : parseFloat(endval);
		graphSeriesData.push([startval, endval]);
	}
	return graphSeriesData;
}

function displayRecords(results) {
	var i, data, ymd, row, background, more, data0, data1, data2, data3,
		haveMore = false,
		meta = results.meta,
		sr = $("#selected_report").text(),
		varhead = sr + (sr.search('temperature') >= 0 ? " (degrees F)" : " (inches)"),
		graphSeriesData = [];
	$("#results_area").append('<table id="results_table" class="abreast"><caption></caption><thead></thead><tbody></tbody><tfoot></tfoot></table>');
	$("#results_table caption").append(meta.name + ', ' + meta.state +
		'<br /><span class="subcaption">Period of record: ' + meta.valid_daterange[0][0] + ' through ' + meta.valid_daterange[0][1] + '</span>');
	$("#results_table thead").append('<tr><th rowspan=2>Date<th colspan=3>' + varhead + '</tr>' +
		'<tr><th>Top Record <th>2nd Record <th>3rd Record</tr>');
	for (i = 0; i < 366; i += 1) {
		data = results.smry[0][i];
		if (data.length > 0) {
			data0 = data.length > 0 ? data[0] : ["-","   -"];
			data1 = data.length > 1 ? data[1] : ["-","   -"];
			data2 = data.length > 2 ? data[2] : ["-","   -"];
			data3 = data.length > 3 ? data[3] : ["-","   -"];
			ymd = data0[1].split("-");
			background = parseInt(ymd[1])%2 === 1 ? "WhiteSmoke" : "white";
			if (data2[0] !== "-" && data2[0] === data3[0]) {
				more = '+';
				haveMore = true;
			} else {
				more = '';
			}
			row = '<tr style="background-color: ' + background + ';"><td>' + parseInt(ymd[1]) + '/' + parseInt(ymd[2]);
			row += '<td>' + (data0[0] === 'T' || data0[0] === '0.00' ? 'processing' : (data0[0]) + ' in ' + data0[1].slice(0, 4));
			row += '<td>' + (data1[0] === 'T' || data1[0] === '0.00' ? 'processing' : (data1[0]) + ' in ' + data1[1].slice(0, 4));
			row += '<td>' + (data2[0] === 'T' || data2[0] === '0.00' ? 'processing' : (data2[0]) + ' in ' + data2[1].slice(0, 4) + more) + '</tr>';
			$("#results_table tbody").append(row);
		}
		graphSeriesData = addToGraphSeries(data, graphSeriesData, varhead);
	}
	if (haveMore) {
		$("#results_area tfoot").append('<tr><td colspan=4>+ indicates same value also occurred in a previous year.</tr>');
	}
	fixTraces(results);
	addGraph(graphSeriesData, varhead);
}

function displayCoverage(results) {
	var i, m, mvals, cmcnt, color, trow, year,
		meta = results.meta,
		data = results.data,
		varhead = $("#selected_report").text().replace("data coverage", " - Missing days per month"),
		daysInMonth = function(yr, mn) {
			return new Date(parseInt(yr), mn + 1, 0).getDate();
		};
	$("#results_area").append('<table id="results_table" class="coverage_table"><caption></caption><thead></thead><tbody></tbody></table>');
	$("#results_table caption").append(meta.name + ', ' + meta.state);
	$("#results_table thead").append('<tr><th rowspan=2>Year<th colspan=12>' + varhead + '</tr>' +
		'<tr><th>Jan<th>Feb<th>Mar<th>Apr<th>May<th>Jun<th>Jul<th>Aug<th>Sep<th>Oct<th>Nov<th>Dec</tr>');
	for (i = 0; i < data.length; i += 1) {
		year = data[i][0];
		mvals = data[i][1];
		trow = "";
		for (m = 0; m < 12; m += 1) {
			if (mvals[m] === "M") {
				cmcnt = daysInMonth(year, m);
				color = "red";
			} else if (mvals[m][1] === 0) {
				cmcnt = "-";
				color = "green";
			} else {
				cmcnt = mvals[m][1];
				color = mvals[m][1] === daysInMonth(year, m) ? "red" : "yellow";
			}
			trow += '<td style="background-color:' + color + ';">' + cmcnt + '</td>';
		}
		$("#results_table tbody").append('<tr><td>' + year + '</td>' + trow + '</tr>');
	}
}

function displayArchiveRecords(results, version, creationdate) {
	var i, data, ymd, row, background, more,
		haveMore = false,
		tval = $("#report").val(),
		station = $("#selected_station").text() !== "None selected" ? $("#selected_station").text() : $("#thr_id").find(".ui-menu-item[data-value='" + $("#thr_id").val() + "']").text(),
		staparts = station.split(" - "),
		sr = $("#selected_report").text(),
		varhead = sr + (sr.search('temperature') >= 0 ? " (degrees F)" : " (inches)"),
		graphSeriesData = [];
	$("#results_area").append('<table id="results_table" class="abreast"><caption></caption><thead></thead><tbody></tbody><tfoot></tfoot></table>');
	$("#results_table caption").append(staparts[1] + ' Area, ' + staparts[0] +
		'<br /><span class="subcaption">Version: ' + version + ' (created ' + creationdate + ')</span>' +
		'<br /><span class="subcaption">Period of record: ' + results.start_yr + ' through ' + results.end_yr + '</span>');
	$("#results_table thead").append('<tr><th rowspan=2>Date<th colspan=3>' + varhead + '</tr>' +
		'<tr><th>Top Record <th>2nd Record <th>3rd Record</tr>');
	for (i = 0; i < 366; i += 1) {
		data = results.data[i];
		ymd = data[0][1].split("-");
		background = parseInt(ymd[1])%2 === 1 ? "WhiteSmoke" : "white";
		if (data[3]) {
			more = '+';
			haveMore = true;
		} else {
			more = '';
		}
		if (tval === "archivehipcpn") {
			data[0][0] = data[0][0] === -1 ? 'Trace' : data[0][0].toFixed(2);
			data[1][0] = data[1][0] === -1 ? 'Trace' : data[1][0].toFixed(2);
			data[2][0] = data[2][0] === -1 ? 'Trace' : data[2][0].toFixed(2);
		}
		row = '<tr style="background-color: ' + background + ';"><td>' + parseInt(ymd[1]) + '/' + parseInt(ymd[2]);
		row += '<td>' + data[0][0] + ' in ' + ymd[0];
		row += '<td>' + data[1][0] + ' in ' + data[1][1].slice(0, 4);
		row += '<td>' + data[2][0] + ' in ' + data[2][1].slice(0, 4) + more + '</tr>';
		$("#results_table tbody").append(row);
		graphSeriesData = addToGraphSeries(data, graphSeriesData, varhead);
	}
	if (haveMore) {
		$("#results_area tfoot").append('<tr><td colspan=4>+ indicates same value also occurred in a previous year.</tr>');
	}
	addGraph(graphSeriesData, varhead);
}

function initChangeTable(v0, v1) {
	var station = $("#selected_station").text() !== "None selected" ? $("#selected_station").text() : $("#thr_id").find(".ui-menu-item[data-value='" + $("#thr_id").val() + "']").text(),
		staparts = station.split(" - "),
		sections= {
			himaxt: 'Highest maximum temperature (deg F)',
			lomint: 'Lowest minimum temperature (deg F)',
			lomaxt: 'Lowest maximum temperature (deg F)',
			himint: 'Highest minimum temperature (deg F)',
			hipcpn: 'Highest precipitation (inches)'
		};
	$("#results_area").append('<table id="results_table" style="display:none;"><caption></caption></table>');
	$("#results_table caption").append('ThreadEx Record Changes From Version ' +
		v0 + ' to ' + (v1 !== "Current" ? "Version " : "") + v1 +
		' for ' + staparts[1] + ' Area, ' + staparts[0] +
		'<br /><span class="subcaption">Current' + (v1 !== "Current" ? ' Version ' + v1 + '; ' : "; ") + 'Period of record: <span id="lsy"></span> - <span id="ley"></span></span>' +
		'<br /><span class="subcaption">Previous Version: ' + v0 + '; Period of record: <span id="psy"></span> - <span id="pey"></span></span>');
	$.each(sections, function(tvar, varhead) {
		$("#results_table").append('<tbody id="' + tvar + '"></tbody>');
		$("#" + tvar).append('<tr style="background-color:WhiteSmoke;"><th colspan=5>' + varhead + '</tr>');
	});
}

function displayChanges(chvar, changes, yr_arr) {
	var i, tvar, latest_value, latest_date, prev_value, prev_date, vcolor, dcolor;
	$("#psy").text(yr_arr[0]);
	$("#pey").text(yr_arr[1]);
	$("#lsy").text(yr_arr[2]);
	$("#ley").text(yr_arr[3]);
	$("#results_table").show();
	if (changes.length === 0) {
		$("#" + chvar).append('<tr><td colspan=5>None</tr>');
	} else {
		$("#" + chvar).append('<tr style="background-color:WhiteSmoke;"><th>Date<th>Current Record <th>Year <th>Previous Record <th>Year</tr>');
		for (i = 0; i < changes.length; i += 1) {
			tvar = changes[i][0];
			latest_date = changes[i][2];
			prev_date = changes[i][4];
			if (tvar === 'hipcpn') {
				latest_value = changes[i][1] === 'Trace' ? 'Trace' : changes[i][1].toFixed(2);
				prev_value = changes[i][3] === 'Trace' ? 'Trace' : changes[i][3].toFixed(2);
			} else {
				latest_value = changes[i][1];
				prev_value = changes[i][3];
			}
			vcolor = latest_value !== prev_value ? "red" : "black";
			dcolor = latest_value === prev_value ? "red" : "black";
			$("#" + tvar).append('<tr><td>' + parseInt(latest_date[1]) + '/' + parseInt(latest_date[2]) +
				'<td style="color:' + vcolor + ';">' + latest_value +
				'<td style="color:' + dcolor + ';">' + latest_date[0] +
				'<td>' + prev_value + '<td>' + prev_date[0] + '</tr>');
		}
	}
	if (chvar === 'hipcpn') {
		$("#progressbar").hide();
	}
}

function displayThreads(results) {
	var i,
		station = $("#selected_station").text() !== "None selected" ? $("#selected_station").text() : $("#thr_id").find(".ui-menu-item[data-value='" + $("#thr_id").val() + "']").text(),
		staparts = station.split(" - ");
	$("#results_area").append('<table id="results_table" class="threads_table"><caption></caption><thead></thead><tbody></tbody></table>');
	$("#results_table caption").append('Station Thread for ' + staparts[1] + ' Area, ' + staparts[0]);
	$("#results_table thead").append('<tr><th><th>Name<th>Period in Thread</tr>');
	for (i = 0; i < results.length; i += 1) {
		$("#results_table tbody").append('<tr><td>' + (i + 1) + '<td>' + results[i].name + '<td>' + results[i].period + '</tr>');
	}
}

function getCoverage() {
	var input_params = {
		sid: $("#thr_id").val(),
		sdate: "por",
		edate: "por",
		elems: [{
			name: $("#report").val().slice(-4),
			interval: "mly",
			duration: "mly",
			reduce: {
				reduce: "cnt_ge_-999",
				add: "mcnt"
			},
			groupby: ["year"]
		}],
		meta: ["name", "state", "valid_daterange"]
	};
	postResults(input_params, "/StnData", displayCoverage);
}

function getRecords() {
	var input_params = {
		sid: $("#thr_id").val(),
		sdate: "por",
		edate: "por",
		elems: [{
			name: $("#report").val().slice(-4),
			interval: "dly",
			duration: "dly",
			smry: {
				reduce: $("#report").val().slice(-6,-4) === "hi" ? "max" : "min",
				add: "date",
				n: 4
			},
			smry_only: 1,
			groupby: ["year","01-01","12-31"]
		}],
		meta: ["name", "state", "valid_daterange"]
	};
	postResults(input_params, "/StnData", displayRecords);
}

function getArchiveRecords() {
	var sid = $("#thr_id").val(),
		report = $("#report").val().replace('archive', '');
	$.get("./" + latest_version_directory + "/" + report + "_records.json", function (jres) {
		$("#progressbar").hide();
		if (jres.hasOwnProperty(sid)) {
			displayArchiveRecords(jres[sid], jres.version, jres.creationdate);
		} else {
			alert("No data available");
		}
	});
}

function getChanges() {
	var sid = $("#thr_id").val(),
		latest_start_yr = 9999, latest_end_yr = 0, prev_start_yr = 9999, prev_end_yr = 0;
	initChangeTable(prev_version_directory.substr(6), latest_version_directory.substr(6));
	$.each(['himaxt', 'lomint', 'lomaxt', 'himint', 'hipcpn'], function(j, tvar) {
		var i, latest_results, latest_value, latest_date, prev_results, prev_value, prev_date,
			changes = [], yr_arr = [];
		$.get("./" + latest_version_directory + "/" + tvar + "_records.json", function (jlres) {
			if (jlres.hasOwnProperty(sid)) {
				latest_results = jlres[sid];
				latest_start_yr = latest_results.start_yr ? Math.min(latest_start_yr, parseInt(latest_results.start_yr)) : latest_start_yr;
				latest_end_yr = latest_results.end_yr ? Math.max(latest_end_yr, parseInt(latest_results.end_yr)) : latest_end_yr;
				$.get("./" + prev_version_directory + "/" + tvar + "_records.json", function (jpres) {
					if (jpres.hasOwnProperty(sid)) {
						prev_results = jpres[sid];
						prev_start_yr = Math.min(prev_start_yr, prev_results.start_yr);
						prev_end_yr = Math.max(prev_end_yr, prev_results.end_yr);
						for (i = 0; i < 366; i += 1) {
							latest_value = latest_results.data[i][0][0];
							if (tvar === 'hipcpn' && latest_value === -1) {
								latest_value = 'Trace';
							}
							latest_date = latest_results.data[i][0][1].split("-");
							prev_value = prev_results.data[i][0][0];
							if (tvar === 'hipcpn' && prev_value === -1) {
								prev_value = 'Trace';
							}
							prev_date = prev_results.data[i][0][1].split("-");
							if ((latest_value !== prev_value) || (latest_date[0] !== prev_date[0])) {
								changes.push([tvar, latest_value, latest_date, prev_value, prev_date]);
							}
						}
					} else {
						prev_start_yr = "-";
						prev_end_yr = "-";
					}
					yr_arr = [prev_start_yr, prev_end_yr, latest_start_yr, latest_end_yr];
					displayChanges(tvar, changes, yr_arr);
				});
			}
		});
	});
}

function getRecentChanges() {
	var latest_start_yr = 9999, latest_end_yr = 0, crnt_start_yr = 9999, crnt_end_yr = 0,
		sid = $("#thr_id").val(),
		input_params = {
			sid: sid,
			sdate: "por",
			edate: "por",
			elems: [{
				name: null,
				interval: "dly",
				duration: "dly",
				smry: {
					reduce: null,
					add: "date",
				},
				smry_only: 1,
				groupby: ["year","01-01","12-31"]
			}],
			meta: ["name", "state", "valid_daterange"]
		};
	initChangeTable(latest_version_directory.substr(6), "Current");
	$.each(['himaxt', 'lomint', 'lomaxt', 'himint', 'hipcpn'], function(j, tvar) {
		var i, latest_results, latest_value, latest_date,crnt_value, crnt_date,
			changes = [], yr_arr = [];
		$.get("./" + latest_version_directory + "/" + tvar + "_records.json", function (jlres) {
			if (jlres.hasOwnProperty(sid)) {
				latest_results = jlres[sid];
				latest_start_yr = Math.min(latest_start_yr, parseInt(latest_results.start_yr));
				latest_end_yr = Math.max(latest_end_yr, parseInt(latest_results.end_yr));
				input_params.elems[0].name = tvar.slice(-4);
				input_params.elems[0].smry.reduce = tvar.slice(-6,-4) === "hi" ? "max" : "min";
				postResults(input_params, "/StnData", function (crnt_results) {
					var csyr = crnt_results.meta.valid_daterange[0][0].split("-"),
						ceyr = crnt_results.meta.valid_daterange[0][1].split("-");
					crnt_start_yr = Math.min(crnt_start_yr, parseInt(csyr[0]));
					crnt_end_yr = Math.max(crnt_end_yr, parseInt(ceyr[0]));
					for (i = 0; i < 366; i += 1) {
						latest_value = latest_results.data[i][0][0];
						if (tvar === 'hipcpn' && latest_value === -1) {
							latest_value = 'Trace';
						}
						latest_date = latest_results.data[i][0][1].split("-");
						if (tvar === 'hipcpn' && crnt_results.smry[0][i][0] === "T") {
							crnt_value = 'Trace';
						} else {
							crnt_value = parseFloat(crnt_results.smry[0][i][0]);
						}
						crnt_date = crnt_results.smry[0][i][1].split("-");
						if ((latest_value !== crnt_value) || (latest_date[0] !== crnt_date[0])) {
							changes.push([tvar, crnt_value, crnt_date, latest_value, latest_date]);
						}
					}
					yr_arr = [latest_start_yr, latest_end_yr, crnt_start_yr, crnt_end_yr];
					displayChanges(tvar, changes, yr_arr);
				});
			};
		});
	});
}

function getThreads() {
	var sid = $("#thr_id").val().replace("thr","");
	$.get("./data/threads_dict.json", function (jres) {
		$("#progressbar").hide();
		displayThreads(jres[sid]);
	});
}

$(function() {
	var menuselect = function(event, ui) {
		var mnb = $(this).prev("button");
		if (ui.item.attr("class").search("noselect") >= 0) {
			$(this).trigger("click");
			return false;
		}
		mnb.show().text(mnb.text().replace("Select","Change"));
		$(this).val(ui.item.data("value")).hide();
		$(this).parent().find("span").html(ui.item.text());
		$("#results_area").empty();
	};
	$("#thr_id").val("BHMthr").menu({
		select: menuselect
	});
	$("#report").val("thread").menu({
		items: "> :not(.ui-widget-header)",
		select: menuselect
	});
	$(".show_menu").button().on("click", function() {
		$(this).next("ul").show();
		$(this).prev("span").empty();
		$(this).hide();
	});
	$("#go").button().on("click", function() {
		var choice = $("#report").val();
		$("#results_area").empty();
		$("#progressbar").show();
		if ($.inArray(choice, ["himaxt", "lomaxt", "himint", "lomint", "hipcpn"]) >= 0) {
			getRecords();
		} else if ($.inArray(choice, ["archivehimaxt", "archivelomaxt", "archivehimint", "archivelomint", "archivehipcpn"]) >= 0) {
			getArchiveRecords();
		} else if (choice === "changes") {
			getChanges();
		} else if (choice === "recentchanges") {
			getRecentChanges();
		} else if ($.inArray(choice, ["covmaxt", "covmint", "covpcpn"]) >= 0) {
			getCoverage();
		} else if (choice === "thread") {
			getThreads();
		} else {
			$("#results_area").append("<p>Selection not implemented</p>");
			$("#progressbar").hide();
		}
	});
	$("#progressbar").progressbar({
		value: false,
		disabled: true
	});
	 $("#info").dialog({
		autoOpen: false,
		modal: true,
		width: $(window).width() * 0.9,
		maxHeight: $(window).height() * 0.9,
		position: {my: "center top", at: "center top", of: $("div.option-container")},
		buttons: [{
			text: "Close",
			click: function() {
				$(this).dialog("close");
			}
		}]
	});
	$("#about").button().on("click", function() {
		$("#info").load("./help/about.html").dialog('option', "title", "Project Information").dialog("open");
	});
	$("#report_info").on("click", function() {
		$("#info").load("./help/report_help.html").dialog('option', "title", "Report Options").dialog("open");
	});
	$.ui.dialog.prototype._focusTabbable = $.noop;
	var urlOptions = urlopts();
	if ('thr_id' in urlOptions && 'variable' in urlOptions) {
		urlOptions.thr_id = urlOptions.thr_id.substr(0,urlOptions.thr_id.length - 3).toUpperCase() + urlOptions.thr_id.substr(urlOptions.thr_id.length - 3).toLowerCase();
		$("#thr_id").val(urlOptions.thr_id);
		$("#selected_station").text($("#thr_id li[data-value=" + urlOptions.thr_id + "]").text());
		urlOptions.variable = urlOptions.variable.toLowerCase();
		$("#report").val(urlOptions.variable);
		$("#selected_report").text($("#report li[data-value=" + urlOptions.variable + "]").text());
		$("#go").trigger("click");
	}
})
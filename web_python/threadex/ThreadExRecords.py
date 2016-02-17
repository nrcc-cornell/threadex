from bsddb import hashopen
from cPickle import loads
from print_exception import print_exception
import ThreadExRecords_io

def process_records (request):
	from threads_dict import threads_dict
	try:
		if request.form and request.form.has_key('variable') and request.form.has_key('thr_id'):
			variable = request.form['variable']
			if variable.find('Select') != -1:
				return ThreadExRecords_io.bad_input('Select a variable from the menu.')
			elif variable in ['maxt','mint','pcpn']:
				return process_coverage(request)
			elif variable == 'changes':
				return process_changes(request)
				
			hilo = variable[0:3]
			element = variable[3:7]
			thr_id = request.form['thr_id']
			call = thr_id[0:3]

			if threads_dict.has_key(call):
				thr_list = []
				threads = threads_dict[call]
				for line in threads:
					seq,coop,wban,icao,name,por,pot = line.split('|')
					if coop.find('-') == -1:
						station = coop.strip()
						srchmthd = 'COOPID'
					elif wban.find('-') == -1:
						station = wban.strip()
						srchmthd = 'WBAN'
					elif icao.find('-') == -1:
						station = icao.strip()
						srchmthd = 'CallSign'
					thr_list.append((seq,station,srchmthd,name,pot))
			else:
				return ThreadExRecords_io.bad_input('Select a valid station.')
				
			if variable == 'thread':
				return process_threads(request,thr_list)
			elif variable in ['-himaxt','-lomaxt','-himint','-lomint','-hipcpn']:
				records_dict = hashopen('/Users/keith/Sites/data/threaded_records.db','r')
				if records_dict.has_key(thr_id):
					thr_recs = loads(records_dict[thr_id])
					records = thr_recs[element][hilo]
					name = '%s, %s' % (thr_recs['name'],thr_recs['state'])
					start_yr, end_yr = thr_recs[element]['start_yr'],thr_recs[element]['end_yr']
					records_dict.close()
					return ThreadExRecords_io.display_records(thr_list, records, name, element, hilo, thr_id, start_yr, end_yr)
				else:
					records_dict.close()
					return ThreadExRecords_io.bad_input('Select a valid station.')
			else:
				return ThreadExRecords_io.bad_input(None)
		else:
			return ThreadExRecords_io.bad_input(None)
	except:
		print_exception()
		return ThreadExRecords_io.bad_input(None)

def process_coverage (request):
	try:
		if request.form and request.form.has_key('variable') and request.form.has_key('thr_id'):
			variable = request.form['variable']
			thr_id = request.form['thr_id']
			call = thr_id[0:3]
			coverage_dict = hashopen('/Users/keith/Sites/data/threaded_coverage.db','r')
			if coverage_dict.has_key(thr_id):
				thr_cov = loads(coverage_dict[thr_id])
				coverage = thr_cov[variable]
				name = '%s, %s' % (thr_cov['name'],thr_cov['state'])
				coverage_dict.close()
			else:
				coverage_dict.close()
				return ThreadExRecords_io.bad_input(None)
		else:
			return ThreadExRecords_io.bad_input(None)
	except:
		print_exception()
		return ThreadExRecords_io.bad_input(None)
	return ThreadExRecords_io.display_coverage(coverage, name, variable)

def process_threads (request,threads):
	try:
		thr_id = request.form['thr_id']
		coverage_dict = hashopen('/Users/keith/Sites/data/threaded_coverage.db','r')
		if coverage_dict.has_key(thr_id):
			thr_cov = loads(coverage_dict[thr_id])
			name = '%s, %s' % (thr_cov['name'],thr_cov['state'])
		else:
			name = ''
		coverage_dict.close()
	except:
		print_exception()
		return ThreadExRecords_io.bad_input(None)
	return ThreadExRecords_io.display_thread(threads, name)

#### beginning of process_changes routines	
# get daily ThreadEx temp records
def get_records (thr_id,rn,infile):
	records_dict = {}
	name = ''
	start_yr = 9999
	end_yr = 9999
	por = (9999,9999)
	try:
		thrdx_dict = hashopen(infile,'r')
		if thrdx_dict.has_key(thr_id):
			thr_recs = loads(thrdx_dict[thr_id])
			name = '%s, %s' % (thr_recs['name'],thr_recs['state'])
			start_yr = min(thr_recs['maxt']['start_yr'],thr_recs['mint']['start_yr'])
			end_yr = max(thr_recs['maxt']['end_yr'],thr_recs['mint']['end_yr'])
			por = (start_yr,end_yr)
			for (element,hilo) in [('maxt','-hi'),('mint','-lo'),('maxt','-lo'),('mint','-hi'),('pcpn','-hi')]:
				k = element+hilo
				records = thr_recs[element][hilo]
				reclist = []
				for tt in range(1,60):
					reclist.append((records[tt][rn-1][0],records[tt][rn-1][1]))
				reclist.append((records[366][rn-1][0],records[366][rn-1][1]))
				for tt in range(60,366):
					reclist.append((records[tt][rn-1][0],records[tt][rn-1][1]))
				records_dict[k] = reclist
		thrdx_dict.close()
	except:
		print_exception()
	return records_dict, name, por

def doy_to_date (doy):
	# convert day of year in range 0-365 to month and day
	md = None
	dc = [-1,30,59,90,120,151,181,212,243,273,304,334,365]
	for mn in range(1,len(dc)):
		if doy <= dc[mn]:
			month = mn
			day = doy-dc[mn-1] 
			smd = '%02d/%02d' % (month,day)
			break
	return smd

def process_changes(request):
	try:
		station = request.form['thr_id']

		crnt = '11.0'
		crntfile = '/Users/keith/Sites/data/threaded_records.db'
		prev = '10.1'
		prevfile = '/Users/keith/progs/Threading/Version_10.1/threaded_records.db'
		
	#	process data and send results for output
		crnt_recs, name, crnt_por = get_records (station,1,crntfile)
		prev_recs, name, prev_por = get_records (station,1,prevfile) 
		
		change_dict = {}
		for var in ['maxt-hi','mint-lo','maxt-lo','mint-hi','pcpn-hi']:
			change_list = []
			for dy in range(0,366):
				if abs(crnt_recs[var][dy][0]-prev_recs[var][dy][0]) >= 0.01 or abs(crnt_recs[var][dy][1]-prev_recs[var][dy][1]) >= 0.01:
#				if crnt_recs[var][dy][0] != prev_recs[var][dy][0] or crnt_recs[var][dy][1] != prev_recs[var][dy][1]:
					if var == 'pcpn-hi':
						change_list.append((doy_to_date(dy), "%5.2f"%round(crnt_recs[var][dy][0],2), crnt_recs[var][dy][1], "%5.2f"%round(prev_recs[var][dy][0],2), prev_recs[var][dy][1]))
					else:
						change_list.append((doy_to_date(dy), int(crnt_recs[var][dy][0]), crnt_recs[var][dy][1], int(prev_recs[var][dy][0]), prev_recs[var][dy][1]))
			if len(change_list) > 0:
				change_dict[var] = change_list
		return ThreadExRecords_io.display_changes(crnt,prev,name,crnt_por,prev_por,change_dict)
	except:
		print_exception()
		return ThreadExRecords_io.bad_input(None)


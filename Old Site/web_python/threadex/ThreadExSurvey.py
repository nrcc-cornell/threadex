from print_exception import print_exception

cwa_dict = {'KABQ': ('Albuquerque',
          [('ABQ', 'ALBUQUERQUE', 'NM'),
           ('CAO', 'CLAYTON', 'NM'),
           ('ROW', 'ROSWELL', 'NM')]),
 'KABR': ('Aberdeen', [('ABR', 'ABERDEEN', 'SD')]),
 'KAKQ': ('Wakefield',
          [('ORF', 'NORFOLK', 'VA'),
           ('RIC', 'RICHMOND', 'VA'),
           ('WAL', 'WALLOPS ISLAND', 'VA')]),
 'KALY': ('Albany', [('ALB', 'ALBANY', 'NY')]),
 'KAMA': ('Amarillo', [('AMA', 'AMARILLO', 'TX')]),
 'KAPX': ('Gaylord',
          [('APN', 'ALPENA', 'MI'),
           ('HTL', 'HOUGHTON LAKE', 'MI'),
           ('ANJ', 'SAULT STE. MARIE', 'MI')]),
 'KARX': ('La Crosse',
          [('LSE', 'LA CROSSE', 'WI'), ('RST', 'ROCHESTER', 'MN')]),
 'KBGM': ('Binghamton',
          [('AVP', 'AVOCA', 'PA'),
           ('BGM', 'BINGHAMTON', 'NY'),
           ('SYR', 'SYRACUSE', 'NY')]),
 'KBIS': ('Bismark', [('BIS', 'BISMARCK', 'ND'), ('ISN', 'WILLISTON', 'ND')]),
 'KBMX': ('Birmingham',
          [('BHM', 'BIRMINGHAM ', 'AL'), ('MGM', 'MONTGOMERY', 'AL')]),
 'KBNA': ('Nashville', [('BNA', 'NASHVILLE', 'TN')]),
 'KBOI': ('Boise', [('BOI', 'BOISE', 'ID'), ('BNO', 'BURNS', 'OR')]),
 'KBOX': ('Boston',
          [('BOS', 'BOSTON', 'MA'),
           ('BDL', 'HARTFORD', 'CT'),
           ('MQE', 'MILTON', 'MA'),
           ('PVD', 'PROVIDENCE', 'RI'),
           ('ORH', 'WORCESTER', 'MA')]),
 'KBRO': ('Brownsville', [('BRO', 'BROWNSVILLE', 'TX')]),
 'KBTV': ('Burlington', [('BTV', 'BURLINGTON', 'VT')]),
 'KBUF': ('Buffalo', [('BUF', 'BUFFALO', 'NY'), ('ROC', 'ROCHESTER', 'NY')]),
 'KBYZ': ('Billings', [('BIL', 'BILLINGS', 'MT'), ('SHR', 'SHERIDAN', 'WY')]),
 'KCAE': ('Columbia', [('AGS', 'AUGUSTA', 'GA'), ('CAE', 'COLUMBIA', 'SC')]),
 'KCAR': ('Caibou', [('CAR', 'CARIBOU', 'ME')]),
 'KCHS': ('Charleston',
          [('CHS', 'CHARLESTON', 'SC'), ('SAV', 'SAVANNAH', 'GA')]),
 'KCLE': ('Cleveland',
          [('CAK', 'AKRON', 'OH'),
           ('CLE', 'CLEVELAND', 'OH'),
           ('ERI', 'ERIE', 'PA'),
           ('MFD', 'MANSFIELD', 'OH'),
           ('TOL', 'TOLEDO', 'OH'),
           ('YNG', 'YOUNGSTOWN', 'OH')]),
 'KCRP': ('Corpus Christi',
          [('CRP', 'CORPUS CHRISTI', 'TX'), ('VCT', 'VICTORIA', 'TX')]),
 'KCTP': ('State College',
          [('MDT', 'MIDDLETOWN/HARRISBURG ', 'PA'),
           ('IPT', 'WILLIAMSPORT', 'PA')]),
 'KCYS': ('Cheyenne',
          [('CYS', 'CHEYENNE', 'WY'), ('BFF', 'SCOTTSBLUFF', 'NE')]),
 'KDDC': ('Dodge City', [('DDC', 'DODGE CITY', 'KS')]),
 'KDEN': ('Denver-Boulder', [('DEN', 'DENVER', 'CO')]),
 'KDLH': ('Duluth',
          [('DLH', 'DULUTH', 'MN'), ('INL', 'INTERNATIONAL FALLS', 'MN')]),
 'KDMX': ('Des Moines',
          [('DSM', 'DES MOINES', 'IA'), ('ALO', 'WATERLOO', 'IA')]),
 'KDTX': ('Detroit-Pontiac',
          [('DTW', 'DETROIT', 'MI'), ('FNT', 'FLINT', 'MI')]),
 'KDVN': ('Quad Cities', [('DBQ', 'DUBUQUE', 'IA'), ('MLI', 'MOLINE', 'IL')]),
 'KEAX': ('Kansas City-Pleasant Hill', [('MCI', 'KANSAS CITY', 'MO')]),
 'KEKA': ('Eureka', [('EKA', 'EUREKA', 'CA')]),
 'KELP': ('El Paso', [('ELP', 'EL PASO', 'TX')]),
 'KEWX': ('Austin-San Antonio',
          [('AUS', 'AUSTIN/BERGSTROM', 'TX'),
           ('ATT', 'AUSTIN/CITY', 'TX'),
           ('DRT', 'DEL RIO', 'TX'),
           ('SAT', 'SAN ANTONIO', 'TX')]),
 'KEYW': ('Key West ', [('EYW', 'KEY WEST', 'FL')]),
 'KFFC': ('Peachtree City',
          [('AHN', 'ATHENS', 'GA'),
           ('ATL', 'ATLANTA', 'GA'),
           ('CSG', 'COLUMBUS', 'GA'),
           ('MCN', 'MACON', 'GA')]),
 'KFGF': ('Grand Forks',
          [('FAR', 'FARGO', 'ND'), ('GFK', 'GRAND FORKS', 'ND')]),
 'KFGZ': ('Flagstaff', [('FLG', 'FLAGSTAFF', 'AZ'), ('INW', 'WINSLOW', 'AZ')]),
 'KFSD': ('Sioux Falls',
          [('HON', 'HURON', 'SD'),
           ('SUX', 'SIOUX CITY', 'IA'),
           ('FSD', 'SIOUX FALLS', 'SD')]),
 'KFWD': ('Ft. Worth',
          [('DAL', 'DALLAS', 'TX'),
           ('DFW', 'DALLAS-FORT WORTH', 'TX'),
           ('ACT', 'WACO', 'TX')]),
 'KGGW': ('Glasgow', [('GGW', 'GLASGOW', 'MT')]),
 'KGID': ('Hastings', [('GRI', 'GRAND ISLAND', 'NE')]),
 'KGJT': ('Grand Junction', [('GJT', 'GRAND JUNCTION', 'CO')]),
 'KGLD': ('Goodland', [('GLD', 'GOODLAND', 'KS')]),
 'KGRB': ('Green Bay', [('GRB', 'GREEN BAY', 'WI')]),
 'KGRR': ('Grand Rapids',
          [('GRR', 'GRAND RAPIDS', 'MI'),
           ('LAN', 'LANSING', 'MI'),
           ('MKG', 'MUSKEGON', 'MI')]),
 'KGSP': ('Greenville-Spartanburg',
          [('AVL', 'ASHEVILLE', 'NC'),
           ('CLT', 'CHARLOTTE', 'NC'),
           ('GSP', 'GREER', 'SC')]),
 'KGYX': ('Gray-Portland',
          [('CON', 'CONCORD', 'NH'), ('PWM', 'PORTLAND', 'ME')]),
 'KHGX': ('Houston', [('IAH', 'HOUSTON', 'TX'), ('GLS', 'GALVESTON', 'TX')]),
 'KHLN': ('Honolulu',
          [('ITO', 'HILO', 'HI'),
           ('HNL', 'HONOLULU', 'HI'),
           ('OGG', 'KAHULUI', 'HI'),
           ('LIH', 'LIHUE', 'HI')]),
 'KHNX': ('San Joaquin Valley-Hanford',
          [('BFL', 'BAKERSFIELD', 'CA'), ('FAT', 'FRESNO', 'CA')]),
 'KHUN': ('Huntsville', [('HSV', 'HUNTSVILLE', 'AL')]),
 'KICT': ('Wichita', [('ICT', 'WICHITA', 'KS')]),
 'KILM': ('Wilmington', [('ILM', 'WILMINGTON', 'NC')]),
 'KILN': ('Wilmington',
          [('CMH', 'COLUMBUS', 'OH'),
           ('CVG', 'COVINGTON/CINCINNATI', 'OH'),
           ('DAY', 'DAYTON', 'OH')]),
 'KILX': ('Lincoln', [('PIA', 'PEORIA', 'IL'), ('SPI', 'SPRINGFIELD', 'IL')]),
 'KIND': ('Indianapolis', [('IND', 'INDIANAPOLIS', 'IN')]),
 'KIWX': ('Northen Indiana',
          [('FWA', 'FORT WAYNE', 'IN'), ('SBN', 'SOUTH BEND', 'IN')]),
 'KJAN': ('Jackson', [('JAN', 'JACKSON', 'MS'), ('MEI', 'MERIDIAN', 'MS')]),
 'KJAX': ('Jacksonville',
          [('GNV', 'GAINESVILLE', 'FL'), ('JAX', 'JACKSONVILLE', 'FL')]),
 'KJKL': ('Jackson', [('JKL', 'JACKSON', 'KY')]),
 'KLBF': ('North Platte',
          [('LBF', 'NORTH PLATTE', 'NE'), ('VTN', 'VALENTINE', 'NE')]),
 'KLCH': ('Lake Charles',
          [('BPT', 'BEAUMONT/PORT ARTHUR', 'TX'),
           ('LCH', 'LAKE CHARLES', 'LA')]),
 'KLIX': ('New Orleans-Baton Rouge',
          [('BTR', 'BATON ROUGE', 'LA'), ('MSY', 'NEW ORLEANS', 'LA')]),
 'KLKN': ('Elko',
          [('EKO', 'ELKO', 'NV'),
           ('ELY', 'ELY', 'NV'),
           ('WMC', 'WINNEMUCCA', 'NV')]),
 'KLMK': ('Louisville',
          [('LEX', 'LEXINGTON', 'KY'), ('SDF', 'LOUISVILLE', 'KY')]),
 'KLOT': ('Chicago', [('ORD', 'CHICAGO', 'IL'), ('RFD', 'ROCKFORD', 'IL')]),
 'KLOX': ('Los Angeles-Oxnard',
           [('LGB', 'LONG BEACH', 'CA'),
            ('CQT', 'LOS ANGELES', 'CA'),
            ('LAX', 'LOS ANGELES', 'CA'),
            ('SMX', 'SANTA MARIA', 'CA')]),
 'KLSX': ('St. Louis',
          [('COU', 'COLUMBIA', 'MO'), ('STL', 'ST. LOUIS', 'MO')]),
 'KLUB': ('Lubbock', [('LBB', 'LUBBOCK', 'TX')]),
 'KLWX': ('Baltimore-Washington',
          [('BWI', 'BALTIMORE', 'MD'),
           ('DCA', 'WASHINGTON DC', 'DC'),
           ('IAD', 'WASHINGTON DC/DULLES', 'DC')]),
 'KLZK': ('Little Rock', [('LIT', 'LITTLE ROCK', 'AR')]),
 'KMAF': ('Midland-Odessa', [('MAF', 'MIDLAND-ODESSA', 'TX')]),
 'KMEG': ('Memphis', [('MEM', 'MEMPHIS', 'TN'), ('TUP', 'TUPELO', 'MS')]),
 'KMFL': ('Miami-South Florida',
          [('MIA', 'MIAMI', 'FL'), ('PBI', 'WEST PALM BEACH', 'FL')]),
 'KMFR': ('Medford', [('MFR', 'MEDFORD', 'OR')]),
 'KMHX': ('Morehead City', [('HSE', 'CAPE HATTERAS', 'NC')]),
 'KMKX': ('Milwaukee', [('MSN', 'MADISON', 'WI'), ('MKE', 'MILWAUKEE', 'WI')]),
 'KMLB': ('Melbourne',
          [('DAB', 'DAYTONA BEACH', 'FL'),
           ('MCO', 'ORLANDO', 'FL'),
           ('VRB', 'VERO BEACH', 'FL')]),
 'KMOB': ('Mobile-Pensacola',
          [('MOB', 'MOBILE', 'AL'), ('PNS', 'PENSACOLA', 'FL')]),
 'KMPX': ('Twin Cities',
          [('MSP', 'MINNEAPPOLIS-ST.PAUL', 'MN'),
           ('STC', 'SAINT CLOUD', 'MN')]),
 'KMQT': ('Marquette', [('MQT', 'MARQUETTE', 'MI')]),
 'KMRX': ('Morristown',
          [('TRI', 'BRISTOL-JHNSN CTY-KN', 'TN'),
           ('CHA', 'CHATTANOOGA', 'TN'),
           ('TYS', 'KNOXVILLE', 'TN'),
           ('OQT', 'OAK RIDGE', 'TN')]),
 'KMSO': ('Missoula', [('FCA', 'KALISPELL', 'MT'), ('MSO', 'MISSOULA', 'MT')]),
 'KMTR': ('San Francisco-Monterey', [('SFO', 'SAN FRANCISCO ', 'CA')]),
 'KOAX': ('Omaha',
          [('LNK', 'LINCOLN', 'NE'),
           ('OFK', 'NORFOLK', 'NE'),
           ('OMA', 'OMAHA', 'NE')]),
 'KOKX': ('New York City-Upton',
          [('BDR', 'BRIDGEPORT', 'CT'),
           ('ISP', 'ISLIP', 'NY'),
           ('LGA', 'NEW YORK', 'NY'),
           ('JFK', 'NEW YORK ', 'NY'),
           ('NYC', 'NEW YORK C.PARK', 'NY'),
           ('EWR', 'NEWARK', 'NJ')]),
 'KOTX': ('Spokane', [('LWS', 'LEWISTON', 'ID'), ('GEG', 'SPOKANE', 'WA')]),
 'KOUN': ('Norman',
          [('OKC', 'OKLAHOMA CITY', 'OK'), ('SPS', 'WICHITA FALLS', 'TX')]),
 'KPAH': ('Paducha', [('EVV', 'EVANSVILLE', 'IN'), ('PAH', 'PADUCAH', 'KY')]),
 'KPBZ': ('Pittshurgh', [('PIT', 'PITTSBURGH', 'PA')]),
 'KPDT': ('Pendleton', [('PDT', 'PENDLETON', 'OR'), ('YKM', 'YAKIMA', 'WA')]),
 'KPHI': ('Philadelphia',
          [('ABE', 'ALLENTOWN', 'PA'),
           ('ACY', 'ATLANTIC CITY ', 'NJ'),
           ('PHL', 'PHILADELPHIA', 'PA'),
           ('ILG', 'WILMINGTON', 'DE')]),
 'KPIH': ('Pocatello', [('PIH', 'POCATELLO', 'ID')]),
 'KPQR': ('Portland',
          [('AST', 'ASTORIA', 'OR'),
           ('EUG', 'EUGENE', 'OR'),
           ('PDX', 'PORTLAND', 'OR'),
           ('SLE', 'SALEM', 'OR')]),
 'KPSR': ('Phoenix', [('PHX', 'PHOENIX', 'AZ'), ('YUM', 'YUMA', 'AZ')]),
 'KPUB': ('Pueblo',
          [('ALS', 'ALAMOSA', 'CO'),
           ('COS', 'COLORADO SPRINGS', 'CO'),
           ('PUB', 'PUEBLO', 'CO')]),
 'KRAH': ('Raleigh',
          [('GSO', 'GREENSBORO-WNSTN-SAL', 'NC'), ('RDU', 'RALEIGH', 'NC')]),
 'KREV': ('Reno', [('RNO', 'RENO', 'NV')]),
 'KRIW': ('Riverton', [('CPR', 'CASPER', 'WY'), ('LND', 'LANDER', 'WY')]),
 'KRLX': ('Charleston',
          [('BKW', 'BECKLEY', 'WV'),
           ('CRW', 'CHARLESTON', 'WV'),
           ('EKN', 'ELKINS', 'WV'),
           ('HTS', 'HUNTINGTON', 'WV')]),
 'KRNK': ('Blacksburg',
          [('LYH', 'LYNCHBURG', 'VA'), ('ROA', 'ROANOKE', 'VA')]),
 'KSEW': ('Seattle ',
          [('OLM', 'OLYMPIA', 'WA'),
           ('UIL', 'QUILLAYUTE', 'WA'),
           ('SEA', 'SEATTLE ', 'WA')]),
 'KSGF': ('Springfield', [('SGF', 'SPRINGFIELD', 'MO')]),
 'KSGX': ('San Diego', [('SAN', 'SAN DIEGO', 'CA')]),
 'KSHV': ('Shreveport', [('SHV', 'SHREVEPORT', 'LA')]),
 'KSJT': ('San Angelo',
          [('ABI', 'ABILENE', 'TX'), ('SJT', 'SAN ANGELO', 'TX')]),
 'KSJU': ('San Juan', [('SJU', 'SAN JUAN', 'PR')]),
 'KSLC': ('Salt Lake City', [('SLC', 'SALT LAKE CITY', 'UT')]),
 'KSTO': ('Sacramento',
          [('RDD', 'REDDING', 'CA'),
           ('SAC', 'SACRAMENTO', 'CA'),
           ('SCK', 'STOCKTON', 'CA')]),
 'KTBW': ('Tampa Bay', [('FMY', 'FORT MYERS', 'FL'), ('TPA', 'TAMPA', 'FL')]),
 'KTFX': ('Great Falls',
          [('GTF', 'GREAT FALLS', 'MT'),
           ('HVR', 'HAVRE', 'MT'),
           ('HLN', 'HELENA', 'MT')]),
 'KTLH': ('Tallahassee', [('TLH', 'TALLAHASSEE', 'FL')]),
 'KTOP': ('Topeka', [('CNK', 'CONCORDIA', 'KS'), ('TOP', 'TOPEKA', 'KS')]),
 'KTSA': ('Tulsa', [('FSM', 'FORT SMITH', 'AR'), ('TUL', 'TULSA', 'OK')]),
 'KTWC': ('Tucson', [('TUS', 'TUCSON', 'AZ')]),
 'KUNR': ('Rapid City', [('RAP', 'RAPID CITY', 'SD')]),
 'KVEF': ('Las Vegas', [('BIH', 'BISHOP', 'CA'), ('LAS', 'LAS VEGAS', 'NV')]),
 'PAFC': ('Anchorage',
          [('ANC', 'ANCHORAGE', 'AK'),
           ('GKN', 'GULKANA', 'AK'),
           ('HOM', 'HOMER', 'AK'),
           ('TKA', 'TALKEETNA', 'AK')]),
 'PAFG': ('Fairbanks',
          [('ANN', 'ANNETTE', 'AK'),
           ('BRW', 'BARROW', 'AK'),
           ('BET', 'BETHEL', 'AK'),
           ('BTT', 'BETTLES', 'AK'),
           ('CDB', 'COLD BAY', 'AK'),
           ('BIG', 'DELTA JUNCTION/FT GREELY', 'AK'),
           ('FAI', 'FAIRBANKS', 'AK'),
           ('AKN', 'KING SALMON', 'AK'),
           ('ADQ', 'KODIAK', 'AK'),
           ('OTZ', 'KOTZEBUE', 'AK'),
           ('MCG', 'MCGRATH', 'AK'),
           ('OME', 'NOME', 'AK'),
           ('SNP', 'ST. PAUL ISLAND', 'AK'),
           ('YAK', 'YAKUTAT', 'AK')]),
 'PAJK': ('Juneau', [('JNU', 'JUNEAU', 'AK')]),
 'PGUM': ('Guam', [('GUM', 'GUAM', 'GU')]),       
 'PACIFIC': ('Pacific Islands', 
             [('STU', 'PAGO PAGO', 'AS'),
              ('KMR', 'MAJURO', 'MH'),
              ('KWA', 'KWAJALEIN', 'MH'),
              ('TKR', 'KOROR', 'PW'),
              ('GSN', 'SAIPAN', 'MP'),
              ('WAK', 'WAKE ISLAND', 'UM'),
              ('TYA', 'YAP', 'FM'),
              ('TTP', 'POHNPEI', 'FM'),
              ('TKK', 'CHUUK', 'FM')]) }


def read_old_comments (request_icao):
	old_comments = []
	try:
		datfil = open('/Users/keith/Sites/data/ThreadExSurvey.txt', 'r')
		for line in datfil.readlines():
			line = line.strip()
			cols = line.split('\t')
			try:
				dt,icao,accept,comments,adddata,addcomments,name,affil,email = cols
			except:
				continue
			if icao == request_icao:
				if accept == "no accept response" and comments == "no comments" and adddata == "no adddata response" and addcomments == "no addcomments":
					continue
				old_comments.append((dt,icao,accept,comments,adddata,addcomments,name,affil,email))
	except:
		pass
	datfil.close()
	return old_comments

def get_cwa (request):
	from threads_dict import threads_dict
	import ThreadExSurvey_io
	cwa = ''
	cwa_name = ''
	cwa_list = []
	cwa_threads = []
	cwa_comments = {}
	if request.form:
		try:
			cwa = request.form['cwa']
			cwa_name,cwa_list = cwa_dict[cwa]
			for (call,name,state) in cwa_list:
				cwa_comments[call] = read_old_comments(call)
				cwa_threads.append(threads_dict[call])
		except:
			print_exception()
	else:
		print_exception()
	return ThreadExSurvey_io.display_form(cwa,cwa_name,cwa_list,cwa_threads,cwa_comments)

def process_survey (request):
# 	write information contained in request.form to a results file
	import sys
	from mail_file import mail_file
	from mx import DateTime
	import ThreadExSurvey_io
	
	if request.form:
		try:
			contact_name = request.form['contact_name']
			if contact_name == '': contact_name = 'name not given'
			contact_office = request.form['contact_office']
			if contact_office == '': contact_office = 'office not given'
			contact_email = request.form['contact_email']
			if contact_email == '': contact_email = 'email not given'
			now = DateTime.now()
			stacnt = 0
			while request.form.has_key('station%d'%stacnt):
				station = request.form['station%d'%stacnt]
				if request.form.has_key('accept%d'%stacnt) and request.form['accept%d'%stacnt] != 'na':
					accept = request.form['accept%d'%stacnt]
				else:
					accept = 'no accept response'
				comments = request.form['comments%d'%stacnt]
				if comments == '' or comments == 'na': comments = 'no comments'
				if request.form.has_key('adddata%d'%stacnt) and request.form['adddata%d'%stacnt] != 'na':
					adddata = request.form['adddata%d'%stacnt]
				else:
					adddata = 'no adddata response'
				addcomments = request.form['addcomments%d'%stacnt]
				if addcomments == '' or addcomments == 'na': addcomments = 'no addcomments'
				survey_file = open('/Users/keith/Sites/data/ThreadExSurvey.txt', 'a')
				survey_file.write('%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' % (now,station,accept,comments,adddata,addcomments,contact_name,contact_office,contact_email))
				survey_file.close()
				stacnt = stacnt+1
		except:
			print_exception()					
	else:
		print_exception()	
		
	mail_file ('KLE1@cornell.edu','ThreadEx survey submitted',None)	
	return ThreadExSurvey_io.thankyou()
		
	

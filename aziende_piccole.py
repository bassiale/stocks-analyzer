from selenium import webdriver
import time
#open the web browser 
driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
#whitelist with all the businesses i want to check
WhiteList = ['ACOR', 'AES', 'AGNC', 'ACI', 'ATI', 'AAL', 'AXL', 'AMWL', 'AMKR', 'NLY', 'AR', 'APA', 'AIV', 'ARRY', 'ASB', 'AVYA', 'BBBY', 'BGCP', 'BLUE', 'BWP', 'BDN', 'BRX', 
'BPL', 'COG', 'CAMP', 'CRC', 'CLMT', 'CBL', 'CNP', 'CTL', 'CNK', 'CLF', 'CLVS', 'CLNY', 'CMC', 'COMM', 'CYH', 'CRK', 'CEIX', 'CLR', 'CXW', 'OFC', 'COTY', 'CVA', 'CVET', 'DAN', 'DCP', 'DVN', 'DBX', 'DNB', 'EE', 'OVV', 'EGN', 'ET', 'EQT', 'ETRN', 'EQC', 'AQUA', 'EZPW', 'FNMA', 'FHN', 'FLO', 'F', 'FOR', 'BEN', 'FMCC', 'FULT', 'GIG', 'GE', 'TMK', 'GOGO', 'GT', 'GPRO', 'GTE', 'GPK', 'GPRE', 'HRB', 'HAL', 'HBI', 'HLIT', 'HA', 'HP', 'HPE', 'HST', 'SATS', 'HBAN', 'HUN', 'HUYA', 'IMGN', 'INO', 'ICPT', 'IPG', 'IVC', 'IRWD', 'STAR', 'JBLU', 'JNPR', 'KEY', 'KIM', 'KMI', 'KN', 'LAUR', 'LM', 'LEVI', 'LXP', 'CLI', 'M', 'MRO', 'MAT', 'MPW', 'MD', 'MLCO', 'MTOR', 'MACK', 'MWA', 'MUR', 'NOV', 'NAVI', 'NKTR', 'EDU', 'NYCB', 'NWL', 'NFX', 'NR', 'NWSA', 'NI', 'NLOK', 'OXY', 'OII', 'ORI', 'OUT', 'OI', 'PK', 'PKD', 'PBCT', 'PRSP', 'PCG', 'PDM', 'PBI', 'PAA', 'PAGP', 'ESI', 'PLUG', 'PPL', 'PCP', 'PRA', 'PSEC', 'QRTEA', 'RRD', 'RMBS', 'RRC', 'RLGY', 'RWT', 'RF', 'REZI', 'SABR', 'SBH', 'SIRI', 'SITC', 'SLM', 'SM', 'SWN', 'SFM', 'SCS', 'SPWR', 'SKT', 'TGNA', 'TME', 'TEVA', 'MAC', 'TWI', 'TRN', 'TTMI', 'TUP', 'TPC', 'UAA', 'UIS', 'X', 'UNM', 'VGR', 'VEON', 'VNE', 'VIAV', 'VST', 'WBC', 'WRE', 'WBT', 'WCG', 'WU', 'RKT', 'WMB', 'NSM', 'XRX'] 
FilteredBuis = []
for business in WhiteList:
       #create the url from the name of the business       
       url = 'https://www.cnbc.com/quotes/'+business+'?qsearchterm='+business.lower()
       #many businesses wont be found so I use try
       try:
             driver.get(url)
             #where he needs to fond the information
             bo = driver.find_element_by_class_name("QuoteStrip-changeUp")
             #there's probably a better way to do this
             s = bo.text
             a = s.index('(')
             v1, v2 = s[0:a], float(s[(a+1):(len(s)-2)])
             #find the price
             search_bar = driver.find_element_by_class_name("QuoteStrip-lastPrice")
             price = float(search_bar.text)
             #filter the businesses
             if v2 >2:
                  FilteredBuis.append(business + " growth:" + str(v2)+", price:"+str(price))
                  print(business+str(price) +'%, '+str(v2))
       except: 
             print('could not find it')
             pass
       continue
#list what you found
print(FilteredBuis)

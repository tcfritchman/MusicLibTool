import sys, os

allowedFormats = ['mp3', 'wma', 'm4a', 'm4p']
rootDir = '.'

def qfilter():


    print "Quality filter selected."
    filterStr = raw_input("Enter a filter string:")
    filters = filterStr.split(" ")
    print filters
    # TODO  Remove invalid filters

    for path, dirs, files in os.walk(rootDir):
	if has_match(files, filters):
	    print path

def has_match(files, filters):
    for f in files:
	for fil in filters:
	    if f.split('.')[-1] == fil:
		return True
    return False
    











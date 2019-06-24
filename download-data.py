import urllib2

from localsettings import TEST_URL

response = urllib2.urlopen(TEST_URL)
data = response.read()

# Write data to file
filename = 'data.csv'
file_ = open(filename, 'w')
file_.write(data)
file_.close()

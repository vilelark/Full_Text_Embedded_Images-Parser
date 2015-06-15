import urllib2
from bs4 import BeautifulSoup
import os

def Fetch(weblink):
	openlink = urllib2.urlopen(weblink)
	x = openlink.read()
	soup = BeautifulSoup(x)

	for link in soup.find_all('a'):
		href = link.get('href')
		try:
			check = href.split('/')[-3]
			if check == 'grants':
				file_name = href.split('/')[-1]
				file_year = href.split('/')[-2]

				file_dir = file_year+r'/'
				if file_year:
						
					if not os.path.exists(file_dir):
						os.makedirs(file_dir)

					if not os.path.exists(file_dir + file_name):
						each_file = urllib2.urlopen(href)
						file_meta = each_file.info()
						file_size = int(file_meta.getheaders('Content-Length')[0])

						f = open(file_dir + file_name, 'wb')
						print 'Downloading: %s ,File Size: %3.2f MB' %(file_name, file_size/1048576.0)
							
						fn_download = 0
						block_size = 52428800
						while True:
							buffer = each_file.read(block_size)
							if not buffer:
								break

							fn_download += len(buffer)
							f.write(buffer)
							status = r'  Download Status: %3.2f%%' %(fn_download * 100.0 / file_size)
							print status

						f.close()
						print
		except Exception, e:
			continue

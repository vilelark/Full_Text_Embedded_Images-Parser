
import os
import urllib2

def all_dir_name(path):
	for root,dirs,files in os.walk(r'%s' %path):
		return dirs

def correct_dir(dirlist):
	dir_list = []
	for name in dirlist:
		if len(name) == 4 and name.isdigit():
			dir_list.append(name)
	return dir_list

def all_dir_last_file(correctdir):
	if correctdir:
		for dir_year in correctdir:
			file_dir = r'%s/' %dir_year
			disk_file_list = os.listdir(file_dir)
			
			if len(disk_file_list) != 0:
				disk_file_name = max(disk_file_list)
				disk_file_info = os.stat(file_dir+disk_file_name)
				disk_file_size = disk_file_info.st_size

				original_file = urllib2.urlopen(r'http://storage.googleapis.com/patents/redbook/grants/%s/%s' %(dir_year,disk_file_name))
				original_file_info = original_file.info()
				original_file_size = int(original_file_info.getheaders('Content-Length')[0])

				if disk_file_size != original_file_size:
					os.remove(file_dir+disk_file_name)

def last_file(correctdir):
	if correctdir:
		dir_year = min(correctdir)
		file_dir = r'%s/' %dir_year
		disk_file_list = os.listdir(file_dir)

		if len(disk_file_list) != 0:
			disk_file_name = max(disk_file_list)
			disk_file_info = os.stat(file_dir+disk_file_name)
			disk_file_size = disk_file_info.st_size

			original_file = urllib2.urlopen(r'http://storage.googleapis.com/patents/redbook/grants/%s/%s' %(dir_year,disk_file_name))
			original_file_info = original_file.info()
			original_file_size = int(original_file_info.getheaders('Content-Length')[0])

			if disk_file_size != original_file_size:
				os.remove(file_dir+disk_file_name)


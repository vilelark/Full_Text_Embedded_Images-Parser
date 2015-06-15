import os
import Checkfile
import Parser

checkdir = Checkfile.all_dir_name(os.getcwd())
correctdir = Checkfile.correct_dir(checkdir)

Checkfile.last_file(correctdir)

Parser.Fetch('http://www.google.com/googlebooks/uspto-patents-redbook.html')
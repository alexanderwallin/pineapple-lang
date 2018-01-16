from shutil import copy2
from os.path import expanduser
from distutils.dir_util import copy_tree

print('Installing package to Sublime Text 3')

home = expanduser("~")
dst = home + '/Library/Application Support/Sublime Text 3/Packages/User'
copy2('pineapple.py', dst)
copy_tree('python-osc/pythonosc', dst + '/pythonosc/')


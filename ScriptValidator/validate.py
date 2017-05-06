# use this to run the stuff. comment it out for now as we are still testing. later we'll run it against the actual folders n shit.

import argparse
import glob

from ScriptValidate import validateFile

parser = argparse.ArgumentParser(description='Validate SNSC3 script files.')
parser.add_argument('folders', type=str, nargs='+', help='Folder(s) containing XML files to validate.')
args = parser.parse_args()

num_files = 0
for folder in args.folders:
  for file in glob.glob('../{}/*.xml'.format(folder)):
    try:
      validateFile(file)
    except:
      continue

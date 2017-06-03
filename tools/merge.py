import json
import yaml
import argparse

from loader import Loader

parser = argparse.ArgumentParser()
parser.add_argument('name', help='Filename')
parser.add_argument('-o', '--out', help='Output file name (default to input file replaced by JSON)')
args = parser.parse_args()

data = yaml.load(open(args.name), Loader)

if args.out:
	new_file = args.out
else:
	new_file = args.name.replace('.yaml', '.json')

json.dump(data, open(new_file, 'w'))

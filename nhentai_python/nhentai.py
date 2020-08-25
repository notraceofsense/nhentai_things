# nhentai.py
# A program for downloading stuff from nhentai using the numbers.
# I was pretty tired when I originally wrote this, thus the code is kinda jank.
# Rewriting to add some cool stuff and make things better.
# TODO: multithreading (Book done), implement saving jsons, idk.
# Excessively commented so that almost anyone can understand.
# usage: nhentai.py <digits> -p/--path <Path to folder> -j/--json (not done)

# This is where we import packages so that I don't have to write code to deal
# with stuff such as HTTP and writing to disk.
# I can't remember if requests is installed by default or not.
# If it isn't, https://requests.readthedocs.io/en/master/user/install/
import sys, os, argparse
from book_thread import *

# This big blob of code here is supposed to handle the command line args.
# https://youtu.be/36lSzUMBJnc?t=176 << This is me right now.
parser = argparse.ArgumentParser(
	description="Download books from nhentai using the book IDs")
parser.add_argument('book_id', metavar='id', type=int, nargs='+',
	help='the desired book IDs')
parser.add_argument('-p', '--path', dest='path', metavar='path', nargs='?',
	default=os.getcwd(), help='Directory to save books in')
parser.add_argument('-j', '--json', dest='json', action='store_true',
	help='Save JSON data for books.')

# Get the args, and put them in some useful variables.
args = vars(parser.parse_args())
id_list = args.get('book_id')
path = args.get('path')

book_threads = []

# For loop, yay batch jobs!
for n in id_list:
	# Yay, multithreading
	t = Book_Thread.from_book_id(n, path, 8)
	t.start()
	book_threads.append(t)

for t in book_threads:
	t.join()
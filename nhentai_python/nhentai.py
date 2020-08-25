# nhentai.py
# A program for downloading stuff from nhentai using the numbers.
# I was pretty tired when I originally wrote this, thus the code is kinda jank.
# Rewriting to add some cool stuff and make things better.
# TODO: multithreading (done), implement saving jsons
# (done, need to rename file to x.json after download), idk.
# Excessively commented so that almost anyone can understand.
# usage: nhentai.py <digits> -p/--path <Path to folder> -j/--json
# -w/--workers <number of workers>

# This is where we import packages so that I don't have to write code to deal
# with stuff such as HTTP and writing to disk.
# I can't remember if requests is installed by default or not.
# If it isn't, https://requests.readthedocs.io/en/master/user/install/
import sys, os, argparse
from book_thread import *
from download_thread import *
from queue import Queue

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
parser.add_argument('-w', '--workers', dest='workers', metavar='workers', type=int,
	default=8, help='Number of worker threads to use when downloading.')

# Get the args, and put them in some useful variables.
args = vars(parser.parse_args())
id_list = args.get('book_id')
path = args.get('path')
json = args.get('json')
workers = args.get('workers')

queue = Queue()

# For loop, yay batch jobs!
for n in id_list:
	t = Book_Thread.from_book_id(n, path, json, queue)
	t.start()

for i in range(int(workers)):
	t = Download_Thread(queue)
	t.daemon = True
	t.start()

queue.join()
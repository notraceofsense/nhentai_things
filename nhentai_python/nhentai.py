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
import requests, sys, os, argparse, threading

# Moved the book-getting method into a function for multithreading.
def get_book(n):
	# Add the book id to the url so we can access the API
	api_url = "https://nhentai.net/api/gallery/{}".format(n)

	# get the JSON so we can get the media id.
	print("{}: Getting metadata from nhentai...".format(n))
	book_json = requests.get(api_url).json()

	# Get the media id from the json so we can access the gallery.
	media_id = book_json['media_id']
	printBook(n, "Media ID: {}".format(media_id))

	# add the media id to the url
	gallery_url = "https://i.nhentai.net/galleries/{}".format(media_id)

	# Make the directory.
	printBook(n, "Making directory...")
	current_dir = os.path.join(path, str(n))
	os.mkdir(current_dir)

	# Here's where the jank begins!
	i = 0
	f = 1

	printBook(n, "Downloading...")

	# For all the pages, get the image type and download them.
	for x in book_json["images"]["pages"]:
		filename = "{}.{}".format(
			f, getImageType(book_json["images"]["pages"][i]["t"]))
		open("{}\{}".format(current_dir, filename), "xb").write(requests.get(
			"{}/{}".format(gallery_url, filename), allow_redirects=True
			).content)

		printBook(n, "{} downloaded.".format("{}/{}".format(gallery_url, filename)))
    
		i += 1
		f += 1

	printBook(n, "Finished downloading.")

# Function that appends book ID to debug messages
def printBook(n, m):
	print("{}: {}".format(n, m))

# A function for getting the full file extentions from the abbreviations in the
# JSON.
# Python doesn't really have proper switch/case support. So we do this little
# hack with dictionaries.
# Part of the reason I want to rewrite this in C#/Java/something else.
# Now if only I could get JSON's to work...
def getImageType(s):
    c = {
        "j": "jpg",
        "p": "png",
        "g": "gif"
    }
    return c.get(s)

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

# For loop, yay batch jobs!
for n in id_list:
	# Yay, multithreading!
	threading.Thread(target=get_book, args=(n,)).start()

for t in threading.enumerate():
	if t == threading.current_thread():
		continue
	t.join()
'''
	this is a docstring [for pylint]
'''

import re
import os

import threading
import requests

from bs4 import BeautifulSoup

os.makedirs('xkcd', exist_ok = True)
# http://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary
# python3 func to check if dir exists

def get_current_comic():
	src = requests.get('http://xkcd.com')
	soup = BeautifulSoup(src.text, "html.parser")
	regex_string = soup.findAll(text = re.compile('Permanent link to this comic: http://xkcd.com/'))
	current = regex_string[0][-5:-1]
	return int(current)

def xkcd_downloader(start, end):
	for number in range(start, end):
		src = requests.get('http://xkcd.com/' + str(number))
		soup = BeautifulSoup(src.text, "html.parser")
		comic_url = soup.select('#comic img') # div id:comic and elem:img
		if comic_url != []:
			print('Downloading comic ' + str(number) + ' ...')
			comic_img = 'http:' + comic_url[0].get('src') # image source
			img = requests.get(comic_img)
			# save to dir
			file = open('./xkcd/' + os.path.basename(str(number)), 'wb')
			file.write(img.content)
			file.close()


if __name__ == '__main__':
	current_comic = get_current_comic()

	threads = []
	for i in range(1, current_comic, 100):
		# steps of 100
		thread_obj = threading.Thread(target = xkcd_downloader, args = (i, min(i+100, current_comic+1)))
		threads.append(thread_obj)
		thread_obj.start()
	for thread_obj in threads:
		thread_obj.join()
		# join - to wait until thread is comeplete

	print('Finished downloading ' + str(current_comic) + ' comics !')
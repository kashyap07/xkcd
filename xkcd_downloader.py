#! /usr/bin/python3
# todo: learn threading and speed this up

import requests, os
from bs4 import BeautifulSoup

os.makedirs('xkcd', exist_ok = True)
# http://stackoverflow.com/questions/273192/how-to-check-if-a-directory-exists-and-create-it-if-necessary
# python3 func to check if dir exists


def xkcd_downloader(start, end):
	for number in range(start, end):
		src = requests.get('http://xkcd.com/' + str(number))
		soup = BeautifulSoup(src.text, 'lxml')
		comicUrl = soup.select('#comic img') # div id:comic and elem:img
		if comicUrl != []:
			print('Downloading comic ' + str(number) + ' ...')
			comicImg = 'http:' + comicUrl[0].get('src') # image source
			img = requests.get(comicImg)
			# save to dir
			file = open('./xkcd/' + os.path.basename(comicImg), 'wb')
			file.write(img.content)
			file.close()

if __name__ == '__main__':
	xkcd_downloader(1728, 1731)
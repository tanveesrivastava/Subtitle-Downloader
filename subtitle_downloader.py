# -*- coding: utf-8 -*-
"""Subtitle Downloader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g7BR4T28uTyId_8ww0J3zfNuRB1ZbYg9
"""

from zipfile import ZipFile 
import io 
import requests 
name = input() 
year_of_release = input() 
name = name.lower() 
final_name = name + '-' + year_of_release 
url = 'http://cdn.subscene.co.in/movies/' 
final_name = final_name.replace(' ', '-') 
#final_ur 
final_name 
final_url = url + final_name + '.zip' 
r = requests.get(final_url) # Request for downloading 
z = ZipFile(io.BytesIO(r.content)) # Opening zip file 
z.extractall() # extracting zip file


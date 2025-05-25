# -*- coding: utf-8 -*-
"""
Created on Mon Nov 1 2021
This is free software, under the terms of the GNU General Public License
Version 3 (www.gnu.org/licenses) without any implied warranty of
merchantability or fitness for a particular purpose.
@author: king.r.paul@gmail.com
"""
import os
import csv
from pprint import pprint as pp
import re
from english_words import *
from bs4 import BeautifulSoup
import requests
import string
import math
from PIL import Image
import os
import requests
from bs4 import BeautifulSoup
from string import Template
import math
from PIL import Image
import os
import numpy as np
from PIL.ExifTags import TAGS


def resize_contain(image, size, resample=Image.LANCZOS, bg_color=(255, 255, 255, 0)):
    """
    Resize image according to size.
    image:      a Pillow image instance
    size:       a list of two integers [width, height]
    """
    img_format = image.format
    img = image.copy()
    img.thumbnail((size[0], size[1]), resample)
    background = Image.new('RGBA', (size[0], size[1]), bg_color)
    img_position = (
        int(math.ceil((size[0] - img.size[0]) / 2)),
        int(math.ceil((size[1] - img.size[1]) / 2))
    )
    background.paste(img, img_position)
    background.format = img_format
    return background.convert('RGBA')

# pixdir = os.path.join(os.getcwd(), 'pix_tmp')
# files = [os.path.join(pixdir, f) for f in  os.listdir(pixdir)]
# for f in files:
#   # rename unnamed files
#   if os.path.isfile(f):
#     with Image.open(f) as im:
#       exif = {}
#       try:
#         for tag, value in im._getexif().items():
#           if tag in TAGS:
#             exif[TAGS[tag]] = value
#         year = exif["DocumentName"]
#         city_state = exif["ImageDescription"]
#         description = exif["Artist"]
#       except:
#         print('missing metadata')
#       base, ext = os.path.splitext(f)
#       name_sm_file = base + '_sm.png'
#       cover = resize_contain(im, [120, 120])
#       cover.save(name_sm_file, 'PNG')


def nav_bar(menu, depth=0):
  assert menu in ('home', 'press', 'notes', 'pubs', 'pics', 'wiki', 'ebooks', 'safe')
  if menu == "home":
    menu_filename = "index"
  else:
    menu_filename = menu
  NAV = """
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="https://en.gravatar.com/kingrpaul" target="_blank"><img src="https://secure.gravatar.com/avatar/f3ef8b36fd1e4983dc51c1abc6b9650e" class="thumbnail rounded" alt="Paul King"> </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button> 
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav mr-auto">
        <li id="nav-index" class="nav-item">
          <a class="nav-link" href="$depth$index.html">home</a>
        </li>
        <li id="nav-press" class="nav-item">
          <a class="nav-link" href="$depth$press.html">press</a>
        </li>
        <li id="nav-notes" class="nav-item">
          <a class="nav-link" href="$depth$notes.html">notes</a>
        </li>
        <li id="nav-pubs" class="nav-item">
          <a class="nav-link" href="$depth$pubs.html">pubs</a>
        </li>
        <li id="nav-pics" class="nav-item">
          <a class="nav-link" href="$depth$pics.html">pics</a>
        </li>
        <li id="nav-wiki" class="nav-item">
          <a class="nav-link" href="$depth$wiki.html">wiki</a>
        </li>
        <li id="nav-ebooks" class="nav-item">
          <a class="nav-link" href="$depth$ebooks.html">ebooks</a>
        </li>
        <li id="nav-safe" class="nav-item">
          <a class="nav-link" href="$depth$safe.html">safe</a>
        </li>
      </ul>
    </div>
  </nav>"""
  target_string = '<a class="nav-link" href="$depth${}.html">{}</a>'.format(menu_filename, menu)
  replacement_string = target_string.replace('<a class="nav-link" href="','<a class="nav-link active" href="')
  result = NAV.replace(target_string, replacement_string)
  result = result.replace("$depth$", "../"*depth)
  return(result)
# print(nav_bar("press", depth=2))

HEAD = \
"""<!DOCTYPE html>
<html lang="en">
<head>
  <title>king.r.paul</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{description}">
  <meta name="keywords" content="{keywords}">
  <meta name="author" content="Paul King">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link rel="shortcut icon" href="favicon/favicon.ico" />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
"""


def make_card(icon_file, modal_file, year, city_state, description, img_index):

  ROW = """\
            <div class="card" style="width: 210px;">
              <a href="#wk_img_{img_index}" class="card-link">
                <img class = "card-img-top middle image p-2" id="wk_img_{img_index}" class="m-1" data-toggle="modal" data-target="#wk_mod_{img_index}" src="{icon_file}"  alt="">
              </a>
              <div class="card-body text-secondary py-1">
                <p class="card-title text-center text-primary">{year}</p>
                <p class="card-subtitle text-center">{city_state}</p>
                <p class="card-subtitle text-center">{description}</p>
              </div>
            </div>
            <div class="modal fade" id="wk_mod_{img_index}" tabindex="-1" role="dialog">
              <div class="modal-dialog" role="document">
                <div class="modal-content">
                  <div class="modal-body">
                    <img class="" style="max-width:100%; max-height:100%" id="wk_img_{img_index}" src="{modal_file}" data-toggle="modal" data-target="#wk_img_{img_index}">
                  </div>
                  <div class="modal-footer">
                    <p class="col-11 text-left">{caption}</p>
                    <button type="button" class="close col" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                  </div>
                </div>
              </div>
            </div>\n"""

  result = ROW.format(icon_file=icon_file, modal_file=modal_file, year=year, city_state=city_state, description=description, img_index=img_index, caption = " ".join([year, city_state, description]))
  return(result)                              

def make_html_pics():
    result = HEAD.format(description = "news items and press releases", 
                         keywords = "medical physics, jeff anderson regional cancer center")
    result += '<body>'
    result += nav_bar('pics')

    result += """\n  <div class="container-fluid">
    <div class="row">
      <div class="col-12 text-primary">
      <div id="" class="">         
        <div class="container-fluid">
          <div class="row">\n"""

    pixdir = os.path.join(os.getcwd(), 'pix_tmp')
    files = [os.path.join(pixdir, f) for f in  os.listdir(pixdir)]
    files.sort(reverse=True)
    # print(files)
    for (img_index, f) in enumerate(files):
      # rename unnamed files
      if not os.path.isfile(f):
        continue
      if "_sm" in f:
        continue

      with Image.open(f) as im:
        exif = {}
        try:
          for tag, value in im._getexif().items():
            if tag in TAGS:
              exif[TAGS[tag]] = value
          year = exif["DocumentName"]
          city_state = exif["ImageDescription"]
          description = exif["Artist"]
        except:
          print('missing metadata')
        base, ext = os.path.splitext(f)
        name_sm_file = base + '_sm.png'
        cover = resize_contain(im, [120, 120])
        cover.save(name_sm_file, 'PNG')


        icon_file = name_sm_file
        modal_file = f
        # caption = " ".join([year, city_state, description])
        img_index = img_index
        result += make_card(icon_file, modal_file, year, city_state, description, img_index)

    result += '\n          </div>\n    </div>\n  </div>\n</div>\n</body>\n</html>'

    # print(result)
    with open ('pics.html', "w") as outfile:
        for line in result:
            outfile.write(line)


make_html_pics()

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

docs =  \
    {1:
        {'year': 2018,
         'title': 'MVCT QA w/TomoHDA &amp; Ray6',
         'icon': "more_horiz",
         'location': 'notes',
         'file': "./notes/mvct_qa/MVCT-QA-with-RS.html",
         'doctype': 'html'},
    2:
        {'year': 2018,
         'title': 'e- Blk w/TomoHDA &amp; Ray6',
         'icon': "more_horiz",
         'location': 'notes',
         'file': "./notes/electron_rof/Electron Output with RS.html",
         'doctype': 'html'},
    3:
        {'year': 2018,
         'title': 'Varian Rails w/Ray6',
         'icon': 'more_horiz',
         'location': 'notes',
         'file': "./notes/ray_varian_rails/Varian Rails with RS.html",
         'doctype': 'html'},
    4:
        {'year': 2020,
         'title': 'Flash, microLinac, CT',
         'icon':  "more_horiz",
         'location': 'notes',
         'file': "./notes/flash_ct/flash_ct.html",
         'doctype': 'html'},
    5:
        {'year': 2020,
         'title': 'RayStation X-Ray Rx Scaling',
         'icon': "more_horiz",
         'location': 'notes',
         'file': "./notes/ray_rx_scale/ray_rx_scale.html",
         'doctype': 'html'},
    6:
        {'year': 2009,
         'title': 'Ultraviolet Tanning Beds',
         'icon': "more_horiz",
         'location': 'notes',
         'file': "./notes/tanning_beds/policy-brief.html",
         'doctype': 'html'},
    7:
        {'year': 2021,
         'title': 'Cadaveric Organ Donation',
         'icon': "more_horiz",
         'location': 'notes',
         'file': "./notes/organ_donor/organ_donor.html",
         'doctype': 'html'},
    8:
        {'year': 2021,
         'title': 'Shared Philosophy of the Scientific Revolution',
         'icon': "more_horiz",
         'location': 'notes',
         'file': "./notes/sci_rev_phil/sci_rev_phil.html",
         'doctype': 'html'},
    9:
        {'year': 2019,
         'title': 'Anderson Regional Cancer Center is the first center in the United States to treat cancer patients using RayStation and the TomoTherapy Treatment Delivery System',
         'icon': "attachment",
         'location': 'press',
         'file': "./_downloads/2019_ARCCIsTheFirstCenterInTheUS.pdf",
         'doctype': 'pdf'},
    10:
        {'year': 2019,
         'title': 'Anderson Regional Cancer Center is the first center in the United States to treat cancer patients using RayStation and the TomoTherapy Treatment Delivery System',
         'icon': "attachment",
         'location': 'press',
         'file': './_downloads/2019_ARCCFirstInTheUSToTreat.pdf',
         'doctype': 'pdf'},
    11:
        {'year': 2018,
         'title': 'RaySearch Receives First Order for the RayCare Oncology Information System',
         'icon': "attachment",
         'location': 'press',
         'file': "./_downloads/2018_FirstOrderFo RayCare.pdf",
         'doctype': 'pdf'}, 
    12:
        {'year': 2015,
         'title': 'Anderson First in State to Offer TomoTherapy for Cancer Patients',
         'icon': "attachment",
         'location': 'press',
         'file': "./_downloads/2015_AndersonFirstInState.pdf",
         'doctype': 'pdf'},
    13:
        {'year': 2014,
         'title': 'Anderson Regional Cancer Center prides itself on providing world class care close to home',
         'icon': "attachment",
         'location': 'press',
         'file': "./_downloads/2014_WorldClassCancerCenter.png",
         'doctype': 'img'},
    14:
        {'year': 2008,
         'title': 'Conformal arc radiotherapy planned with Pinnacle3, Jeff Anderson Regional Cancer Center',
         'icon': "attachment",
         'location': 'press',
         'file': "./_downloads/2008_ConformalArcRadiotherapy.pdf",
         'doctype': 'pdf'},
    15:
        {'year': 2003,
         'title': 'Jeff Anderson Celebrates 75th Anniversary with Opening of Jeff Anderson Regional Cancer Center',
         'icon': "attachment",
         'location': 'press',
         'file': "./_downloads/2003_JeffAndersonCelebrates_.pdf",
         'doctype': 'pdf'},
    16:
        {'year': 2000,
         'title': 'Jeff Anderson team pioneers prostate cancer treatment',
         'icon': "image",
         'location': 'press',
         'file': "./_downloads/2000_JeffAndersonTeamPPioneers.jpg",
         'doctype': 'img'},
    17:
        {'year': 2019,
         'title': 'Simplistic Tomotherapy Model Predicts RayStation Treatment Times Within 20&#37; for First 16 Plans, PO-GePV-T-278, AAPM',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2019_SimplisticTomotherapyModel.pdf",
         'doctype': 'pdf'},
    18:
        {'year': 2014,
         'title': 'Simplifying Assumption for Determining Sc and Sp, <span class="text-nowrap">SU-E-T-293</span>, AAPM',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2014_SimplifyingAssumptionFor.pdf",
         'doctype': 'pdf'},
    19:
        {'year': 2013,
         'title': 'Role of step size &amp; dwell time in inverse opt for prost impl, J Med Phys',
         'icon': "link",
         'location': 'pubs',
         'file': "http://www.jmp.org.in/article.asp?issn=0971-6203;year=2013;volume=38;issue=3;spage=148;epage=154;aulast=Manikandan",
         'doctype': 'web'},
    20:
        {'year': 2013,
         'title': 'Role of step size &amp; dwell time in inverse opt for prost impl, J Med Phys',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2013_RoleOfStepSizeAndMaxDwell.pdf",
         'doctype': 'pdf'},
    21:
        {'year': 2013,
         'title': 'Estimation of Eff Fld Size with Leaf-Based Algorithm, <span class="text-nowrap">SU-E-T-7</span>, AAPM',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2013_EstimationOfEffectiveField.pdf",
         'doctype': 'pdf'},
    22:
        {'year': 2013,
         'title': 'Estimation of Eff Fld Size with Leaf-Based Algorithm, <span class="text-nowrap">SU-E-T-7</span>, AAPM',
         'icon': "file_download",
         'location': 'pubs',
         'file': "./_downloads/2013_EstimationOfEffectiveFieldSize.pptx",
         'doctype': 'ppt'},
    23:
        {'year': 2012,
         'title': 'The New Professional’s Resume, NPSC Report, AAPM Newsletter',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2012_NewProfessionalResume.pdf",
         'doctype': 'pdf'},
    24:
        {'year': 2010,
         'title': 'Therapists should not have to wear personnel dosimetry badges, Med Phys',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2010_RadiationTherapistsShould_.pdf",
         'doctype': 'pdf'},
    25:
        {'year': 2008,
         'title': 'Comment on the interplay effect in prost IMRT delivery, Med Phys',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2008_CommentOnQuantifying.pdf",
         'doctype': 'pdf'},
    26:
        {'year': 2007,
         'title': 'Comment on IMRT administered at greater than 10 MV, Med Phys',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2007_CommentOnIMRTShould_.pdf",
         'doctype': 'pdf'},
    27:
        {'year': 2004,
         'title': 'Reviewer: Radiologic Science for Technologists, 8th Edition, Bushong',
         'icon': "link",
         'location': 'pubs',
         'file': "http://amzn.to/23gKJdt",
         'doctype': 'web'},
    28:
        {'year': 2001,
         'title': 'A simple method for electron energy constancy measurement, JACMP',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2001_ASimpleMethodForElectron.pdf",
         'doctype': 'pdf'},
    29:
        {'year': 2001,
         'title': 'In Regard to the ABS Recommendations for Pd-103 Brachytherapy',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2001_InRegardToTheABSRecommendation_.pdf",
         'doctype': 'pdf'},
    30:
        {'year': 2001,
         'title': 'Geometry function of a linear brachytherapy source, JACMP',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2001_GeometryFunctionOALinear_.pdf",
         'doctype': 'pdf'},
    31:
        {'year': 2000,
         'title': 'Radioimmunoguided Surgery Using Prostascint for Supraclav Mets',
         'icon': "link",
         'location': 'pubs',
         'file': "https://www.ncbi.nlm.nih.gov/pubmed/11018634",
         'doctype': 'web'},
    32:
        {'year': 2000,
         'title': 'Radioimmunoguided Surgery Using Prostascint for Supraclav Mets',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/2000_RadioimmunoguidedSurgery.pdf",
         'doctype': 'pdf'},
    33:
        {'year': 1990,
         'title': 'CMOS Analog IC X-Ray Image Sensor Array',
         'icon': "more_horiz",
         'location': 'pubs',
         'file': "./_downloads/1990_CMOSAnalogICX-RayImage.pdf",
         'doctype': 'pdf'},
    34:
        {'year': 2020,
         'title': 'San Jose, CA',
         'icon': "./icon/2020_Xoft_Physics_SanJoseCA.jpg",
         'location': 'pics',
         'file': "./full/2020_Xoft_Physics_SanJoseCA.jpg",
         'doctype': 'img'}


    }

years = dict([(key, docs[key]['year']) for key in docs])
titles = dict([(key, docs[key]['title']) for key in docs])
icons =  dict([(key, docs[key]['icon']) for key in docs])
files =  dict([(key, docs[key]['file']) for key in docs])
doc_types =  dict([(key, docs[key]['doctype']) for key in docs])

def keys_of_type(l):
    assert l in ('home', 'press', 'notes', 'pubs', 'pics', 'wiki', 'ebooks', 'safe')
    return([key for key in docs if docs[key]['location']==l])

press_keys = sorted(keys_of_type('press'), key=years.__getitem__, reverse=True)
notes_keys = sorted(keys_of_type('notes'), key=years.__getitem__, reverse=True)
pubs_keys = sorted(keys_of_type('pubs'), key=years.__getitem__, reverse=True)
pics_keys = sorted(keys_of_type('pics'), key=years.__getitem__, reverse=True)
assert pubs_keys == [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]


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
  <link rel="shortcut icon" href="favicon.ico" />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
"""

def make_html_index():
    result = HEAD.format(description = "personal homepage", 
                         keywords = "medical physics, jeff anderson regional cancer center")
    result += '\n<body>\n'
    result += nav_bar('home')
    result += '\n<body>\n<html>\n'
    assert len(result) == 2527
    with open ('index.html', "w") as outfile:
        for line in result:
            outfile.write(line)
# make_html_index()

def make_rows(keys):
    ROW = """\
          <li class="list-group-item">
            <a class="" href="{file}">
              <div class="row">
                <div class="col-sm-1"><span class="material-icons">{icon}</span></div>
                <div class="col-sm-1 text-secondary">{year}</div>
                <div class="col-sm-10 text-secondary">{title}</div>
              </div>
            </a>
          </li>\n"""
    result = ""
    for key in keys:
        if os.path.exists(os.path.splitext(files[key])[0]+".html"):
          result += ROW.format(year = str(years[key]), 
                              title = titles[key],
                                file = os.path.splitext(files[key])[0]+".html",
                                icon = icons[key])
        else:
          result += ROW.format(year = str(years[key]), 
                              title = titles[key],
                                file = files[key],
                                icon = icons[key])

    return(result)                              

#####################
def make_pic_rows(keys):
    ROW = """\
          <li class="list-group-item">
            <a class="" href="{file}">
              <div class="row">
                <div class="col-sm-4"><span style="padding-left: 2px;padding-right:2px; padding-top: 2px; padding-bottom: 2px; display:inline-block;"><img style="max-height:120px" src="./icon/2020_Xoft_Physics_SanJoseCA_icon.jpg"></img></span></div>
                <div class="col-sm-1 text-secondary">{year}</div>
                <div class="col-sm-7 text-secondary">{title}</div>
              </div>
            </a>
          </li>\n"""
    result = ""
    for key in keys:
        if os.path.exists(os.path.splitext(files[key])[0]+".html"):
          result += ROW.format(year = str(years[key]), 
                              title = titles[key],
                                file = os.path.splitext(files[key])[0]+".html",
                                icon = icons[key])
        else:
          result += ROW.format(year = str(years[key]), 
                              title = titles[key],
                                file = files[key],
                                icon = icons[key])

    return(result)                              



#####################



def make_html_press():
    result = HEAD.format(description = "news items and press releases", 
                         keywords = "medical physics, jeff anderson regional cancer center")
    result += '<body>'
    result += nav_bar('press')

    result += """\n  <div class="container-fluid">
    <div class="row">
      <div class="col-12 text-primary">
        <div id="section1" class="">
          <ul class="list-group text-secondary">\n"""
    result += make_rows(press_keys)
    result += '\n          </ul>\n          </div>\n    </div>\n  </div>\n</div>\n</body>\n</html>'
    with open ('press.html', "w") as outfile:
        for line in result:
            outfile.write(line)
make_html_press()

def make_html_notes():
    result = HEAD.format(description = "assorted notes", 
                         keywords = "")
    result += '<body>'
    result += nav_bar('notes')

    result += """\n  <div class="container-fluid">
    <div class="row">
      <div class="col-12 text-primary">
        <div id="section1" class="">
          <ul class="list-group text-secondary">\n"""
    result += make_rows(notes_keys)
    result += '\n          </ul>\n          </div>\n    </div>\n  </div>\n</div>\n</body>\n</html>'
    with open ('notes.html', "w") as outfile:
        for line in result:
            outfile.write(line)
make_html_notes()


def make_html_pubs():
    result = HEAD.format(description = "publications", 
                         keywords = "medical physics, jeff anderson regional cancer center")
    result += '<body>'
    result += nav_bar('pubs')

    result += """\n  <div class="container-fluid">
    <div class="row">
      <div class="col-12 text-primary">
        <div id="section1" class="">
          <ul class="list-group text-secondary">\n"""
    result += make_rows(pubs_keys)
    result += '\n          </ul>\n          </div>\n    </div>\n  </div>\n</div>\n</body>\n</html>'
    with open ('pubs.html', "w") as outfile:
        for line in result:
            outfile.write(line)
make_html_pubs()

def make_html_pics():
    result = HEAD.format(description = "picture gallery", 
                         keywords = "")
    result += '<body>'
    result += nav_bar('pics')

    result += """\n  <div class="container-fluid">
    <div class="row">
      <div class="col-12 text-primary">
        <div id="section1" class="">
          <ul class="list-group text-secondary">\n"""
    result += make_pic_rows(pics_keys)
    result += '\n          </ul>\n          </div>\n    </div>\n  </div>\n</div>\n</body>\n</html>'
    with open ('pics_.html', "w") as outfile:
        for line in result:
            outfile.write(line)
make_html_pics()



def download_container_html(keys):
  downloads = []
  for key in keys:
    result = HEAD
    result += "\n<body>"
    result += nav_bar(docs[key]['location'], depth=1)
    if doc_types[key] == 'pdf':
      content = '\n  <div style="height: 100%;"><object data="{source}" type="application/pdf" width="500" height="678">not found </object></div>'
    elif doc_types[key] == 'img':
      content = '<img src="{source}" style="max-width: 80vw;"> '
    else:
      continue
    result += content.format(source = os.path.split(files[key])[-1])
    result += "\n</body>\n</html>\n"
    with open (os.path.splitext(files[key])[0] + '.html', "w") as outfile:
      for line in result:
        outfile.write(line)
download_container_html(press_keys)
download_container_html(pubs_keys)



# years = dict([(key, docs[key]['year']) for key in docs])
# titles = dict([(key, docs[key]['title']) for key in docs])
# icons =  dict([(key, docs[key]['icon']) for key in docs])
# files =  dict([(key, docs[key]['file']) for key in docs])                         # long filenames with path
# doc_types =  dict([(key, docs[key]['doctype']) for key in docs])                  # 'ppt', 'pdf', 'web', 'img', 'html'
# press_keys = sorted(keys_of_type('press'), key=years.__getitem__, reverse=True)   # file_download', 'more_horiz', 'attachment', 'link'
# notes_keys = sorted(keys_of_type('notes'), key=years.__getitem__, reverse=True)
# pubs_keys = sorted(keys_of_type('pubs'), key=years.__getitem__, reverse=True)

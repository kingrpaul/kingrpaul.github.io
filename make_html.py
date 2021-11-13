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
  

def make_rows(*args):

    """
    Does stuff
    """

    indent = ["\n" + " "*12, "\n" + " "*16, "\n" + " "*20, "\n" + " "*24, "\n" + " "*28]
    material_icons = ["attachment, more_horiz"]

    result = ""
    # print(args)
    for document in args:
        result += indent[0] + '<li class="list-group-item">'
        result += indent[0] + '<div class="row">'
        result += indent[1] + '<div class="col-11">'
        result += indent[2] + document[0]
        result += indent[1] + '</div>'
        result += indent[1] + '<div class="col-1">'
        for link in document[1]:
            result += indent[2] + '<a class="" href="' + link[0] + '" target="_blank">'
            result += indent[3] + '<span class="' + link[1] + '</span>'
            result += indent[2] + '</a>'
        result += indent[1] + '</div>'                            
        result += indent[0] + '</div>'                            
        result +=  indent[0] + '</li>'

    return(result)

press = [
    ['2019<br/>Anderson Regional Cancer Center is the first center in the United States to treat cancer patients using RayStation and the TomoTherapy Treatment Delivery System', 
        [("./_downloads/2019_ARCCIsTheFirstCenterInTheUS.pdf", 
             "attachment"),
         ('./_downloads/2019_ARCCFirstInTheUSToTreat.pdf', 
             "attachment")]],
    ['2018<br/>RaySearch Receives First Order for the RayCare Oncology Information System', 
        [("./_downloads/2018_FirstOrderFo RayCare.pdf", 
            "attachment")]],
    ['2015<br/>Anderson First in State to Offer TomoTherapy for Cancer Patients', 
        [("./_downloads/2015_AndersonFirstInState.pdf", 
            "attachment")]],
    ['2014<br/>Anderson Regional Cancer Center prides itself on providing world class care close to home', 
        [("./_downloads/2014_WorldClassCancerCenter.png", 
            "attachment")]],
    ['2008<br/>Conformal arc radiotherapy planned with Pinnacle3, Jeff Anderson Regional Cancer Center', 
        [("./_downloads/2008_ConformalArcRadiotherapy.pdf", 
            "attachment")]],
    ['2003<br/>Jeff Anderson Celebrates 75th Anniversary with Opening of Jeff Anderson Regional Cancer Center', 
        [("./_downloads/2003_JeffAndersonCelebrates_.pdf", 
            "attachment")]],
    ['2000<br/>Jeff Anderson team pioneers prostate cancer treatment', 
        [("./_downloads/2000_JeffAndersonTeamPPioneers.jpg", 
            "attachment")]]
]

# print(make_rows(*press))

notes =  [
    ['2018<br/>MVCT QA w/TomoHDA &amp; Ray6', 
        [("./notes/mvct_qa/MVCT-QA-with-RS.html", 
             "more_horiz")]],
    ['2018<br/>e- Blk w/TomoHDA &amp; Ray6', 
        [("./notes/electron_rof/Electron Output with RS.html", 
             "more_horiz")]],
    ['2018 <br/>Varian Rails w/Ray6', 
        [("./notes/ray_varian_rails/Varian Rails with RS.html", 
             "more_horiz")]],
    ['2020 <br/>Flash, microLinac, CT', 
        [("./notes/flash_ct/flash_ct.html", 
             "more_horiz")]],
    ['2020 <br/>RayStation X-Ray Rx Scaling', 
        [("./notes/ray_rx_scale/ray_rx_scale.html", 
             "more_horiz")]],
    ['2009 <br/>Ultraviolet Tanning Beds', 
        [("./notes/tanning_beds/policy-brief.html", 
             "more_horiz")]],
    ['2021 <br/>Cadaveric Organ Donation', 
        [("./notes/organ_donor/organ_donor.html", 
             "more_horiz")]],
    ['2021 <br/>Shared Philosophy of the Scientific Revolution', 
        [("./notes/sci_rev_phil/sci_rev_phil.html", 
             "more_horiz")]]
]

# print(make_rows(*notes))

pubs =  [
    ['2019<br/>Simplistic Tomotherapy Model Predicts RayStation Treatment Times Within 20&#37; for First 16 Plans, PO-GePV-T-278, AAPM', 
        [("./_downloads/2019_SimplisticTomotherapyModel.pdf",
             "more_horiz")]],
    ['2014<br/>Simplifying Assumption for Determining Sc and Sp, <span class="text-nowrap">SU-E-T-293</span>, AAPM',
        [("./_downloads/2014_SimplifyingAssumptionFor.pdf",
             "more_horiz")]],
    ['2013<br/>Role of step size &amp; dwell time in inverse opt for prost impl, J Med Phys',
        [("http://www.jmp.org.in/article.asp?issn=0971-6203;year=2013;volume=38;issue=3;spage=148;epage=154;aulast=Manikandan", 
             "link"),
        ("./_downloads/2013_RoleOfStepSizeAndMaxDwell.pdf",
             "more_horiz")]],
    ['2013<br/>Estimation of Eff Fld Size with Leaf-Based Algorithm, <span class="text-nowrap">SU-E-T-7</span>, AAPM',
        [("./_downloads/2013_EstimationOfEffectiveField.pdf",
             "more_horiz"),
        ("./_downloads/2013_EstimationOfEffectiveFieldSize.pptx"
             "file_download")]],
    ['2012<br/>The New Professional’s Resume, NPSC Report, AAPM Newsletter',
        [("./_downloads/2012_NewProfessionalResume.pdf",
             "more_horiz")]],
    ['2010<br/>Therapists should not have to wear personnel dosimetry badges, Med Phys',
        [("./_downloads/2010_RadiationTherapistsShould_.pdf",
             "more_horiz")]],
    ['2008<br/>Comment on the interplay effect in prost IMRT delivery, Med Phys',
        [("./_downloads/2008_CommentOnQuantifying.pdf",
             "more_horiz")]],
    ['2007<br/>Comment on IMRT administered at greater than 10 MV, Med Phys',
        [("./_downloads/2007_CommentOnIMRTShould_.pdf",
             "more_horiz")]],
    ['2004<br/>Reviewer: Radiologic Science for Technologists, 8th Edition, Bushong',
        [("http://amzn.to/23gKJdt",
             "link")]],
    ['2001<br/>A simple method for electron energy constancy measurement, JACMP',
        [("./_downloads/2001_ASimpleMethodForElectron.pdf",
             "more_horiz")]],
    ['2001<br/>In Regard to the ABS Recommendations for Pd-103 Brachytherapy',
        [("./_downloads/2001_InRegardToTheABSRecommendation_.pdf",
             "more_horiz")]],
    ['2001<br/>Geometry function of a linear brachytherapy source, JACMP',
        [("./_downloads/2001_GeometryFunctionOALinear_.pdf",
             "more_horiz")]],
    ['2000<br/>Radioimmunoguided Surgery Using Prostascint for Supraclav Mets',
        [("https://www.ncbi.nlm.nih.gov/pubmed/11018634",
             "link"),
        ("./_downloads/2000_RadioimmunoguidedSurgery.pdf",
             "more_horiz")]],
    ['1990<br/>CMOS Analog IC X-Ray Image Sensor Array',
        [("./_downloads/1990_CMOSAnalogICX-RayImage.pdf",
             "more_horiz</span>")]]
]

print(make_rows(*pubs))

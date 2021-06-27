# -*- coding: utf-8 -*-

"""advocacy.py: Create a webpage."""
__author__      = "Paul King"
__copyright__   = "Copyright 2021, Meridian, MS"
__email__       = "king.r.paul@ieee.org"

import os
from pprint import pprint as pp
from PIL import Image
from PIL.ExifTags import TAGS
from PIL import Image, ExifTags
import re

webpage ="""<!DOCTYPE html PUBLIC"-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="X-UA-Compatible" content="IE=Edge" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title> Policy Brief &#8212; Tanning Beds</title>
    <meta name="author" content="{Paul King}">
    <meta name="description" content="This document is a policy brief advocating for a federal role in the regulation of tanning beds.">
    <meta name=\"keywords\" content=\"skin cancer, melanoma, basal cell carcinoma, squamous cell carcinoma, BCC, SCC, actinic keratosis, dysplastic nevi, malignant, mole, nevus, sun, sunscreen, ultraviolet light, tanning booths\">
    <link rel="stylesheet" href="./alabaster.css" type="text/css" />
    <link rel="stylesheet" href="./pygments.css" type="text/css" />
    <script type="text/javascript" id="documentation_options" data-url_root="../../" src="../../_static/documentation_options.js"></script>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
    <link rel="stylesheet" href="./custom.css" type="text/css" />
    <meta name="viewport" content="width=device-width, initial-scale=0.9, maximum-scale=0.9" />
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
  </head>
  <body>
      <div class="document">
      <div class="documentwrapper">
        <div class="bodywrapper">
          <div class="body" role="main">
            <div class="section" id="policy-brief-tanning-beds">
              <div class="container-fluid row"  style="background-color: #F8E6FF;">
                <div class="container col-sm-9">
                  <h1 style="color: #7030a0;">Policy Brief<br/><small style="color: #9262b7;">One small step can go a long way in protecting American girls from radiogenic skin cancer.</small></h1>
                </div> 
                <div class="container col-sm-3">
                  <img src="Picture1.png" class="rounded float-right img-responsive" alt="tanning bed"> 
                 </div>
              </div>
              <p>Almost half of all cancers occur on the skin making the skin the most common site of cancer induction (Beilenson, 2009). Ultraviolet light is the dominant cause of skin cancer (ACS, 1991) and this disease is projected to cause 11,000 deaths in 2009 (Beilenson, 2009). Tanning beds use electronic ultraviolet (UV) lamps as an artificial source of UV light, which quickly tans the skin of the occupant. These devices were introduced in the U.S. by Friedrich Wolff in 1978 (Houston, 2008). While early in this nation’s history, a fair complexion might signify wealth and the avoidance of outdoor, tan-producing, agrarian labor; today, it more generally implies leisure and is typically associated with the perception of wealth, health, and physical attractiveness (Loh, 2008). So naturally, the tanning bed business has grown into a $5B a year industry (Loh, 2008) with 25,000 tanning salons operating in the U.S. (Hareyan, 2009). In many cities, these near-ubiquitous tanning salons outnumber both Starbucks and McDonalds (Mapes, 2009). On average, over a million Americans per day (Mapes, 2009), or over 30 million each year (Loh, 2008), use a tanning bed to darken their skin. The nation’s rate of skin cancer has paralleled this growth in the use of tanning beds, particularly among people who begin before age 30 (Nyback, 1990). The national incidence of invasive melanoma has more than doubled since tanning beds were introduced in 1978 (NCI, 2009). Tanning beds are primarily used by girls and young women (Reinberg, 2009), with nearly 70% of tanning bed users being female and between the ages of 16 and 29 (Mapes, 2009). One tanning bed user in 13 is an adolescent (Mallis, 2009) with nearly 40% of teenage girls reporting use of a tanning bed within the last year (Beilenson, 2009).</p>
              <p>The UV spectrum produced by tanning beds includes both a more-penetrating UVB component and a less-penetrating UVA component. In addition to being carcinogenic, both UVA and UVB are immunosuppressive (Thomas, 2009) and exposure to ten tanning sessions in two weeks is known to produce immune suppression (Mallis, 2009). The U.S. Food and Drug Administration (FDA) advises that those with certain medical conditions, such as lupus, diabetes, and susceptibility to cold sores; avoid using tanning beds (Reinberg, 2009). The American Cancer Society (ACS), more generally, considers the use of tanning beds to be a health hazard and recommends that they be avoided altogether (Reinberg, 2009). In July, the World Health Organization’s (WHO’s) International Agency for Research on Cancer (IARC) completed a study of tanning beds and re-designated these devices from “probably carcinogenic to humans” into its highest risk category, designating it definitely “carcinogenic to humans” (Reinberg, 2009). IARC found that the risk of melanoma on the skin, the most lethal form of skin cancer, rises 75% when use of tanning beds begins before age 30 and also finds evidence of a link between tanning bed use and the incidence of ocular melanoma (Reinberg, 2009).</p>
              <p>Though many manufacturers are now increasing the more-penetrating UVB component of their tanning beams, to speed up the tanning process (Mallis, 2009), FDA regulation does specify a minimal beam-quality performance standard, which places some restraint on the proportion of the tanning light that is permitted to be in the more-penetrating UVB part of the spectrum (21CFR1040.20). There is a false, but widespread, perception that UVA is “good UV” while UVB is “bad UV” (Mapes, 2009).  And, it is important to recognize that IARC’s designation of UV radiation as “carcinogenic to humans” applies to the full ultraviolet spectrum; the less-penetrating UVA, the more-penetrating UVB, as well as the most-penetrating UVC (Reinberg, 2009). It is also notable that, though FDA regulation requires a manufacturer to specify the UV lamp model for which the tanning bed was designed (21CFR1040.20), it does not prevent substitutions and salon operators often tamper with these lamps to achieve a more intense ultraviolet exposure (Loh, 2008).</p>
              <p>Also, though the manufacturer must post warning labels on the tanning bed (21CFR1040.20), many tanning salon operators misrepresent the health risks, openly advertising that tanning beds do not cause cancer (Loh, 2008) and the industry generally claims that the use of these devices is healthy (Britt, 2006). Tanning beds are often advertised as a safe alternative to exposure to the sun (Mallis, 2009) (FTC, 1997). A German study of indoor-tanners (Borner, Schutz, & Wiedemann, 2009) found a widespread public perception that artificial tanning is safe or even healthy and a widespread, though mistaken, public perception that tanning bed use “prepares” the skin in a protective way for exposure to the sun. It is common practice, for example, among U.S. college students to use tanning lights to create a “base” tan, in anticipation of further near-term solar exposure (ACS, 2000). A minimum erythema dose (MED) is the amount of UV light required to redden exposed skin and, though the MED varies with skin type, a twenty minute tanning bed exposure typically delivers quadruple the minimum erythema dose (Mallis, 2009). An eight-to-twenty minute tanning session often delivers a more intense UV exposure than an entire afternoon spent in natural sunlight (Mallis, 2009).</p>
              <p>Use of a tanning bed is a pleasant experience, producing a sense of relaxation and well being, and research suggests that the use of tanning beds leads the body to produce natural opioids and endorphins (Britt, 2006). But, there is also significant evidence that tanning bed use can be addictive, and discontinuing the use of tanning beds has been observed to produce the withdrawal symptoms of jitteriness and nausea (Britt, 2006). Excessive sun tanning has been identified and studied as a substance-related psychological disorder (Warthan, Uchida, & Wagner, 2005).  Exploiting this, most tanning salons in the U.S. use buffet-style unlimited price packaging (Mapes, 2009) which encourages the frequent and extended use of tanning beds. This positive reinforcement was substantiated by Borner, et al (2009), who found that those who use tanning beds frequently, more than ten times per year; also use them for long durations, greater than fifteen minutes per session.</p> 
              <p>The first priority of WHO, in response to the findings of IARC, is to reduce the use of tanning beds by persons under age 18 (Reinberg, 2009) and in France, where IARC is located, those under age 18 are already prohibited from using tanning beds (Thomas, 2009). Germany is considering, but has not yet enacted age restrictions on the use of tanning beds (Borner, Schutz, & Wiedemann, 2009). In September, Wales banned the use of tanning beds by minors and there is interest in extending this ban to England (Morton & Wighton, 2009). Unmanned, coin-operated tanning booths have made the Welsh law difficult to enforce and coin-operated booths have already been outlawed in Scotland (Morton & Wighton, 2009). Unconstrained by law, U.S. tanning bed operators have been found to make these beds available to tanners at any age and without restraint (Narayan, 2009). </p>
              <p>A study in the Denver area, in fact, concluded that the use of UV tanning-beds was commonly and specifically marketed to adolescents through high school newspaper advertisments and the study’s authors recommended that public health policies prohibit the targeting of minors by tanning booth operators (Freeman, Francis, Lundahl, Bowland, & Dellavalle, 2006). Legal research has found broad similarities in business-model between the indoor tanning industry and the cigarette industry. Both are described as selling an “unreasonably dangerous” carcinogen and in each case it is asserted that the industry systematically lied to its consumers about the health effects associated with an image-motivated, acquired-behavior (Loh, 2008). There is, at present, no national policy restricting the use of tanning beds by minors in the United States (Narayan, 2009).</p>
              <p>Twenty-nine states, however, do regulate the use of tanning beds by minors (Kasprak, 2009) and in 2009, 22 states have introduced (NCSL, 2009) and four states have passed (Kasprak, 2009) new legislation or legislative amendments restricting indoor tanning by minors. Existing and proposed restrictions vary widely, setting limits at the ages of 18, 16, 16½, 15, 14, and 13. In some cases, these laws ban the use of tanning beds outright or ban them without a physician’s prescription, which sometimes must specify a diagnosis or the number of tanning sessions.  Some policies require written parental consent, which must sometimes be given in the presence of the operator. In some cases, this consent must specify the tanning frequency, require positive identification, or even require a notarized signature.  In one case, the tanner must quantify her (or his) skin-type in terms of its sensitivity to the sun.  In some cases, a parent must be present, during the first visit or during all visits. And, in some states, the parent must certify an acknowledgement of the risks or guarantee that the child will use eye protection (NCSL, 2009). </p>
              <p>A pending Texas bill would require that any minor under 18 be both accompanied by a parent and have physician approval (Mapes, 2009), though that state’s law now permits unrestricted use of tanning beds by anyone over age 16 ½ (Beilenson, 2009). Both New York, which has among the fewest tanning salons per capita, and Charleston, WV, which has the most tanning salons per capita (Mapes, 2009), ban the use of tanning beds before age 14 and each requires parental consent until the age of 18 (NCSL, 2009). At the county level, efforts are underway in Howard County, Maryland and Suffolk County, New York to ban the use of tanning beds by persons under age 18 (Beilenson, 2009). In addition to these 29 states, four counties also currently regulate the use of tanning beds by minors (Beilenson, 2009). </p>
              <p>At the U.S. federal level, tanning beds are jointly regulated by the FDA, which enforces manufacturing and labeling standards, and by the Federal Trade Commission (FTC), which seeks to protect consumers against fraud and unfair business practices, including false claims (FTC, 1997).  FDA regulations require that tanning beds be labeled ``DANGER -- Ultraviolet radiation” and carry warnings about the potential for eye injury, skin injury, allergic reaction, premature skin aging, skin cancer, and the increased sensitivity created by some cosmetics and medications (21CFR1040.20) which includes common medications such as antihistamines and oral contraceptives (FTC, 1997). This labeling must also include exposure factors that the manufacturer recommends for use in tanning (21CFR1040.20), but does not constrain what those recommendations should be.  These warning requirements were established in 1985, just seven years after tanning beds were introduced and long before the national incidence of skin cancer had reached its present level. Though an FDA agency review of these warnings began in 2007 (Reinberg, 2009), these requirements have now been in place for a full 24 years. Though FDA regulations do place some limits on the tanning beam’s spectrum, require that a tanning bed be delivered with protective eyewear and a timer, and require that the protective eyewear meet a certain attenuation standard; these regulations place no limit on the intensity of the beam, as it reaches either the skin or the eye (21CFR1040.20).</p>
              <p>In terms of public health, a lighted tanning bed resembles nothing so much as a lit cigarette; with a profitable and well-lobbied industry that dishonestly sells a false image of health and vitality, while targeting a known carcinogen to young American girls, which is delivered through addictive behavior. An international call has been made to protect the public from radiogenic skin cancer by protecting children from ultraviolet tanning booths. The European nations are rapidly answering that call.  In this country, many states, and even some counties, are attempting to respond to this threat to the public’s health by restricting the access of minors to tanning booths. Though these responses have been slow, complicated, fragmented, and inconsistent; a consensus has clearly developed in these regional incubators of national policy.  No tanning booth operator, anywhere in the nation, should be permitted to UV-irradiate children for money any more than any convenience store operator, anywhere in the nation, should be permitted to sell children cigarettes.</p>
              <p>A small, but key, step forward in the protection of children from UV tanning beds would be to amend Title XIX of the Social Security Act to require that each state, as a condition of receiving Medicaid federal matching funds, specify in legislation by 2011, some minimum age limit on the use of commercially operated UV-lamp-based tanning devices and that this age must be no less than 13. First and foremost, this would mandate the creation of some age restriction for the protection of girls in the 21 states where no such protections now exist. It would also catalyze a re-evaluation and tightening of the policies in those states which already have restrictions. Leaving the policy details to the states creates federal leadership and coordination while also showing deference to state sovereignty and a respect for the traditional role of state governments in public health. Linking this policy change to the Medicaid program makes it a joint-venture, undertaken in cooperation between the federal and state governments, intended to protect children, improve the health of the public, and reduce the cost of healthcare to society by reducing the incidence of this very preventable disease.</p>
              <hr/>
              [REFERENCE LIST]
              <p>R. Paul King, MS<br/><time datetime="2009-10-20">October 20, 2009</time></p>
            </div>
          </div>
        </div>
      </div>
    <div class="footer">
      &copy;2019, RPK | Page uses <a href="http://sphinx-doc.org/">Sphinx 1.7.9</a>, <a href="https://github.com/bitprophet/alabaster">Alabaster 0.7.11</a> &amp; <a href="https://getbootstrap.com/docs/3.3/">Bootstrap 3.4.1</a>
    </div>
    [MODALS]
    """

references = {
  "(21CFR1040.20)": "21CFR1040.20. (1985, September 6). Title 21 Volume 8, Parts 800 to 1299. Retrieved from Food and Drugs, Part 1040 -- Performance Standards for Light-Emitting Products: frwebgate.access.gpo.gov",
  "(ACS, 2000)":"ACS. (2000, May 16). Tanning Beds May Increase Skin Cancer Risk. (A. C. Society, Producer) Retrieved 10 11, 2009, from ACS News Center: www.cancer.org",
  "(ACS, 1991)":"ACS. (1991). Textbook of Clinical Oncology (First Edition ed.). (A. I. Holleb, D. J. Fink, & G. P. Murphy, Eds.) Atlanta, GA: American Cancer Society.",
  "(Beilenson, 2009)":"Beilenson, P. L. (2009, September 22). Howard County Seeks to Ban Indoor Tanning for Youth Under 18. Press Packet . Columbia, MD, USA: Howard County Health Department.",
  "(Borner, Schutz, & Wiedemann, 2009) ":"Borner, F. U., Schutz, H., & Wiedemann, P. (2009). A population-based survey on tanning bed use in Germany. BMC Dermatology , 9 (6).",
  "(Britt, 2006)":"Britt, R. R. (2006, March 28). Indoor Tanning Addictive, Study Suggests. (Imaginova, Producer) Retrieved from Live Science: www.livescience.com",
  "(Freeman, Francis, Lundahl, Bowland, & Dellavalle, 2006)":"Freeman, S., Francis, S., Lundahl, K., Bowland, T., & Dellavalle, R. P. (2006). UV Tanning Advertisements in High School Newspapers. Arch Dermatol. , 142 (4), 460-462.",
  "(FTC, 1997)":"FTC. (1997, August). Indoor Tanning. FTC Fact for Consumers , www.ftc.gov . Washington, DC, USA: Federal Trade Commission, Bureau of Consumer Protection, Office or Consumer and Business Education.",
  "(Hareyan, 2009)":"Hareyan, A. (2009, July 29). Despite skin cancer millions use tanning beds. Retrieved from Emax Health, Home>>Cancer Treatment>>Skin Cancer: www.emaxhealth.com",
  "(HealthDay, 2009)":"HealthDay. (2009, September 21). Many Teens Circumvent Tanning Bed Laws. (U. N. Health, Producer) Retrieved from Medlne Plus: www.nlm.nih.gov",
  "(Houston, 2008)":"Houston, R. (2008). Indoor Tanning Beds. Retrieved from indoor tanning beds .net: indoortanningbeds.net",
  "(Kasprak, 2009)":"Kasprak, J. (2009). Tanning Beds. Conneticut General Assembly, Office of Legislative Research.",
  "(Loh, 2008)":"Loh, A. Y. (2008). Are artificial tans the new cigarette? How plaintiffs can use the lessons of tobacco litigation in bringing claims against the indoor tanning industry. Mich Law Rev , 107 (2), 365-390.",
  "(Mallis, 2009)":"Mallis, H. (2009, September). Tanning Beds: Safe Alternative to the Sun? Retrieved from National Research Center For Women & Families: www.center4research.org",
  "(Mapes, 2009)":"Mapes, D. (2009, March 12). In many cities, tanning salons exceed Starbucks. Retrieved October 11, 2009, from MSNBC.com: www.msnbc.msn.com",
  "(Morton & Wighton, 2009)":"Morton, E., & Wighton, K. (2009, October 1). We're dying for a tan. The Sun .",
  "(Narayan, 2009)":"Narayan, A. (2009, October 12). Cancer and Teen Tanning: Where's the Regulation? Time .",
  "(NCI, 2009)":"NCI. (2009, May 29). SEER Cancer Statistics Review 1975-2006. Retrieved from National Cancer Institute - Surveillance Epidemiology and End Results: seer.cancer.gov",
  "(NCSL, 2009)":"NCSL. (2009, October 12). Tanning Restrictions for Minors A State-by-State Comparison. (N. C. Legislators, Producer) Retrieved from NCSL Home > State & Federal Issues: Issue Areas >Health > Tanning Restrictions for Minors state laws summary: //204.131.235.67/programs/health/tanningrestrictions",
  "(Nyback, 1990)":"Nyback, G. (1990, July 29). Staten Islanders who use tanning beds at definite risk for cancer. Staten Island Real-Time News .",
  "(Reinberg, 2009)":"Reinberg, S. (2009, July 28). Tanning Beds Get Highest Carcinogen Rating. U. S. News and World Report.",
  "(Thomas, 2009)":"Thomas, R. (2009, September 2). Should tanning bed be banned for use by teenagers? Retrieved from Skin Care Guide: www.skincareguide.ca",
  "(Warthan, Uchida, & Wagner, 2005)":"Warthan, M. M., Uchida, T., & Wagner, R. F. (2005). UV Light Tanning as a Type of Substance-Related Disorder. ARCH DERMATOL , 141, 963-966."
}

inline_cites = ["(Beilenson, 2009)", "(ACS, 1991)", "(Houston, 2008)", 
  "(Loh, 2008)", "(Hareyan, 2009)", "(Mapes, 2009)", "(Nyback, 1990)", 
  "(NCI, 2009)", "(Reinberg, 2009)", "(Mallis, 2009)", "(Thomas, 2009)", 
  "(21CFR1040.20)", "(Britt, 2006)", "(FTC, 1997)", 
  "(Borner, Schutz, & Wiedemann, 2009)", "(ACS, 2000)", 
  "(Warthan, Uchida, & Wagner, 2005)", "(Morton & Wighton, 2009)", 
  "(Narayan, 2009)", 
  "(Freeman, Francis, Lundahl, Bowland, & Dellavalle, 2006)", 
  "(Kasprak, 2009)", "(NCSL, 2009)"]
cite_num = lambda inline :([""] + inline_cites).index(inline)
# print(cite_num("(Beilenson, 2009)"))

full_ref = lambda inline : {
  "(21CFR1040.20)": "21CFR1040.20. (1985, September 6). Title 21 Volume 8, Parts 800 to 1299. Retrieved from Food and Drugs, Part 1040 -- Performance Standards for Light-Emitting Products: frwebgate.access.gpo.gov",
  "(ACS, 2000)":"ACS. (2000, May 16). Tanning Beds May Increase Skin Cancer Risk. (A. C. Society, Producer) Retrieved 10 11, 2009, from ACS News Center: www.cancer.org",
  "(ACS, 1991)":"ACS. (1991). Textbook of Clinical Oncology (First Edition ed.). (A. I. Holleb, D. J. Fink, & G. P. Murphy, Eds.) Atlanta, GA: American Cancer Society.",
  "(Beilenson, 2009)":"Beilenson, P. L. (2009, September 22). Howard County Seeks to Ban Indoor Tanning for Youth Under 18. Press Packet . Columbia, MD, USA: Howard County Health Department.",
  "(Borner, Schutz, & Wiedemann, 2009)":"Borner, F. U., Schutz, H., & Wiedemann, P. (2009). A population-based survey on tanning bed use in Germany. BMC Dermatology , 9 (6).",
  "(Britt, 2006)":"Britt, R. R. (2006, March 28). Indoor Tanning Addictive, Study Suggests. (Imaginova, Producer) Retrieved from Live Science: www.livescience.com",
  "(Freeman, Francis, Lundahl, Bowland, & Dellavalle, 2006)":"Freeman, S., Francis, S., Lundahl, K., Bowland, T., & Dellavalle, R. P. (2006). UV Tanning Advertisements in High School Newspapers. Arch Dermatol. , 142 (4), 460-462.",
  "(FTC, 1997)":"FTC. (1997, August). Indoor Tanning. FTC Fact for Consumers , www.ftc.gov . Washington, DC, USA: Federal Trade Commission, Bureau of Consumer Protection, Office or Consumer and Business Education.",
  "(Hareyan, 2009)":"Hareyan, A. (2009, July 29). Despite skin cancer millions use tanning beds. Retrieved from Emax Health, Home>>Cancer Treatment>>Skin Cancer: www.emaxhealth.com",
  "(HealthDay, 2009)":"HealthDay. (2009, September 21). Many Teens Circumvent Tanning Bed Laws. (U. N. Health, Producer) Retrieved from Medlne Plus: www.nlm.nih.gov",
  "(Houston, 2008)":"Houston, R. (2008). Indoor Tanning Beds. Retrieved from indoor tanning beds .net: indoortanningbeds.net",
  "(Kasprak, 2009)":"Kasprak, J. (2009). Tanning Beds. Conneticut General Assembly, Office of Legislative Research.",
  "(Loh, 2008)":"Loh, A. Y. (2008). Are artificial tans the new cigarette? How plaintiffs can use the lessons of tobacco litigation in bringing claims against the indoor tanning industry. Mich Law Rev , 107 (2), 365-390.",
  "(Mallis, 2009)":"Mallis, H. (2009, September). Tanning Beds: Safe Alternative to the Sun? Retrieved from National Research Center For Women & Families: www.center4research.org",
  "(Mapes, 2009)":"Mapes, D. (2009, March 12). In many cities, tanning salons exceed Starbucks. Retrieved October 11, 2009, from MSNBC.com: www.msnbc.msn.com",
  "(Morton & Wighton, 2009)":"Morton, E., & Wighton, K. (2009, October 1). We're dying for a tan. The Sun .",
  "(Narayan, 2009)":"Narayan, A. (2009, October 12). Cancer and Teen Tanning: Where's the Regulation? Time .",
  "(NCI, 2009)":"NCI. (2009, May 29). SEER Cancer Statistics Review 1975-2006. Retrieved from National Cancer Institute - Surveillance Epidemiology and End Results: seer.cancer.gov",
  "(NCSL, 2009)":"NCSL. (2009, October 12). Tanning Restrictions for Minors A State-by-State Comparison. (N. C. Legislators, Producer) Retrieved from NCSL Home > State & Federal Issues: Issue Areas >Health > Tanning Restrictions for Minors state laws summary: //204.131.235.67/programs/health/tanningrestrictions",
  "(Nyback, 1990)":"Nyback, G. (1990, July 29). Staten Islanders who use tanning beds at definite risk for cancer. Staten Island Real-Time News .",
  "(Reinberg, 2009)":"Reinberg, S. (2009, July 28). Tanning Beds Get Highest Carcinogen Rating. U. S. News and World Report.",
  "(Thomas, 2009)":"Thomas, R. (2009, September 2). Should tanning bed be banned for use by teenagers? Retrieved from Skin Care Guide: www.skincareguide.ca",
  "(Warthan, Uchida, & Wagner, 2005)":"Warthan, M. M., Uchida, T., & Wagner, R. F. (2005). UV Light Tanning as a Type of Substance-Related Disorder. ARCH DERMATOL , 141, 963-966."
}[inline]
# print(full_ref("(Beilenson, 2009)"))

def make_ref_list():
  ref_list = [full_ref(cite) for cite in inline_cites]
  result ="\n"
  result += " "*14 + '<h4 class="text-center">References</h4>\n'
  result += " "*16 + '<table class="docutils footnote" frame="void" id="f1" rules="none">\n'
  result += " "*18 + '<tbody valign="top">\n'
  for num,item in enumerate(ref_list):
    result += " "*22 + '<tr>'
    result += '<td>' + str(num + 1) + '. </td>'
    result += '<td>'
    result += item
    result += "</td>"
    result += '</tr>\n'
  result += " "*18 + '</tbody>\n'
  result += " "*16 + '</table>\n'
  return(result)

def make_ref(num):
  pt1 = '<a href="#" data-toggle="tooltip" data-placement="top" title="click">'
  pt1 += '<sup class="text-info font-weight-bold" data-toggle="modal" data-target="#modal_'
  pt2 = '">'
  pt3 = '</sup></a>'
  return pt1 + str(num) + pt2 + str(num) + pt3

def make_modals():
  result = '<!-- Modals -->\n'
  for cite in inline_cites:
    num = cite_num(cite)
    result += '    <!-- ' + str(num) + ' -->\n'
    result += '     <div class="modal fade" id="modal_' +  str(num) + '" role="dialog">\n'    
    result += '       <div class="modal-dialog">\n'
    result += '         <div class="modal-content">\n'
    result += '           <div class="modal-header">\n'
    result += '             <button type="button" class="close" data-dismiss="modal">&times;</button>\n'
    result += '             <h4 class="modal-title">' + cite + '</h4>\n'
    result += '           </div>\n'
    result += '           <div class="modal-body">\n'
    result += '             <p>'+ full_ref(cite) + '</p>\n'
    result += '           </div>\n'
    result += '           <div class="modal-footer">\n'
    result += '             <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n'
    result += '           </div>\n'
    result += '         </div>\n'
    result += '       </div>\n'
    result += '     </div>'
  return(result)

for cite in inline_cites:
  webpage = webpage.replace(" " + cite, make_ref(cite_num(cite)))
  webpage = webpage.replace(cite, make_ref(cite_num(cite)))
webpage = webpage.replace('[REFERENCE LIST]', make_ref_list())

abbrevs = {"UV": "ultraviolet", "FDA": "Food and Drug Administration", 
  "IARC": "International Agency for Research on Cancer", 
  "FTC": "Federal Trade Commission", "WHO": "World Health Organization",
  "MED": "minimum erythema dose"}
for abbr in abbrevs:
  webpage = webpage.replace(abbr, '<abbr title="' + abbrevs[abbr] + '">' + abbr + '</abbr>')

webpage = webpage.replace('[MODALS]', make_modals())

with open("advocacy_py.html", "w") as html:
  html.write(webpage)
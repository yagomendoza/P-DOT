############################################################################################
#
# P-DOT
# Programmable database for my on-chain trades.
#
# Creation Date: 2022-04-12
# Last Modification: 2022-04-12
# Version: 1
#
# Main author: Yago MENDOZA
# 
# Python version: 3.8.2
############################################################################################

# -*- coding: utf-8 -*-

import requests
from f_aux import MLPrint

def getContent(web_url):
    try:
        r = requests.get(web_url)
        return str(r.content)
    except:
        mss = ['The request to access the source code of the following page failed.',
               web_url,
               'Suspected causes',
               '- Global page downtime',
               '- Wrong request function arguments'
            ]
        MLPrint(*mss)
    
def cuter (content,pre_elem,post_elem):
    r = ''
    try:
        p_ = content.find(pre_elem)
        content = content[p_+len(pre_elem):]
        for el in content:
            if el != post_elem:
                r+=el
            else:
                return r
    except:
        pass
    

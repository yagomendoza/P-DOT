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

from online_data_scrapper import cuter, getContent

def get_current_market_price (coin_name):
    return float(
        cuter(getContent('https://coinmarketcap.com/currencies/'+coin_name.lower()+'/'),
              '"statistics":{"price":',
              ',')
             )
############################################################################################
#
# P-DOT
# Programmable database for my on-chain trades.
#
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

DATABASE_FILE = 'operation_data_base.txt'

def open_data_base ():
    with open(DATABASE_FILE) as f:
        return [line.strip() for line in f.readlines()]




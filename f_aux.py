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

def MLPrint (*args):
    '''
    Parameters
    ----------
    *args : TYPE
        It accepts both a list of phrases and an unlimited set of string arguments,
        although in the first case the argument must be introduced by means of the
        special character "*".
    '''
    for line in args:
        print(line)
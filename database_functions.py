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

from datetime import datetime
from access_functions import open_data_base

class operation ():
    
    def __init__ (self, operation_row):
        
        '''
        Examples
        
        0000001|2022/04/12/16/44|purchase|BTC(bitcoin)|0.00616/1.55/40155.1596|BINANCE|""
        0000002|2022/04/12/16/44|sale|BTC(bitcoin)|0.00616/1.55/40717.1333|COINBASE|""
        0000003|2022/04/12/16/44|swap|BTC(bitcoin)/BTC(bitcoin)|0.00616/1.55|BINANCE|""
        0000004|2022/04/12/16/44|transfer|BTC(bitcoin)|0.00616/1.55|BINANCE/COINBASE|staking or storage or yield farming|""
        0000004|2022/04/12/16/44|get|BTC(bitcoin)|0.00616/1.15|BINANCE|""
        0000004|2022/04/12/16/44|pay|BTC(bitcoin)|0.00616/1.15|BINANCE|""
        
        '''
        
        pts = operation_row.split('|')
        
        self.ID = pts[0]
        self.datetime = datetime(*[int(_) for _ in pts[1].split('/')])
        self.type = pts[2]
        
        if self.type != "swap":
            self.coin = pts[3][:-1].split('(')
        else:
            self.gvn_coin = [c[:-1].split('(') for c in pts[3].split('/')][0]
            self.obt_coin = [c[:-1].split('(') for c in pts[3].split('/')][1]
        
        nms = pts[4].split('/')
        if self.type in ['purchase','sale']:
            self.market_price = float(nms[-1])
        self.total = float(nms[0])
        self.fee = float(nms[1])
        
        if self.type != 'transfer':
            self.location = pts[5]
        else:
            self.departure_location = pts[5].split('/')[0]
            self.arrival_location = pts[5].split('/')[1]
            
        if self.type == 'transfer':
            self.purpose = pts[6]
        
        self.description = pts[-1][1:-1]
            

'''
CLASS DATABASE (contains class operation)

Database.display_coins(non_existent=True/False, name=True, acronym=True)

Database.select('acronym' or 'name') (como un filter) >> new database
'''

class CryptoDatabase (list):
    
    def __init__ (self):
        
        for row in open_data_base():
            self.append(operation(row))
            
    
    def filter (self,a):
        
        return 4
    
    def add_op (self):
    
        available_types = ["purchase","sale","swap","transfer","get","pay"]
        
        print('OPERATION TYPE '+"*"*14)
        gen = (_ for _ in range(len(available_types)))
        for type in available_types:
            n = next(gen)+1
            if n==1:
                print("*can be either "+"'"+type+"'"+" "+"("+str(n)+")")
            else:
                print(" "*(23-len(type))+"'"+type+"'"+" "+"("+str(n)+")")
        
        type_pt = available_types[int(input('>> Operation type : '))-1]
        
        print('DATETIME '+"*"*20)
        year = int(input('Year : '))
        month = int(input('Month : '))
        day = int(input('Day : '))
        hour = int(input('Hour : '))
        minute = int(input('Minute : '))
        second = int(input('Second : '))
        
        datetime_pt = '/'.join(year,month,day,hout,minute,second)
        
        print('COIN(s)/TOKEN(s) '+"*"*13)
        
        if self.type != "swap":
            coin_name = input('Coin/token name : ')
            coin_acronym = input('Coin/token acronym : ')
            
            coin_pt = coin_acronym.upper()+"("+coin_name.lower()+")"
            
        else:
            og_coin_name = input('Outgoing coin/token name : ')
            og_coin_name_coin_acronym = input('Outgoing coin/token acronym : ')
            ic_coin_name = input('Incmoing coin/token name : ')
            ic_coin_acronym = input('Incoming coin/token acronym : ')
            
            coin_ptA = og_coin_acronym.upper()+"("+og_coin_name.lower()+")"
            coin_ptB = ic_coin_acronym.upper()+"("+ic_coin_name.lower()+")"
            
            coin_pt = coin_ptA+"/"+coin_ptB
        
        print('RAW DATA '+"*"*¿?)
        print('LOCATION '+"*"*¿?)
        ### print('Purpose '+"*"*¿?)
        print('DESCRIPTION (optional) '+"*"*¿?)


    def display_coins(self,name=True,acronym=True,
                      non_existent=False):
        coins = []
        for op in self:
            coins.append(op)
            
class Portafolio (dict):
    
    def __init__ (self):
        
        self.a = HACER EL COMPUTO FINAL DE COMO VAN LAS CSOAS (que no las estadisticas)
        
        
        
        

    

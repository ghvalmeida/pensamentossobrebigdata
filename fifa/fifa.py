# -*- coding: utf-8 -*-

import urllib
import json
import sys
from time import gmtime, strftime
import random
import copy
import time

matches = { 
  #'IMT57': u'Quarta-de-final Partida 57: Brasil x W50 (Colômbia ou Uruguai) em Fortaleza',
  #'IMT58': u'Quarta-de-final W53 (França ou Nigéria) x W54 (Alemanha ou Argélia) no Rio de Janeiro',
  #'IMT59': u'Quarta-de-final W51 (Holanda ou México) x W52 (Costa Rica ou Grécia) em Salvador',
  #'IMT60': u'Quarta-de-final W55 (Argentina ou Suíça) x W56 (Bélgica ou Estados Unidos) em Brasília',
  'IMT61': u'Semi-final W57 (Sequência do Brasil) x W58 em Belo Horizonte',
  'IMT62': u'Semi-final W59 x W60 em São Paulo',
  #'IMT63': u'3o. e 4o. lugares L61 x L62 em Brasília',
  'IMT64': u'Final W61 x W62 no Rio de Janeiro' 
}

categories = { '1': u'Categoria 1',
               '2': u'Categoria 2',
               '3': u'Categoria 3',
               '4': u'Categoria 4' 
               #'5': u'Cadeirante',
               #'13': u'Deficiência',
               #'14': u'Obeso' 
}

def emit_alert():
  for i in range(1,20):
    print '\a'
  time.sleep(59)
     
def get_datetime():
  return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def main():
  print 'System stared at ' + get_datetime()
  print 'Monitoring matches'
  print json.dumps(matches, sort_keys=True, indent=4, separators=(',', ': '))
  print 'Monitoring categories'
  print json.dumps(categories, sort_keys=True, indent=4, separators=(',', ': '))

  json_fifa = read_json_fifa()
  last_product_prices_quantity = process_json_data(json_fifa) 

  while True:
    json_fifa = read_json_fifa()
    product_prices_quantity = process_json_data(json_fifa)

#    if (len(last_product_prices_quantity) and
#       random.random() > 0.5):
#      print 'Randomly increasing quantity'
#      product_price = copy.deepcopy(last_product_prices_quantity[0])
#      product_price['Quantity'] = int(product_price['Quantity']) + 100 
#      product_prices_quantity.append(product_price)
#
#    if random.random() > 0.9:
#      print 'New random price'
#      qtty = random.randint(1, 10)
#      category = random.randint(1, 5)
#      product_prices_quantity.append( { "PRPCategoryId": category, "PRPProductId": "IMT64", "Quantity": qtty } )

    diff = product_prices_diff(product_prices_quantity, last_product_prices_quantity)
    if len(diff):
      print get_datetime()
      print json.dumps(diff, sort_keys=True, indent=4, separators=(',', ': '))
      #emit_alert()

    last_product_prices_quantity = product_prices_quantity

def product_prices_diff(product_prices, last_product_prices):
  result = []
  for product_price in product_prices:
    found = False
    for last_product_price in last_product_prices:
      if (product_price['PRPCategoryId'] == last_product_price['PRPCategoryId'] and
          product_price['PRPProductId'] == last_product_price['PRPProductId']):
        found = True
        if int(product_price['Quantity']) > int(last_product_price['Quantity']):
          result.append(product_price)
          break
    if not found:
      result.append(product_price)
  return result;
    
def filter_product_prices(product_prices):
  filtered = []
  for product_price in product_prices:
    if (int(product_price['Quantity']) > 0 and
        matches.has_key(product_price['PRPProductId']) and
        categories.has_key(product_price['PRPCategoryId'])):
      filtered.append(product_price)
  return filtered


def process_json_data(json_fifa):
  filtered_product_prices = []
  #print json.dumps(json_fifa, sort_keys=True, indent=4, separators=(',', ': '))
  d = json_fifa['d']
  #print json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
  data = d['data']
  #print json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
  data_str = ''
  for d in data:
    data_str = data_str + d
  #print data_str
  data_json = json.loads(data_str)
  #print json.dumps(data_json, sort_keys=True, indent=4, separators=(',', ': '))
  product_prices = data_json['BasicCodes']['PRODUCTPRICES']
  #print json.dumps(product_prices, sort_keys=True, indent=4, separators=(',', ': '))
  filtered_product_prices = filter_product_prices(product_prices)
  # print json.dumps(filtered_product_prices, sort_keys=True, indent=4, separators=(',', ': '))
  return filtered_product_prices


def read_json_fifa():
  result = urllib.urlopen('https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c=BRA')
  #print result
  json_fifa_txt = result.read()
  json_fifa = json.loads(json_fifa_txt)
  return json_fifa 

if __name__ == "__main__":
   main()

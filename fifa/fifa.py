# -*- coding: utf-8 -*-

import urllib
import json
import sys
from time import gmtime, strftime

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
     
def get_datetime():
  return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def main():
  print 'System stared at ' + get_datetime()
  print 'Monitoring matches'
  print json.dumps(matches, sort_keys=True, indent=4, separators=(',', ': '))
  print 'Monitoring categories'
  print json.dumps(categories, sort_keys=True, indent=4, separators=(',', ': '))
  print emit_alert()

  json_fifa = read_json_fifa()
  last_product_prices_quantity = process_json_data(json_fifa) 

  while True:
    json_fifa = read_json_fifa()
    product_prices_quantity = process_json_data(json_fifa)
    #print json.dumps(product_prices_quantity, sort_keys=True, indent=4, separators=(',', ': '))
    if product_prices_quantity != last_product_prices_quantity:
      print get_datetime()
      print json.dumps(product_prices_quantity, sort_keys=True, indent=4, separators=(',', ': '))
      emit_alert()

def dict_diff():
  return ''
    
def filter_product_prices(product_prices):
  filtered = []
  for product_price in product_prices:
    if (product_price['Quantity'] != '-1' and
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
#json_fifa = {"d": {"general_message": "null", "errors": [], "success": "true", "Type": "null", "actionOnSuccess": "null", "dataExtra": "null", "__type": "TOPS.ajaxResponse", "data": "{\"BasicCodes\":{\"PRODUCTPRICES\":[{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"5\",\"Quantity\":\"0\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"1\",\"Quantity\":\"1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"1\",\"Quantity\":\"0\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"2\",\"Quantity\":\"0\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"3\",\"Quantity\":\"43\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"5\",\"Quantity\":\"0\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"5\",\"Quantity\":\"3\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"}]}}", "data2": "null"}}

if __name__ == "__main__":
   main()
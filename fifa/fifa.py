# -*- coding: utf-8 -*-

import urllib
import json
import sys
from time import gmtime, strftime
import random
import copy
import time

shall_print = False
mock_prices = []
mock = {
    "d": {
        "Type": "null",
        "__type": "TOPS.ajaxResponse",
        "actionOnSuccess": "null",
        "data": "{\"BasicCodes\":{\"PRODUCTPRICES\":[{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT01\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT02\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT03\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT04\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT05\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT06\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT07\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT08\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT09\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT10\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT11\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT12\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT13\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT14\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT15\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT16\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT17\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT18\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT19\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT20\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT21\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT22\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT23\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT24\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT25\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT26\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT27\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT28\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT29\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT30\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT31\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT32\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT33\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT34\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT35\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT36\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT37\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT38\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT39\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT40\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT41\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT42\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT43\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT44\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT45\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT46\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT47\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT48\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT49\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT50\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT51\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT52\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT53\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT54\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT55\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT56\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT57\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT58\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT59\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT60\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT61\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT62\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT63\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"1\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"2\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"3\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"4\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"5\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"13\",\"Quantity\":\"-1\"},{\"PRPProductId\":\"IMT64\",\"PRPCategoryId\":\"14\",\"Quantity\":\"-1\"}]}}",
        "data2": "null",
        "dataExtra": "null",
        "errors": [],
        "general_message": "null",
        "success": True
    }
}

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
  print '\a'*20
  time.sleep(59)
     
def get_datetime():
  return strftime("%Y-%m-%d %H:%M:%S", gmtime())

def main():
  print 'System stared at ' + get_datetime()
  print 'Monitoring matches'
  print json.dumps(matches, sort_keys=True, indent=4, separators=(',', ': '))
  print 'Monitoring categories'
  print json.dumps(categories, sort_keys=True, indent=4, separators=(',', ': '))

  #build_mock()

  #json_fifa = read_json_mock()
  json_fifa = read_json_fifa()
  last_product_prices_quantity = process_json_data(json_fifa) 

  while True:
    #json_fifa = read_json_mock()
    json_fifa = read_json_fifa()
    if shall_print:
      print 'Shall print'

    product_prices_quantity = process_json_data(json_fifa)

    diff = product_prices_diff(product_prices_quantity, last_product_prices_quantity)
    if shall_print:
      print 'Last'
      print last_product_prices_quantity
      print 'Current'
      print product_prices_quantity
      print 'Diff'
      print diff

    if len(diff):
      print get_datetime()
      print json.dumps(diff, sort_keys=True, indent=4, separators=(',', ': '))
      emit_alert()

    last_product_prices_quantity = product_prices_quantity
    time.sleep(5)

def product_prices_diff(product_prices, last_product_prices):
  result = []
  for product_price in product_prices:
    for last_product_price in last_product_prices:
      if (product_price['PRPCategoryId'] == last_product_price['PRPCategoryId'] and
          product_price['PRPProductId'] == last_product_price['PRPProductId']):
        if int(product_price['Quantity']) > int(last_product_price['Quantity']):
          print 'Increasing quantity'
          result.append(copy.deepcopy(product_price))
        break
  return result;
    
def filter_product_prices(product_prices):
  filtered = []
  for product_price in product_prices:
    if (matches.has_key(product_price['PRPProductId']) and
        categories.has_key(product_price['PRPCategoryId'])):
      filtered.append(copy.deepcopy(product_price))
  return filtered


def process_json_data(json_fifa):
  filtered_product_prices = []
  #print json.dumps(json_fifa, sort_keys=True, indent=4, separators=(',', ': '))
  product_prices = json_fifa 
  #print json.dumps(product_prices, sort_keys=True, indent=4, separators=(',', ': '))
  filtered_product_prices = filter_product_prices(product_prices)
  # print json.dumps(filtered_product_prices, sort_keys=True, indent=4, separators=(',', ': '))
  return filtered_product_prices

def build_mock():
  global mock
  global mock_prices

  d = mock['d']
  data = d['data']
  data_str = ''
  for d in data:
    data_str = data_str + d
  data_json = json.loads(data_str)
  mock_prices = data_json['BasicCodes']['PRODUCTPRICES']  

def alter_mock():
  global mock_prices
  global shall_print

  found = False
  i = random.randint(0, len(mock_prices)-1)
  if random.random() > 0.7:
    product_price = mock_prices[i]
    if random.random() > 0.1:
      product_price['Quantity'] = -1
    else:
      if (matches.has_key(product_price['PRPProductId']) and
          categories.has_key(product_price['PRPCategoryId'])):
        found = True 
      if found:
        print 'Increasing tickets'
        print 'Old'
        print product_price
      product_price['Quantity'] = int(product_price['Quantity']) + random.randint(5, 10) 
      if found:
        print 'New'
        print product_price
  if found:
    print 'Found. Shall print'
    shall_print = True
  else:
    shall_print = False

def read_json_mock():
  global mock_prices
  alter_mock()
  return mock_prices 

def read_json_fifa():
  try:
    url_result = urllib.urlopen('https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c=BRA')
  except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
    return []
  except:
    raise

  if url_result.getcode()<>200:
    return []
  json_fifa_txt = url_result.read()
  json_fifa = json.loads(json_fifa_txt)
  #print json.dumps(json_fifa, sort_keys=True, indent=4, separators=(',', ': '))

  d = json_fifa['d']
  data = d['data']
  data_str = ''
  for d in data:
    data_str = data_str + d
  data_json = json.loads(data_str)
  product_prices = data_json['BasicCodes']['PRODUCTPRICES']

  return product_prices 

if __name__ == "__main__":
   main()

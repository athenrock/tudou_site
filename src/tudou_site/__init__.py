# /usr/bin/env python
# -*- coding: utf-8 -*-  
#---------------------------------------  
#   程序：   
#   作者：wanghui  
#   日期：15-12-31
#   语言：Python   
#   操作：  
#   功能：
#---------------------------------------  

import datetime
import settings
import redis

rds = redis.StrictRedis(**settings.redis_option)

# /usr/bin/env python
# -*- coding: utf-8 -*-  
# ---------------------------------------
#   程序：   
#   作者：wanghui  
#   日期：15-12-31
#   语言：Python   
#   操作：  
#   功能：
# ---------------------------------------
import os.path

mysql_option = dict(
    host='192.168.8.246',
    port=4406,
    db='spk',
    passwd='12345678',
    user='ytx'
)
verify_option = dict(
    verify_code_timeout=60
)

redis_option = dict(
    host='192.168.8.246',
    port=6379,
    db=0,
    password=None,
)

mail_option = dict(
    mail_host="smtp.263.net",  # 设置服务器
    mail_user="yktong@vansky.cn",  # 用户名
    mail_pass="vansky001",  # 口令
    mail_postfix="vansky.cn",  # 发件箱的后缀
)
api_host = "http://api.m.shangpin.com/api"

upload_path = "/data/yktong/uploads"  # 与nginx配置相同

app = dict(
    template_path=os.path.join(os.path.dirname(__file__), "../templates"),
    static_path=os.path.join(os.path.dirname(__file__), "../static"),
    xsrf_cookies=True,
    cookie_secret="uj2&amp;e*-28+=q*w5r@jgtsujm#*#-_eg5nbf#s&amp;jbv3&amp;na086mhk",
    session_secret="ujijl;dsak8(&23kjsddngni88&^&#@4sdkjfkdgi9;_324jndgiajsdifjdgns",
    session_timeout=6000,
    # pwd_secret="Jug%&_12HH719h23_&^%$13mzo",
    pwd_secret="Jug%&_12HH7123_&^%$13mzo",
    login_url="/login",
    debug=True,
)

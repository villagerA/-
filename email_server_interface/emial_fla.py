# -*-coding=utf-8 -*-
from flask import Flask
from flask import request
import os
import sys
import urllib2
import re
import mysql.connector
import time
import datetime

import codecs


reload(sys)
sys.setdefaultencoding('utf8')
conn = mysql.connector.connect(
    user='root',
    password='123456',
    database='allin',
    charset="utf8")
cursor = conn.cursor()

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # return '<h1>Home</h1>'
    cursor.execute('show tables')
    rows = cursor.fetchall()
    keywords=''
    for i in rows:
        if i[0]!='shedule':
            keywords = keywords+i[0]+' '
    keywords = keywords.strip().replace(' ',', ')

    return '''<h1>Home</h1>
                <p>当前存在的关键词有：{}</p>
                <p>你想发送的关键词为</p>
              <form action="/getnum" method="post">
              <p><input name="keyword"></p>
              <p><button type="submit">开始</button></p>
              </form>
              '''.format(keywords)


# @app.route('/signin', methods=['GET'])
# def signin_form():
#     return '''<form action="/signin" method="post">
#               <p><input name="username"></p>
#               <p><input name="password" type="password"></p>
#               <p><button type="submit">Sign In</button></p>
#               </form>'''

@app.route('/getnum', methods=['POST'])
def getnum():
    # 需要从request对象读取表单内容：
    keyword = request.form['keyword']
    # return keyword

    keyword2 = '\'' + keyword + '\''
    # # keyword = '\'smartcity\''
    # return 'select email from smartcity where keyword = '+keyword2+' LIMIT 5'

    cursor.execute('select count(email) from '+keyword+' where keyword = '+keyword2)
    # conn.commit()
    rows = cursor.fetchall()
    cursor.execute('select shedule from shedule where keyword = '+keyword2)
    srows = cursor.fetchall()
    # str = ''
    # for i in rows:
    #     em = "-c " + i[0] + ' '
    #     str = str + em
    # order = '#!/bin/bash' +'\r\n'+'(echo "Content-Type: text/html";cat mail.txt)|/usr/sbin/sendmail ' + str
    # fw2 = codecs.open('D:\\bashss.sh', 'w', 'utf-8')
    # fw2.write(order)
    return '''<h1>关键词状态</h1>
                <p>关键词 {} 的数目为：{}<p>
                <p>上次发送的位置为：{}<p>
                <form action="/sendemail" method="post">
                    <p><input  type = "hidden" name="keyword" value = {}></p>
                    <p>发送邮箱开始的位置为：</p>
                    <p><input name="start"></p>
                    <p>发送邮箱的数目：</p>
                    <p><input name="num"></p>
                    <p><button type="submit">发送</button></p>
                </form>
                '''.format(keyword, rows[0][0],srows[0][0],keyword)


@app.route('/sendemail', methods=['POST'])
def sendemail():
    # 需要从request对象读取表单内容：
    keyword = request.form['keyword']
    # return keyword

    keyword2 = '\'' + keyword + '\''
    start = request.form['start']
    num = request.form['num']
    # # keyword = '\'smartcity\''
    # return 'select email from '+keyword+' where keyword = '+keyword2+' LIMIT 5'

    cursor.execute('select email from '+keyword+' where keyword = '+keyword2+'  LIMIT '+start+','+num)
    # conn.commit()
    rows = cursor.fetchall()
    str1 = ''
    for i in rows:
        em = "-c " + i[0] + ' '
        str1 = str1 + em
    order = '#!/bin/bash' +'\r\n'+'(echo "Content-Type: text/html";cat mail.txt)|/usr/sbin/sendmail ' + str1
    shedule = str(int(start)+int(num))
    cursor.execute('update shedule set shedule ='+shedule+'  where keyword = '+keyword2)
    # order = '(echo "Content-Type: text/html";cat mail.txt)|/usr/sbin/sendmail -c 478203136@qq.com -c 2594400136@qq.com'
    # fw2 = codecs.open('/ss.sh', 'w', 'utf-8')
    # fw2.write(order)
    # os.system(order)
    return '''<h1>命令已生成</h1>
                <p>%s</p>''' % order



if __name__ == '__main__':
    app.run(port=5001)

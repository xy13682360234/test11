#!/usr/bin/python3
# encoding:utf-8
from flask import Flask, url_for, jsonify, render_template, request
import flask
import time
# url_for 接受两个参数（endpoint,**value）endpoint没有指定就是默认的函数名，根据 view_func.__name__
import test111
import pymysql
import json
import requests
app = Flask(__name__)
import decimal
import re

import datetime
import json

# 解决jsonify中文乱码
class Config(object):
    DEBUG = True
    JSON_AS_ASCII = False

# 解决jsonify中文乱码从配置对象来加载配置
app.config.from_object(Config)

#处理TypeError: Object of type datetime is not JSON serializable 问题
#dic = {'name': 'jack', 'create_time': datetime.datetime(2019, 3, 19, 10, 6, 6)}
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)

class DateDecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        super(DecimalEncoder, self).default(obj)

# 规避TypeError: Object of type ‘Decimal‘ is not JSON serializable报错
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)
class mysqltest(object):
    def __init__(self):
        self.host = 'localhost'
        self.user = 'root'
        self.password = '000000'
        self.port = 3306
        self.database = 'test'
class mysqltest():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)




@app.route('/url_for/')
def url_for_demo():
    return 'url_for_demo'
@app.route('/index/')
def index():
  #        函数的名字
  return url_for('url_for_demo')
@app.route('/API/query/ChineseLessThanMath', endpoint='test112',methods=['GET'])
def ChineseLessThanMath():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test')

    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    sql = "select t1.s_score as '语文',t2.s_score as '数学',t1.s_id,t3.* from\
      (select s_score,s_id from score where c_id ='01') t1,\
      (select s_score,s_id  from score where c_id ='02') t2, student t3 where t1.s_id=t2.s_id and t1.s_id=t3.s_id and t1.s_score <t2.s_score"
    print(sql)
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data1 = cursor.fetchone()
    data = cursor.fetchall()
    db.close()
    print('data:', data, '\n', 'data1:', data1)
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    # return json.dumps(data, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren1)

@app.route('/content.html', methods=['get'])
def content(name=None):
    return render_template('content.html')

@app.route('/right.html', methods=['get'])
def right(name=None):
    class Person(object):
        Email = 'XXX@XXX.com';
        time = time.time();

    dell=Person()

    context={
        'username':"王亚锋",
        'age': "18",
        'gender': "男",
        'flag': "王者",
        'hero': "猴子",
        'person':dell,
        'wwwurl':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('right.html', **context)

@app.route('/left.html', methods=['get'])
def left(name=None):
    class Person(object):
        Email = 'XXX@XXX.com';
        time = time.time();

    dell=Person()

    context={
        'username':"王亚锋",
        'age': "18",
        'gender': "男",
        'flag': "王者",
        'hero': "猴子",
        'person':dell,
        'wwwurl':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('left.html', **context)


# app.add_url_rule('/list/1111', endpoint='test112', view_func=test112,
#                  methods=['GET'])  # 这里endpoint可以不填 ，view_func 一定要是函数名：具体看下面源码解释

@app.route('/', methods=['get'])
def hello(name=None):
    class Person(object):
        Email = 'XXX@XXX.com';
        time = time.time();

    dell=Person()

    context={
        'username':"王亚锋",
        'age': "18",
        'gender': "男",
        'flag': "王者",
        'hero': "猴子",
        'person':dell,
        'wwwurl':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }
    }
    return render_template('hello.html', **context)


# app.add_url_rule('/list/1111', endpoint='test112', view_func=test112,
#                  methods=['GET'])  # 这里endpoint可以不填 ，view_func 一定要是函数名：具体看下面源码解释


def mysqldbini():
    # from-data格式参数

    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询

    sql1 = "SET GLOBAL slow_query_log=ON;"
    sql2= "SET GLOBAL long_query_time=1;"
    print(sql1)
    cursor.execute(sql1)
    data1 = cursor.fetchall()
    cursor.execute(sql2)
    data2 = cursor.fetchall()
    print(data1,data2)
    db.commit()
mysqldbini()
@app.route('/API/query/student/TotalScore', methods=['post'])
def TotalScore():
    # from-data格式参数
    id = flask.request.json.get('id')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    if int(id)<1000001:
        sql = "select s_name,sum(s_score) from  `student_score_100w` where s_id='{0}';".format(id)
    elif int(id)<2000001:
        sql = "select s_name,sum(s_score) from  `student_score_200w` where s_id='{0}';".format(id)
    elif int(id) < 3000001:
        sql = "select s_name,sum(s_score) from  `student_score_300w` where s_id='{0}';".format(id)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    print('ren1--------------\n',ren1)
    if ren1:
        ren = ren1
    else:
        ren = {'msg': '用户名或密码错误', 'msg_code': -1}

    return json.dumps(ren, ensure_ascii=False,cls=DateDecimalEncoder)
    #return jsonify(ren)
@app.route('/API/query/student/Score', methods=['post'])
def studentScore():
    # from-data格式参数
    id = flask.request.json.get('id')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    if int(id)<1000001:
        sql = "select * from  `student_score_100w` where s_id='{0}';".format(id)
    elif int(id)<2000001:
        sql = "select * from  `student_score_200w` where s_id='{0}';".format(id)
    elif int(id) < 3000001:
        sql = "select * from  `student_score_300w` where s_id='{0}';".format(id)
    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    print(data)
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    print('ren1--------------\n',ren1)
    if ren1:
        ren = ren1
    else:
        ren = {'msg': '用户名或密码错误', 'msg_code': -1}

    return json.dumps(ren, ensure_ascii=False,cls=DateDecimalEncoder)
    #return jsonify(ren)


@app.route('/API/query/AvgLessThanSixth', methods=['post'])
def AvgLessThanSixth():
    # from-data格式参数
    usrname = flask.request.json.get('usrname')
    Avgsroce = flask.request.json.get('Avgsroce')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    sql = "select avg(s_score),t1.s_id,t3.s_name from  score t1,student t3 where t1.s_id=t3.s_id  group by t1.s_id having avg(s_score)>{0};".format(Avgsroce)
    print(sql)
    cursor.execute(sql)

    # 使用 fetchone() 方法获取单条数据.
    data1 = cursor.fetchone()
    data = cursor.fetchall()
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    print(ren1)
    if usrname and Avgsroce:
        if usrname == 'test':
            ren = ren1
        else:
            ren = {'msg': '用户名或密码错误', 'msg_code': -1}
    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    # return jsonify(json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder))

@app.route('/API/Add/Student', methods=['post'])
def AddStudent():
    # from-data格式参数
    global data,ren1
    name = flask.request.json.get('name')
    birth = flask.request.json.get('birth')
    sex = flask.request.json.get('sex')
    moble = flask.request.json.get('moble')
    dynasty = flask.request.json.get('dynasty')
    Emperortitle = flask.request.json.get('Emperortitle')
    Evaluation = flask.request.json.get('Evaluation')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

    if name and birth and sex and moble and dynasty and Emperortitle and Evaluation:
        sql = "insert into student(s_name,s_birth,s_sex,moble,dynasty,Emperortitle,Evaluation) values('{0}','{1}','{2}',{3},'{4}','{5}','{6}');".format(name, birth, sex,
                                                                                                      moble,dynasty , Emperortitle ,Evaluation)
        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        db.close()
        ren1 = dict(zip(lista, listb))
    elif name and birth and sex and moble and dynasty and Evaluation :
        sql = "insert into student(s_name,s_birth,s_sex,moble,dynasty,Evaluation) values('{0}','{1}','{2}',{3},'{4}','{5}');".format(name, birth, sex,
                                                                                                      moble,dynasty , Evaluation )
        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        db.close()
        ren1 = dict(zip(lista, listb))

    elif name and birth and sex and moble and dynasty and Emperortitle :
        sql = "insert into student(s_name,s_birth,s_sex,moble,dynasty,Emperortitle) values('{0}','{1}','{2}',{3},'{4}','{5}');".format(name, birth, sex,
                                                                                                      moble,dynasty , Emperortitle )
        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        db.close()
        ren1 = dict(zip(lista, listb))
    elif name and birth and sex and moble and dynasty:
        sql = "insert into student(s_name,s_birth,s_sex,moble,dynasty) values('{0}','{1}','{2}',{3},'{4}');".format(name, birth, sex,moble,dynasty)
        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        db.close()
        ren1 = dict(zip(lista, listb))
    elif name and birth and sex and moble:
        sql = "insert into student(s_name,s_birth,s_sex,moble) values('{0}','{1}','{2}',{3});".format(name, birth, sex,
                                                                                                      moble)
        print(sql)
        print('-----------------------------------')
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        db.close()
        ren1 = dict(zip(lista, listb))
    elif name and birth and sex :
        sql = "insert into student(s_name,s_birth,s_sex) values('{0}','{1}','{2}');".format(name, birth, sex)
        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        db.close()
        ren1 = dict(zip(lista, listb))



    # # 使用 execute()  方法执行 SQL 查询
    # sql = "insert into student(s_name,s_birth,s_sex,moble) values('{0}','{1}','{2}',{3});".format(name,birth,sex,moble)
    # print(sql)
    # cursor.execute(sql)
    # db.commit()
    #
    # # 使用 fetchone() 方法获取单条数据.
    # data1 = cursor.fetchone()
    # data = cursor.fetchall()

    #print(ren1)
    # elif name and birth and sex:
    #     #print(ren1)
    #     ren = ren1
    else:
        ren1 = {'msg': '参数错误', 'msg_code': 1001}
    #return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren1)
@app.route('/API/Del/Student', methods=['post'])
def DelStudent():
    # from-data格式参数Student
    name = flask.request.json.get('name')
    id = flask.request.json.get('id')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    sql = "delete from student where s_id='{0}' and s_name ='{1}';".format(id,name)
    print(sql)
    cursor.execute(sql)
    db.commit()

    # 使用 fetchone() 方法获取单条数据.
    data1 = cursor.fetchone()
    data = cursor.fetchall()
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    if name and id:
        ren = ren1
    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    # return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)
@app.route('/API/Update/Student', methods=['post'])
def UpdateStudent():
    # from-data格式参数
    name = flask.request.json.get('name')
    birth = flask.request.json.get('birth')
    sex = flask.request.json.get('sex')
    moble = flask.request.json.get('moble')
    id = flask.request.json.get('id')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    if id and name and birth and sex and moble:
        sql = "update student set s_name = '{0}' , s_birth = '{1}' , s_sex = '{2}',moble ='{4}' where s_id = {3};".format(
            name, birth, sex, id, moble)

        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        ren1 = dict(zip(lista, listb))
        ren = ren1
    elif id and name and birth and sex :
        sql = "update student set s_name = '{0}' , s_birth = '{1}' , s_sex = '{2}' where s_id = {3};".format(
            name, birth, sex, id)

        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        ren1 = dict(zip(lista, listb))
        ren = ren1
    elif id and name and birth :
        sql = "update student set s_name = '{0}' , s_birth = '{1}'  where s_id = {2};".format(
            name, birth,  id)

        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        ren1 = dict(zip(lista, listb))
        ren = ren1
    elif id and name :
        sql = "update student set s_name = '{0}'   where s_id = {1};".format(
            name, id)

        print(sql)
        cursor.execute(sql)
        db.commit()
        data = cursor.fetchall()
        lista = ['msg', 'msg_code', 'data']
        listb = ['请求成功', 200, data]
        ren1 = dict(zip(lista, listb))
        ren = ren1

    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    # return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)


@app.route('/API/Update/Score', methods=['post'])
def UpdateScore():
    # from-data格式参数
    sid = flask.request.json.get('sid')
    cid = flask.request.json.get('cid')
    score = flask.request.json.get('score')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    if int(sid)<1000001:
        sql = "UPDATE `score_s100w` SET s_score={0}  WHERE s_id={1} AND c_id={2};".format(score,sid,cid)
    elif int(sid)<2000001:
        sql = "UPDATE `score_s200w` SET s_score={0}  WHERE s_id={1} AND c_id={2};".format(score,sid,cid)
    elif int(sid)<3000001:
        sql = "UPDATE `score_s300w` SET s_score={0}  WHERE s_id={1} AND c_id={2};".format(score,sid,cid)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data = cursor.fetchall()
        
        msg_code = 200
        msg = '请求成功'
        print(data, '\n')
    except Exception as e :
        # if re.findall('Duplicate entry',e,flags=re.IGNORECASE)!=[]:
        #     print(type(e))
        data = 'Duplicate entry \'\' for key \'PRIMARY\''
        msg_code = 100
        msg = '请求失败'
    lista = ['msg', 'msg_code', 'data']
    listb = [msg, msg_code, str(data)]
    ren1 = dict(zip(lista, listb))
    if sid and cid and score:
        ren = ren1

    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    # return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)


@app.route('/API/Add/Score', methods=['post'])
def AddScore():
    # from-data格式参数
    sid = flask.request.json.get('sid')
    cid = flask.request.json.get('cid')
    score = flask.request.json.get('score')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    sql = "insert into score(s_id,c_id,s_score) values('{0}','{1}',{2});".format(sid,cid,score)
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        # 使用 fetchone() 方法获取单条数据.
        data1 = cursor.fetchone()
        data = cursor.fetchall()
        msg_code = 200
        msg = '请求成功'
        print(data, '\n')
    except Exception as e :
        # if re.findall('Duplicate entry',e,flags=re.IGNORECASE)!=[]:
        #     print(type(e))
        data = 'Duplicate entry \'\' for key \'PRIMARY\''
        msg_code = 100
        msg = '请求失败'
    lista = ['msg', 'msg_code', 'data']
    listb = [msg, msg_code, str(data)]
    ren1 = dict(zip(lista, listb))
    if sid and cid and score:
        ren = ren1

    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    # return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)
@app.route('/API/Del/Score', methods=['DELETE'])
def DelScore():
    # from-data格式参数Student
    sid = flask.request.json.get('sid')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    # 使用 cursor() 方法创建一个游标对象 cursor
    cursor = db.cursor()
    # 带字段名称的游标
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    # 使用 execute()  方法执行 SQL 查询
    sql = "delete from  score where s_id>= '{0}' ;".format(sid)
    print(sql)
    cursor.execute(sql)
    db.commit()

    # 使用 fetchone() 方法获取单条数据.
    data1 = cursor.fetchone()
    data = cursor.fetchall()
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    if sid:
        ren = ren1
    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    # return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)

@app.route('/API/Query/Student', methods=['GET'])
def QueryStudent():
    name = (request.args["name"])
    moble = (request.args["moble"])
    # name = flask.request.json.get('name')
    # moble = flask.request.json.get('moble')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "SELECT * FROM student  WHERE s_name ='{}' AND moble ='{}';".format(name,moble)
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    print('data:\n', data)
    print('data:\n', type(data))
    if data ==():
        data ='无数据'
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    print('ren1:\n',ren1)
    if name and moble:
        ren = ren1
    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    #return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)

@app.route('/API/Query/Student/Allinfo', methods=['POST'])
def QueryStudentAllinfo():
    id = flask.request.json.get('id')
    #moble = (request.args["moble"])
    # name = flask.request.json.get('name')
    # moble = flask.request.json.get('moble')
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='000000',
                         database='test',
                         charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "SELECT s.s_id AS s_id,\
   s.s_name         AS s_name,\
  s.s_sex          AS s_sex,\
  s.moble          AS moble,\
  d.dorm_id        AS dorm_id,\
  d.room_id        AS room_id,\
  d.bed_id         AS bed_id,\
  c.grade_id       AS grade_id,\
  c.class_id       AS class_id,\
  c.t_id           AS t_id,\
  class.class_name AS class_name,\
  w.s_score            AS s_score \
FROM student s \
     LEFT JOIN dormitory_student_relationship d \
       ON d.s_id = s.s_id \
    LEFT JOIN class_student_relationship c \
      ON c.id = s.s_id \
   LEFT JOIN class \
     ON class.grade_id = c.grade_id \
          AND c.class_id = class.class_id \
 LEFT JOIN score_s100w w \
ON w.s_id = s.s_id \
WHERE w.s_id ='{}';".format(id)
    print(sql)
    cursor.execute(sql)
    db.commit()
    # 使用 fetchone() 方法获取单条数据.
    data = cursor.fetchall()
    print('data:\n', data)
    print('data:\n', type(data))
    if data ==():
        data ='无数据'
    lista = ['msg', 'msg_code', 'data']
    listb = ['请求成功', 200, data]
    ren1 = dict(zip(lista, listb))
    print('ren1:\n',ren1)
    if id :
        ren = ren1
    else:
        ren = {'msg': '参数错误', 'msg_code': 1001}
    #return json.dumps(ren, ensure_ascii=False,cls=DecimalEncoder)
    return jsonify(ren)


# #请求上下文
# with app.test_request_context():
#     pass

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=9000)
# app.run(debug=True)

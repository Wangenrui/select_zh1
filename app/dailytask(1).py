#!/usr/bin/python
# -*- coding: utf-8 -*-
#周文超测试用的

import MySQLdb
import time
from Crypto.Random import random
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "select_zh1.settings")
from django.db.models import Q
import sys
import django
django.setup()
from app.models import *
from django.forms.models import model_to_dict
from django.db import connection
from password import prpcrypt
import datetime
from decimal import Decimal
import uuid


LOCAL_DB = {
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'root',
    'PASSWORD': '1',
    'INSTANCE': 'select_zh1'}#数据库名，咱们就是select_zh1,我测试用的11

local_conn = MySQLdb.connect(host=LOCAL_DB['HOST'], user=LOCAL_DB['USER'],
                             passwd=LOCAL_DB['PASSWORD'], port=LOCAL_DB['PORT'], charset='utf8')
local_cur = local_conn.cursor()
local_conn.select_db(LOCAL_DB['INSTANCE'])


def dictfetchall(cursor):
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
        ]


def fetch_local(sql, arg):
    local_cur.execute(sql, arg)       
    return dictfetchall(local_cur)
#33


def process():
    try:
        print 'start daily task'        
        start_date = startdate()
        start_time = timetypechange(start_date)
        #第一志愿被分配
        if time.time() >= start_time and time.time() <= (start_time+24*60*60.0):
            print time.time()
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 1 GROUP BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str(stu_no)+','+str(1) +')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' +str(stu_no) +'OR volunteer_topic_no_id='+str(volunteer_topic_no_id)
                fetch_local(sql, [])
        #第二志愿被分配
        elif time.time() >= (start_time+24*60*60.0) and time.time() <= (start_time+2*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 2 GROUP BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                # sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str##(stu_no)+','+str(1) +')''''

                # fetch_local(sql, [])'''
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
        # 第三志愿被分配
        elif time.time() >= (start_time+2*24*60*60.0) and time.time() <= (start_time+3*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 3 GROUP BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                # sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str##(stu_no)+','+str(1) +')''''

                # fetch_local(sql, [])'''
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
        # 第四志愿被分配
        elif time.time() >= (start_time+3*24*60*60.0) and time.time() <= (start_time+4*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 4 GROUP BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                # sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str##(stu_no)+','+str(1) +')''''

                # fetch_local(sql, [])'''
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
        # 第五志愿被分配
        elif time.time() >= (start_time+4*24*60*60.0) and time.time() <= (start_time+5*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 5 GROUP BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                # sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str##(stu_no)+','+str(1) +')''''

                # fetch_local(sql, [])'''
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
        # 第六志愿被分配
        elif time.time() >= (start_time+5*24*60*60.0) and time.time() <= (start_time+6*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 6 GROUP BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                # sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str##(stu_no)+','+str(1) +')''''

                # fetch_local(sql, [])'''
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
        else :
            print 'daozhele'

        local_conn.commit()           
        
        print 'end daily task'

    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def startdate():
    try:
        sql = '''SELECT `select3_start` FROM `app_date_setting` WHERE `activation` =1'''
        rss = fetch_local(sql, [])
        start_date = rss[0]['select3_start']
        print str(start_date)
        return start_date
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def timetypechange(sdate):
    #将其转换为时间数组
    timeArray = time.strptime(sdate, "%Y-%m-%d")
    #转换为时间戳:
    timeStamp = time.mktime(timeArray)
    print timeStamp
    return timeStamp

def random():
    try:
        start_date = startdate()
        start_time = timetypechange(start_date)
        if time.time() > (start_time+6*24*60*60.0):
            achieveyear = Date_setting.objects.get(activation=1)
            year = achieveyear.year
            topic=[]
            list_teacher=[]
            list_selected_num=[]
            list_topic_num=[]
            rate=[]
            #取当前年份topic表中不在application_state中的id,major_id;当前年份学生不在application_state中的user_id,major_id;
            sql = '''SELECT id,major_id,tea_no FROM app_topic WHERE id not in (SELECT app_application_state.topic FROM app_application_state ) and year = '''+ year
            unselected_topic = fetch_local(sql, [])#id,major_id,tea_no
            sql = '''SELECT user_id,major_id FROM app_select_sysuser WHERE user_id not in (SELECT app_application_state.topic FROM app_application_state ) and year = ''' + year
            unselect_stu = fetch_local(sql, [])#user_id,major_id

            #获取全部老师user_id 存入list_teacher=[]
            sql = '''SELECT user_id FROM app_select_sysuser WHERE (role_id=3 or role_id=4) and achieve_year='''+year
            all_teano = fetch_local(sql, [])#tea user_id
            for teano in all_teano :
                list_teacher.append(teano['user_id'])

            # 获取全部老师已被选题目数 存入list_selected_num=[]
            for teano in list_teacher:
                num=0
                topic_id=[]
                sql = '''SELECT id FROM app_topic WHERE tea_no='''+teano+" and achieve_year="+year
                topicid = fetch_local(sql, [])
                for id in topic_id:
                    topic_id.append(id['id'])
                for id in topic_id:
                    if len(Application_state.objects.filter(topic=id))!=0:
                        num = num + 1
                list_selected_num.append(num)

            #获取全部老师的规定题目数 存入list_topic_num
            for teano in list_teacher:
                sql = '''SELECT topic_num FROM app_teacher_topic_num WHERE tea_no='''+teano+" and achieve_year="+year
                topicnum = fetch_local(sql, [])
                list_topic_num.append(topicnum['topic_num'])

            #获取全部老师 已选题目数/规定题目数 存入rate[]
            for index in range(len(list_teacher)):
                rate.append(float(list_selected_num[index])/float(list_topic_num[index]))

            #向题目池中添加题目id topic[] 根据比率决定向题目池中添加的个数 由低到高分别为4,3,2,1
            for a in unselected_topic:
                index = list_teacher.index(a['tea_no'])
                if rate[index]>=0 and rate[index]<0.25:
                    topic.append(a['id'])
                    topic.append(a['id'])
                    topic.append(a['id'])
                    topic.append(a['id'])
                elif rate[index]>=0.25 and rate[index]<0.5:
                    topic.append(a['id'])
                    topic.append(a['id'])
                    topic.append(a['id'])
                elif rate[index]>=0.5 and rate[index]<0.75:
                    topic.append(a['id'])
                    topic.append(a['id'])
                elif rate[index]>=0.75 and rate[index]<1:
                    topic.append(a['id'])

            #随机匹配
            for stu in unselect_stu:
                while True:
                    index = random.randint(0, len(topic) - 1)
                    topic = Topic.objects.get(id=topic[index])
                    major = topic.major_id
                    if stu['major_id']==major:
                        sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                            topic[index]) + ',' + str(stu['id']) + ',' + str(1) + ')'
                        fetch_local(sql, [])
                        while topic.count(topic[index]) > 0:
                            a.remove(topic[index])
                        break
            print '随机分配结束'
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])


process()

local_conn.commit()
local_cur.close()
local_conn.close()

exit()


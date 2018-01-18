#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import time
from Crypto.Random import random



LOCAL_DB = {
    'HOST': '127.0.0.1',
    'PORT': 3306,
    'USER': 'root',
    'PASSWORD': '1',
    'INSTANCE': 'select_zh1'}

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
def random1():
    try:
        start_date = startdate()
        start_time = timetypechange(start_date)
        year = str(2017)
        list_teacher = []
        if 1>0:#time.time() > (start_time+6*24*60*60.0):
            #achieveyear = Date_setting.objects.get(activation=1)
            #year = achieveyear.year

            print 'daozhele'
            topic=[]

            list_selected_num=[]
            list_topic_num=[]
            rate=[]
            #取当前年份topic表中不在application_state中的id,major_id;当前年份学生不在application_state中的user_id,major_id;
            sql = '''SELECT id,major_id,tea_no FROM app_topic a WHERE id not in (SELECT app_application_state.topic FROM app_application_state ) and a.year = '''+ year
            print sql
            unselected_topic = fetch_local(sql, [])#id,major_id,tea_no
            sql = '''SELECT user_id,major_id FROM app_select_sysuser WHERE user_id not in (SELECT app_application_state.topic FROM app_application_state ) and achieve_year = ''' + year
            unselect_stu = fetch_local(sql, [])#user_id,major_id

            #获取全部老师user_id 存入list_teacher=[]
            sql = '''SELECT user_id FROM app_select_sysuser WHERE (role_id=3 or role_id=4) and achieve_year='''+year
            all_teano = fetch_local(sql, [])#tea user_id
            for teano in all_teano :
                list_teacher.append(teano['user_id'])
            print list_teacher
            print len(list_teacher)

            # 获取全部老师已被选题目数 存入list_selected_num=[]
            for teano in list_teacher:
                num=0
                topic_id=[]
                sql = '''SELECT id FROM app_topic WHERE tea_no='''+teano+" and year="+year
                topicid = fetch_local(sql, [])
                print 'nn'
                for id in topicid:
                    topic_id.append(id['id'])
                    print 'hb'
                for id in topic_id:
                    sql = '''SELECT topic FROM app_application_state where topic='''+str(id)
                    a = fetch_local(sql, [])
                    print 'ha'
                    print a
                    if len(a)!=0:
                        num = num + 1
                list_selected_num.append(num)
            print list_selected_num

            #获取全部老师的规定题目数 存入list_topic_num
            for teano in list_teacher:
                sql = '''SELECT topic_num FROM app_teacher_topic_num WHERE tea_no='''+teano+" and year="+year
                print sql
                topicnum = fetch_local(sql, [])
                print 'qq'
                print topicnum
                print len(topicnum)
                #print topicnum[0]['topic_num']
                if len(topicnum)==0:
                    print 'we'
                    list_topic_num.append(1)
                    print 'rng'
                else:
                    list_topic_num.append(topicnum[0]['topic_num'])
                print 'daozhele1'
            #获取全部老师 已选题目数/规定题目数 存入rate[]
            print int(len(list_teacher))
            for index in range(0,len(list_teacher)-1):
                rate.append(float(list_selected_num[index])/float(list_topic_num[index]))
            print 'daozhele2'
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
            print 'daozhele3'
            #随机匹配
            for stu in unselect_stu:
                while True:
                    index = random.randint(0,len(topic) - 1)
                    print 'gg'
                    print index
                    sql = '''select major_id from app_topic where id='''+topic[index]
                    majorid = fetch_local(sql, [])

                    if stu['major_id']==majorid['major_id']:
                        sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                            topic[index]) + ',' + str(stu['id']) + ',' + str(1) + ')'
                        fetch_local(sql, [])
                        while topic.count(topic[index]) > 0:
                            a.remove(topic[index])
                        break
            print '随机分配结束'
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

random1()

local_conn.commit()
local_cur.close()
local_conn.close()

exit()


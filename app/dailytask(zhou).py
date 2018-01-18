#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import time


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

def process():
    try:
        print 'start daily task'        
        start_date = startdate()
        start_time = timetypechange(start_date)
        #第一志愿被分配
        if time.time() >= start_time and time.time() <= (start_time+24*60*60.0):

            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 1 AND volunteer_topic_no_id>=0 GROUP  BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES ('''+str(volunteer_topic_no_id)+','+str(stu_no)+','+str(1) +')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' +str(stu_no) +' OR volunteer_topic_no_id='+str(volunteer_topic_no_id)
                print sql
                fetch_local(sql, [])
        #第二志愿被分配
        elif time.time() >= (start_time+24*60*60.0) and time.time() <= (start_time+2*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 2 AND volunteer_topic_no_id>=0 GROUP  BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                    volunteer_topic_no_id) + ',' + str(stu_no) + ',' + str(1) + ')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' + str(
                    stu_no) + ' OR volunteer_topic_no_id=' + str(volunteer_topic_no_id)
                print sql
                fetch_local(sql, [])
        elif time.time() >= (start_time+2*24*60*60.0) and time.time() <= (start_time+3*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 3 AND volunteer_topic_no_id>=0 GROUP  BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                    volunteer_topic_no_id) + ',' + str(stu_no) + ',' + str(1) + ')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' + str(
                    stu_no) + ' OR volunteer_topic_no_id=' + str(volunteer_topic_no_id)
                print sql
                fetch_local(sql, [])
        elif time.time() >= (start_time+3*24*60*60.0) and time.time() <= (start_time+4*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 4 AND volunteer_topic_no_id>=0 GROUP  BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                    volunteer_topic_no_id) + ',' + str(stu_no) + ',' + str(1) + ')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' + str(
                    stu_no) + ' OR volunteer_topic_no_id=' + str(volunteer_topic_no_id)
                print sql
                fetch_local(sql, [])
        # 第五志愿被分配
        elif time.time() >= (start_time+4*24*60*60.0) and time.time() <= (start_time+5*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 5 AND volunteer_topic_no_id>=0 GROUP  BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                    volunteer_topic_no_id) + ',' + str(stu_no) + ',' + str(1) + ')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' + str(
                    stu_no) + ' OR volunteer_topic_no_id=' + str(volunteer_topic_no_id)
                print sql
                fetch_local(sql, [])
        # 第六志愿被分配
        elif time.time() >= (start_time+5*24*60*60.0) and time.time() <= (start_time+6*24*60*60.0):
            sql = '''SELECT stu_no,volunteer_topic_no_id,MAX(score) FROM app_application a LEFT JOIN app_select_sysuser b ON b.user_id = a.stu_no WHERE volunteer_no = 6 AND volunteer_topic_no_id>=0 GROUP  BY volunteer_topic_no_id '''
            rss = fetch_local(sql, [])
            for rs in rss:
                stu_no = rs['stu_no']
                volunteer_topic_no_id = rs['volunteer_topic_no_id']
                sql = ''' INSERT INTO `app_application_state`(`topic`, `selected_stu_no`, `submit`) VALUES (''' + str(
                    volunteer_topic_no_id) + ',' + str(stu_no) + ',' + str(1) + ')'
                fetch_local(sql, [])
                # TODO：删除该学生在app_applicaton里的信息，sql，并fetch_local(sql,[])
                sql = '''DELETE FROM app_application WHERE  stu_no=''' + str(
                    stu_no) + ' OR volunteer_topic_no_id=' + str(volunteer_topic_no_id)
                print sql
                fetch_local(sql, [])
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

process()

local_conn.commit()
local_cur.close()
local_conn.close()

exit()


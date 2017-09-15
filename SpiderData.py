#coding=utf-8
import re  # 正则表达式
import WaterData
import urllib2  # 网络访问模块
import time
import codecs  #解决编码问题的关键 ，使用codecs.open打开文件
import sys   #1解决不同页面编码问题

reload(sys)                         # 2
sys.setdefaultencoding('utf-8')     # 3

name_dict={"0":"0000"}
# 解析数据
def parse_name(state_name):
    name_str = state_name.split('"')[5]
    name_list= name_str.split("!!")
    for name in name_list:
        if name=="":
            break
        id=name.split("$")[0]
        value=name.split("$")[1]
        name_dict[id]=value
    print "解析地理位置完成"

def parse_data(state_info):
    data_str=state_info.split('"')[5]
    data_list=data_str.split("!!")
    for data in data_list:
        if data=="":
            break
        data_list = data.split("$")

        single_data= WaterData.WaterData()
        single_data.Id=data_list[0]
        print single_data.Id
        if name_dict.has_key(single_data.Id):
            single_data.State_name=name_dict[single_data.Id]
        else:
            single_data.State_name="0000"
        single_data.Time=data_list[1]
        single_data.PH_value=data_list[2]
        single_data.PH_Level=data_list[3]
        single_data.Dissolved_OX=data_list[4]
        single_data.Dissolved_OX_Level=data_list[5]
        single_data.KMnO=data_list[6]
        single_data.KMnO_Level=data_list[7]
        single_data.NH3N=data_list[10]
        single_data.NH3N_Level=data_list[11]
        single_data.Date=data_list[12]

        save_single_data(single_data)

        print data_list


def parse_station_info(station_info):
    info_str=station_info.split('"')[5]
    info_list=info_str.split("!!")
    for single_station in info_list:
        print single_station

# 获取html数据
def get_data(home):
    request = urllib2.Request(home)
    response = urllib2.urlopen(request)
    html = response.read()
    #print html
    stainfo=""
    staname=""
    stationinfo=""
    lines=html.split("\r\n")
    for line in lines:
        if 'name="stainfo"' in line:
            stainfo=line
        if 'name="staname"' in line:
            staname=line
        if 'name="stationinfo"' in line:
            stationinfo=line

    print stainfo
    print staname
    #print stationinfo

    parse_name(staname)
    parse_data(stainfo)
    #parse_station_info(stationinfo)

    print "解析水质数据完成"

def save_single_data(Object):
    global StateCount
    StateCount+=1
    file.write(Object.Id+","+Object.State_name+","+Object.Date+","
    +Object.Time+","+Object.PH_value+","+Object.PH_Level+","
    +Object.Dissolved_OX +","+Object.Dissolved_OX_Level+","
    +Object.KMnO+","+Object.KMnO_Level+","+Object.NH3N+","
    +Object.NH3N_Level + "\n")


if __name__ == '__main__':

    StateCount = 0

    home = 'http://online.watertest.com.cn/'  # 起始位置

    # 时间间隔单位s
    time_i=60

    while 1:
        time_str=time.strftime('%Y-%m-%d %H.%M',time.localtime(time.time()))+".csv"
        print time_str
        file = open(time_str, "a+")  # 文件操作
        file.write("ID,地址,日期,时间,PH,级别,溶解氧,级别,氨氮,级别,高锰酸盐指数,级别\n")

        get_data(home)
        print time_str+"总共" + str(StateCount) + "条数据"
        file.close()
        time.sleep(time_i)



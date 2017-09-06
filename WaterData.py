#coding: utf-8
# 水质类定义
class WaterData(object):
    def __init__(self):
        self.Id = None
        self.State_name = None
        self.Date=None
        self.Time=None

        self.PH_value = None
        self.PH_Level = None

        self.Dissolved_OX = None
        self.Dissolved_OX_Level = None

        self.KMnO = None
        self.KMnO_Level = None

        self.NH3N = None
        self.NH3N_Level = None

        self.Station_Info = None
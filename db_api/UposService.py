#! /usr/bin/python3

import datetime
import json     # json
import pymysql  # mariadb
import Logger

from datetime import datetime, date

# json dumps시 dict내용의 datatime클래스를 formatting string타입으로 바꿈
def datetime_to_json_formatting(o):
    if isinstance(o, (date, datetime)):
        return o.strftime('%Y%m%d%H%M%S')
def datetime_to_json_formatting_daily(o):
    if isinstance(o, (date, datetime)):
        return o.strftime('%Y%m%d')
def datetime_to_json_formatting_hour(o):
    if isinstance(o, (date, datetime)):
        return o.strftime('%Y%m%d%H')

_logger = Logger.Logger("UposService")

#############################################################################################################################################
# 전력 데이터


def GetConnection():
    connection = pymysql.connect(host='59.3.14.15', port=8010, user='root', password='1234',
                                    db='upos_service', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    return connection
# def GetConnection():
#     connection = pymysql.connect(host='146.56.183.172', port=3306, user='edu_usr', password='edu_pwd',
#                                     db='upos_service', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
#     return connection
    

# 2022-04-01 00:00:29
async def GetLpDataDaily(startDate: str, endDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            startDate = datetime.strptime(startDate, '%Y%m').strftime("%Y-%m")
            endDate = datetime.strptime(endDate, '%Y%m').strftime("%Y-%m")
            query = "select a.runDatetime as runDate, cast(sum(a.Power) as char) as sumData " + \
                    "from " + \
                    "( " + \
                    "   select runDatetime, Power " + \
                    "   from UnitReal " + \
                    f"   where left(runDatetime,10) between '{startDate}' and '{endDate}' " + \
                    ") a " +\
                    "group by left(runDatetime,10);"

            cursor.execute(query)
            # row_headers=[x[0] for x in cursor.description] #this will extract row headers
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting_daily, indent=4)
            # print(f"{datetime.datetime.now()} : succeed to do 'GetLpDataDaily('{startDate}',{endDate})'")
            _logger.Info(
                f"succeed to do 'GetLpDataDaily('{startDate}',{endDate})'")
            return json_data

    except Exception as ex:
        # print(f"{datetime.datetime.now()} : error to do 'GetLpDataDaily('{startDate}',{endDate})'")
        _logger.Info(f"error to do 'GetLpDataDaily('{startDate}',{endDate})'")


async def GetLpDataHourly(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            runDate = datetime.strptime(runDate, '%Y%m%d').strftime('%Y-%m-%d')
            query = f"""
                SELECT a.runDatetime AS runDate, CAST(SUM(a.Power) AS CHAR) AS sumData
                FROM (
                SELECT runDatetime, Power
                FROM UnitReal
                WHERE LEFT(runDatetime,10) = '{runDate}'
                ) a
                GROUP BY LEFT(runDatetime, 13);
            """
            
            cursor.execute(query)
            # row_headers=[x[0] for x in cursor.description] #this will extract row headers
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting_hour, indent=4)
            # print(f"{datetime.datetime.now()} : succeed to do 'GetLpDataHourly('{runDate}')'")
            _logger.Info(f"succeed to do 'GetLpDataHourly('{runDate}')'")
            return json_data

    except Exception as ex:
        # print(f"{datetime.datetime.now()} : error to do 'GetLpDataHourly('{runDate}'")
        _logger.Info(f"error to do 'GetLpDataHourly('{runDate}'")


#############################################################################################################################################

async def GetUpiData(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            # query = "SELECT LpID, LpDate, cast(LpData as char) as LpData FROM wm_fems.Raw_KepcoDayLpData where LpDate > %s limit 2;"
            unit_query = "select " +\
                        "   szUnitID, runDatetime, " +\
                        "   cast((Power/ChilledWater_eUSRT) as char) as UnitUpi " +\
                        "from UnitReal " +\
                        f"where runDatetime = '{runDate}';"
            cursor.execute(unit_query)
            # row_headers=[x[0] for x in cursor.description] #this will extract row headers
            unit_rv = cursor.fetchall()

            system_query = "select a.runDatetime as runDate, cast((sum(Power)/sum(ChilledWater_eUSRT)) as char) as SystemUpi " + \
                    "from " + \
                    "( " +\
                    "   select runDatetime, Power, ChilledWater_eUSRT from UnitReal " + \
                    f"  where runDatetime = '{runDate}'" + \
                    ") a " +\
                    " group by runDatetime order by runDatetime; "

            cursor.execute(system_query)
            # row_headers=[x[0] for x in cursor.description] #this will extract row headers
            system_rv = cursor.fetchall()
            # ress = str(rv)
            rv = unit_rv + system_rv
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            # print(f"{datetime.datetime.now()} : succeed to do 'GetUpiData('{ahu_id}','{startDate}','{endDate}')'")
            _logger.Info(
                f"succeed to do 'GetUpiData('{runDate}')")
            return json_data

    except Exception as ex:
        # print(f"{datetime.datetime.now()} : error to do 'GetUpiData('{ahu_id}','{startDate}','{endDate}')'")
        _logger.Info(
            f"error to do 'GetUpiData('{runDate}')")

async def Get_ChilledWater_T_Data(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            query = "select szUnitID, runDatetime, " +\
                "   cast(ChilledWater_Delta_T as char) as ChilledWater_Delta_T, " +\
                "   cast(ChilledWater_Out_T as char) as ChilledWater_Out_T " +\
                "from UnitReal " +\
                f"where runDatetime = '{runDate}';"
            cursor.execute(query)
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            message = f"succeed to do 'Get_ChilledWater_T_Data('{runDate}')'"
            _logger.Info(message)
            return json_data

    except Exception as ex:
        message = f"error to do 'Get_ChilledWater_T_Data('{runDate}')'"
        _logger.Info(message)

async def GetInfoData(szUnitID: str, runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            query = f"""
                    select
                    cast(Vane_Pct as char) as Vane_Pct,
                    cast(_ChilledWater_In_T as char) as _ChilledWater_In_T,
                    cast(_ChilledWater_Out_T as char) as _ChilledWater_Out_T,
                    cast(CoolingWater_In_T as char) as CoolingWater_In_T,
                    cast(CoolingWater_Out_T as char) as CoolingWater_Out_T,
                    cast(Motor_A as char) as Motor_A,
                    cast(OilTank_T as char) as OilTank_T,
                    cast(OilPress_Delta_T as char) as OilPress_Delta_T,
                    cast(Evaporator_T as char) as Evaporator_T,
                    cast(Evaporator_P as char) as Evaporator_P,
                    cast(Condenser_T as char) as Condenser_T,
                    cast(Condenser_P as char) as Condenser_P
                    from UnitReal
                    where runDatetime = '{runDate}' and szUnitID = '{szUnitID}';
                    """
            cursor.execute(query)
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            message = f"succeed to do 'GetInfoData('{szUnitID}', '{runDate}')'"
            _logger.Info(message)
            return json_data

    except Exception as ex:
        message = f"error to do 'GetInfoData('{szUnitID}', '{runDate}')'"
        _logger.Info(message)

async def GetnowefficiencyData(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            query = f"""
                SELECT runDatetime AS run_datetime, 
                CAST(AVG(Equipment_Running_eEff) AS CHAR) AS Equipment_Running_eEff,
                CAST(AVG(Equipment_Running_tEff) AS CHAR) AS Equipment_Running_tEff
                FROM UnitReal
                WHERE runDatetime = '{runDate}' 
                AND Equipment_Running_eEff != 0 
                AND Equipment_Running_tEff != 0
                GROUP by runDatetime;
            """
            cursor.execute(query)
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            message = f"succeed to do 'GetefficiencyData('{runDate}')'"
            _logger.Info(message)
            return json_data

    except Exception as ex:
        message = f"error to do 'GetefficiencyData('{runDate}')'"
        _logger.Info(message)

async def GetefficiencyData(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            runDate = datetime.strptime(runDate, '%Y%m%d').strftime('%Y-%m-%d')
            query = f"""
                SELECT runDatetime AS run_datetime, 
                CAST(AVG(Equipment_Running_eEff) AS CHAR) AS Equipment_Running_eEff,
                CAST(AVG(Equipment_Running_tEff) AS CHAR) AS Equipment_Running_tEff
                FROM UnitReal
                WHERE LEFT(runDatetime,10) = '{runDate}' 
                AND Equipment_Running_eEff != 0 
                AND Equipment_Running_tEff != 0
                GROUP by runDatetime;
            """
            cursor.execute(query)
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            message = f"succeed to do 'GetefficiencyData('{runDate}')'"
            _logger.Info(message)
            return json_data

    except Exception as ex:
        message = f"error to do 'GetefficiencyData('{runDate}')'"
        _logger.Info(message)

async def GetRunNumData(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            query = f"""
                SELECT runDatetime AS runDatetime,
                CAST(SUM(Run_Time) AS CHAR) AS run_num,
                CAST(CEILING(SUM(ChilledWater_tUSRT)/1000) AS CHAR) AS run_num_cal
                FROM UnitReal
                WHERE runDatetime = '{runDate}' 
                GROUP by runDatetime;
            """
            cursor.execute(query)
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            message = f"succeed to do 'Getrun_numData('{runDate}')'"
            _logger.Info(message)
            return json_data

    except Exception as ex:
        message = f"error to do 'GetMLData('{runDate}')'"
        _logger.Info(message)

async def GetMLData(runDate: str):
    try:
        connection = GetConnection()

        with connection.cursor() as cursor:
            query = f"""
                SELECT 
                runDatetime AS runDatetime,                
                CAST(SUM(Power) AS CHAR) AS Power,
                CAST(AVG(ChilledWater_Delta_T) AS CHAR) AS ChilledWater_Delta_T,
                CAST(AVG(Part_Load_Ratio) AS CHAR) AS Part_Load_Ratio,
                CAST(SUM(ChilledWater_eUSRT) AS CHAR) AS ChilledWater_eUSRT,
                CAST(SUM(ChilledWater_tUSRT) AS CHAR) AS ChilledWater_tUSRT,
                CAST(AVG(Temperature_Control_Eff) AS CHAR) AS Temperature_Control_Eff,
                CAST((SUM(Power)/SUM(ChilledWater_eUSRT)) AS CHAR) AS Energy_ePUB,
                CAST((SUM(Power)/SUM(ChilledWater_tUSRT)) AS CHAR) AS Energy_tPUB
                FROM UnitReal
                WHERE runDatetime = '{runDate}' AND Power != 0 
                GROUP by runDatetime;
            """
            cursor.execute(query)
            rv = cursor.fetchall()
            # ress = str(rv)
            json_data = json.dumps(rv, default=datetime_to_json_formatting, indent=4)
            message = f"succeed to do 'GetMLData('{runDate}')'"
            _logger.Info(message)
            return json_data

    except Exception as ex:
        message = f"error to do 'GetMLData('{runDate}')'"
        _logger.Info(message)
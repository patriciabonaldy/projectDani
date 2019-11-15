#from config.database import OracleDB
import json

def profis():
    l_nrst = nr_status()
    print (l_nrst)
    return l_nrst

def nr_status():
    #sqlString = 
    """select *
                   from nr_status
                   where run_date in (select run_date from nightrun)
                   order by start_date desc"""
    """ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_nrst = res.fetchall()"""
    data = [['1' , '1' , 'Olivos' , 'Esteban Echeverria 2870' , 'Munro' , '4756-2360' , '1' , 'A' , '1' , 'None' , 'Buenos Aires' , '1605' , 'None' , 'None' , 'None' , 'None' , 'B' , 'None' , 'None' , 'None' , 'None' , 'None' , '1999-01-18 12:59:16' , '1' , '1988-03-03 00:00:00' , '1' , '1' , 'None' , '7796613000010' , 'None' , 'R1' , '3' , 'Olivo' , '1' , '1' , '0']]

    jsonObj = json.dumps(data)
    #data_nrst = {"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
    return jsonObj
#from config.database import OracleDB


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
    data_nrst = {"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
    return data_nrst
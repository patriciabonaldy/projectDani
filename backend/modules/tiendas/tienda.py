#from config.database import OracleDB

def stores():
    l_store = store()
    print (l_store)
    return l_store

def store():
    #sqlString = 
    """select STORE_NO, MBS_TYPE, STATUS, NAME, ADDRESS, TOWN, PHONE_NO, BANK_ACCOUNT_NO, BANK_NAME, STORE_TYPE, BUILDING, PROV_COUNTY_STATE, ADDR_PST_CD, POB_NO, POB_PST_CD, TELEX_NO, TELEFAX_NO, BANK_ADDRESS, BANK_TOWN, BANK_COUNTY, BANK_POSTAL_CD, BANK_POB_NO, BANK_POB_PST_CD, EIS_DATE, BONUS_ACTIVE_STORE, OPENING_DATE, LIKE_FOR_LIKE, REGION_NO, E_MAIL, GLN, REFURBISH_DATE, STATE_ID, REGION_PR, SHORT_NAME, CHAIN, COT, DELIV_CD
                    from store
                    order by store_no"""
    """ora = OracleDB().connect()
    res = ora.execute(sqlString)
    data_store = res.fetchall()"""
    #data_store = {"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}
    data = [['1' , '1' , 'Olivos' , 'Esteban Echeverria 2870' , 'Munro' , '4756-2360' , '1' , 'A' , '1' , 'None' , 'Buenos Aires' , '1605' , 'None' , 'None' , 'None' , 'None' , 'B' , 'None' , 'None' , 'None' , 'None' , 'None' , '1999-01-18 12:59:16' , '1' , '1988-03-03 00:00:00' , '1' , '1' , 'None' , '7796613000010' , 'None' , 'R1' , '3' , 'Olivo' , '1' , '1' , '0'],
            ['1' , '1' , 'Olivos' , 'Esteban Echeverria 2870' , 'Munro' , '4756-2360' , '1' , 'A' , '1' , 'None' , 'Buenos Aires' , '1605' , 'None' , 'None' , 'None' , 'None' , 'B' , 'None' , 'None' , 'None' , 'None' , 'None' , '1999-01-18 12:59:16' , '1' , '1988-03-03 00:00:00' , '1' , '1' , 'None' , '7796613000010' , 'None' , 'R1' , '3' , 'Olivo' , '1' , '1' , '0'],
            ['1' , '1' , 'Olivos' , 'Esteban Echeverria 2870' , 'Munro' , '4756-2360' , '1' , 'A' , '1' , 'None' , 'Buenos Aires' , '1605' , 'None' , 'None' , 'None' , 'None' , 'B' , 'None' , 'None' , 'None' , 'None' , 'None' , '1999-01-18 12:59:16' , '1' , '1988-03-03 00:00:00' , '1' , '1' , 'None' , '7796613000010' , 'None' , 'R1' , '3' , 'Olivo' , '1' , '1' , '0']
            ]

    #jsonObj = json.dumps(data)
    return data
from config.database import OracleDB
from flask import jsonify

def get_prof_1703_hosp():
    sqlstr = """select batch_id,error_ind,offer_id,event_id,sub_event_id,activity_id,deal_id,offer_type_parent_id,offer_type_id,offer_val,base_price_type,threshold_id,offer_desc,event_desc,sub_event_desc,activity_desc,offer_comments,offer_status,offer_start_date,offer_end_date,get_val,get_val_type,get_type,get_qty,get_prod_level,get_prod_group_condition,buy_prod_level,buy_val,buy_type,buy_qty,buy_prod_group_condition,discount_coupon_flag,discount_coupon_start_date,discount_coupon_end_date,cumulative_flag,gift_flag,hit_level,funding_type,vendor_funding,special_instructions,event_type,promo_motive,offer_attr_01_char,offer_attr_02_char,offer_attr_03_char,offer_attr_04_char,offer_attr_01_no,offer_attr_02_no,offer_attr_03_no,offer_attr_04_no,offer_attr_01_flag,offer_attr_02_flag,offer_attr_03_flag,offer_attr_04_flag,offer_attr_01_date,offer_attr_02_date,offer_attr_03_date,offer_attr_04_date,offer_attr_01_desc,offer_attr_02_desc,offer_attr_03_desc,offer_attr_04_desc,origin_id,record_status,create_user_id,create_datetime
                from
                prof_1703_hosp
                where batch_id in (select batch_id
                                    from mkstg_etl_ctrl_status@stage_profi
                                    where rundate in (select run_date from nightrun)
                                    and interface_group not in ('TRANSFER','ORDERS')
                                    and origin_id = 1)"""
    ora = OracleDB().connect()
    res = ora.execute(sqlstr)
    payload_prof_1703_hosp = []
    context_prof_1703_hosp = {}
    for data_prof1703log in res:
        context_prof_1703_hosp = {'batch_id': data_prof1703log[0],'error_ind': data_prof1703log[1],'offer_id': data_prof1703log[2],'event_id': data_prof1703log[3],'sub_event_id': data_prof1703log[4],'activity_id': data_prof1703log[5],'deal_id': data_prof1703log[6],'offer_type_parent_id': data_prof1703log[7],'offer_type_id': data_prof1703log[8],'offer_val': data_prof1703log[9],'base_price_type': data_prof1703log[10],'threshold_id': data_prof1703log[11],'offer_desc': data_prof1703log[12],'event_desc': data_prof1703log[13],'sub_event_desc': data_prof1703log[14],'activity_desc': data_prof1703log[15],'offer_comments': data_prof1703log[16],'offer_status': data_prof1703log[17],'offer_start_date': data_prof1703log[18],'offer_end_date': data_prof1703log[19],'get_val': data_prof1703log[20],'get_val_type': data_prof1703log[21],'get_type': data_prof1703log[22],'get_qty': data_prof1703log[23],'get_prod_level': data_prof1703log[24],'get_prod_group_condition': data_prof1703log[25],'buy_prod_level': data_prof1703log[26],'buy_val': data_prof1703log[27],'buy_type': data_prof1703log[28],'buy_qty': data_prof1703log[29],'buy_prod_group_condition': data_prof1703log[30],'discount_coupon_flag': data_prof1703log[31],'discount_coupon_start_date': data_prof1703log[32],'discount_coupon_end_date': data_prof1703log[33],'cumulative_flag': data_prof1703log[34],'gift_flag': data_prof1703log[35],'hit_level': data_prof1703log[36],'funding_type': data_prof1703log[37],'vendor_funding': data_prof1703log[38],'special_instructions': data_prof1703log[39],'event_type': data_prof1703log[40],'promo_motive': data_prof1703log[41],'offer_attr_01_char': data_prof1703log[42],'offer_attr_02_char': data_prof1703log[43],'offer_attr_03_char': data_prof1703log[44],'offer_attr_04_char': data_prof1703log[45],'offer_attr_01_no': data_prof1703log[46],'offer_attr_02_no': data_prof1703log[47],'offer_attr_03_no': data_prof1703log[48],'offer_attr_04_no': data_prof1703log[49],'offer_attr_01_flag': data_prof1703log[50],'offer_attr_02_flag': data_prof1703log[51],'offer_attr_03_flag': data_prof1703log[52],'offer_attr_04_flag': data_prof1703log[53],'offer_attr_01_date': data_prof1703log[54],'offer_attr_02_date': data_prof1703log[55],'offer_attr_03_date': data_prof1703log[56],'offer_attr_04_date': data_prof1703log[57],'offer_attr_01_desc': data_prof1703log[58],'offer_attr_02_desc': data_prof1703log[59],'offer_attr_03_desc': data_prof1703log[6],'offer_attr_04_desc': data_prof1703log[61],'origin_id': data_prof1703log[62],'record_status': data_prof1703log[63],'create_user_id': data_prof1703log[64],'create_datetime': data_prof1703log[65] }
        payload_prof_1703_hosp.append(context_prof_1703_hosp)
        context_prof_1703_hosp = {}
    return jsonify(payload_prof_1703_hosp)
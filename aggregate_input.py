import pandas as pd
import collections

def sepdata(data):
    return data%100

def input_crash_summary(ws, temp, pattern, pt, ct, rt, rs, b1, b2):
    ws['C3'].value = pattern
    ws['E3'].value = len(temp)
    ws['C4'].value = ct
    ws['C5'].value = pt
    ws['C6'].value = '보행자'
    ws['C7'].value = rt
    ws['C8'].value = rs
    ws['C9'].value = b1
    ws['C10'].value = b2


def aggregate_result(temp):
    acc_type_col = ['사망', '중상', '경상', '부상신고']
    ar = []

    data = collections.Counter(temp['사고내용'])
    mask = collections.Counter(acc_type_col)

    mask_data = mask+data

    for value in mask_data.values():
        ar.append(value-1)
    
    return ar


def fat_aggregate_result(temp):
    pivot = temp.groupby('pattern')[['사망자수', '중상자수', '경상자수', '부상신고자수']].sum()
    list = [pivot['사망자수'][0], pivot['중상자수'][0], pivot['경상자수'][0], pivot['부상신고자수'][0]]
    return list


def daynight_aggregate_result(temp):
    day_night_col = ['주', '야']
    dar = []

    data = collections.Counter(temp['주야'])
    mask = collections.Counter(day_night_col)

    mask_data = mask+data

    for value in mask_data.values():
        dar.append(value-1)
    
    return dar


def time_aggregate_result(temp):
    time_col = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    tar = []

    temp['시간대'] = temp['발생일시'].apply(sepdata)
    
    data = collections.Counter(temp['시간대'])
    mask = collections.Counter(time_col)

    mask_data = mask+data

    for value in mask_data.values():
        tar.append(value-1)
    
    return tar


def weather_aggregate_result(temp):
    wt_col = ['맑음', '흐림', '비', '안개', '눈', '기타/불명']
    war = []

    data = collections.Counter(temp['기상상태'])
    mask = collections.Counter(wt_col)

    mask_data = mask+data
    
    for value in mask_data.values():
        war.append(value-1)
    return war


def roadcond_aggregate_result(temp):
    road_cond_col = ['건조', '젖음/습기', '서리/결빙', '적설', '기타', '해빙', '침수']
    rar = []

    data = collections.Counter(temp['노면상태2'])
    mask = collections.Counter(road_cond_col)

    mask_data = mask+data

    for value in mask_data.values():
        rar.append(value-1)
    
    return rar


def law_aggregate_result(temp):
    law_col = ['과속', '과로', '교차로운행방법위반', '보행자보호의무위반', '부당한회전', '신호위반', '안전거리미확보', '안전운전의무불이행', '앞지르기금지위반', '앞지르기방법위반', '일시정지위반', '중앙선침범', '직진우회전전진방해', '진로양보불이행', '차로위반(진로변경)', '철길건널목통과방법', '정비불량', '기타']
    lar = []

    data = collections.Counter(temp['법규위반1당2'])
    mask = collections.Counter(law_col)

    mask_data = mask+data

    for value in mask_data.values():
        lar.append(value-1)
    
    return lar


def roadshape2_aggregate_result(temp):
    temp['도로선형123'] = temp['도로선형1'] + "-" + temp['도로선형2'] + "-" +  temp['도로선형3']

    road_shape_col = ['직선-직선-평지','직선-직선-오르막','직선-직선-내리막','커브ㆍ곡각 -우-평지  ','커브ㆍ곡각 -우-오르막','커브ㆍ곡각 -우-내리막','커브ㆍ곡각 -좌-평지  ','커브ㆍ곡각 -좌-오르막','커브ㆍ곡각 -좌-내리막','기타구역-기타구역-기타/서비스구역']
    rar = []
    
    data = collections.Counter(temp['도로선형123'])
    mask = collections.Counter(road_shape_col)

    mask_data = mask+data

    for value in mask_data.values():
        rar.append(value-1)
    
    return rar


def intersection_aggregate_result(temp):
    intersection_shape_col = ['교차로아님', '교차로 - 삼지', '교차로 - 사지', '교차로 - 오지이상', '교차로 - 회전']
    iar = []
    
    data = collections.Counter(temp['교차로형태2'])
    mask = collections.Counter(intersection_shape_col)

    mask_data = mask+data

    for value in mask_data.values():
        iar.append(value-1)
    
    return iar


def roadsep_aggegate_result(temp):
    road_sep_col = ['분리시설 없음', '노면표시', '도로표지병', '방책등', '화단', '기타분리시설']
    rar = []
    
    data = collections.Counter(temp['중앙분리시설2'])
    mask = collections.Counter(road_sep_col)

    mask_data = mask+data

    for value in mask_data.values():
        rar.append(value-1)
    
    return rar


def input_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    ws['C14'] = list[0]
    ws['D14'] = str(list_percent[0])+'%'
    ws['E14'] = list[1]
    ws['F14'] = str(list_percent[1])+'%'
    ws['G14'] = list[2]
    ws['H14'] = str(list_percent[2])+'%'
    ws['I14'] = list[3]
    ws['J14'] = str(list_percent[3])+'%'
    ws['K14'] = sum(list)


def input_fat_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    ws['C15'] = list[0]
    ws['D15'] = str(list_percent[0])+'%'
    ws['E15'] = list[1]
    ws['F15'] = str(list_percent[1])+'%'
    ws['G15'] = list[2]
    ws['H15'] = str(list_percent[2])+'%'
    ws['I15'] = list[3]
    ws['J15'] = str(list_percent[3])+'%'
    ws['K15'] = sum(list)


def input_daynight_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    ws['C19'] = list[0]
    ws['D19'] = str(list_percent[0])+'%'
    ws['C20'] = list[1]
    ws['D20'] = str(list_percent[1])+'%'


def input_time_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    idx = 24
    for t in list:
        cell = 'C'+str(idx)
        ws[cell].value = t
        idx += 1

    idx = 24
    for t in list_percent:
        cell = 'D'+str(idx)
        ws[cell].value = str(t) + "%"
        idx += 1


def input_weather_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    ws['C51'] = list[0]
    ws['D51'] = str(list_percent[0])+'%'
    ws['C52'] = list[1]
    ws['D52'] = str(list_percent[1])+'%'
    ws['C53'] = list[2]
    ws['D53'] = str(list_percent[2])+'%'
    ws['C54'] = list[3]
    ws['D54'] = str(list_percent[3])+'%'
    ws['C55'] = list[4]
    ws['D55'] = str(list_percent[4])+'%'
    ws['C56'] = list[5]
    ws['D56'] = str(list_percent[5])+'%'


def input_roadcond_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    ws['C60'] = list[0]
    ws['D60'] = str(list_percent[0])+'%'
    ws['C61'] = list[1]
    ws['D61'] = str(list_percent[1])+'%'
    ws['C62'] = list[2]
    ws['D62'] = str(list_percent[2])+'%'
    ws['C63'] = list[3]
    ws['D63'] = str(list_percent[3])+'%'
    ws['C64'] = list[4]
    ws['D64'] = str(list_percent[4])+'%'


def input_law_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]

    idx = 19
    for t in list:
        cell = 'G'+str(idx)
        ws[cell].value = t
        idx += 1

    idx = 19
    for t in list_percent:
        cell = 'H'+str(idx)
        ws[cell].value = str(t) + "%"
        idx += 1
        
    
def input_roadshape2_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]
    
    
    idx = 40
    for t in list:
        cell = 'G'+str(idx)
        ws[cell].value = t
        idx += 1

    idx = 40
    for t in list_percent:
        cell = 'H'+str(idx)
        ws[cell].value = str(t) + "%"
        idx += 1
        
        
def input_intersection_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]
    
    idx = 53
    for t in list:
        cell = 'G'+str(idx)
        ws[cell].value = t
        idx += 1

    idx = 53
    for t in list_percent:
        cell = 'H'+str(idx)
        ws[cell].value = str(t) + "%"
        idx += 1
        
        
def input_roadsep_aggregate_result(ws, list):
    list_percent = [round(x*100/sum(list),2) for x in list]
    
    idx = 61
    for t in list:
        cell = 'G'+str(idx)
        ws[cell].value = t
        idx += 1

    idx = 61
    for t in list_percent:
        cell = 'H'+str(idx)
        ws[cell].value = str(t) + "%"
        idx += 1
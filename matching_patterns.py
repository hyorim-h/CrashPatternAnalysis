import pandas as pd
from pattern_divide import *
import os
import warnings
warnings.filterwarnings(action='ignore')

cpath = os.path.dirname((os.path.abspath('__file__')))
dtf = pd.read_excel(cpath+'/차대사람사고(18-20)_원본데이터.xlsx', header=3)

patterns = []
parties = []
crashs = []
roads = []
behaviors = []

for index, row in dtf.iterrows():
    party1 = party(row['당사자종별1당'])

    party2 = 'PE'
    
    roadtype = road_type(row['도로종류'])
    roadshape = road_shape(row['도로형태'])

    behavior1 = behavior_type1(row['행동유형1당2'])
    behavior2 = behavior_type2(row['행동유형2당2'])

    crash = crash_type(row['사고유형2'])

    party12 = party1 + party2
    road = roadtype + roadshape
    behavior = behavior1 + behavior2
    pattern = party12 + "-" + crash + "-" + road + "-" + behavior
    patterns.append(pattern)
    parties.append(party12)
    crashs.append(crash)
    roads.append(road)
    behaviors.append(behavior)
    

dtf.insert(0, 'pattern', patterns)
# dtf['pattern'] = patterns
dtf['party'] = parties
dtf['crash'] = crashs
dtf['road'] = roads
dtf['behavior'] = behaviors

os.mkdir(cpath + '/산출물')
dtf.to_csv(cpath + '/산출물/교통사고패턴매칭.csv', encoding='cp949', index=False)
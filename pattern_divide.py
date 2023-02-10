# 당사자 구분
def party(data):
    # 당사자: 사륜차
    if data == '승용차':
        return "AM"
    elif data == '승합차':
        return "BU"
    elif data == '화물차':
        return "TR"
    elif data == '특수차':
        return "SP"

    # 당사자: 이륜차
    elif data == '이륜차':
        return "TW"
    elif data == '원동기장치자전거':
        return "MC"
    elif data == '개인형이동수단(PM)':
        return "PM"

    # 당사자: 자전거
    elif data == '자전거':
        return "BC"

    # 당사자: 기타 기계
    elif data == '건설기계':
        return "CM"
    elif data == '농기계':
        return "FM"
    elif data == '사륜오토바이(ATV)':
        return "AT"

    # 당사자: 보행자
    elif data == '보행자':
        return "PE"

    # 당사자: 기타
    else:
        return "ZZ"

# 사고유형 구분
def crash_type(data):
    # 사고유형: 차대사람-횡단중
    if data == '횡단중':
        return "C"

    # 사고유형: 차대사람-차도통행중
    elif data == '차도통행중':
        return "R"

    # 사고유형: 차대사람-길가장자리구역통행중
    elif data == '길가장자리구역통행중':
        return "S"
    
    # 사고유형: 차대사람-보도통행중
    elif data == '보도통행중':
        return "P"

    # 사고유형: 차대사람-기타
    else:
        return "Z"

# 도로종류 구분
def road_type(data):
    # 도로종류: 고속국도
    if data == "고속국도":
        return "E"
    
    # 도로종류: 군도
    elif data == "군도":
        return "G"

    # 도로종류: 시도
    elif data == "시도":
        return "S"

    # 도로종류: 일반국도
    elif data == "일반국도":
        return "H"

    # 도로종류: 지방도
    elif data == "지방도":
        return "R"

    # 도로종류: 특별광역시도
    elif data == "특별광역시도":
        return "M"

    # 도로종류: 기타
    else:
        return "Z"

# 도로선형 구분
def road_shape(data):
    # 도로형태: 교차로
    if data == '교차로내':
        return "I1"
    elif data == '교차로횡단보도내':
        return "I2"
    elif data == '교차로부근':
        return "I3"

    # 도로형태: 단일로
    elif data == '기타단일로':
        return "R1"
    elif data == '지하차도(도로)내':
        return "R2"
    elif data == '교량위':
        return "R3"
    elif data == '고가도로위':
        return "R4"
    elif data == '터널안':
        return "R5"

    #도로형태: 기타
    else:
        return "ZZ"

def behavior_type1(data):
    # 행동유형 1당: 직진 관련
    if data == '직진 중':
        return "D1"
    elif data == '진로변경 중':
        return "D2"
    elif data == '앞지르기 중':
        return "D3"
    
    # 행동유형 1당: 회전 관련
    elif data == '좌회전 중':
        return "T1"
    elif data == '우회전 중':
        return "T2"
    elif data == 'U턴 중':
        return "T3"

    # 행동유형 1당: 주정차
    elif data == '주정차중':
        return "P1"

    # 행동유형 1당: 후진 중
    elif data == '후진 중':
        return "R1"

    # 행동유형 1당: 주행 중 대기
    elif data == '주행 중 대기':
        return "S1"

    # 행동유형 2당: 기타
    else:
        return "ZZ"


def behavior_type2(data):
    # 행동유형 2당: 횡단보도
    if data == '횡단보도내':
        return "C1"
    elif data == '횡단보도외':
        return "C2"

    # 행동유형 2당: 도로
    elif data == '등지고 통행':
        return "R1"
    elif data == '마주보고 통행':
        return "R2"
    elif data == '도로위 작업 중':
        return "R3"
    elif data == '도로위 놀이 중':
        return "R4"

    # 행동유형 2당: 보도
    elif data == '보도 통행':
        return "P1"

    #행동유형 2당: 길가장자리
    elif data == '길가장자리구역 통행':
        return "S1"

    # 행동유형 2당: 승하차
    elif data == '승차 중 관련':
        return "O1"
    elif data == '하차 중 관련':
        return "O2"

    # 행동유형 2당: 기타
    else:
        return "ZZ"
import pyupbit
import numpy as np

# count=7 : 7일 동안의 원화시장에 대한 ohlcv(open(시가),high(고가),low(저가),close(종가),volume(거래량) 의 약자)를 불러옴!! )
df = pyupbit.get_ohlcv("KRW-BTC", count=7) 

# 변동폭 돌파 기준 범위 계산, (고가 - 저가) * k값
df['range'] = (df['high'] - df['low']) * 0.5

# target(매수가), range 칼럼을 한 칸씩 밑으로 내림 (.shift(1))
df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032_수수료 일단 없는걸로.

# ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값)
df['ror'] = np.where(df['high'] > df['target'], #고가가 목표가 보다 크면 매수 진행 
                     df['close'] / df['target'], #종가가 목표가 분의 종가 = 수익률
                     1)

# 누적 곱 계산 (cumprod) -> 누적 수익률
df['hpr'] = df['ror'].cumprod()

# Draw Down(하락폭) 계산 (누적 최대 값과 현재 hpr 차이 / 누적 최대 값 * 100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# Max Draw Down = MDD
print("MDD(%): ", df['dd'].max())

# 엑셀로 출력 
df.to_excel("dd.xlsx")
import pyupbit

access = "i21O7HSXXDDsIWk3FBeetwGd0h628ZEwSegQWURE"          # Access key 
secret = "vT10kMfxcmeTwCkdKAJb1dNhnhFoNJMxMfZGwQqm"          # Secret key 
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP(리플) 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회



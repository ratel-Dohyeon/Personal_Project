import pyupbit


access = "ms8sp1v8xmoJquh7bZCXvaSDN5L1842N9ioulR4Z"          # Access key 
secret = "6rN5xpaQ2TedouBx8WZkZUcYuAqwj9I5ocm6ENOr"          # Secret key 
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # 나의 KRW-XRP(리플) 조회
print(upbit.get_balance("KRW-DOGE"))    # 나의 KRW-DOGE(도지) 조회
print(upbit.get_balance("KRW-BTT"))     # 나의 KRW-BTT(비트토렌트) 조회
print(upbit.get_balance("KRW-OBSR"))    # 나의 KRW-OBSR(옵저버) 조회
print(upbit.get_balance("KRW-EOS"))     # 나의 KRW-EOS(이오스) 조회
print(upbit.get_balance("KRW-MARO"))    # 나의 KRW-MARO(마로) 조회
print(upbit.get_balance("KRW-ICX"))     # 나의 KRW-ICX(아이콘) 조회
print(upbit.get_balance("KRW-PLA"))     # 나의 KRW-PLA(플레이댑) 조회
print(upbit.get_balance("KRW-ONG"))     # 나의 KRW-XRP(온톨로지가스) 조회
print(upbit.get_balance("KRW-SOLVE"))   # 나의 KRW-SOLVE(솔브케어) 조회
print(upbit.get_balance("KRW-KNC"))     # 나의 KRW-KNC(카이버네트워크) 조회
print(upbit.get_balance("KRW-AQT"))     # 나의 (알파쿼크) 조회
print(upbit.get_balance("KRW-HUNT"))    # 나의 (헌트) 조회
print(upbit.get_balance("KRW-CVC"))     # 나의 (시빅) 조회
print(upbit.get_balance("KRW-AERGO"))   # 나의 (아르고) 조회
print(upbit.get_balance("KRW-JST"))     # 나의 (저스트) 조회
print(upbit.get_balance("KRW-STORJ"))   # 나의 (스토리지) 조회
print(upbit.get_balance("KRW-FCT2"))    # 나의 (피르마체인) 조회
print(upbit.get_balance("KRW-IOTA"))    # 나의 (아이오타) 조회
print(upbit.get_balance("KRW-DMT"))     # 나의 (디마켓) 조회
print(upbit.get_balance("KRW-LBC"))     # 나의 (엘비알와이크레딧) 조회
print(upbit.get_balance("KRW-SBD"))     # 나의 (스팀달러) 조회
print(upbit.get_balance("KRW-QKC"))     # 나의 (쿼크체인) 조회
print(upbit.get_balance("KRW-LOOM"))    # 나의 (룸네트워크) 조회
print(upbit.get_balance("KRW-ELF"))     # 나의 (엘프) 조회
print(upbit.get_balance("KRW-GLM"))     # 나의 (골렘) 조회
print(upbit.get_balance("KRW-ETH"))     # 나의 (이더리움) 조회
print(upbit.get_balance("KRW-ETC"))     # 나의 (이더리움클래식) 조회
print(upbit.get_balance("KRW-BTC"))     # 나의 (비트코인) 조회
print(upbit.get_balance("KRW-BCH"))     # 나의 (비트코인캐시) 조회
print(upbit.get_balance("KRW-QTUM"))     # 나의 (퀀텀) 조회
print(upbit.get_balance("KRW-DOT"))     # 나의 (폴카닷) 조회
print(upbit.get_balance("KRW-NEO"))     # 나의 (네오) 조회
print(upbit.get_balance("KRW-VET"))     # 나의 (비체인) 조회
print(upbit.get_balance("KRW-SSX"))     # 나의 (썸씽) 조회
print(upbit.get_balance("KRW-ADA"))     # 나의 (에이다) 조회
print(upbit.get_balance("KRW-LTC"))     # 나의 (라이트코인) 조회
print(upbit.get_balance("KRW-POWR"))     # 나의 (파워렛저) 조회
print(upbit.get_balance("KRW-XLM"))     # 나의 (스텔라루멘) 조회
print(upbit.get_balance("KRW-BTG"))     # 나의 (비트코인골드) 조회
print(upbit.get_balance("KRW-TRX"))     # 나의 (트론) 조회
print(upbit.get_balance("KRW-STRK"))     # 나의 (스트라이크) 조회
print(upbit.get_balance("KRW-WAVES"))     # 나의 (웨이브) 조회
print(upbit.get_balance("KRW-MED"))     # 나의 (메디블록) 조회
print(upbit.get_balance("KRW-LINK"))     # 나의 (체인링크) 조회


print(upbit.get_balance("KRW"))         # 보유 현금 조회



import jwt
import string
from datetime import datetime as dt
from datetime import timedelta 
from datetime import timezone
from datetime import time




try:
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjU5MzQwMSwianRpIjoiNDgyNmRjZDItNGEwNy00NmI2LTgwYzktODQ4OTcwN2MyNDZhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjQwMTg1MzU2LTk2YzMtNDQzYi1hNzBiLWY2OGZiNjM0Njc4YyIsIm5iZiI6MTYyNjU5MzQwMSwiZXhwIjoxNjI5MTg1NDAxfQ.14Nlekboeewk_JToHTlyu1cijKtgA6dpiKVelbQlH4Y"
    d = jwt.decode(token,"YpS/7FkfQqe0Iep3/nC9tEuAEQEq43h6r2ZWElsV7i8=" , algorithms=["HS256"])
    exp_time = d['exp']
    now_time = dt.now().timestamp()
    diff = exp_time - now_time
    print()

    day = int(diff / 86400)
    remain = diff % 86400
    hour = int(remain / 3600)
    remain1 = diff % 3600
    mins = int(remain1 / 60)
    sec = exp_time - (day * 86400) - (hour * 3600) - (mins * 60)
    print(f"{day} {hour} {mins} {sec}")

except jwt.InvalidSignatureError:
    print("Fail!!")
import pandas as pd
from cipher.cipher import make_key
from cipher.cipher import make_signature
import pickle

# 模擬データフレームの作成
send_data_list = []

# カギの作成
secret_key, public_key = make_key()

bt_addrs = ["12:34:56:78:AA:BB", "12:34:56:78:AA:CC", "12:34:56:78:AA:DD",12345678]
device_name = ["19G1101001A","19G1101001B","19G1101001",12345678]

df = pd.DataFrame(list(zip(bt_addrs, device_name)), columns=['bt_addrs', 'device_name'])

### ↑は模擬データフレームの作成 ###

# pickle df
# create a file
picklefile = open('df_marks', 'wb')
# pickle the dataframe
bytes_df = pickle.dump(df, picklefile)

# 署名の作成
signature = make_signature(secret_key, df)

# 模擬送信データの作成
send_data_list.append(bytes_df)
send_data_list.append(public_key)
send_data_list.append(signature)

# 内容の確認
print(send_data_list)

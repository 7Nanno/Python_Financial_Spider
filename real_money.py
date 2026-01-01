import os
import pandas as pd
import time
import random
base_dir=os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "赚钱资产.xlsx")
for i in range(1, 4): 
    #模拟抓到了数据
    now=time.strftime("%H:%M:%S") #格式化时间
    money=random.randint(500, 1000) #随即变出500到1000块钱
    df_new=pd.DataFrame([{"时间": now, "金额": money}])
    if not os.path.exists(file_path):
        df_new.to_excel(file_path, index=False)#如果绰号地址里无文件则直接新建并保存
else:
    old_data=pd.read_excel(file_path)#如果有文件，先读出旧的，贴上新的，再存回去
    combined=pd.concat([old_data, df_new], ignore_index=True)
    combined.to_excel(file_path, index=False)
    print(f"√成功记录第{i}笔，存到了{file_path}")
    time.sleep(2)#歇两秒别跑太快
    os.startfile(base_dir)
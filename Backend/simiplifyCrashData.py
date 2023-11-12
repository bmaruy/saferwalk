import csv
import pandas as pd


df = pd.read_csv('trafficData/Traffic_Crashes_Resulting_in_Injury_20231111.csv', low_memory=False)
df.to_csv('trafficData/similifiedCrashData.csv', columns=['cnn_intrsctn_fkey', 'cnn_sgmt_fkey', 'ped_action','number_injured','number_killed'])

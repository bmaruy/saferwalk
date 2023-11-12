import csv
import pandas as pd

def conditions(row):
    val=row['number_injured'] + 5*row['number_killed']
    if row['ped_action'] == "No Pedestrian Involved":
        val += 0
    else:
        val += 2
    return val

cnn_intrsctn_fkey = pd.read_csv('trafficData/similifiedCrashData.csv')

cnn_intrsctn_fkey['ped_action'] = cnn_intrsctn_fkey.apply(conditions,axis=1)

#cnn_intrsctn_fkey.rename(columns={"ped_action":"danger"})

cnn_sgmt_fkey = cnn_intrsctn_fkey.copy()

cnn_intrsctn_fkey.groupby(['cnn_intrsctn_fkey']).mean()
cnn_intrsctn_fkey["ped_action"] = (cnn_intrsctn_fkey["ped_action"]/cnn_intrsctn_fkey['ped_action'].mean())
print(cnn_intrsctn_fkey)
cnn_intrsctn_fkey.to_csv('intersectonValue.csv', columns=['cnn_intrsctn_fkey', 'ped_action'])


cnn_sgmt_fkey.dropna(subset=['cnn_sgmt_fkey'], inplace=True)


cnn_sgmt_fkey.groupby(['cnn_sgmt_fkey']).mean()
cnn_sgmt_fkey["ped_action"] = (cnn_sgmt_fkey["ped_action"]/cnn_sgmt_fkey['ped_action'].mean())
print(cnn_sgmt_fkey)
cnn_sgmt_fkey.rename(columns={"cnn_sgmt_fkey":"cnn_intrsctn_fkey"})
cnn_sgmt_fkey.to_csv('segmentValue.csv', columns=['cnn_sgmt_fkey', 'ped_action'])



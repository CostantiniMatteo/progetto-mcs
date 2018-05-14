import matplotlib.pyplot as plt  
import pandas as pd  

dt = pd.read_csv(
    "../logs/res.log", 
    sep=',', 
    encoding="utf-8-sig", 
)


plt.figure(figsize=(12, 14)) 



plt.ylim(0, max(dt.loc[:, 'time'])    
plt.xlim(0, 16)  
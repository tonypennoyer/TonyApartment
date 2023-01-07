import pandas as pd

# Using Weighted Product Model (WPM)

#### Grading Weight
### Subway 10
### Park 9
### Cost 8
### Space 8
### Finish 6
### Laundry 5
### Stores 3


d = {'mins_to_subway':[0,1],'mins_to_park':[0,1],'cost':[0,1], 'broker_fee':[0,1]'laundry':[0,1],'sq_ft':[0,1],'finish':[0,1],'stores':[0,1],'elevator':[1,0],'exposure':[0,1]}
df = pd.DataFrame(data=d)

print(df)




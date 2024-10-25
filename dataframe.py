#Ro'zimatov Shuhrat

import pandas as pd

data={
'ism':['Shuhrat','Bunyod','Azizbek','Odiljon','Temur','Sobirjon','Javoxir',
       'Asliddin','Avazbek','Adhamjon'],
'yosh':[18,19,19,19,19,19,22,19,19,19],
'manzil':["Farg'ona","Farg'ona","Farg'ona","Farg'ona","Farg'ona","Qo'qon",
          "Namangan","Qashqadaryo","Namangam","Namangan"]
}
df=pd.DataFrame(data)

print(df)

df['yosh']++1

fargonaliklar=df[df['manzil']=="Farg'ona"]
print("Farg'onaliklar ro'yxati:\n",fargonaliklar)
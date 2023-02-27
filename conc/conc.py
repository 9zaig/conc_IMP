import pandas as pd


excel_url = './data/20C.xlsx' #파일 이름 바꾸세요
# current= pd.read_excel(excel_url,sheet_name=10,usecols='A',nrows=200)
df= pd.read_excel(excel_url,sheet_name=None,usecols='C',nrows=200)
df_all=pd.concat(df,axis=1)
# df_all=pd.concat([current,df_all],axis=1)
print(df_all)

df_all.to_excel('./res/res.xlsx')
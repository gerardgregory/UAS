#Nama: Gerard Gregory
#NIM: 12220095
#Deskripsi: UAS Pemrograman Komputer

import streamlit as st
import pandas as pd
import plotly.express as px

#merge data
data=pd.read_csv ("produksi_minyak_mentah.csv")
dataNegara=pd.read_json ('kode_negara_lengkap.json')
dataNegara=dataNegara.rename(columns={"alpha-3":"kode_negara"})
data=pd.merge(dataNegara,data,on='kode_negara')

#selektor display
selectorNegara=data['name'].drop_duplicates()
selectorTahun=data['tahun'].drop_duplicates()
selectorBesar=[*range(1, 250, 1)]

#Judul
st.title('Data Produksi Minyak Dunia')
st.markdown('oleh Gerard Gregory 12220095')

'''
________________________________________________________________________
'''

#No.1: Produksi Minyak Tiap Negara Per Tahun
st.markdown('Produksi Minyak Tiap Negara per Tahun')
selectNegara=st.selectbox('Pilih Negara: ',selectorNegara)
dataA=data[data['name'] == selectNegara]
dataA_graph=px.line(
  dataA,
  x="tahun",
  y="produksi",
  title=str("Produksi Minyak Negara "+selectNegara)
)
st.plotly_chart(dataA_graph)

'''
________________________________________________________________________
'''

#No.2: Produksi Minyak n-besar pada Tahun x
st.markdown('Produksi Minyak n-besar per Tahun')
selectTahun=st.selectbox('Pilih Tahun: ', selectorTahun)
selectBanyakNegara=st.select_slider('Pilih Banyak Negara: ', options=selectorBesar, value=10)
dataB=data[data['tahun']==selectTahun]
dataB=dataB.sort_values(["produksi"],ascending=[0])
dataB=dataB[:selectBanyakNegara]
dataB_graph=px.bar(
  dataB,
  x="name",
  y="produksi",
  title=str(str(selectBanyakNegara)+" Negara Terbesar Produksi Minyak pada Tahun "+str(selectTahun))
)
st.plotly_chart(dataB_graph)

'''
________________________________________________________________________
'''

#No. 3: Produksi Minyak n-besar Kumulatif
st.markdown('Produksi Minyak n-besar Kumulatif')
selectBanyakNegara2=st.select_slider('Pilih Banyak Negara: ', options=selectorBesar)
dataC=data.groupby(["name"])["produksi"].sum().reset_index()
dataC=dataC.sort_values(["produksi"],ascending=[0])
dataC=dataC[:selectBanyakNegara2]
dataC_graph=px.bar(
  dataC,
  x="name",
  y="produksi",
  title=str(str(selectBanyakNegara2)+" Negara Terbesar Produksi Minyak Kumulatif")
)
st.plotly_chart(dataC_graph)

'''
________________________________________________________________________
'''

##Informasi 

st.markdown('Informasi Berdasarkan Tahun')
selectTahun2=st.selectbox('Pilih Tahun: ', selectorTahun)

'''
________________________________________________________________________
'''

st.markdown('Negara dengan jumlah produksi terbesar')
dataD=data[data['tahun']==selectTahun2]
dataD=dataD.sort_values(["produksi"],ascending=[0])
dataD=dataD[:1]
dataD[["name","kode_negara","region","sub-region","produksi"]]

'''
________________________________________________________________________
'''

st.markdown('Negara dengan jumlah produksi terkecil')
dataE=data[data['tahun']==selectTahun2]
dataE=dataE.sort_values(["produksi"],ascending=[1])
dataE= dataE.loc[dataE["produksi"]>0]
dataE=dataE[:1]
dataE[["name","kode_negara","region","sub-region","produksi"]]

'''
________________________________________________________________________
'''

st.markdown('Negara dengan jumlah produksi nol')
dataF=data[data['tahun']==selectTahun2]
dataF=dataF.sort_values(["produksi"],ascending=[1])
dataF= dataF.loc[dataF["produksi"]==0]
dataF[["name","kode_negara","region","sub-region"]]

'''
________________________________________________________________________
'''

st.markdown('Informasi Kumulatif')

'''
________________________________________________________________________
'''

st.markdown('Negara dengan jumlah produksi terbesar kumulatif')
dataG=data.groupby(["name"])["produksi"].sum().reset_index()
dataG=dataG.sort_values(["produksi"],ascending=[0])
dataTemp=data
dataTemp.drop("produksi", axis=1, inplace=True)
dataG=pd.merge(dataG,dataTemp,on='name')
dataG=dataG.drop_duplicates("name")
dataG[:1][["name","kode_negara","region","sub-region","produksi"]]

'''
________________________________________________________________________
'''

st.markdown('Negara dengan jumlah produksi terkecil kumulatif')
dataH=dataG.sort_values(["produksi"],ascending=[1])
dataH=dataH.loc[dataH["produksi"]>0]
dataH=dataH[:1]
dataH[["name","kode_negara","region","sub-region","produksi"]]

'''
________________________________________________________________________
'''

st.markdown('Negara dengan jumlah produksi nol kumulatif')
dataI=dataG.sort_values(["produksi"],ascending=[1])
dataI=dataI.loc[dataI["produksi"]==0]
dataI[["name","kode_negara","region","sub-region"]]

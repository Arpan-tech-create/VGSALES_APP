import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
plt.rcParams.update({'font.size': 16})

#reading The Datasets
read=pd.read_csv('vgsales.csv')


# Genre Counts
st.sidebar.header("COUNTING_FEATURE's VALUES")
st.header("Data Analysis on VGSALES")
st.sidebar.subheader('POPULAR_GENRE')
gen=read.Genre.value_counts()
st.sidebar.write(gen)


fig=plt.figure(figsize=(10,5))
bar=sns.barplot(x=read.Genre.value_counts(),y=read.Genre.value_counts().index)
plt.title("Popular GENRES",loc='right',color='purple')
st.pyplot(fig)

#new Dataset

new=read.sort_values(by=['Global_Sales'],ascending=False).head(10)
st.write(new)


fig=plt.figure(figsize=(5,7))
plt.pie(new.Platform.value_counts(),labels=new.Platform.value_counts().index,autopct='%1.1f%%')
plt.title("Popular Platform Based on Global_Sales",loc='right')
plt.legend()
st.pyplot(fig)


st.sidebar.subheader('POPULAR_Platform')
plat=read.Platform.value_counts(ascending=False)
st.sidebar.write(plat)



pub=read['Publisher'].value_counts().head(10)

st.write(pub)

fig=plt.figure(figsize=(5,7))
sns.pairplot(read)
st.pyplot(plt)

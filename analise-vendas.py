import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

with st.sidebar:
    st.title("Analise de Zona")
    upload_file = st.file_uploader("Coloque o seu arquivo aqui")



if upload_file is not None:

    df = pd.read_csv(upload_file)

    with st.sidebar:
       
       placa_selected = st.radio("Placa", ["1","2"], index=None)
       distinct_zone = df["Zone"].unique().tolist()
       zone_select = st.selectbox("Zona Específica", distinct_zone)
       
       if placa_selected:
          df = df[df["Board"] == placa_selected]
       
       
       if zone_select:
          df = df[df["Zone"] == zone_select]


        
        
        
    st.write("Zona por Placa")
    
    #col1 = st.columns(1)
    #cl_total = df.groupby("Zone")[["Board"]].reset_index()
    #fig_cl = px.bar(cl_total, x="Zone", y="Board", title="Faturamento por filial")
    #col1.plotly_chart(fig_cl, use_container_width=True)

    st.bar_chart(df, x="Zone", y="Port")

    st.dataframe(df, use_container_width=True)

    



    



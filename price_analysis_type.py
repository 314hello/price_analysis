import streamlit as st
import pandas as pd
import plotly.express as px

if st.button('⭠ 回到首頁'):
    st.switch_page('price_analysis_home.py')

st.header('消費者物價指數－以基本分類分類')
tab1, tab2 = st.tabs(['統計表','年增率統計表'])

with tab1:
    popover = st.popover('Tips')
    with popover:
        st.write('在圖表右上方可以將圖表放大')
    df1 = pd.read_excel('price_analysis_type_data.xlsx')
    fig1 = px.line(df1,x='日期',y='數值',color='種類',title='CPI折線圖(以基本分類分類) - 113年1月至114年1月',labels={'數值': 'CPI'})
    #fig1.update_yaxes(range=[90,110])
    st.plotly_chart(fig1)
    st.write('基期 : 110年=100')
    expander_dataframe1 = st.expander('打開資料表格(可以下載資料)')
    with expander_dataframe1:
        st.write('在表格右上方按下下載按鈕將檔案存檔下載')
        st.dataframe(df1)
    expander_table1 = st.expander('打開資料表格(僅供閱覽)')
    with expander_table1:
        st.table(df1)
    expander_source1 = st.expander('資料來源')
    with expander_source1:
        st.write('https://dmz26.moea.gov.tw/GA/common/Common.aspx?code=K&no=2')
    

with tab2:
    popover = st.popover('Tips')
    with popover:
        st.write('在圖表右上方可以將圖表放大')
    df2 = pd.read_excel('price_analysis_type_rate_data.xlsx')
    fig2 = px.line(df2,x='日期',y='數值',color='種類',title='CPI年增率折線圖(以基本分類分類) - 113年1月至114年1月',labels={'數值': 'CPI年增率'})
    #fig2.update_yaxes(range=[0,5])
    st.plotly_chart(fig2)
    #不用基期
    expander_dataframe2 = st.expander('打開資料表格(可以下載資料)')
    with expander_dataframe2:
        st.write('在表格右上方按下下載按鈕將檔案存檔下載')
        st.dataframe(df2)
    expander_table2 = st.expander('打開資料表格(僅供閱覽)')
    with expander_table2:
        st.table(df2)
    expander_source2 = st.expander('資料來源')
    with expander_source2:
        st.write('https://dmz26.moea.gov.tw/GA/common/Common.aspx?code=K&no=2')
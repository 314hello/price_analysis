import streamlit as st
import pandas as pd
import plotly.express as px

if st.button('⭠ 回到首頁'):
    st.switch_page('price_analysis_home.py')

st.header('生產者及進出口物價指數')
tab1, tab2 = st.tabs(['統計表','年增率統計表'])

with tab1:
    popover = st.popover('Tips')
    with popover:
        st.write('在圖表右上方可以將圖表放大')
    df1 = pd.read_excel('price_analysis_producer_data.xlsx')
    fig1 = px.line(df1,x='日期',y='數值',color='種類',title='PPI折線圖 - 113年1月至114年1月',labels={'數值': '物價指數'})
    st.plotly_chart(fig1)
    st.write('基期 : 110年=100')
    expander_explain1 = st.expander('專有名詞說明')
    with expander_explain1:
        st.write('PPI - 生產者物價指數(Producer Price Index)')
        st.write('MPI - 進口物價指數(Import Price Index)')
        st.write('XPI - 出口物價指數(Export Price Index)')
    expander_dataframe1 = st.expander('開資料表格(可以下載資料)')
    with expander_dataframe1:
        st.write('在表格右上方按下下載按鈕將檔案存檔下載')
        st.dataframe(df1)
    expander_table1 = st.expander('打開資料表格(僅供閱覽)')
    with expander_table1:
        st.table(df1)
    expander_source1 = st.expander('資料來源')
    with expander_source1:
        st.write('https://dmz26.moea.gov.tw/GA/common/Common.aspx?code=K&no=3')
    

with tab2:
    popover = st.popover('Tips')
    with popover:
        st.write('在圖表右上方可以將圖表放大')
    df2 = pd.read_excel('price_analysis_producer_rate_data.xlsx')
    fig2 = px.line(df2,x='日期',y='數值',color='種類',title='PPI年增率折線圖 - 113年1月至114年1月',labels={'數值': '物價數值年增率'})
    st.plotly_chart(fig2)
    #不用基期
    expander_explain2 = st.expander('專有名詞說明')
    with expander_explain2:
        st.write('PPI - 生產者物價指數(Producer Price Index)')
        st.write('MPI - 進口物價指數(Import Price Index)')
        st.write('XPI - 出口物價指數(Export Price Index)')
    expander_dataframe2 = st.expander('打開資料表格(可以下載資料)')
    with expander_dataframe2:
        st.write('在表格右上方按下下載按鈕將檔案存檔下載')
        st.dataframe(df2)
    expander_table2 = st.expander('打開資料表格(僅供閱覽)')
    with expander_table2:
        st.table(df2)
    expander_source2 = st.expander('資料來源')
    with expander_source2:
        st.write('https://dmz26.moea.gov.tw/GA/common/Common.aspx?code=K&no=3')
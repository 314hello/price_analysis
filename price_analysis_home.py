import streamlit as st

st.title('臺灣物價統計及分析')

if st.button('消費者物價指數－以商品性質分類',use_container_width=True):
    st.switch_page('price_analysis_product.py')
if st.button('消費者物價指數－以基本分類分類',use_container_width=True):
    st.switch_page('price_analysis_type.py')
if st.button('生產者及進出口物價指數',use_container_width=True):
    st.switch_page('price_analysis_producer.py')
import streamlit as st

pages = {
    'Home': [
        st.Page('price_analysis_home.py',title='首頁'),
    ],
    '統計資料及圖表': [
        st.Page('price_analysis_product.py',title='消費者物價指數－以商品性質分類'),
        st.Page('price_analysis_type.py',title='消費者物價指數－以基本分類分類'),
        st.Page('price_analysis_producer.py',title='生產者及進出口物價指數')
    ]
}

pg = st.navigation(pages)
pg.run()
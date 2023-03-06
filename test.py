

import streamlit as st  # 🎈 data web app development



st.set_page_config(
    page_title="Real-Time Data Science Dashboard",
    page_icon="✅",
    layout="wide",
)

st.markdown("""
    <style>
    #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v4{
     background-color : #ADD8E6;
     
     }

     #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div > div:nth-child(1) > div > div.css-ocqkz7.e1tzin5v4 > div.css-1r6slb0.e1tzin5v2 > div:nth-child(1) > div > div > div > div > div > img{
     
     border-radius : 50% ;
     }
    </style>
    """,unsafe_allow_html=True)
col1 , col2   = st.columns([0.2, 1])

with col2 :
     st.title('💡Elecricity Consumption Dashboard💡')

import streamlit.components.v1 as components
def main():
    
        
        html_temp = """<h1>📈Consumption Analysis📈</h1>
        <script type='module' src='https://prod-apnortheast-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-apnortheast-a.online.tableau.com/t/codedivas/views/dashboard/Dashboard4/b9d4b70b-8c8f-46c7-bcab-83de931cc91b/68227c30-efdc-4f2c-83ba-f8dbafe90cc7' width='1300' height='1000' hide-tabs toolbar='bottom' ></tableau-viz>
        <br/>
        <h1 margin-left = '50px'>📈Predictions About Future Electricity Consumption 📈</h1>
        <br/>
        <script type='module' src='https://prod-apnortheast-a.online.tableau.com/javascripts/api/tableau.embedding.3.latest.min.js'></script><tableau-viz id='tableau-viz' src='https://prod-apnortheast-a.online.tableau.com/t/codedivas/views/predict_16778288703010/Dashboard1' width='1300' height='900' hide-tabs toolbar='bottom' ></tableau-viz>"""
        components.html(html_temp, width = 2550,  height =2500)
        
    
if __name__ == "__main__":    
    main()


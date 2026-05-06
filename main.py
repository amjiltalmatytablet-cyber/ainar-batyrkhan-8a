import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Беттің параметрлерін орнату
st.set_page_config(page_title="Road Safety & Logistics AI", layout="wide")

st.title("🚘 Қазақстандағы ЖКО талдау және Логистикалық мониторинг")
st.markdown("---")

# 1. ДЕРЕКТЕРДІ ГЕНЕРАЦИЯЛАУ
def get_data():
    # Sunburst деректері
    causes_data = {
        "Category": ["Адам", "Адам", "Адам", "Инфрақұрылым", "Инфрақұрылым", "Техника", "Техника"],
        "Sub_Category": ["Жылдамдық", "Мас күйде", "Шаршау", "Жол сапасы", "Жарықтандыру", "Тежегіш", "Доңғалақ"],
        "Count": [500, 200, 150, 180, 70, 60, 40]
    }
    
    # Heatmap деректері
    days = ['Дүйсенбі', 'Сейсенбі', 'Сәрсенбі', 'Бейсенбі', 'Жұма', 'Сенбі', 'Жексенбі']
    hours = [f"{i}:00" for i in range(24)]
    heatmap_matrix = np.random.randint(10, 60, size=(7, 24))
    heatmap_matrix[4:, 17:22] += 50  # Кешкі және демалыс уақытын күшейту
    
    # Line Chart деректері
    years = list(range(2018, 2027))
    transit = [15, 18, 14, 22, 28, 35, 42, 50, 65]
    
    return pd.DataFrame(causes_data), heatmap_matrix, days, hours, years, transit

df_causes, h_matrix, days, hours, years, transit = get_data()

# 2. ВИЗУАЛИЗАЦИЯ БЛОКТАРЫ (2 бағанға бөлу)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎯 ЖКО негізгі себептері")
    fig_sun = px.sunburst(df_causes, path=['Category', 'Sub_Category'], values='Count',
                          color='Count', color_continuous_scale='Reds')
    st.plotly_chart(fig_sun, use_container_width=True)

with col2:
    st.subheader("📈 Транзиттік әлеует (БЕ-БҚ жолы)")
    fig_line = px.line(x=years, y=transit, markers=True, labels={'x': 'Жыл', 'y': 'млн тонна'})
    fig_line.update_traces(line_color='#00CC96', line_width=4)
    st.plotly_chart(fig_line, use_container_width=True)

st.markdown("---")

# 3. HEATMAP БЛОГЫ
st.subheader("🔥 Апаттардың уақыт бойынша тығыздығы")
fig_heat = px.imshow(h_matrix, labels=dict(x="Уақыт", y="Апта күні", color="Апат саны"),
                    x=hours, y=days, aspect="auto", color_continuous_scale='YlOrRd')
st.plotly_chart(fig_heat, use_container_width=True)

# 4. AI ҰСЫНЫСТАРЫ (Динамикалық блок)
st.sidebar.header("🤖 AI Сараптамасы")
st.sidebar.info("""
**Ұсыныс №1:** 'Батыс Еуропа - Батыс Қытай' жолының 245-300 км аралығында ақылды жарықтандыруды қосу қажет.

**Ұсыныс №2:** Жұма күндері сағат 18:00-де қаладан шығыс бағытқа қосымша экипаждарды орналастыру.

**Ұсыныс №3:** Жүк көліктері үшін міндетті 'Anti-sleep' датчиктерін енгізу.
""")

# Қосымша интерактивтілік
if st.button('Есепті жүктеу (PDF)'):
    st.success("Есеп дайындалуда... (Бұл функцияны іске асыру үшін ReportLab қажет)") 
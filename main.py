from pathlib import Path
import streamlit as st

from db.db import DB
from components.register_tab import register_customer
from components.customers_tab import set_customers_table
from components.management_tab import set_management_tab

st.session_state.language = "es"
app_db = DB()
st.set_page_config(layout="wide")

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
CSS_FILE = current_dir / "styles" / "main.css"

with open(CSS_FILE) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

img, title = st.columns([0.1, 0.9])
with img:
    st.image("assets/images/gimnas_puente_logo.jpg", use_column_width="always")
with title:
    st.text("")
    st.text("")
    st.title("Gimnàs Puente")

tab1, tab2, tab3, tab4 = st.tabs(["Panel Principal", "Registro", "Analiticas", "Manejo de Datos"])
with tab1:
    set_customers_table(app_db)
with tab2:
    register_customer(app_db)
with tab3:
    st.text("under construction")
with tab4:
    set_management_tab()




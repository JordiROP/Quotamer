import streamlit as st


def set_management_tab():
    imp, exp, _ = st.columns([1, 1.5, 0.5])
    with imp:
        with st.container(border=True):
            st.header("Importar datos")
            imp_csv, imp_json, imp_sql = st.columns(3)
            with imp_csv:
                st.button("Importar como CSV")
            with imp_json:
                st.button("Importar como JSON")
            with imp_sql:
                st.button("Importar como SQL")
    with exp:
        with st.container(border=True):
            st.header("Exportar datos")
            exp_csv, exp_json, exp_sql, exp_but = st.columns(4)
            with exp_csv:
                st.button("Exportar como CSV")
            with exp_json:
                st.button("Exportar como JSON")
            with exp_sql:
                st.button("Exportar como SQL")
            with exp_but:
                st.button("Exportar como SEPA")

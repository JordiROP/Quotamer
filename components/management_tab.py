import streamlit as st

from services import data_management


def set_management_tab(app_db):
    imp, exp, _ = st.columns([1, 1.5, 0.5])
    with imp:
        with st.container(border=True):
            st.header("Importar datos")
            imp_csv, imp_json, imp_sql = st.columns(3)
            with imp_csv:
                imp_csv_button = st.button("Importar como CSV")
            with imp_json:
                imp_json_button = st.button("Importar como JSON")
            with imp_sql:
                imp_sql_button = st.button("Importar como SQL")
    with exp:
        with st.container(border=True):
            st.header("Exportar datos")
            exp_csv, exp_json, exp_sql, exp_but = st.columns(4)
            with exp_csv:
                exp_csv_button = st.button("Exportar como CSV")
            with exp_json:
                exp_json_button = st.button("Exportar como JSON")
            with exp_sql:
                exp_sql_button = st.button("Exportar como SQL")
            with exp_but:
                exp_sepa_button = st.button("Exportar como SEPA")

    if imp_csv_button:
        data_management.import_as_csv(app_db)
    if imp_json_button:
        data_management.import_as_json(app_db)
    if imp_sql_button:
        data_management.import_as_sql(app_db)
    if exp_csv_button:
        data_management.export_as_csv(app_db)
    if exp_json_button:
        data_management.export_as_json(app_db)
    if exp_sql_button:
        data_management.export_as_sql(app_db)
    if exp_sepa_button:
        data_management.export_as_json(app_db)

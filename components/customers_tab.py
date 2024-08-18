from datetime import datetime
import streamlit as st

from models.customer import Customer


def set_user_updated(status):
    st.session_state.user_created = status


@st.dialog("Panel de confirmación de registro", width="large")
def update_confirmation(customer, db):
    st.warning("Por favor confirma que los campos son correctos, "
               "pulsa 'Confirmar' si todo está bien, en caso contrario pulsa la 'X' en la esquina derecha")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(f"DNI: {customer.dni}")
        st.text(f"Nombre: {customer.name}")
        st.text(f"1er Apellido: {customer.surname1}")
        st.text(f"2do Apellido: {customer.surname2}")
        st.text(f"Fecha Nacimiento: {customer.birthdate}")
        st.text(f"Telefono: {customer.phone}")
        st.text(f"Email: {customer.email}")
    with col2:
        st.text(f"Calle: {customer.street}")
        st.text(f"Portal: {customer.portal}")
        st.text(f"Puerta: {customer.door}")
        st.text(f"Ciudad: {customer.city}")
        st.text(f"Código Postal: {customer.cp}")
    with col3:
        st.text(f"IBAN: {customer.iban}")
        st.text(f"Cuota: {customer.quota}")
        st.text(f"Fecha Alta: {customer.register_date}")
        st.text(f"Fecha Baja: {customer.drop_date}")
        st.text(f"Activo: {customer.active}")

    ok = st.button("Confirmar")

    if ok:
        result = db.update_customer(customer)
        st.rerun()


def select_customer_details(selection, app_db):
    st.header(f"Detalle {selection.get("nombre", "")} " +
              f"{selection.get("apellido1", "")} " +
              f"{selection.get("apellido2", "")}")
    with st.form("user_details", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_input("DNI", key="details_dni", value=selection.get("dni", ""))
            st.text_input("Nombre", key="details_name", value=selection.get("nombre", ""))
            st.text_input("Primer Apellido", key="details_f_surname", value=selection.get("apellido1", ""))
            st.text_input("Segundo Apellido", key="details_s_surname", value=selection.get("apellido2", ""))
            st.date_input("Fecha de Nacimiento", key="details_birthday",
                          value=datetime.strptime(selection.get("fecha_nacimiento", ""), '%d/%m/%Y'))
            st.text_input("Numero de Telefono", key="details_phone", value=selection.get("telefono", ""))
            st.text_input("Email", key="details_email", value=selection.get("email", ""))
        with col2:
            st.text_input("Calle", key="details_street", value=selection.get("calle", ""))
            st.text_input("Portal", key="details_portal", value=selection.get("portal", ""))
            st.text_input("Puerta", key="details_door", value=selection.get("puerta", ""))
            st.text_input("City", key="details_city", value=selection.get("ciudad", ""))
            st.text_input("Código Postal", key="details_cp", value=selection.get("CP", ""))
        with col3:
            st.text_input("IBAN", key="details_iban", value=selection.get("IBAN", ""))
            st.number_input("Cuota", key="details_quota", value=selection.get("cuota", ""))
            st.date_input("Fecha de Alta", key="details_register_date",
                          value=datetime.strptime(selection.get("alta", ""), '%d/%m/%Y'))
            st.date_input("Fecha de Baja", key="details_drop_date",
                          value=datetime.strptime(selection.get("baja", ""), '%d/%m/%Y'))
            st.checkbox("Activo", key="details_active", value=True if selection.get("activo", "") == "Y" else False)

        submitted = st.form_submit_button("Confirmar")
        print(submitted)
        if submitted:
            customer = Customer(dni=st.session_state.details_dni, name=st.session_state.details_name,
                                surname1=st.session_state.details_f_surname,
                                surname2=st.session_state.details_s_surname,
                                birthdate=st.session_state.details_birthday, phone=st.session_state.details_phone,
                                email=st.session_state.details_email, street=st.session_state.details_street,
                                portal=st.session_state.details_portal, door=st.session_state.details_door,
                                cp=st.session_state.details_cp, city=st.session_state.details_city,
                                iban=st.session_state.details_iban, active=st.session_state.details_active,
                                register_date=st.session_state.details_register_date,
                                quota=st.session_state.details_quota, drop_date=st.session_state.details_drop_date)
            update_confirmation(customer, app_db)

        if "user_created" in st.session_state:
            if st.session_state.user_created:
                st.toast("Usuario creado correctamente", icon="✅")
            elif not st.session_state.user_created:
                st.toast("Se ha producido un error", icon="❌")
                if "user_created" in st.session_state:
                    del st.session_state.user_created


def set_customers_table(app_db):
    st.markdown("<style>{div[role=dialog]:{width: 70%}}</style>", unsafe_allow_html=True)
    customers_df = app_db.get_customers()
    event = st.dataframe(customers_df,
                         use_container_width=True,
                         selection_mode=["single-row"],
                         hide_index=True,
                         on_select="rerun")
    if event.selection.rows:
        select_customer_details(customers_df.iloc[event.selection.rows[0]].to_dict(), app_db)

import streamlit as st

from models.customer import Customer
from services.formater import INPUT_DATE_FORMAT, DATETIME_DATE_FORMAT
from services.lang_manager import LanguageManager


def init_customer(customer=None):
    if "customer" not in st.session_state:
        st.session_state.customer = Customer.create_empty_customer()
    elif customer is None:
        st.session_state.customer = st.session_state.customer
    else:
        st.session_state.customer = customer


def set_user_created(status):
    st.session_state.user_created = status


def clean_session():
    if "user_created" in st.session_state:
        del st.session_state.user_created
    if "customer" in st.session_state:
        del st.session_state.customer


@st.dialog("Panel de confirmación de registro", width="large")
def register_confirmation(customer, db):
    language = st.session_state.language
    register_confirmation_title = LanguageManager.\
        get_register_tab_fields().get("confirm_register_title").get(language)
    register_confirmation_warning = LanguageManager.\
        get_register_tab_fields().get("confirm_register_warning").get(language)
    register_confirmation_fields = LanguageManager.\
        get_register_tab_fields().get("register_fields").get(language)
    st.warning(register_confirmation_warning)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(f"DNI: {customer.dni}")
        st.text(f"Nombre: {customer.name}")
        st.text(f"1er Apellido: {customer.surname1}")
        st.text(f"2do Apellido: {customer.surname2}")
        st.text(f"Fecha Nacimiento: {customer.birthdate.strftime(DATETIME_DATE_FORMAT)}")
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
        st.text(f"Fecha Alta: {customer.register_date.strftime(DATETIME_DATE_FORMAT)}")

    but_col1, but_col2, *_ = st.columns([1] * 10)
    with but_col1:
        ok = st.button("Confirmar")
    with but_col2:
        ko = st.button("Cancelar")

    if ok:
        result = db.insert_customer(customer)
        set_user_created(result)
        init_customer(Customer.create_empty_customer())
        st.rerun()
    if ko:
        st.rerun()


def register_customer(db):
    st.header("Panel de Registro")
    init_customer()
    with st.form("register_form", clear_on_submit=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text_input("DNI", key="dni", value=st.session_state.customer.dni)
            st.text_input("Nombre", key="name", value=st.session_state.customer.name)
            st.text_input("Primer Apellido", key="f_surname", value=st.session_state.customer.surname1)
            st.text_input("Segundo Apellido", key="s_surname", value=st.session_state.customer.surname2)
            st.date_input("Fecha de Nacimiento", key="birthday",
                          value=st.session_state.customer.birthdate, format=INPUT_DATE_FORMAT)
            st.text_input("Numero de Telefono", key="phone", value=st.session_state.customer.phone)
            st.text_input("Email", key="email", value=st.session_state.customer.email)
        with col2:
            st.text_input("Calle", key="street", value=st.session_state.customer.street)
            st.text_input("Portal", key="portal", value=st.session_state.customer.portal)
            st.text_input("Puerta", key="door", value=st.session_state.customer.door)
            st.text_input("City", key="city", value=st.session_state.customer.city)
            st.text_input("Código Postal", key="cp", value=st.session_state.customer.cp)
        with col3:
            st.text_input("IBAN", key="iban", value=st.session_state.customer.iban)
            st.number_input("Cuota", key="quota", value=st.session_state.customer.quota)
            st.date_input("Fecha de Alta", key="register_date",
                          value=st.session_state.customer.register_date, format=INPUT_DATE_FORMAT)

        submitted = st.form_submit_button("Confirmar")

        if submitted:
            customer = Customer(dni=st.session_state.dni, name=st.session_state.name,
                                surname1=st.session_state.f_surname, surname2=st.session_state.s_surname,
                                birthdate=st.session_state.birthday, phone=st.session_state.phone,
                                email=st.session_state.email, street=st.session_state.street,
                                portal=st.session_state.portal, door=st.session_state.door,
                                cp=st.session_state.cp, city=st.session_state.city, iban=st.session_state.iban,
                                register_date=st.session_state.register_date, quota=st.session_state.quota, active=True)
            init_customer(customer)
            register_confirmation(customer, db)

        if "user_created" in st.session_state:
            if st.session_state.user_created:
                st.toast("Usuario creado correctamente", icon="✅")
                clean_session()
            elif not st.session_state.user_created:
                st.toast("Se ha producido un error", icon="❌")
                if "user_created" in st.session_state:
                    del st.session_state.user_created

    del_button = st.button("Limpiar Campos")

    if del_button:
        clean_session()
        st.rerun()

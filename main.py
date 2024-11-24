import streamlit as st
from pandas.core.reshape.util import tile_compat
from requests import session
from streamlit import session_state

st.set_page_config(page_title='Stock info', layout='centered')

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

def login():
    if st.button('Login'):
        st.session_state['logged_in'] = True
        st.rerun()

def logout():
    if st.button('Logout'):
        st.session_state['logged_in'] = False
        st.rerun()

login = st.Page(login, title='login', icon='🍕')
logout = st.Page(logout, title='logout', icon='🍜')

stock_description = st.Page(page='maintenance/stock_description.py', title='Description', icon='🔬')
stock_history = st.Page(page='maintenance/stock_history.py', title='History', icon='🧩')
stock_forecasts = st.Page(page='maintenance/stock_forecasts.py', title='Forecast', icon='♾️')
stock_update = st.Page(page='presentation/database_operations.py', title='Data update', icon='🎡')
page_info = st.Page(page='presentation/info_about.py', title='"About this" page', icon='🐣')


if session_state['logged_in']:
    pg = st.navigation({'Instrument':[stock_description,
                                      stock_history,
                                      stock_forecasts],
                        'Maintenance':[stock_update,
                                       page_info],
                        'Logout':[logout]}
                       )
else:
    pg = st.navigation([login])

if __name__ == '__main__':
    pg.run()

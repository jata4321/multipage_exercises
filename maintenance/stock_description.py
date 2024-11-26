import streamlit as st
import yfinance as yf

st.subheader('Instrument description')

try:
    instrument = yf.Ticker(st.session_state['instrument'])
    st.markdown(f'##### Intel about *{instrument.ticker}* from Yahoo Finance:')
    instrument_info = instrument.info

    st.markdown(f'*{instrument_info["longBusinessSummary"]}*')
    st.divider()
    for enum, (key, value) in enumerate(instrument_info.items()):
        if enum < 7:
            st.markdown(f'{key}: {value}')

except any([TimeoutError, KeyError]) as e:
    st.error(f'No intel about {st.session_state["instrument"]}. Error {e}')
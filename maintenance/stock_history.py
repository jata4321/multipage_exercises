import streamlit as st
import yfinance as yf
import altair as alt

instrument = yf.Ticker(st.session_state['instrument'])
df = instrument.history(period='max')

st.dataframe(df.resample('Y').mean())

# Add a Streamlit slider to allow the user to select a date range for the data
date_range = st.slider(
    "Select Date Range",
    value=(df.index.min().to_pydatetime(), df.index.max().to_pydatetime()),
    format="YYYY-MM-DD"
)

# Filter the dataframe based on the date range selected by the user
df = df.loc[date_range[0]:date_range[1]]


# Update the Altair chart to use the smoothed data
chart = alt.Chart(df.reset_index()).mark_line(
    line={'color': 'green'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='olive', offset=0),
               alt.GradientStop(color='green', offset=1)],
    )
).encode(
    x='Date:T',
    y=alt.Y('Close:Q').scale(zero=False)  # Use the smoothed data
).properties(
    title='Closing Prices Over Time'
)


chart2 = alt.Chart(df.reset_index()).mark_area(
    line={'color': 'green'},
    color=alt.Gradient(
        gradient='linear',
        stops=[alt.GradientStop(color='olive', offset=0),
               alt.GradientStop(color='green', offset=1)],
        x1=1, x2=1, y1=1, y2=0
    )
).encode(
    x='Date:T',
    y=alt.Y('Close:Q').scale(type='symlog', zero=False),
).properties(
    title='Closing Prices Over Time'
)
# Create an Altair area chart with a gradient

# Display the chart using Streamlit
st.altair_chart(chart, use_container_width=True)
st.altair_chart(chart2, use_container_width=True)

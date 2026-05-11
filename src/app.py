import streamlit as st
import plotly.express as px
st.set_page_config(page_title="Cloud Data Dashboard", layout="wide")
st.title("Cloud Data Dashboard")
st.write("A beginner-friendly business intelligence dashboard.")
from src.analysis import (
    load_data,
    get_total_revenue,
    get_sales_by_region,
    get_sales_by_product,
    get_top_product,
)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv""

df = load_data(DATA_FILE)

total_revenue = get_total_revenue(df)
top_product = get_top_product(df)

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Revenue", f"£{total_revenue:,.2f}")

with col2:
    st.metric("Top Product", top_product)

st.subheader("Sales by Region")
region_sales = get_sales_by_region(df)
fig_region = px.bar(region_sales, x="region", y="revenue")
st.plotly_chart(fig_region, use_container_width=True)

st.subheader("Sales by Product")
product_sales = get_sales_by_product(df)
fig_product = px.pie(product_sales, names="product", values="revenue")
st.plotly_chart(fig_product, use_container_width=True)

st.subheader("Raw Data")
st.dataframe(df)
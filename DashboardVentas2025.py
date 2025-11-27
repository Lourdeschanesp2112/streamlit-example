import streamlit as st
import pandas as pd
import plotly as px

st.set_page_config(page_title='Análisis de Ventas y Ganancias', page_icon='📊', layout='wide')

st.title('Análisis de Ventas y Ganancias de Productos')

# --- Carga de Datos ---
file_path = 'SalidaVentas.xlsx'
df = pd.read_excel(file_path)

# --- Visualización de Datos Inicial ---
st.subheader('Primeras Filas del DataFrame')
st.text(df.head().to_string())

st.subheader('Tipos de Datos del DataFrame')
st.text(df.dtypes.to_string())

# --- Top 5 Productos por Ventas ---
st.subheader('Top 5 Productos por Ventas')
top_5_products = df.groupby('Product Name')['Sales'].sum().nlargest(5).reset_index()
top_5_products.columns = ['Product Name', 'Total Sales']
fig_sales = px.bar(
    top_5_products,
    x='Product Name',
    y='Total Sales',
    title='Top 5 Productos por Ventas',
    labels={'Product Name': 'Producto', 'Total Sales': 'Ventas Totales'}
)
st.plotly_chart(fig_sales, width='stretch')

# --- Top 5 Productos por Ganancias ---
st.subheader('Top 5 Productos por Ganancias')
top_5_products_profit = df.groupby('Product Name')['Profit'].sum().nlargest(5).reset_index()
top_5_products_profit.columns = ['Product Name', 'Total Profit']
fig_profit = px.bar(
    top_5_products_profit,
    x='Product Name',
    y='Total Profit',
    title='Top 5 Productos por Ganancias',
    labels={'Product Name': 'Producto', 'Total Profit': 'Ganancias Totales'}
)
st.plotly_chart(fig_profit, width='stretch')

# --- Comparación Gráfica de Ventas y Ganancias para Productos Destacados ---
# Re-generar unique_top_products y product_metrics para el script consolidado
top_sales_products_list = df.groupby('Product Name')['Sales'].sum().nlargest(5).index.tolist()
top_profit_products_list = df.groupby('Product Name')['Profit'].sum().nlargest(5).index.tolist()
combined_products_set = set(top_sales_products_list + top_profit_products_list)
unique_top_products = list(combined_products_set)

filtered_df = df[df['Product Name'].isin(unique_top_products)]
product_metrics = filtered_df.groupby('Product Name')[['Sales', 'Profit']].sum().reset_index()

st.subheader('Ventas y Ganancias Combinadas para Productos Destacados')
fig_combined = px.bar(
    product_metrics,
    x='Product Name',
    y=['Sales', 'Profit'],
    title='Ventas y Ganancias Totales de Productos Destacados',
    labels={'value': 'Cantidad', 'variable': 'Métrica'},
    barmode='group'
)
st.plotly_chart(fig_combined, width='stretch')

import pandas as pd

file_path = 'SalidaVentas.xlsx'
df = pd.read_excel(file_path)
st.subheader('Primeras Filas del DataFrame')
st.text(df.head().to_string())
import plotly.graph_objects as go

# Calculate top 5 products by sales
top_5_products_sales = df.groupby('Product Name')['Sales'].sum().nlargest(5).reset_index()
top_5_products_sales.columns = ['Product Name', 'Total Sales']

# Create the bar chart using Plotly Graph Objects
fig_top_sales_go = go.Figure(
    data=[
        go.Bar(
            x=top_5_products_sales['Product Name'],
            y=top_5_products_sales['Total Sales'],
            marker_color=top_5_products_sales['Total Sales'], # Color by sales value
            marker_colorscale='Plasma' # Use a Plasma color scale
        )
    ]
)

fig_top_sales_go.update_layout(
    title_text='Top 5 Productos Más Vendidos',
    xaxis_title='Producto',
    yaxis_title='Ventas Totales',
    xaxis={'categoryorder':'total descending'}
)

fig_top_sales_go.show()

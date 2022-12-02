import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid.shared import GridUpdateMode
from st_aggrid.shared import ColumnsAutoSizeMode

st.set_page_config(page_title="Marketing BI", layout="wide") 
new_title = '<p style="font-family:sans-serif; color:#121212; font-size: 42px;">Marketing BI - Project 1</p>'

st.markdown(new_title, unsafe_allow_html=True)

@st.experimental_memo(ttl=7200)
def read_df(path):
    orders_df = pd.read_csv(path, parse_dates=["Order Date"])
    return orders_df

orders_df = read_df("supermarket_data.csv")

cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('Bakery')) {
        return {
            'color': 'white',
            'backgroundColor': '#b1cbbb' //light green
        }
    } else if (params.value.includes('Food Grains')){
            return {
                'color' : 'white',
                'backgroundColor': '#eea29a'  // light red
                }
    } else {
        return {
            'color': 'black',
            'backgroundColor': 'white'
        }
    }
};
"""
)
        
gb = GridOptionsBuilder.from_dataframe(orders_df)
gb.configure_pagination(paginationPageSize=25, paginationAutoPageSize=False)
gb.configure_column("Category", cellStyle=cellsytle_jscode)
gb.configure_column("Sales", 
                    type=["numericColumn","numberColumnFilter","customNumericFormat"], 
                    valueFormatter="data.Sales.toLocaleString('en-US', {style: 'currency', currency: 'INR', maximumFractionDigits:1})") 
gb.configure_column("Profit", 
                    type=["numericColumn","numberColumnFilter","customNumericFormat"], 
                    valueFormatter="data.Profit.toLocaleString('en-US', {style: 'currency', currency: 'INR', maximumFractionDigits:1})") 
gb.configure_column("Discount", 
                    valueFormatter="data.Discount.toLocaleString('en-US', {style: 'percent', maximumFractionDigits:2 })"
                    ) 

gridOptions = gb.build()

data = AgGrid(orders_df, 
       gridOptions=gridOptions,
       allow_unsafe_jscode=True,
       update_mode=GridUpdateMode.FILTERING_CHANGED,
       enable_enterprise_modules=False,
       columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS,
       width=10
)



import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid.shared import GridUpdateMode
from st_aggrid.shared import ColumnsAutoSizeMode

st.set_page_config(page_title="Marketing BI", layout="wide") 
st.title('Marketing BI - Project 1')

def format(x):
    return "₹{:,.1f}".format(x)
def format_pcnt(x):
    return "{:.1f} %".format(100 * x)


orders_df = pd.read_csv("supermarket_data.csv", parse_dates=["Order Date"])
orders_df["Sales Rup"] = orders_df["Sales"]
orders_df["Sales Rup"] = orders_df["Sales Rup"].apply(format)
orders_df["Discount"] = orders_df["Discount"].apply(format_pcnt)
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

gridOptions = gb.build()

data = AgGrid(orders_df, 
       gridOptions=gridOptions,
       allow_unsafe_jscode=True,
       #update_mode=GridUpdateMode.MODEL_CHANGED
       update_mode=GridUpdateMode.FILTERING_CHANGED,
       enable_enterprise_modules=False,
       columns_auto_size_mode=ColumnsAutoSizeMode.FIT_CONTENTS
       
            
)



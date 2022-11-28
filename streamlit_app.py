import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode
from st_aggrid.shared import GridUpdateMode

st.set_page_config(page_title="Marketing BI", layout="wide") 
st.title('🎈 Marketing BI - Project 1')



orders_df = pd.read_csv("supermarket_data.csv", parse_dates=["Order Date"])

# container = st.container()

# with container:
#     st.markdown('----')
#     sliders = st.columns(4)
#     #st.markdown('----')
#     sliders2 = st.columns(4)
#     st.markdown('----')

# with sliders[0]:
#     sales_slider = st.slider("price", 0.0, 10000.0, [1000.0, 8000.0])

# with sliders[1]:
#     discount_slider = st.slider("voucher", 0.0, 10000.0, [1000.0, 8000.0])

# with sliders[2]:
#     adult_slider = st.slider("adults", 0, 30, [2, 8])
#     children_slider = st.slider("children", 0, 30, [1, 5])

# with sliders[3]:
#     insurence_slider = st.slider("insuderence", 0.0, 10000.0, [1000.0, 8000.0])
    
# with sliders2[0]:
#     sales_slider = st.slider("price1", 0.0, 10000.0, [1000.0, 8000.0])
    
# with sliders2[1]:
#     sales_slider = st.slider("price3", 0.0, 10000.0, [1000.0, 8000.0])

# with sliders2[2]:
#     sales_slider = st.slider("price4", 0.0, 10000.0, [1000.0, 8000.0])

# with sliders2[3]:
#     sales_slider = st.slider("pricej", 0.0, 10000.0, [1000.0, 8000.0])
    
# add this

cellsytle_jscode = JsCode(
    """
function(params) {
    if (params.value.includes('Bakery')) {
        return {
            'color': 'white',
            'backgroundColor': 'green'
        }
    } else if (params.value.includes('Food Grains')){
            return {
                'color' : 'white',
                'backgroundColor': 'red'
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
gb.configure_column("Category", cellStyle=cellsytle_jscode,)

gridOptions = gb.build()

data = AgGrid(orders_df, 
       gridOptions=gridOptions,
       allow_unsafe_jscode=True,
       #update_mode=GridUpdateMode.MODEL_CHANGED
       update_mode=GridUpdateMode.FILTERING_CHANGED,
       enable_enterprise_modules=False
)



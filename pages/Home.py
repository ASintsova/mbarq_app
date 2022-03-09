import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
import plotly.express as px


def app():
    url = "https://github.com/MicrobiologyETHZ/mbarq"
    st.markdown(f""" 

    This app allows exploration of data processed and analyzed with [mBARq tool]({url})
 
    ### Options:
    1. **Library Map**: Allows you to visualize the insertions present in your library and provides some basic summary statistics.
        - Requires mapping file generated by `mbarq map` command
        
    2. **PCA**: Generates an interactive PCA plot
        - Requires merged count file generated by `mbarq count` and a the same sample data file used for the analysis
        
    3. **Barcode Abundance**
    
    4. **Differential Abundance**
    
    5. **Pathway Visualisation**
    
    Links and citations
    
    """)
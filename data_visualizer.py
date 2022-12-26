import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
figure=plt.figure()
def date_converter(date_col):
    result=list()
    values=date_col.values
    for value in values:
        result.append(str(value).split("T")[0])
    return result
st.markdown("<h1 style='text-align: center;'>Data Visualizer</h1>", unsafe_allow_html=True)
st.markdown("---", unsafe_allow_html=True)
files_names=list()
files=st.file_uploader("Upload your files", type=["xlsx"], accept_multiple_files=True)
if files: 
    for file in files:
        files_names.append(file.name)
        print(files_names)
    selected_files=st.multiselect("Multiselect", options=files_names)
    if selected_files:
        options=st.radio("Select Entity Against Date", options=["None", "GPU", "CPU", "RAM", "KEYBOARD", "CASING"])
        if options != "None":
            for file in files:
                if file.name in selected_files:
                    shop_data=pd.read_excel(file, index_col=0) 
                    item=list(shop_data[options]) 
                    dates=date_converter(shop_data["DATE"])
                    index=np.arrange(len(dates))
                    plt.xticks(index, dates)
                    plt.gcf().autofmt_xdate()
                    plt.plot(index, item, label=file.name, marker="o")
                    plt.xlabel("Date")
                    plt.ylabel("option")
                    plt.title(options+"chart")
                    plt.grid(True)
                    plt.legend()
                    print(dates)
                st.write(figure)               
from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd


#----LOAD ASSETS-----
img_Biotique_facewash = Image.open("img/Biotique_facewash.png")
img_Dot_Key_facewash = Image.open("img/Dot_Key_facewash.png")
img_derma_facewash=Image.open("img/derma_facewash.png")
img_mama_facewash=Image.open("img/mama_facewash.png")



#---FACE WASH---
with st.container():
	st.header("Face wash")
	st.write("##")
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_Biotique_facewash)


	with text_column:
		st.subheader("Biotique Facewash")
		st.write(
			"""
			Biotique Fresh Neem Pimple Control Face Wash ,
			 Ayurvedic and Organically Pure, Prevents Pimples, 
			 100% Botanical Extracts , Suitable for All Skin Types 
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/hPIPU9h)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_Dot_Key_facewash)


	with text_column:
		st.subheader("Dot & Key Facewash")
		st.write(
			"""
			Dot & Key CICA Face Wash for Acne Prone Skin, 2% Salicylic Acid Face Wash
			 with Green Tea , For Oily & Sensitive Skin , Sulphate Free Face Wash for Men & Women,
			  Oil Control Face Wash with Zinc
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/8URpkYR)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_derma_facewash)


	with text_column:
		st.subheader("Derma Co Facewash")
		st.write(
			"""
			The Derma Co 1% Salicylic Acid Gel Face Wash With Salicylic Acid & Witch Hazel For Active Acne 
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/6xo7zIN)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mama_facewash)


	with text_column:
		st.subheader("Mamaearth Facewash")
		st.write(
			"""
			Mamaearth Ubtan Natural Face Wash For all Skin Type with Turmeric & Saffron for Tan Removal 
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/9cGDE3x)")


#--GRAPH
with st.container():
    st.header('Graph')

    ##---LOAD DATAFRAME
    excel_file = 'Excel/facewash.xlsx'
    sheet_name = 'Sheet1'

    df = pd.read_excel(excel_file,
                       sheet_name=sheet_name,
                       usecols='A:C',
                       header=0)

    groupby = st.selectbox(
        'What would you like to analyze?',
        ('Rating', 'Cost'),
    )

    #--PLOT BAR GRAPH
    if groupby == 'Rating':
        fig1 = px.bar(df,
                     x='Product',
                     y='Rating',
                     color='Product',
                     template='plotly_white'
                    )             
        st.plotly_chart(fig1)

    if groupby == 'Cost':
        fig2 = px.bar(df,
                     x='Product',
                     y='Cost',
                     color='Product',
                     template='plotly_white'
                    )
        st.plotly_chart(fig2)



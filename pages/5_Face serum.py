from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd


#----LOAD ASSETS-----
img_garnier_faceserum= Image.open("img/garnier_faceserum.png")
img_derma_co_faceserum = Image.open("img/derma_co_faceserum.png")
img_minimalist_faceserum = Image.open("img/minimalist_faceserum.png")
img_mamaearth_faceserum= Image.open("img/mamaearth_faceserum.png")



#---FACE SERUM---
with st.container():
	st.header("Face Serum")
	st.write("##")
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_derma_co_faceserum)


	with text_column:
		st.subheader("The Derma Co Face Serum")
		st.write(
			"""
			The Derma Co 10% Vitamin C Face Serum with Vitamin C, 5% Niacinamide & Hyaluronic Acid for Skin Radiance

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/e32I0IC)")


#second product
with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mamaearth_faceserum)


	with text_column:
		st.subheader("Mamaearth Face Serum")
		st.write(
			"""
			Mamaearth Vitamin C Daily Glow Face Serum for Men & Women - Vitamin C Serum for Glowing Skin, Oily Skin & Dark Spots, With 50x Vitamin C 

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/gzmT8hK)")


#third product
with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_garnier_faceserum)


	with text_column:
		st.subheader("Garnier Face Serum")
		st.write(
			"""
			Garnier Skin Naturals, Face Serum, Increases Skin's Glow Instantly and Reduces Spots Overtime, Bright Complete Vitamin C Booster

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/47QAchn)")

#fourth product
with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_minimalist_faceserum)


	with text_column:
		st.subheader("Minimalist Face Serum")
		st.write(
			"""
			Minimalist 10% Vitamin C Face Serum for Glowing Skin (Beginner Friendly Potent Vitamin C Formula) - Highly Stable & Effective Skin Brightening Vit C Serum - Non Irritating

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/8gqSUd2)")


#--GRAPH
with st.container():
    st.header('Graph')

    ##---LOAD DATAFRAME
    excel_file = 'Excel/face_serum.xlsx'
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
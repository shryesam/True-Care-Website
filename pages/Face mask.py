from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd


#----LOAD ASSETS-----
img_bio_facepack= Image.open("img/bio_facepack.png")
img_dermaCo_facepack = Image.open("img/dermaCo_facepack.png")
img_mamaearth_facepack = Image.open("img/mamaearth_facepack.png")
img_mCaff_facepack= Image.open("img/mCaff_facepack.png")



#---FACE MASK---
with st.container():
	st.header("Face Mask")
	st.write("##")
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mCaff_facepack)


	with text_column:
		st.subheader("mCaffeine Face Mask")
		st.write(
			"""
			mCaffeine Coffee De Tan Face Pack Mask with Kaolin Clay, Multani Mitti & Bentonite Clay
			 ,Removes Tan, Cleanses Pores & Controls Excess Oil  For All Skin Types

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/2tzOQu9)")

#second product
with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mamaearth_facepack)


	with text_column:
		st.subheader("Mamaearth Face Pack")
		st.write(
			"""
			Mamaearth Multani Mitti Face Pack with Multani Mitti and Bulgarian Rose for Oil Control & Acne
			 ,Hydrating & Glowing ,Paraben-Free ,No Silicones - No Sulphates

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/0kW6kZx)")

#third product
with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_dermaCo_facepack)


	with text_column:
		st.subheader("The Derma Co Face Mask")
		st.write(
			"""
			The Derma Co 2% Salicylic Acid Clay Face Mask for Acne & Blemish Prone Skin

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/9YCVz9o)")
#fourth product
with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_bio_facepack)


	with text_column:
		st.subheader("Biotique Face Pack")
		st.write(
			"""
			Biotique Fruit Brightening Depigmentation and Tan Removal Face Pack- Ayurvedic and Organically Pure- Tan Removal Face Pack for All Skin Types-100% Botanical Extracts

			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/81zIg37)")

#--GRAPH
with st.container():
    st.header('Graph')

    ##---LOAD DATAFRAME
    excel_file = 'Excel/Kajal.xlsx'
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
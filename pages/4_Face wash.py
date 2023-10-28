from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#----LOAD ASSETS-----
img_Biotique_facewash = Image.open("img/Biotique_facewash.png")
img_Dot_Key_facewash = Image.open("img/Dot_Key_facewash.png")



#---KAJAL---
with st.container():
	st.header("Facewash")
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


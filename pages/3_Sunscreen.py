from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#----LOAD ASSETS-----
img_Derma_Co_sunscreen = Image.open("img/Derma_Co_sunscreen.png")
img_Dot_Key_sunscreen = Image.open("img/Dot_Key_sunscreen.png")



#---KAJAL---
with st.container():
	st.header("Sunscreen")
	st.write("##")
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_Dot_Key_sunscreen)


	with text_column:
		st.subheader("Dot & Key Sunscreen")
		st.write(
			"""
			Dot & Key Vitamin C + E Super Bright Sunscreen SPF 50 , Water-Light, 
			UVA/UVB & Blue Light Protection , For Even Toned & Glowing Skin ,
			 With Liquid SPF 50+++ , No White Cast,  For All Skin Types
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/c0ZgyWE)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_Derma_Co_sunscreen)


	with text_column:
		st.subheader("Derma Co Sunscreen")
		st.write(
			"""
			The Derma Co 1% Hyaluronic Sunscreen Aqua Ultra Light Gel with
			 SPF 50 PA++++ For Broad Spectrum, UV A, UV B & Blue Light Protection
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/hf7Wo8A)")


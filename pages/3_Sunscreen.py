from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#----LOAD ASSETS-----
img_Derma_Co_sunscreen = Image.open("img/Derma_Co_sunscreen.png")
img_Dot_Key_sunscreen = Image.open("img/Dot_Key_sunscreen.png")
img_bio_sunscreen=Image.open("img/bio_sunscreen.png")
img_mama_sunscreen=Image.open("img/mama_sunscreen.png")



#---SUNSCREEN---
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

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_bio_sunscreen)


	with text_column:
		st.subheader("Biotique Sunscreen")
		st.write(
			"""
			Biotique Sandalwood Sunscreen Ultra Soothing Face Lotion, 
			SPF 50+ ,Ultra Protective Lotion, Keeps Skin Soft, Fair and Moisturized
			, Water Resistant, For All Skin Types
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/7opafHg)")


with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mama_sunscreen)


	with text_column:
		st.subheader("Mamaearth Sunscreen")
		st.write(
			"""
			Mamaearth Daily Glow Sunscreen SPF 50 PA+++, No White Cast with Vitamin C 
			& Turmeric for Sun Protection & Glow 
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/0tKypvu)")



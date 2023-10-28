from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie


#----LOAD ASSETS-----
img_farm_herb = Image.open("img/farm_herb.png")
img_tat_sat = Image.open("img/tatsat.png")
img_soul_tree = Image.open("img/soultree.png")
img_mama_earth= Image.open("img/mamaearth.png")



#---KAJAL---
with st.container():
	st.header("Kajal")
	st.write("##")
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_farm_herb)


	with text_column:
		st.subheader("Farm Herb Kajal")
		st.write(
			"""
			Farmherbs 100% Herbal Kajal Stick for Adults - Olive wax based , 
			  Certified Lead-free, irritation-free, waterproof, relaxing creamy texture, Black, Matte Finish
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/bY5t4mE)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_tat_sat)


	with text_column:
		st.subheader("Tat Sat Kajal")
		st.write(
			"""
			TATSAT-100% Natural Ayurvedic kajal Pencil with Herbs to nourish eyes,Medicated Soot,
			Desi Cow Ghee & Almond oil , No Preservatives ,  No chemicals , No irritation 
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/aY1y3eW)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_soul_tree )


	with text_column:
		st.subheader("SoulTree Kajal")
		st.write(
			"""
			SoulTree Ayurvedic Pure Black Kajal - 100% Natural, Matte Finish for Soothing 
			& Cleansing effect
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/gRKAB9t)")

with st.container():
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mama_earth)


	with text_column:
		st.subheader("Mamaearth Kajal")
		st.write(
			"""
			Mamaearth Long Stay Natural Black Kajal, Smudge-Proof and Waterproof ,   
			11-Hour Long Stay, Charcoal Black Kajal for Women
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/1XTiB2k)")



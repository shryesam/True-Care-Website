from PIL import Image 
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd


#----LOAD ASSETS-----
img_mama_lipbalm =Image.open("img/mamalip.png") 
img_kau_lip = Image.open("img/kau_lip.png")
img_cocoa_lip = Image.open("img/cocoa_lip.png")
img_khadi_lip = Image.open("img/khadi_lip.png")
img_nivea_lip = Image.open("img/nivea_lip.png")

#----LIPBALM----
with st.container():
	st.header("Lipbalm")
	st.write("##")
	image_column,text_column=st.columns((1,2))

	with image_column:
		st.image(img_mama_lipbalm)


	with text_column:
		st.subheader("Mamaearth Natural Lip Balm")
		st.write(
			"""
			Mamaearth 100% Natural Lip Balm for Women & Men 2g (Rose) ,
			 Natural Tint , 12-Hour Moisturization , Heals Dry & Chapped Lips
			"""
		)

		st.markdown("[Buy here>](https://amzn.eu/d/dwsnfNr)")

	with st.container():
		image_column,text_column=st.columns((1,2))

		with image_column:
			st.image(img_kau_lip)

		with text_column:
			st.subheader("Kaumudi Lip Balm")
			st.write(
				"""
				Kaumudi Handmade & 100% Natural Lip Balm  
				made with Rose & Saffron Essential oil , Best for Dry, Damaged & Chapped Lips ,
				 Hydrates & Moisturizes (Cherry Lip)
				 """
				)
			st.markdown("[Buy here>](https://amzn.eu/d/4U4IE3W)")

	with st.container():
		image_column,text_column=st.columns((1,2))

		with image_column:
			st.image(img_cocoa_lip)

		with text_column:
		    st.subheader("Himalaya Rich Cocoa Butter Lip Balm")
		    st.write(
			    """
			    Himalaya Rich Cocoa Butter Lip Care Lip Balm ,Glossy,Natural Color ,
			    Moisturising, Soothing, Nourishing
			    """
		        )

		    st.markdown("[Buy here>](https://amzn.eu/d/gj70b0K)")

	with st.container():
		image_column,text_column=st.columns((1,2))

		with image_column:
			st.image(img_nivea_lip)

		with text_column:
		    st.subheader("NIVEA Original Care Lip Balm")
		    st.write(
			    """
			     NIVEA Original Care Lip Balm ,
			    24 H Melt in Moisture Formula ,   
			    Natural Oils ,Nourished Lips

			    """
		        )

		    st.markdown("[Buy here>](https://amzn.eu/d/b4oXojQ)")


#--GRAPH
with st.container():
    st.header('Graph')

    ##---LOAD DATAFRAME
    excel_file = 'Excel/lip_balm.xlsx'
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

	




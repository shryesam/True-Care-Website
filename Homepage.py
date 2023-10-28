import requests
import streamlit as st
from streamlit_lottie import st_lottie

#Find more emojis here:https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md#heart
st.set_page_config(page_title="True Care",page_icon=":fleur_de_lis:",layout="wide")

def load_lottieurl(url):
	r = requests.get(url)
	if r.status_code != 200:
		return None
	return r.json()


#----LOAD ASSETS-----
lottie_coding="https://lottie.host/497d8173-5108-455c-a0f4-44cf7e082faf/XAZQsFi9YA.json"



#-----HEADER SECTION-----
with st.container():
	st.subheader("Welcome to True Care  :heart:")
	st.title("Where Beauty Meets Care ")
	st.write(
		"""
		Your Journey to Radiant Skin Begins Here at True Care!\n
		 Discover the specialized care you need right here!
		 """
		 )


#-----SKINCARE TIPS-----
with st.container():
	st.write("---")
	left_column, right_column = st.columns(2)
	with left_column:
		st.header("Skincare tips")
		st.write("##")
		st.write(
			"""
			
			Transform your skincare routine with these beginner-friendly tips.\n
			:diamond_shape_with_a_dot_inside: Start with a Gentle Cleanser\n
			:diamond_shape_with_a_dot_inside: Moisturize Regularly\n
			:diamond_shape_with_a_dot_inside: Use Sunscreen Daily\n
			:diamond_shape_with_a_dot_inside: Stay Hydrated and Eat Well\n
			:diamond_shape_with_a_dot_inside: Get Adequate Sleep


			 """)

		st.write("[Youtube link >](https://youtu.be/0XDiG5lL0Dw?si=uJjQPb0SIdFH3axV)")

	with right_column:
		st_lottie(lottie_coding, height=300, key="skincare")


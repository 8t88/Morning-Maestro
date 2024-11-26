import requests
import streamlit as st

# import os
# import json
# import requests
# import SessionState

st.title("Dawn Chorus Generator")
st.header("Make a dawn chorus from an assortment of birds")

st.write("Choose the birds to use in your dawn chorus")

def generate_chorus(inputs):

	st.write("Creating your dawn chorus. This could take some time")

	response = requests.post(f"http://0.0.0.0:8001/api/v1/generate_chorus/", json=inputs, verify=False)
	json_response = response.json()
	wav_gen = json_response.get("wav_gen")
	#wav_gen = class_values[json_response.get("wav_gen")]
	
	return wav_gen

# choose_model = st.sidebar.selectbox(
#     "Pick model you'd like to use",
#     ("Model 1 (10 classes)", # original 10 classes
#      "Model 2 (11 classes)", # original 10 classes + donuts
#      "Model 3 (11 classes + non-food class)") # 11 classes (same as above) + not_food class
# )

# bird_selection = st.checkbox(
# 	"Select the birds to use in your dawn chorus"
# 	"bird a"
# 	"bird b"
# 	"bird c"
# 	)

# for bird in bird_list:
# 	st.checkbox(bird)




birda = st.checkbox("American Crow")
birdb = st.checkbox("American Dipper")
birdc = st.checkbox("American Goldfinch")

selected_birds = [birda, birdb, birdc]

#if birds_selected:
pred_button = st.button("Generate")
if pred_button:
    #session_state.pred_button = True 
    #maybe redirect?
    chorus_wav = generate_chorus(selected_birds)
    st.audio(chorus_wav)
    #st.audio(chorus_wav, sample_rate=sample_rate)


#get the list of birds selected, send that as input to the api request

#

import streamlit as st
import pickle
import pandas as pd

vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.header('SQL injection detection program:')

option = st.selectbox(
     'Choose method',
     ('','Input', 'Import'))
if option == 'Input':
	text = st.text_input('Input text!')
	if text != '':
		pred = model.predict(pd.DataFrame(vectorizer.transform(pd.DataFrame([text], columns=['Sentence'])['Sentence'].values.astype('U')).toarray()))[0]
		
		if pred == 0:
			pred_text = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Clear of SQL injection</p>'
			st.write(pred_text, unsafe_allow_html=True)
		elif pred==1:
			pred_text = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">SQL injection detected</p>'
			st.write(pred_text, unsafe_allow_html=True)
elif option == 'Import':
	uploaded_file = st.file_uploader("Add text file !")
	if uploaded_file:
		for text in uploaded_file:
			pred = model.predict(pd.DataFrame(vectorizer.transform(pd.DataFrame([text], columns=['Sentence'])['Sentence'].values.astype('U')).toarray()))[0]
			if pred == 0:
				pred_text = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Clear of SQL injection</p>'
				st.write(pred_text, unsafe_allow_html=True)
			elif pred==1:
				pred_text = '<p style="font-family:sans-serif; color:Red; font-size: 42px;">SQL injection detected</p>'
				st.write(pred_text, unsafe_allow_html=True)
else:
	pass


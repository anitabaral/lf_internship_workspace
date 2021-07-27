import streamlit as st
st.title('First Day Journal Of Leapfrog Internship')

st.header('34th batch machine learning interns')
st.subheader('Everyone is great!!')
st.image('./ml_internship_members.png' )

st.header('Our Mentors')
st.markdown('> Shishir Bhattarai')
st.markdown('> Sushil Ghimire')

st.header('Learnings')

st.subheader('Learning about get/post requests:')
st.text("Use POST for destructive actions such as creation (I'm aware of the irony), editing, and deletion, because you can't hit a POST action in the address bar of your browser. Use GET when it's safe to allow a person to call an action. ")
st.markdown('**Get**: It requests the data from a specified resource ')
st.markdown('> In case of Get request, only limited amount of data can be sent because data is sent in header. ')
st.markdown('> Get request is not secured because data is exposed in URL bar.')
st.markdown('> Get request can be bookmarked.')
st.markdown('> Get request is idempotent . It means second request will be ignored until response of first request is delivered')
st.markdown('> Get request is more efficient and used more than Post.')

st.markdown('**Post**: It submits the processed data to a specified resource')
st.markdown('> In case of post request, large amount of data can be sent because data is sent in body.')
st.markdown('> Post request is secured because data is not exposed in URL bar.')
st.markdown('> Post request cannot be bookmarked.')
st.markdown('> Post request is non-idempotent.')
st.markdown('> Post request is less efficient and used less than get.')

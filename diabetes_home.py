import streamlit as st

# Define a function 'app()' which accepts 'census_df' as an input.
def app(diabetes_df):

    # Set the title to the home page contents.
  st.title(' Early Diabetes Prediction Web App')  
    # Provide a brief description for the web app.
  st.markdown('''
  Diabetes is a chronic (long-lasting) health condition that affects how your body turns food into energy.

  There isnt a cure yet for diabetes, but losing weight, eating healthy food, and being active can really help in reducing the impact of diabetes.

  This Web app will help you to predict whether a person has diabetes or is prone to get diabetes in future by analysing the values of several features using the Decision Tree Classifier.
  ''')
    # Add the 'beta_expander' to view full dataset 
  st.header('View Dataset')
  with st.beta_expander('dataset'):
    st.table(list(diabetes_df.columns))
    # Add a checkbox in the first column. Display the column names of 'diabetes_df' on the click of checkbox.
  st.subheader('Column Description:')
  c1,c2,c3=st.beta_columns(3)
  with c1:
    if st.checkbox('Show all the columns'):
      st.table(diabetes_df)
  with c2:
    if st.checkbox('View column data-types'):
      st.table(diabetes_df.dtype)
  with c3:
    if st.checkox('View column data'):
      ch=st.selectbox('Select column',tuple(df.columns))
      st.write(diabetes_df[ch])
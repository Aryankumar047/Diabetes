import diabetes_home
import diabetes_predict
import diabetes_plots
pages_dict = {"Home": diabetes_home, 
           "Predict Diabetes": diabetes_predict, 
           "Visualise Decision Tree": diabetes_plots}

st.sidebar.title('Navigation')
user_ch=st.sidebar.radio('Go to',pages_dict.keys())
selected_pg=pages_dict[user_ch]
selected_pg.app(diabetes_df)

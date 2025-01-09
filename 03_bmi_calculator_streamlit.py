import streamlit as st

#Add title
st.title('Welcome to BMI Calculator')

#Take in Weight Input
weight = st.number_input('What is your Weight (in kgs)?')

#Take in Height input
status = st.radio('Select your height format:',
                  ('cm', 'meters', 'feet'))

#Compare Status Value
if(status == 'cm'):
    height = st.number_input('centimeters')
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text('Enter some value of Height')
elif(status == 'meters'):
    height = st.number_input('meters')
    try:
        bmi = weight / (height ** 2)
    except:
        st.text('Enter some value of height')
else:
    height = st.number_input('feet')
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text('Enter some value of Height')

#check if the button is pressed or not
if(st.button('Calculate BMI')):
    #print the BMI index
    st.text('Your BMI Index is {}.'.format(bmi))

    #give the interpretation of BMI Index
    if(bmi<10):
        st.error('Your are Extremely Underweight')
    elif(bmi >= 16 and bmi < 18.5):
        st.warning('You are Underweight')
    elif(bmi >= 18.5 and bmi < 25):
        st.success('Healthy')
    elif(bmi >= 25 and bmi < 30):
        st.warning('Overweight')
    elif(bmi >= 30):
        st.error('Extremely Overweight')
import streamlit as st


# Grade Constants
grade=("A","B","C","D","E")

#Function Valdate the Mark
def ValidateMark(mark):
    if mark >=90:
        st.success(f"Grade: {grade[0]}") 
    elif mark >=80:
        st.info(f"Grade: {grade[1]}")
    elif mark >=70 :
        st.warning(f"Grade: {grade[2]}")
    elif mark >=60 :
        st.warning(f"Grade: {grade[3]}")
    elif mark>=0 :
        st.error(f"Grade: {grade[4]}")

st.title("SSLC Total & Percentage Calculator")

marks=[]

def AddRowElements(subjectName):
    col1, col2, col3 = st.columns(3, vertical_alignment="center")  
    with col1:
        st.header(subjectName)  
    with col2:
        marks.append(st.number_input(f"Enter marks for {subjectName}", min_value=0, max_value=100, step=1,label_visibility="collapsed" ,key=f"mark_{subjectName}"))
    with col3:
        ValidateMark(marks[-1])

def Footer():
    col1, col2, col3 = st.columns(3, vertical_alignment="center") 
    with col1:
        st.header("Total & Percentage")  
    with col2:
        st.success(f"Total Marks: {sum(marks)}/500")
    with col3:
        st.success(f"Percentage: {sum(marks)/len(marks):.2f}%")

def Clear_Form():
    for key in st.session_state.keys():
         if key=="name_input":
             st.session_state[key] = ""
         else:
             st.session_state[key] = 0  

name=st.text_input("Enter your name",key="name_input")
AddRowElements("Tamil")
AddRowElements("English")
AddRowElements("Maths")
AddRowElements("Science")
AddRowElements("Social Science")
Footer()    

st.button("Clear Form", on_click=Clear_Form)    

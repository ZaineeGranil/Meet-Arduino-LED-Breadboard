import streamlit as st

st.title("Meet Arduino, LED & Breadboard")
st.write("Name: zaineejayne08")
st.write("Wokwi Project: https://wokwi.com/projects/480927894703285249")

st.subheader("Arduino Code")
st.code("""
void setup() {
  pinMode(8, OUTPUT);
}
void loop() {
  digitalWrite(8, HIGH);
}
""", language="cpp")

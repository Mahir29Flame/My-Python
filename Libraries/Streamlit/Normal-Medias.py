import streamlit as st
import requests
from pathlib import Path

st.set_page_config(page_title="Texts & Images", page_icon=":tada:", layout="wide")
st.title("This is a freakin basic title")

st.header("This is a Stupid basic header")

st.subheader("This is a Std. basic subheader")

st.text("This is a basic text")

st.markdown('''
##### This is a Normal 📩***Markdown:*** 
{

codes in markdown:

```python
print("Hello World")
```

```javascript
console.log("Hello World")
```
}
''', unsafe_allow_html=True)

st.write("Code in ST:")
st.code('print("Hello World")', language='python')

json = requests.get('https://official-joke-api.appspot.com/jokes/random')
st.write("JSON:")
st.json(json.json())

st.image("https://www.w3schools.com/howto/img_fjords.jpg", caption="Fjords")
st.image(Path("Libraries\Streamlit\static\illusion.png"), caption="Illusion")
st.image("https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3aWN0dXk4eTdjemozazJlN29qdmlwZm01OGtsYnc4eWh6dGk1MHg5byZlcD12MV9naWZzX3RyZW5kaW5nJmN0PWc/3ov9k1173PdfJWRsoE/giphy.gif", caption="Gif")
st.video("https://youtu.be/pJxeyK7it0o?si=g5Uh82T-rFv7pXjR")
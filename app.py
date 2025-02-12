import streamlit as st
from pathlib import Path
import base64

# Initial page config
st.set_page_config(
     page_title='AI APIs cheat sheet',
     layout="centered",
     initial_sidebar_state="collapsed",
)

def main():
    cs_sidebar()
    cs_body()
    return None

# Thanks to streamlitopedia for the following code snippet
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# sidebar
def cs_sidebar():

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('Streamlit cheat sheet')

    st.sidebar.markdown('''
<small>Summary of the [docs](https://docs.streamlit.io/), as of [Streamlit v1.25.0](https://www.streamlit.io/).</small>
    ''', unsafe_allow_html=True)

    st.sidebar.markdown('__Install and import__')

    st.sidebar.code('$ pip install streamlit')

    st.sidebar.code('''
# Import convention
>>> import streamlit as st
''')

    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
# Just add it after st.sidebar:
>>> a = st.sidebar.radio(\'Choose:\',[1,2])
    ''')

    st.sidebar.markdown('__Magic commands__')
    st.sidebar.code('''
'_This_ is some __Markdown__'
a=3
'dataframe:', data
''')

    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
    ''')

    st.sidebar.markdown('__Pre-release features__')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')
    st.sidebar.markdown('<small>Learn more about [experimental features](https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features)</small>', unsafe_allow_html=True)

    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>[Cheat sheet v1.25.0](https://github.com/daniellewisDL/streamlit-cheat-sheet)  | Aug 2023 | [Daniel Lewis](https://daniellewisdl.github.io/)</small>''', unsafe_allow_html=True)

    return None

##########################
# Main body of cheat sheet
##########################

def cs_body():

    #st.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.header('Streamlit cheat sheet')

#     st.markdown('''
# <small>Summary of the [docs](https://docs.streamlit.io/), as of [Streamlit v1.25.0](https://www.streamlit.io/).</small>
#     ''', unsafe_allow_html=True)

    st.markdown('__Mistral AI__')

    st.code('$ pip install mistralai ')

    st.code(body = '''
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print(chat_response.choices[0].message.content)
''',
    language = "python",
    line_numbers = True,
    wrap_lines = True
    )



    st.markdown('__Anthropic__')

    st.code('$ pip install anthropic ')

    st.code(body = '''
import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="my_api_key",
)

message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=8192,
    temperature=0,
    system="Your system prompt here",
    messages=[]
)
print(message.content)
''',
    language = "python",
    line_numbers = True,
    wrap_lines = True
    )

    return None

# Run main()

if __name__ == '__main__':
    main()

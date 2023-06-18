import streamlit as st

with st.sidebar:
    st.title('Lexical Analyzer & Parser')
    st.subheader('by Kelompok 4 (IF-45-10) \n'
                 '1. Gerald Shabran Rasyad (1301213435)\n'
                 '2. Gloria Natasya Irene Sidebang (1301213445) \n'
                 '3. Dewa Putu Fajar Wijayakusuma (1301213161)')

def parser(sentences):
    sentences = sentences.split()
    iter1 = ["x"]
    Numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    check = ["for", iter1, "in", "range", "(", Numbers, ")", ":" ,"print", "(", iter1, ")"]

    state = 1
    out = True

    for sentence in sentences:
        if type(check[state-1]) is list: 
            if sentence not in check[state - 1]:
                out = False
                break
        else:
            if sentence != check[state - 1]:
                out = False
                break
    state += 1

    if out and state == len(check) + 1:
        st.info("Input diterima!")
    elif out and state != len(check) + 1:
        st.error(f"Error: Akhir input yang tidak diharapkan, terjebak di state {state}")
    else:
        st.error("Parsing Error!")

def token_analyzer(ForPythonSyntax):
    # Regular expressions for token matching
    REGEX_FOR = ["for"]
    REGEX_VAR = ["x"]
    REGEX_IN = ["in"]
    REGEX_ANGKA = ["0", "1", "2", "3", "4", "5", "6", "7","8" ,"9","10"]
    REGEX_RANGE = ["range"]
    REGEX_PRINT = ["print"]


    # Token definition
    TOKENS = [
        ("FOR", REGEX_FOR),
        ("VAR", REGEX_VAR),
        ("IN", REGEX_IN),
        ("ANGKA", REGEX_ANGKA),
        ("RANGE", REGEX_RANGE),
        ("PRINT", REGEX_PRINT),
        ("(", ["("]),
        (")", [")"]),
        (":", [":"])
    ]

    ForPythonSyntax = ForPythonSyntax.replace(" ", "")

    tokens = []

    while ForPythonSyntax:
        found_token = False
        for token_type, regex_list in TOKENS:
            for regex in regex_list:
                if ForPythonSyntax.startswith(regex):
                    tokens.append((ForPythonSyntax[: len(regex)], token_type))
                    ForPythonSyntax = ForPythonSyntax[len(regex) :]
                    found_token = True
                    break
            if found_token:
                break
        if not found_token:
            st.error(f"Error: Invalid token '{ForPythonSyntax[0]}'")
            break

    colt1, colt2 = st.columns([8, 4])
    for token, token_type in tokens:
        with colt1:
            st.info(f"Token: {token}")
        with colt2:
            st.info(f"Type: {token_type}")
        

st.title('Lexical Analyzer & Parser ')

with st.form(key='Input For Loop Python Code'):
    kode = st.text_input('Masukkan Code')
    st.form_submit_button('Check')

senteces = kode 
st.subheader('Lexical Analyzer Checker')
parser(senteces)

st.subheader("Token Analysis Result")
token_analyzer(senteces)

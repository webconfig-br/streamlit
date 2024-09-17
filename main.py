from json import loads
import streamlit as st
import pandas as pd

st.markdown("""
            # Exibidor de arquivos
            ## Faça o upload dos arquivos :smile: :heart:
            """)

st.text_input('Email')
st.text_input('Password', max_chars=10, type='password')

arquivo = st.file_uploader('Faça o upload de um arquivo', type=['csv','jpg','json','py','wav'])

if arquivo:
    match arquivo.type.split('/'):
        case 'image','jpeg'|'png':
            st.image(arquivo)
        case 'text', 'csv':
            df = pd.read_csv(arquivo)
            st.dataframe(df)
            st.line_chart(df)
        case 'application', _:
            st.json(loads(arquivo.read()))
        case 'text', 'x-python':
            st.code(arquivo.read().decode())
        case 'audio', _:
            st.audio(arquivo)
else:
    st.error('Nenhum arquivo carregado')
            
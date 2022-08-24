import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_icon="🔗", page_title="Garvey编程文档", layout="wide")
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
with st.sidebar:
    choose_menu = option_menu("Garvey编程文档", ["python基础","mysql","django","pyqt","golang基础","git"])
    st.markdown('''
    #### 作者： Garvey Wu
    #### 哔哩哔哩： GarveyWuCoding
    #### 豆瓣镜像:
    ```
    -i https://pypi.douban.com/simple/
    ```
    #### Pycharm快捷键:
    ```
    1. Ctrl + D：复制当前行
    2. Ctrl + E：删除当前行
    3. Shift + Enter：快速换行
    4. Ctrl +/：快速注释（选中多行可批量注释）
    5. Tab：缩进当前行（选中多行可批量缩进）
    6. Shift + Tab：取消缩进（选中多行后可批量取消缩进）
    7. Ctrl + F：查找
    8. Ctrl + H：替换
    ```
    ''')
if choose_menu=="django":
    config, orm = st.tabs(["配置","ORM"])
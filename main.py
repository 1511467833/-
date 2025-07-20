import streamlit as st
from utils import generate_script

st.title("视频脚本生成器")

#网页上加一个侧边栏，让用户提供自己的API密钥
with st.sidebar:
    api_key = st.text_input("请输入OpenAI API密钥：",type="password")#text_input会返回用户当前的输入，用一个值进行保存
    #有些用户不知道哪里获取API密钥，我们也可以去添加一个能够直达官网的密钥创建页面的链接
    st.markdown("[获取OpenAI API密钥](https://api-docs.deepseek.com/)")

subject = st.text_input("请输入视频的主题")
video_length = st.number_input("请输入视频的大致时长（单位：分钟）", min_value=0.1,step=0.1)
creativity = st.slider("请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）",min_value=0.0,max_value=1.0,value=0.2,step=0.1)
submit = st.button("生成脚本")#button函数返回的会是一个布尔值，在用户没有点击时会返回false，点击后返回true，因此可以使用条件判断来得知用户是否点击了按钮

#如果用户没有提交密钥
if submit and not api_key:
    st.info("请输入你的API密钥")
    st.stop()#这个函数的作用是：执行到这里之后，之后的代码都不会被执行了

#如果用户提供了密钥，但是没有提供视频主题
if submit and not subject:
    st.info("请输入视频的主题")
    st.stop()

#如果用户输入的视频长度小于0.1
if submit and not video_length >= 0.1:
    st.info("视频长度需要大于或等于0.1")
    st.stop()

#正常执行
if submit:
    with st.spinner(("AI正在思考中，请稍等...")):#只要下面那行代码没有运行完，网页上就会一直有一个加载中的效果
        search_result,title,script = generate_script(subject,video_length,creativity,api_key)
    st.success("视频脚本已生成！")
    st.subheader("标题：")#添加一个副标题
    st.write(title)
    st.subheader("视频脚本：")  # 添加一个副标题
    st.write(script)
    #用折叠组件来显示维基百科的搜索结果
    with st.expander("维基百科搜索结果"):
        st.info(search_result)

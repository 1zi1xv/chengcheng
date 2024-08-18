'''我的主页'''
import streamlit as st
from PIL import Image
import time



page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','网站跳转'])

def page_1():
    '''我的兴趣推荐'''
    with open("巡光.mp3",'rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('20240617.jpg')
    st.write('梓旭的电影推荐')
    st.write('这个杀手不太冷静')
    st.write('梓旭的游戏推荐')
    st.write('和平地铁、巅峰极速')
    st.write('梓旭的书籍推荐')
    st.write('《长征的故事》')
    st.write('梓旭的习题推荐')
    st.write('点中点')

    
def page_2():
    with open("起风了.mp3",'rb')as f:
            
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('20240616.jpg')
    '''我的图片处理工具'''
    st.write(':sunglasses:图片换色小程序:sunglasses')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4=st.tabs(['原图','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,2,0,1))






            
        st.image(img)
        st.image(img_change(img,0,2,1))
def img_change(img,rc,gc,bc):
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img



    

def page_3():
    with open("最后一页.mp3",'rb')as f:
            
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('20240618.jpg')
    '''我的智能词典'''
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        time_list=f.read().split('\n')
    for i in range(len(time_list)):
        time_list[i]=time_list[i].split('#')
    time_dict={}
    for i in time_list:
        time_dict[int(i[0])]=int(i[1])
    
    word=st.text_input('输入要查找的单词')

    if word in words_dict:
        roading = st.progress(0, '开始查询')
        for i in range(1, 101, 1):
            time.sleep(0.02)
            roading.progress(i, '正在查询'+str(i)+'%')
        roading.progress(100, '查询完毕！')
        st.write(words_dict[word])            
        n=words_dict[word][0]
        if n in time_dict:
            time_dict[n]+=1
        else:
            time_dict[n]=1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message=''
            for k,v in time_dict.items():
                message+=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            

            f.write(message)
        st.write('查询次数:',time_dict[n])
                       
        if word in words_dict:

            if word=='666':
                st.snow()





def page_4():
    with open("离别开出花.mp3",'rb')as f:
            
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('20240620.jpg')    
    '''我的留言区'''
    st.write('我的留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        with st.chat_message('⛄'):
            st.write(i[1],':',i[2])
    name=st.selectbox('我是……',['阿短','编程猫','老师'])
    new_message=st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message=''
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)
def page_5():
    '''图片跳转'''
    # 跳转按钮link_button()
    with open("一笑江湖.mp3",'rb')as f:
            
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('20240621.jpg')




    
    
    # 如何创建跳转按钮
    # 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？
    
    # 应用：兴趣推广_分享链接指引
    st.write('----')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['贴吧', 'bilibili','百度','知乎','淘宝','豆瓣','环球网','幕布'])
    if go == '贴吧':
        st.link_button('点击跳转', 'https://www.baidu.com/')
    elif go == 'bilibili':
        st.link_button('点击跳转', 'https://www.bilibili.com/')
    elif go == '百度':
        st.link_button('点击跳转', 'https://www.baidu.com/')
    elif go == '知乎':
        st.link_button('点击跳转', 'https://www.zhihu.com/')
    elif go == '淘宝':
        st.link_button('点击跳转', 'https://www.taobao.com/')
    elif go == '豆瓣':
        st.link_button('点击跳转', 'https://www.douban.com/')
    elif go == '环球网':
        st.link_button('点击跳转', 'https://www.huanqiu.com/')
    elif go == '幕布':
        st.link_button('点击跳转', 'https://www.mubu.com/')





if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '网站跳转':
    page_5()

                              
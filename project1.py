import tkinter as tk
import tkinter.messagebox
import pickle
import os
from tkinter import ttk
from tkinter import scrolledtext#滚动文本框
from tkinter import END
import tkinter.scrolledtext as ScrolledText
from PIL import Image, ImageTk
###########################################################定义备忘录类######################################################
def resize( w_box, h_box, pil_image): #参数是：要适应的窗口宽、高、Image.open后的图片
  w, h = pil_image.size #获取图像的原始大小   
  f1 = 1.0*w_box/w 
  f2 = 1.0*h_box/h    
  factor = min([f1, f2])   
  width = int(w*factor)    
  height = int(h*factor)    
  return pil_image.resize((width, height), Image.ANTIALIAS)   
class Memo:
    def __init__(self,thing,date):
        ################初始化
        #self._id = len(R.memo_list)-1
        ################
        #self._id=0
        self.thing = thing
        self.date = date
    def talk(self):
        def addition():
            self.thing=var_addition.get()
            self.date=var_additiontime.get()
            one = {'thing':self.thing,'date':self.date}
            R.add(one)
        #self._id += 1
        window_add=tk.Toplevel(window)
        window_add.geometry('300x200')
        window_add.title('新增事件')
        var_addition=tk.StringVar()
        var_addition.set('请输入新增事件')
        entry_addition = tk.Entry(window_add, textvariable=var_addition, font=('宋体', 14))   # 显示成明文形式
        entry_addition.place(x=45,y=40)
        var_additiontime=tk.StringVar()
        var_additiontime.set('请输入新增事件的时间')
        entry_additiontime = tk.Entry(window_add, textvariable=var_additiontime, font=('宋体', 14))   # 显示成明文形式
        entry_additiontime.place(x=45,y=100)
        btn_addition = tk.Button(window_add, text='确认添加', bg='purple',fg='white',command=addition)
        btn_addition.place(x=120,y=150)
        #获取内容
        #新增项
        
        
    #@property
    """def id(self): #如果有文件的话
        num=len(R.memo_list)-1
        return self._id"""

#############################################定义备忘录管理操作############################################################
memo_list = []
class MemoAdmin:
    """管理记录"""
    def __init__(self,memo_list):   # 初始化数据
        self.memo_list = memo_list
        
    def add(self,one):    # 增加方法
        self.memo_list.append(one)
        R.query()
        tkinter.messagebox.showinfo(title='成功', message='添加成功！ ')
        """for i in self.memo_list:
            print(i)
            print("\n")"""
    def search(self):#查询方法
        def searchthing():
            thing_s=var_searchthing.get()
            flag=0
            for dic in self.memo_list:
                if dic['thing']==thing_s:
                    flag=1
                    window_searchthing=tk.Toplevel(window_search)
                    window_searchthing.geometry('300x200')
                    window_searchthing.title('查询结果')
                    s_t = ScrolledText.ScrolledText(window_searchthing)
                    s_t.pack()
                    s_t.insert(END,"\t")
                    s_t.insert(END,dic['thing'])
                    s_t.insert(END,"\t")
                    s_t.insert(END,dic['date'])
                    s_t.insert(END,"\n")
            if flag==1:
                tkinter.messagebox.showinfo( title='成功', message='查询成功！ ')
            else:
                tkinter.messagebox.showerror(title='失败', message='无该记录！ ')

        def searchtime():
            thing_t=var_searchtime.get()
            flag=0
            for dic in self.memo_list:
                if dic['date']==thing_t:
                    flag=1
                    window_searchtime=tk.Toplevel(window_search)
                    window_searchtime.geometry('300x200')
                    window_searchtime.title('查询结果')
                    s_time = ScrolledText.ScrolledText(window_searchtime)
                    s_time.pack()
                    s_time.insert(END,"\t")
                    s_time.insert(END,dic['thing'])
                    s_time.insert(END,"\t")
                    s_time.insert(END,dic['date'])
                    s_time.insert(END,"\n")
            if flag==1:
                tkinter.messagebox.showinfo( title='成功', message='查询成功！ ')
                window_search.destroy()
            else:
                tkinter.messagebox.showerror(title='失败', message='无该记录！ ')
                window_search.destroy()
                    
        window_search=tk.Toplevel(window)
        window_search.geometry('250x156')
        window_search.title('查询信息')
        window_search.resizable(False,False)

        label_search_one = tk.Label(window_search, text='请输入你想要查询的名称或时间',  font=('宋体', 12))
        label_search_one.place(x=10,y=30)
        var_searchthing=tk.StringVar()
        var_searchthing.set('事件')
        entry_searchthing = tk.Entry(window_search, textvariable=var_searchthing, font=('宋体', 14))   # 显示成明文形式
        btn_searchthing = tk.Button(window_search, text='查询事件', bg='purple',fg='white',command=searchthing)
        entry_searchthing.place(x=10,y=60)
        btn_searchthing.place(x=30,y=115)

        
        var_searchtime=tk.StringVar()
        var_searchtime.set('时间')
        entry_searchtime = tk.Entry(window_search, textvariable=var_searchtime, font=('宋体', 14))   # 显示成明文形式
        btn_searchtime = tk.Button(window_search, text='查询时间', bg='purple',fg='white',command=searchtime)
        entry_searchtime.place(x=10,y=90)
        btn_searchtime.place(x=150,y=115)
    def dele(self):    # 删除方法
        def assure_dele():
            try:
                deleid=int(var_deleid.get())
                num_memo=len(self.memo_list)
                if deleid>(num_memo-1):
                    tkinter.messagebox.showerror('Error','The input too large!')
                else:
                    self.memo_list.pop(deleid)
                    window_dele.destroy()
                    tkinter.messagebox.showinfo(title='成功', message='删除成功！ ')
            except ValueError:
                tkinter.messagebox.showerror('Error','The input is not an intager!')
                
                
            
        window_dele=tk.Toplevel(window)
        window_dele.geometry('250x156')
        window_dele.title('删除信息')
        window_dele.resizable(False,False)
        #设置图片
       
        w_box2=250
        h_box2=156
        pil_image2=Image.open('p2.jpg')
        w2,h2=pil_image2.size
        pil_image2_resized2=resize(w_box2,h_box2,pil_image2)
        tk_image2=ImageTk.PhotoImage(pil_image2_resized2)
        label_photo2=tk.Label(window_dele,image=tk_image2, width=w_box2, height=h_box2)
        label_photo2.place(x=0,y=0)
        
        label_dele_one = tk.Label(window_dele, text='请输入你想要删除的事件序号',  font=('宋体', 12))
        label_dele_one.place(x=10,y=30)
        var_deleid=tk.StringVar()
        var_deleid.set('示例：1')
        entry_deleid = tk.Entry(window_dele, textvariable=var_deleid, font=('宋体', 14))   # 显示成明文形式
        btn_assure_dele = tk.Button(window_dele, text='确认删除', bg='purple',fg='white',command=assure_dele)
        entry_deleid.place(x=10,y=70)
        btn_assure_dele.place(x=90,y=115)
        #temp = input('请选择你将要删除的记录（示例 1或者2或者3 ）:')
        #self.memo_list.pop(int(temp)-1)
        
        R.query()
    def modify(self):   # 修改方法
        """temp1 = input('请输入你要修改的记录（示例 1或者2或者3）:')
        temp2 = input(f'你要修改的记录是{self.memo_list[int(temp1)-1]}，请输入要修改的值（示例：name:zhangsan）:')
        temp3 = temp2.split(':')
        self.memo_list[int(temp1)-1][temp3[0]] = temp3[1]   # 列表中找出嵌套的字典key和value"""
        def assure_modify_one():
            def assure_modify_two():
                newthing=var_modifything.get()
                newtime=var_modifytime.get()
                self.memo_list[modifyid]['thing']=newthing
                self.memo_list[modifyid]['date']=newtime
                window_assure_modify.destroy()
                tkinter.messagebox.showinfo(title='成功', message='修改成功！ ')

            try:
                modifyid=int(var_modifyid.get())
                num_memo=len(self.memo_list)
                if modifyid>(num_memo-1):
                    tkinter.messagebox.showerror('Error','The input too large!')
                else:
                    window_assure_modify=tk.Toplevel(window_modify)
                    window_assure_modify.geometry('250x300')
                    window_assure_modify.title('修改信息')
                    label_modi_thing=tk.Label(window_assure_modify, text='请输入你想要修改的事件',  font=('宋体', 12))
                    label_modi_time=tk.Label(window_assure_modify, text='请输入你想要修改的时间',  font=('宋体', 12))
                    var_modifything=tk.StringVar()
                    var_modifything.set('示例：完成语文作业')
                    entry_modifything = tk.Entry(window_assure_modify, textvariable=var_modifything, font=('宋体', 14))   # 显示成明文形式
                    var_modifytime=tk.StringVar()
                    var_modifytime.set('示例：10:24')
                    entry_modifytime = tk.Entry(window_assure_modify, textvariable=var_modifytime, font=('宋体', 14))   # 显示成明文形式
                    btn_assure_modify_two=tk.Button(window_assure_modify, text='确认修改', bg='purple',fg='white',command=assure_modify_two)
                    #放置按钮标签
                    label_modi_thing.place(x=40,y=50)
                    entry_modifything.place(x=30,y=100)
                    label_modi_time.place(x=40,y=150)
                    entry_modifytime.place(x=30,y=200)
                    btn_assure_modify_two.place(x=100,y=250)
            except ValueError:
                tkinter.messagebox.showerror('Error','The input is not an intager!')
            
          
        window_modify=tk.Toplevel(window)
        window_modify.geometry('300x200')
        window_modify.title('修改信息')
        label_modifify_one = tk.Label(window_modify, text='请输入你想要修改的事件序号',font=('宋体', 12))
        label_modifify_one.place(x=40,y=40)
        var_modifyid=tk.StringVar()
        var_modifyid.set('示例：1')
        entry_modifyid = tk.Entry(window_modify, textvariable=var_modifyid, font=('宋体', 14))   # 显示成明文形式
        btn_assure_modify_one = tk.Button(window_modify, text='确认修改', bg='purple',fg='white',command=assure_modify_one)
        entry_modifyid.place(x=45,y=80)
        btn_assure_modify_one.place(x=120,y=150)



        
        R.query()
    """def save(self,username):   # 数据保存在文件内
        with open('%s.pickle'%username,'wb') as f:
            f.write(pickle.dumps(memo_list))
            print('保存成功')"""
    """def load(self):   # 下载文件
        with open('db.pkl','rb') as f:
            data = pickle.loads(f.read())
            print(data)
            print('下载成功')"""
    def query(self):   # 查询所有数据
        def assure_query():
            window_query.destroy()
        window_query=tk.Toplevel(window)
        window_query.geometry('300x200')
        window_query.title('查询结果')
        st = ScrolledText.ScrolledText(window_query)
        st.pack()
        j=0
        for dic in self.memo_list:
            st.insert(END,j)
            st.insert(END,"\t")
            st.insert(END,dic['thing'])
            st.insert(END,"\t")
            st.insert(END,dic['date'])
            st.insert(END,"\n")
            j=j+1
           
        btn_assure_query = tk.Button(window_query, text='确认', command=assure_query)
        btn_assure_query.pack()
        """S=Scrollbar(window_query)
        T=Text(window_query, height=4, width=50)
        S.pack(side=RIGHT, fill=Y)
        T.pack(side=LEFT, fill=Y)
        S.config(command=T.yview)
        T.config(yscrollcommand=S.set)
        quote=self.memo_list
        T.insert(END, quote)
        window_query.mainloop(  )"""
        


#建立对象(全局变量)
L = Memo('事件','日期')
R = MemoAdmin(memo_list)
####################################################操作窗口#######################################################
        
def get_image(filename,width,height):
    #打开指定图片并缩放至指定尺寸
    im=Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

 

def action():
    #获取名字
    username=var_username.get() 
    #加载文件内容
    #设置异常捕获
    try:
        with open('%s.pickle'%username,'rb') as memofile:
            #将之前文件储存的信息加载
            R.memo_list=pickle.load(memofile)
            memofile.close()
    except FileNotFoundError:
        #没有读取到memofile，程序创建memofile文件
        with open('%s.pickle'%username,'wb') as memofile:
            information=[{'thing':'事项','date':'日期'}]
            pickle.dump(information,memofile)
            R.memo_list=[{'thing':'事项','date':'日期'}]
            memofile.close()
   
    def save():
        with open('%s.pickle'%username,'wb') as f:
            pickle.dump(R.memo_list,f)
            tkinter.messagebox.showinfo(title='成功', message='保存成功！ ')
            f.close()
    #建立操作窗口
    window_act=tk.Toplevel(window)
    window_act.geometry('250x296')
    window.resizable(False,False)
    window_act.title('备忘录操作')
    
    #设置图片
    w_box1=250
    h_box1=296
    pil_image1=Image.open('p4.jpg')
    w1,h1=pil_image1.size
    pil_image1_resized1=resize(w_box1,h_box1,pil_image1)
    tk_image1=ImageTk.PhotoImage(pil_image1_resized1)
    label_photo1=tk.Label(window_act,image=tk_image1, width=w_box1, height=h_box1)
    label_photo1.pack()
    button_search=tk.Button(window_act, text='查询事项',font=('宋体', 10), command=R.search)
    button_search.place(x=150,y=60)
    button_query=tk.Button(window_act, text='显示事项',font=('宋体', 10), command=R.query)
    button_query.place(x=150,y=100)
    button_add=tk.Button(window_act, text='新增事项', font=('宋体', 10),command=L.talk)
    button_add.place(x=150,y=140)
    button_modi=tk.Button(window_act, text='修改事项',font=('宋体', 10), command=R.modify)
    button_modi.place(x=150,y=180)
    button_dele=tk.Button(window_act, text='删除事项', font=('宋体', 10),command=R.dele)
    button_dele.place(x=150,y=220)
    button_save=tk.Button(window_act, text='保存事项',font=('宋体', 10), command=save)
    button_save.place(x=150,y=260)
    window_act.mainloop()
    












######################################注册登录函数############################################
def login():
    #获取用户输入的username和password
    username=var_username.get()
    userpassword=var_userpassword.get()
    #设置异常捕获
    try:
        with open('user_information.pickle','rb') as userfile:
            user_information=pickle.load(userfile)
    except FileNotFoundError:
        #没有读取到usefile，程序创建usefile文件
        with open('user_information.pickle','wb') as userfile:
            user_information={'admin':'admin'}
            pickle.dump(user_information,userfile)
            userfile.close()
    if username in user_information:
        if userpassword==user_information[username]:
            tkinter.messagebox.showinfo(title='Welcome', message='Login sucessfully. ')
            action()
            #############登陆成功###################
        else:
            tkinter.messagebox.showerror(message='Error, your password is wrong, please try again.')
    else:#用户名不存在
        is_register = tkinter.messagebox.askyesno('Welcome！ ', 'You have not register yet. Register now?')
        # 提示需不需要注册新用户
        if is_register:
            register()
        

def register():
    def register_to_system():
        #获取文本框中的内容
        nn=newname.get()
        np=newpassword.get()
        npc=newpassword_confirm.get()
        #设置异常捕获
        try:
            with open('user_information.pickle','rb') as userfile:
                user_information=pickle.load(userfile)
        except FileNotFoundError:
            #没有读取到usefile，程序创建usefile文件
            with open('user_information.pickle','wb') as userfile:
                user_information={'admin':'admin'}
                pickle.dump(user_information,userfile)
                userfile.close()
        #打开文件，读出信息
        with open('user_information.pickle','rb') as userfile:
            #加载已有信息,是为了之后添加方便。
            existed_user_information=pickle.load(userfile)
        #判断密码是否一致
        if np!=npc:
            tkinter.messagebox.showerror('Error','Your password is different from your confirm.')
        elif nn in existed_user_information:
            tkinter.messagebox.showerror('Error','This username has already been registered!')
        else:
            existed_user_information[nn]=np
            with open('user_information.pickle','wb') as userfile:
                pickle.dump(existed_user_information, userfile)
            tkinter.messagebox.showinfo('Welcome', 'you have successfully signed up!')
            # 然后销毁窗口。
            window_register.destroy()
            #函数结束
    window_register=tk.Toplevel(window)
    window_register.geometry('300x200')
    window_register.title('Please register now')

    #赋值操作
    newname=tk.StringVar()# 将输入的注册名赋值给变量
    newname.set('1067988338@qq.com')#将最初显示定为...
    tk.Label(window_register, text='User name: ').place(x=10, y=10)  # 将`User name:`放置在坐标（10,10）。
    entry_newname = tk.Entry(window_register, textvariable=newname)  # 创建一个注册名的`entry`，变量为`new_name`
    entry_newname.place(x=130, y=10)  # `entry`放置在坐标（150,10）.

    newpassword = tk.StringVar()
    tk.Label(window_register, text='Password: ').place(x=10, y=50)
    entry_userpassword = tk.Entry(window_register, textvariable=newpassword, show='*')
    entry_userpassword.place(x=130, y=50)
 
    newpassword_confirm = tk.StringVar()
    tk.Label(window_register,text='Confirm password: ').place(x=10, y=90)
    entry_newpassword_confirm = tk.Entry(window_register, textvariable=newpassword_confirm, show='*')
    entry_newpassword_confirm.place(x=130, y=90)

    #执行register_to_system
    button_confirm_register=tk.Button(window_register, text='Register', command=register_to_system)
    button_confirm_register.place(x=180, y=120)









###############################################程序主窗口##########################################################
#实例化object，建立窗口window
window=tk.Tk()
#给可视化窗口起名字
window.title('备忘录')
#设定窗口大小
window.geometry('300x400+150+100')
window.resizable(False,False)
#设置图片
w_box=300
h_box=400
pil_image=Image.open('p1.jpg')
w,h=pil_image.size
pil_image_resized=resize(w_box,h_box,pil_image)
tk_image=ImageTk.PhotoImage(pil_image_resized)
label_photo=tk.Label(window,image=tk_image, width=w_box, height=h_box)
label_photo.pack()

"""#放置用户名和密码的标签
l1 = tk.Label(window, text='用户名', bg='gray', font=('宋体', 12), width=30, height=2)
l2 = tk.Label(window, text='密码', bg='gray', font=('宋体', 12), width=30, height=2)"""
#放置两个文本框收集信息
var_username=tk.StringVar()
var_username.set('1067988338@qq.com')
var_userpassword=tk.StringVar()
entry_username = tk.Entry(window, textvariable=var_username, font=('宋体', 14))   # 显示成明文形式
entry_password = tk.Entry(window, show='*', textvariable=var_userpassword,font=('Arial', 14))  # 显示成密文形式
entry_username.place(x=50,y=170)
entry_password.place(x=50,y=250)
#放置按钮
btn_login = tk.Button(window, bg='purple',text='Login', fg='white',command=login)
btn_login.place(x=60, y=300)
btn_sign_up = tk.Button(window, bg='purple',text='Sign up',fg='white', command=register)
btn_sign_up.place(x=200, y=300)
#主窗口循环显示
window.mainloop()
###############################################结束###################################################################

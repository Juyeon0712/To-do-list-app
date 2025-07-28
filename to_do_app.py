import streamlit as st

st.set_page_config(
    page_title='To-Do list',
    page_icon='✅',
    layout = 'centered'
)


st.title('📝 나의 할일 목록'
, anchor='title-section',
help="anchor 존재")
# st.markdown("# 📆 나의 할일 목록")
# st.markdown("# [📆 나의 할일 목록]https://www.google.com)")

st.write(' 간단하고 효율적인 할일 관리를 시작해보세요!')

st.header('📖 사용법',divider=True)
# st.header('📖 사용법2',divider=True)
# st.header('📖 사용법3',divider=True)
# st.header('📖 사용법4',divider=True)
# st.header('📖 사용법5',divider=True)

# st.subheader('1. 할일 추가',anchor='subheader-section',help="subheader 존재1")
# st.subheader('2. 완료 표시')
# st.subheader('3. 할일 삭제')
# st.subheader('4. 일괄 관리',anchor='subheader-section',help="subheader 존재2") 북마크처럼 할 수 있음

# st.markdown('### 1. 할일 추가')

st.write("""
1. **할일 추가**: 텍스트 입력 후 '추가하기' 버튼 클릭 \n
2. **완료 표시**: 체크박스를 클릭하여 완료 표시 \n
3. **할일 삭제**: 🗑️ 버튼으로 개별 삭제\n
4. **일괄 관리**: 완료된 할일만 삭제하거나 전체 삭제
""") 


# st.markdown('안녕하세요. <font size=16>환영합니다.</font>'
#     ,unsafe_allow_html=True
#     ,help='캡션입니다.') #마크다운에서도 HTML 적용 가능 마크다운, write, html 직접 적용하거나로 꾸민다.
# # st.caption('안녕하세요. <font size=16>환영합니다.</font>'
# #     ,unsafe_allow_html=True
# #     ,help='캡션입니다.')
# st.caption('안녕하세요.', help='캡션입니다.')

# st.code('import streamlit as st', language='javascript=html') #코드블럭이 생김
# st.code('ifont size=16>환영합니다.</font>', language='javascript=html') #코드블럭이 생김

# st.code('import streamlit as st')
# st.code('''import streamlit as st
# a=st.button('안녕')
# if a:
#         st.text('버튼클릭')
# else:
#     st.text('버튼클릭안함')''',height=50, line_numbers=True, wrap_lines=True)

# st.code('ifont size=16>환영합니다.</font>', language='javascript=html') #코드블럭이 생김

# st.divider() #구분선 추가

# with st.echo():
#      num= 1+1
#      st.write(num)
# #코드 블럭도 보여주고, 실행 결과도 보여준다.

# def get_user_name():
#     return 'juyeon'

# with st.echo():
#     def get_p():
#         return '!!!'

#     g='안녕'
#     v=get_user_name()
#     p=get_p()

#     st.write(g,v,p)

# st.write('잘가')

# st.latex(r'ax^2 + bx + c = 0', help= '2차 방정식')
# st.text('안녕하세요.', help='텍스트입니다.')
# st.help()
# st.html('<ifont size=16>환영합니다.</font>')




def custom_warning(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #ff6b35;
        background-color: var(--warning-bg, #fff3cd);
        border-radius: 0.25rem;
        color: var(--warning-text, #856404);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --warning-bg: #3d2914;
                --warning-text: #ffcc02;
            }}
        }}
        [data-theme="dark"] {{
            --warning-bg: #3d2914;
            --warning-text: #ffcc02;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_success(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
        background-color: var(--success-bg, #d4edda);
        border-radius: 0.25rem;
        color: var(--success-text, #155724);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --success-bg: #1e3a24;
                --success-text: #4caf50;
            }}
        }}
        [data-theme="dark"] {{
            --success-bg: #1e3a24;
            --success-text: #4caf50;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_info(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #17a2b8;
        background-color: var(--info-bg, #d1ecf1);
        border-radius: 0.25rem;
        color: var(--info-text, #0c5460);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --info-bg: #0d2a3a;
                --info-text: #5bc0de;
            }}
        }}
        [data-theme="dark"] {{
            --info-bg: #0d2a3a;
            --info-text: #5bc0de;
        }}
    </style>
    """, unsafe_allow_html=True)

def custom_error(message):
    st.markdown(f"""
    <div style="
        padding: 0.75rem 1rem;
        margin: 1rem 0;
        border-left: 4px solid #dc3545;
        background-color: var(--error-bg, #f8d7da);
        border-radius: 0.25rem;
        color: var(--error-text, #721c24);
        font-size: 14px;
        line-height: 1.5;
    ">
         {message}
    </div>
    <style>
        @media (prefers-color-scheme: dark) {{
            :root {{
                --error-bg: #3a1a1d;
                --error-text: #f44336;
            }}
        }}
        [data-theme="dark"] {{
            --error-bg: #3a1a1d;
            --error-text: #f44336;
        }}
    </style>
    """, unsafe_allow_html=True)

# custom_error('에러입니다.')
# st.error('에러입니다.')
# message에 에러입니다가 들어감?

st.subheader('➕ 새로운 할일 추가')

new_todo = st.text_input('할일을 입력하세요 :', 
placeholder = '예: 장보기, 운동하기, 책 읽기')

submitted = st.button('추가하기')

# 세션 스테이트 초기화 session_state에 딕셔너리{} 형태로 뭔가가 있을 텐데 초기화 시키며 안 돼서 이 작업을 진행
if 'todos' not in st.session_state:
    st.session_state.todos = [] #리스트에 저장을 함.

if submitted:
    if new_todo.strip(): # 빈문자열이 아닌지 판단하는 함수 / 딕셔너리 형태로 뿌려줌?
     st.session_state.todos.append({
        'tast': new_todo.strip(),
        'completed': False
     })
     custom_success(f"✅'{new_todo}'가 추가되었습니다.")
    else:
        custom_warning('⚠️ 할일을 입력해주세요.') # 추가되지 않은 경우


st.divider()

st.subheader('📕 할일 목록')

# st.write(st.session_state.todos)

# st.write(len(st.session_state.todosst.session_state.todos)) 
#값이 있는지 확인하고, 목록들을 순회하면서 뿌려줬따?

if st.session_state.todos:
    for i in reversed(range(len(st.session_state.todos))):
        todo=st.session_state.todos[i]

        col1,col2,col3 = st.columns([0.1,0.7,0.2])

        with col1:
            completed=st.checkbox("",
            value=todo['completed'],
            key=f"check_{i}", # 키가 중복되지 않게 키 값을 다르게 만들어줌.
            help= '완료 체크')

            if completed!=todo['completed']:
                st.session_state.todos[i]['completed']=completed #completed가 True가 되도록 만들어줌.
                st.rerun() # 초기값만 저장이 돼. 업데이트 시키기 위해서 st.rerun을 활용함..? 값을 덮어써야 할 때는
                # st.write('...') 써도 출력 안돼?

        with col2:
            if completed:
                st.markdown(f"~~{todo['tast']}~~", help= '완료된 할일') #취소선이 생길 수 있도록, f스트링 용법 활용해서 만들어봄.
            else:
                st.write(todo['tast']) #완료되지 않은 경우

        with col3:
            if st.button("🗑️", key=f"delete_{i}", help="삭제"): # 키가 중복되지 않게 작성
                st.session_state.todos.pop(i) # 리스트에서 삭제할 때에는 pop이라는 함수를 사용 .i index 몇 번째 삭제할지 전달
                custom_success("삭제되었습니다!") # 삭제 되었음을 알려줌.
                st.rerun() #삭제하면 데이터가 바뀌었으니까 st.rerun()을 활용해서 초기화시켜줌?
                
        if i>=0:
            st.markdown('---')

else:
    custom_info("➕아직 할일이 없습니다. 새로운 할일을 추가해보세요!")

# 통계  및 관리 세션 표시
if st.session_state.todos:  #정보가 있는지 확인하고
    total_todos=len(st.session_state.todos) #총 5개가 있어(이미지상으로)
    completed_todos = 0

    for i in st.session_state.todos: # todo 앱을 계속 순회를 하면서 아래로 내려가는? 0.1.2.3.4를 순회하면서 뽑아오는 것.
        if i['completed']:
            completed_todos +=1 #0+1, 
    remaining_todos=total_todos-completed_todos #남은 갯수를 확인하기 위해서 remaining
    if completed_todos>0:
        completion_rate = (completed_todos/total_todos*100)
    else:
        completion_rate=0

    col1, col2= st.columns(2)

    with col1:
        if st.button("🗑️모든 할일 삭제", type="secondary"): #버튼을 생성해서 
            st.session_state.todos=[] #여기에 할일 목록이 0.1.2.3.4. 저장됨 => 빈 리스트로 전달하면 초기화 됨.
            custom_success("모든 할일이 삭제되었습니다.")
            st.rerun()
    with col2:
        if completed_todos>0: #체크된 박스가 0개 이상일 때
            if st.button(f"✅완료된 할일 {completed_todos}개 삭제", type="secondary"): #버트늘 누르면 반복하면서 남은 할일만 남겨둔다.
                todo_list=[]
                for i in st.session_state.todos: #덮어씌운다. 순회한다. {"todo" : "할일1", "complted: True,False"} i에서 complted를 뽑아오는 것
                    # print(i)
                    if not i['completed']: #not을 빼면 True인 것만 저장이되고, not을 붙이면 flase인것만
                        todo_list.append(i) #False일때를 뽑아와서 남은 할일만 다시 저장하겠다는 말
                st.session_state.todos=todo_list
                #         print(i)
                # todo_list=[]
                # for i in st.session_state.todos:
                #     if not todo['completed']:
                #         print(i)
                custom_success("완료된 할일 {completed_todos}개가 삭제되었습니다.") #오류가 나는데?
                st.rerun() # 다시 웹을 재실행 하는 함수

    st.subheader("📊통계")
    
    def display_state(title,value,delta=None,value_color=None): #타이틀에는 전체 할일 완료된 할일..
        delta_str=""
        if delta is not None:
            if delta>0:
                delta_str=f"(⬆️{delta})"
            elif delta<0:
                delta_str=f"(⬇️{delta})" #여기 왜 안 되는지
            else:
                delta_str="" #0일 경우 아무것도 출력하지 않게
        if value_color is None:
            value_color= "var(--text-color, #262730)"

        st.markdown(f"""
            <div style="
                padding: 1rem; 
                background-color: var(--stat-bg, #f0f2f6); 
                border: 1px solid var(--stat-border, transparent);
                border-radius: 10px; 
                text-align: center;
                box-shadow: var(--stat-shadow, 0 1px 3px rgba(0,0,0,0.1));
            ">
                <div style="
                    font-size: 18px; 
                    font-weight: bold; 
                    color: var(--title-color, #262730);
                    margin-bottom: 0.5rem;
                ">{title}</div>
                <div style="
                    font-size: 32px; 
                    font-weight: bold; 
                    color: {value_color};
                ">{value}{delta_str}</div>
            </div>
            <style>
                /* 라이트모드 기본값 */
                :root {{
                    --stat-bg: #f0f2f6;
                    --stat-border: transparent;
                    --stat-shadow: 0 1px 3px rgba(0,0,0,0.1);
                    --title-color: #262730;
                    --text-color: #262730;
                }}
                
                /* 다크모드 스타일 */
                @media (prefers-color-scheme: dark) {{
                    :root {{
                        --stat-bg: #2b2b35;
                        --stat-border: #404040;
                        --stat-shadow: 0 1px 3px rgba(0,0,0,0.3);
                        --title-color: #fafafa;
                        --text-color: #fafafa;
                    }}
                }}
                
                /* Streamlit 다크모드 */
                [data-theme="dark"] {{
                    --stat-bg: #2b2b35;
                    --stat-border: #404040;
                    --stat-shadow: 0 1px 3px rgba(0,0,0,0.3);
                    --title-color: #fafafa;
                    --text-color: #fafafa;
                }}
            </style>
        """, unsafe_allow_html=True)


    col1,col2,col3=st.columns(3)

    with col1:
        display_state("전체 할일", total_todos)
    with col2:
        display_state("완료된 할일", completed_todos, delta=completed_todos,value_color="#4CAF50") #value_color 글자색
    with col3:
        display_state("남은 할일", remaining_todos, delta=-remaining_todos,value_color="#f44336") #-remaining

# -----------------------
# 할일 추가했는지 먼저 확인(목록이 있어야 한다. 목록이 없으면 계산할 수 없음. )
#     진행률 변수 completion_rate 100 일때 모든 할일 완료 custom_success
#     진행률 변수 completion_rate 80 일때 거의 다 완료 custom_info
#     진행률 변수 completion_rate 50 일때 절반 완료 custom_warning
#     진행률 변수 completion_rate 0 일때 절반 완료 custom_error
#     else 진행률 소수점 1자리까지 출력해주세요.
# 할일 목록이 없으면 할일을 추가해보세요. custom_info로 꾸며보기 
# ---------------------- 

    if completion_rate==100:
        custom_success("모든 할일 완료")
    elif completion_rate>=80:
        custom_info("거의 다 완료")
    elif completion_rate>=50:
        custom_warning("절반 완료")
    elif completion_rate==0:
        custom_error("화이팅")
    custom_warning(f"진행률: {completion_rate: .1f}%")   
else:
    custom_info("할일을 추가해보세요")
    











# todo_list = []

# if not todo_list: 
#     custom_info("할 일 목록이 없습니다. 할일을 추가해보세요")
# else:
#     completion_rate == (completed_todos/total_todos*100)

#     if completion_rate == 100:
#         custom_success("모든 할일 완료")
    











st.divider()

# st.markdown("""
# <footer style="background-color: #f2f2f2; padding: 20px; text-align: center;">
#   <p>&copy; 2025 나의 웹사이트. 모든 권리 보유.</p>
#   <p>
#     <a href="/about.html">회사 소개</a> | 
#     <a href="/contact.html">문의하기</a> | 
#     <a href="/privacy.html">개인정보 처리방침</a>
#   </p>
# </footer>
# """, unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 0.8em;'>
    💡 팁: 엔터키를 눌러서 빠르게 할일을 추가할 수 있어요!
    </div>
    """, 
    unsafe_allow_html=True)

st.markdown(""" 
<footer style="background-color: #33ccff; padding: 20px; text-align: center;">
  <p>&copy; 2025 나의 웹사이트. 모든 권리 보유.</p>
  <p>
    <a href="/about.html">회사 소개</a> | 
    <a href="/contact.html">문의하기</a> | 
    <a href="/privacy.html">개인정보 처리방침</a>
  </p>
</footer>""", unsafe_allow_html=True)


st.markdown("""
<footer style="background-color: #2699E6; color: white; text-align: center; padding: 20px;">
    <p>&copy; 2025 Company Name. All rights reserved.</p>
</footer>""", unsafe_allow_html=True)




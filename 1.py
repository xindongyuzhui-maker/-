import streamlit as st
import random

# 页面配置
st.set_page_config(page_title="专业版福彩摇号器", layout="centered")

# 自定义样式：让号码看起来像圆球
st.markdown("""
    <style>
    .red-ball {
        background-color: #ff4b4b;
        color: white;
        border-radius: 50%;
        padding: 10px;
        width: 40px;
        height: 40px;
        display: inline-block;
        text-align: center;
        margin: 5px;
        font-weight: bold;
    }
    .blue-ball {
        background-color: #1c83e1;
        color: white;
        border-radius: 50%;
        padding: 10px;
        width: 40px;
        height: 40px;
        display: inline-block;
        text-align: center;
        margin: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

def display_balls(balls, color="red"):
    html = ""
    for b in sorted(balls):
        html += f'<div class="{color}-ball">{str(b).zfill(2)}</div>'
    st.markdown(html, unsafe_allow_html=True)

st.title("🎰 专业版福彩摇号器")

# 创建标签页
tab1, tab2, tab3, tab4 = st.tabs(["双色球", "福彩3D", "快乐8", "七乐彩"])

# --- 1. 双色球 ---
with tab1:
    st.header("双色球")
    mode_ssq = st.radio("选择模式", ["标准单式 (6+1)", "小复式 (7+1)", "蓝球复式 (6+2)"], horizontal=True)
    
    if st.button("随机生成5注", key="ssq"):
        st.subheader("随机结果：")
        for i in range(5):
            st.write(f"第 {i+1} 注：")
            red_cnt, blue_cnt = 6, 1
            if "7+1" in mode_ssq: red_cnt = 7
            if "6+2" in mode_ssq: blue_cnt = 2
            reds = random.sample(range(1, 34), red_cnt)
            blues = random.sample(range(1, 17), blue_cnt)
            display_balls(reds, "red")
            display_balls(blues, "blue")
            st.divider()

# --- 2. 福彩3D ---
with tab2:
    st.header("福彩3D")
    mode_3d = st.selectbox("选择玩法", ["直选", "组三", "组六"])
    
    if st.button("随机生成5注", key="3d"):
        st.subheader("随机结果：")
        for i in range(5):
            if mode_3d == "直选":
                res = [random.randint(0, 9) for _ in range(3)]
            elif mode_3d == "组三":
                a, b = random.sample(range(0, 10), 2)
                res = [a, a, b]
                random.shuffle(res)
            else:
                res = random.sample(range(0, 10), 3)
            st.write(f"第 {i+1} 注： {' '.join(map(str, res))}")
        st.divider()

# --- 3. 快乐8 ---
with tab3:
    st.header("快乐8")
    play_type = st.slider("选择玩法 (选一至选十)", 1, 10, 10)
    
    if st.button("随机生成5注", key="kl8"):
        st.subheader(f"随机选{play_type}结果：")
        for i in range(5):
            nums = random.sample(range(1, 81), play_type)
            st.write(f"第 {i+1} 注：")
            display_balls(nums, "red")
            st.divider()

# --- 4. 七乐彩 ---
with tab4:
    st.header("七乐彩")
    if st.button("随机生成5注", key="qlc"):
        st.subheader("随机结果：")
        for i in range(5):
            nums = random.sample(range(1, 31), 7)
            st.write(f"第 {i+1} 注：")
            display_balls(nums, "red")
            st.divider()

st.caption("🎲 随机数由 Python 生成，仅供娱乐，请理性购彩。")

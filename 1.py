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
    .gray-ball {
        background-color: #f0f2f6;
        color: #31333F;
        border-radius: 10px;
        padding: 10px;
        display: inline-block;
        margin: 5px;
        border: 1px solid #d1d5db;
    }
    </style>
    """, unsafe_allow_html=True)


def display_balls(balls, color="red"):
    html = ""
    for b in sorted(balls):
        html += f'<div class="{color}-ball">{str(b).zfill(2)}</div>'
    st.markdown(html, unsafe_allow_html=True)


st.title("🎰 专业版福彩摇号器")

# 创建标签页对应不同彩种
tab1, tab2, tab3, tab4 = st.tabs(["双色球", "福彩3D", "快乐8", "七乐彩"])

# --- 1. 双色球 ---
with tab1:
    st.header("双色球")
    mode_ssq = st.radio("选择模式", ["标准单式 (6+1)", "小复式 (7+1)", "蓝球复式 (6+2)"], horizontal=True)

    if st.button("开始摇号", key="ssq"):
        red_cnt, blue_cnt = 6, 1
        if "7+1" in mode_ssq: red_cnt = 7
        if "6+2" in mode_ssq: blue_cnt = 2

        reds = random.sample(range(1, 34), red_cnt)
        blues = random.sample(range(1, 17), blue_cnt)

        st.subheader("中奖结果：")
        display_balls(reds, "red")
        display_balls(blues, "blue")

# --- 2. 福彩3D ---
with tab2:
    st.header("福彩3D")
    mode_3d = st.selectbox("选择玩法", ["直选", "组三 (两个数字相同)", "组六 (三个数字不同)"])

    if st.button("开始摇号", key="3d"):
        if mode_3d == "直选":
            res = [random.randint(0, 9) for _ in range(3)]
        elif mode_3d == "组三":
            # 先选两个不同的数
            a, b = random.sample(range(0, 10), 2)
            res = [a, a, b]
            random.shuffle(res)  # 打乱顺序
        else:  # 组六
            res = random.sample(range(0, 10), 3)

        st.subheader("中奖结果：")
        # 3D通常不排序，显示原始摇出顺序
        cols = st.columns(3)
        for i, n in enumerate(res):
            cols[i].metric(f"第{i + 1}位", n)

# --- 3. 快乐8 ---
with tab3:
    st.header("快乐8")
    play_type = st.slider("选择玩法 (选一至选十)", 1, 10, 10)

    if st.button("开始摇号", key="kl8"):
        nums = random.sample(range(1, 81), play_type)
        st.subheader(f"选{play_type}结果：")
        display_balls(nums, "red")
        st.info("💡 快乐8每期开奖共20个号，你选的号在其中即可。")

# --- 4. 七乐彩 ---
with tab4:
    st.header("七乐彩")
    if st.button("开始摇号", key="qlc"):
        nums = random.sample(range(1, 31), 7)
        st.subheader("中奖结果：")
        display_balls(nums, "red")

st.divider()
st.caption("🎲 随机数由 Python Secrets/Random 模块生成，仅供娱乐，购买请前往官方网点。")
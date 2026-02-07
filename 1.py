import streamlit as st
import random

# 页面配置
st.set_page_config(page_title="移动版福彩摇号器", layout="centered")

# 深度优化手机端布局的 CSS
st.markdown("""
    <style>
    /* 1. 强制去掉网页两侧的留白，让内容占满屏幕 */
    .block-container {
        padding-top: 1rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0.5rem !important;
        padding-right: 0.5rem !important;
    }
    
    /* 2. 标题字号缩小 */
    .main-title {
        font-size: 20px !important;
        text-align: center;
        margin-bottom: 5px;
        color: #333;
    }

    /* 3. 球体尺寸再次压缩：28px 确保 10 个球在一行也不断行 */
    .ball-container {
        display: flex;
        flex-wrap: nowrap; /* 强制不换行 */
        gap: 2px;          /* 球与球之间的极小间距 */
        margin-bottom: 5px;
        justify-content: flex-start;
        overflow-x: auto;  /* 万一屏幕太窄，允许横向微调而不是断行 */
    }
    
    .ball {
        color: white;
        border-radius: 50%;
        width: 28px;      /* 进一步缩小 */
        height: 28px;
        line-height: 28px;
        text-align: center;
        font-weight: bold;
        font-size: 12px;  /* 字号同步缩小 */
        flex: 0 0 auto;   /* 防止球被挤压变形 */
    }
    .red-ball { background-color: #ff4b4b; }
    .blue-ball { background-color: #1c83e1; }
    
    /* 每一注文字样式 */
    .bet-label {
        font-size: 12px;
        color: #888;
        margin-top: 5px;
        margin-bottom: 2px;
    }

    /* 调整 Tab 标签页的高度和字体 */
    .stTabs [data-baseweb="tab"] {
        padding-left: 10px !important;
        padding-right: 10px !important;
        font-size: 14px !important;
    }
    </style>
    """, unsafe_allow_html=True)

def display_balls(balls, color_class):
    balls_html = "".join([f'<div class="ball {color_class}">{str(b).zfill(2)}</div>' for b in sorted(balls)])
    return f'<div class="ball-container">{balls_html}</div>'

st.markdown('<h1 class="main-title">🎰 移动版福彩摇号器</h1>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["双色球", "3D", "快乐8", "七乐彩"])

# --- 1. 双色球 ---
with tab1:
    mode_ssq = st.radio("玩法", ["标准", "7+1", "6+2"], horizontal=True)
    if st.button("生成 5 注", key="ssq"):
        for i in range(5):
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            red_cnt = 7 if "7+1" in mode_ssq else 6
            blue_cnt = 2 if "6+2" in mode_ssq else 1
            reds = random.sample(range(1, 34), red_cnt)
            blues = random.sample(range(1, 17), blue_cnt)
            # 红蓝球放在同一个容器，确保它们连在一起
            balls_html = "".join([f'<div class="ball red-ball">{str(b).zfill(2)}</div>' for b in sorted(reds)])
            balls_html += "".join([f'<div class="ball blue-ball">{str(b).zfill(2)}</div>' for b in sorted(blues)])
            st.markdown(f'<div class="ball-container">{balls_html}</div>', unsafe_allow_html=True)

# --- 2. 福彩3D ---
with tab2:
    mode_3d = st.selectbox("模式", ["直选", "组三", "组六"])
    if st.button("生成 5 注", key="3d"):
        for i in range(5):
            if mode_3d == "直选":
                res = [random.randint(0, 9) for _ in range(3)]
            elif mode_3d == "组三":
                a, b = random.sample(range(0, 10), 2)
                res = sorted([a, a, b])
            else:
                res = sorted(random.sample(range(0, 10), 3))
            st.write(f"第 {i+1} 注： {' '.join(map(str, res))}")

# --- 3. 快乐8 ---
with tab3:
    play_type = st.select_slider("玩法(选几)", options=list(range(1, 11)), value=10)
    if st.button("生成 5 注", key="kl8"):
        for i in range(5):
            nums = random.sample(range(1, 81), play_type)
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            st.markdown(display_balls(nums, "red-ball"), unsafe_allow_html=True)

# --- 4. 七乐彩 ---
with tab4:
    if st.button("生成 5 注", key="qlc"):
        for i in range(5):
            nums = random.sample(range(1, 31), 7)
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            st.markdown(display_balls(nums, "red-ball"), unsafe_allow_html=True)

st.divider()
st.caption("🎲 仅供娱乐，请理性购彩")

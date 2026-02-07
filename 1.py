import streamlit as st
import random

# 页面配置：初始缩放比例优化
st.set_page_config(page_title="移动版福彩摇号器", layout="centered")

# 针对手机端优化的 CSS
st.markdown("""
    <style>
    /* 调整大标题字体 */
    .main-title {
        font-size: 24px !important;
        text-align: center;
        margin-bottom: 10px;
    }
    /* 球体基础样式：缩小尺寸以适应手机 */
    .ball-container {
        display: flex;
        flex-wrap: wrap;
        gap: 4px;
        margin-bottom: 8px;
    }
    .ball {
        color: white;
        border-radius: 50%;
        width: 32px;
        height: 32px;
        line-height: 32px;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }
    .red-ball { background-color: #ff4b4b; }
    .blue-ball { background-color: #1c83e1; }
    
    /* 每一注的文字样式 */
    .bet-label {
        font-size: 14px;
        color: #666;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    /* 缩小 3D 数字间距 */
    .d3-text {
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 5px;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

def display_balls(balls, color_class):
    # 将球排列在一个紧凑的容器里
    balls_html = "".join([f'<div class="ball {color_class}">{str(b).zfill(2)}</div>' for b in sorted(balls)])
    return f'<div class="ball-container">{balls_html}</div>'

st.markdown('<h1 class="main-title">🎰 移动版福彩摇号器</h1>', unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["双色球", "福彩3D", "快乐8", "七乐彩"])

# --- 1. 双色球 ---
with tab1:
    mode_ssq = st.radio("玩法", ["标准6+1", "小复式7+1", "蓝复式6+2"], horizontal=True)
    if st.button("点击生成 5 注", key="ssq"):
        for i in range(5):
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            red_cnt = 7 if "7+1" in mode_ssq else 6
            blue_cnt = 2 if "6+2" in mode_ssq else 1
            reds = random.sample(range(1, 34), red_cnt)
            blues = random.sample(range(1, 17), blue_cnt)
            
            # 显示红球和蓝球
            html = display_balls(reds, "red-ball") + display_balls(blues, "blue-ball")
            st.markdown(html, unsafe_allow_html=True)

# --- 2. 福彩3D ---
with tab2:
    mode_3d = st.selectbox("玩法选择", ["直选", "组三", "组六"])
    if st.button("点击生成 5 注", key="3d"):
        for i in range(5):
            if mode_3d == "直选":
                res = [random.randint(0, 9) for _ in range(3)]
            elif mode_3d == "组三":
                a, b = random.sample(range(0, 10), 2)
                res = sorted([a, a, b])
            else:
                res = sorted(random.sample(range(0, 10), 3))
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="d3-text">{" ".join(map(str, res))}</div>', unsafe_allow_html=True)

# --- 3. 快乐8 ---
with tab3:
    play_type = st.select_slider("玩法(选几)", options=list(range(1, 11)), value=10)
    if st.button("点击生成 5 注", key="kl8"):
        for i in range(5):
            nums = random.sample(range(1, 81), play_type)
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            st.markdown(display_balls(nums, "red-ball"), unsafe_allow_html=True)

# --- 4. 七乐彩 ---
with tab4:
    if st.button("点击生成 5 注", key="qlc"):
        for i in range(5):
            nums = random.sample(range(1, 31), 7)
            st.markdown(f'<div class="bet-label">第 {i+1} 注</div>', unsafe_allow_html=True)
            st.markdown(display_balls(nums, "red-ball"), unsafe_allow_html=True)

st.divider()
st.caption("🎲 随机结果仅供参考，请理性购彩")

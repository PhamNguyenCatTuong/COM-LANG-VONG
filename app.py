import streamlit as st

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide",
    initial_sidebar_state="collapsed" # Mặc định ẩn sidebar để giống menu 2 gạch
)

# =========================
# CSS TÙY CHỈNH & FIX LỖI GIAO DIỆN
# =========================
st.markdown("""
<style>
/* Ẩn các thành phần mặc định để web không bị xê dịch */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}

/* Fix lỗi kéo trái kéo phải trên điện thoại */
html, body {
    max-width: 100vw;
    overflow-x: hidden;
    margin: 0;
    padding: 0;
}

.main .block-container {
    padding: 0 !important;
}

/* Cấu hình Banner mới */
.hero {
    min-height: 80vh;
    background: 
        linear-gradient(to top, rgba(0,0,0,0.7), transparent),
        url("https://vtv1.mediacdn.vn/2019/9/22/com-vong-1569116799014631327178.jpg"); /* Hình ảnh cốm làng vòng thực tế */
    background-size: cover;
    background-position: center;
    position: relative;
    display: flex;
    align-items: flex-end; /* Đưa nội dung xuống dưới cùng */
    justify-content: flex-start; /* Nằm bên tay trái */
    padding: 20px;
}

/* Nội dung banner trên Mobile */
.hero-box {
    max-width: 85%;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: 28px !important; /* Nhỏ lại cho mobile */
    line-height: 1.1;
    margin: 5px 0;
    color: white;
}

.hero p {
    font-size: 15px !important;
    line-height: 1.2; /* Khoảng cách dòng gần nhau hơn */
    margin: 0;
    color: rgba(255,255,255,0.9);
}

/* Sidebar Menu (Dấu 2 gạch) */
[data-testid="stSidebarNav"] {
    padding-top: 2rem;
}

/* Style cho Contact Card */
.contact-card {
    background: #f9f9f9;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #2e7d32;
    margin: 20px;
    color: #333;
}
</style>
""", unsafe_allow_html=True)

# =========================
# QUẢN LÝ ĐIỀU HƯỚNG (MULTI-PAGE)
# =========================
# Sơ đồ menu theo ảnh bạn gửi
menu_options = [
    "Thông tin sản phẩm", # Trang đầu tiên hiện ra
    "Chất lượng & Chứng nhận",
    "Truy xuất nguồn gốc",
    "Bao bì & Thu hồi",     # Mục bổ sung mới
    "Nội dung truyền thông",
    "Liên hệ"
]

# Sử dụng sidebar của Streamlit làm menu "xổ ra"
with st.sidebar:
    st.title("🌾 Menu")
    choice = st.radio("Chuyển trang:", menu_options)

# =========================
# NỘI DUNG TỪNG TRANG
# =========================

if choice == "Thông tin sản phẩm":
    # Banner chỉ hiện ở trang chủ (Thông tin sản phẩm)
    st.markdown("""
    <section class="hero">
        <div class="hero-box">
            <h1>Cốm Làng Vòng</h1>
            <p>Hạt xanh non, dẻo thơm tinh tế.</p>
            <p>Đặc sản truyền thống Hà Nội.</p>
        </div>
    </section>
    """, unsafe_allow_html=True)
    
    st.header("Thông tin chi tiết")
    st.write("- **Tên sản phẩm:** Cốm tươi Làng Vòng")
    st.write("- **Mã sản phẩm:** LV-001")
    st.write("- **Thương hiệu:** Đặc sản Hà Nội")

elif choice == "Chất lượng & Chứng nhận":
    st.header("Chất lượng & Chứng nhận")
    st.info("Sản phẩm đạt chứng nhận OCOP 4 sao và kiểm định ATVSTP định kỳ.")

elif choice == "Truy xuất nguồn gốc":
    st.header("Truy xuất nguồn gốc")
    st.write("- **Nguồn nguyên liệu:** Lúa nếp cái hoa vàng")
    st.write("- **Khu vực sản xuất:** Làng Vòng, Cầu Giấy, Hà Nội")

elif choice == "Bao bì & Thu hồi":
    st.header("Thông tin bao bì & Thu hồi")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Vật liệu")
        st.write("- **Mực in:** Mực thực phẩm an toàn")
        st.write("- **Giấy:** Giấy kraft thân thiện môi trường")
    with col2:
        st.subheader("Quy trình thu hồi")
        st.write("- **Thời gian:** Trong vòng 24h nếu có lỗi đóng gói")

elif choice == "Nội dung truyền thông":
    st.header("Truyền thông")
    st.video("https://www.youtube.com/watch?v=your_video_id") # Thay bằng link video thật

elif choice == "Liên hệ":
    st.header("Liên hệ với chúng tôi")
    # Fix lỗi Contact Card không hiện thông tin
    st.markdown("""
    <div class="contact-card">
        <h4>🌾 Thông tin chính thức</h4>
        <p><b>Địa chỉ:</b> Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội</p>
        <p><b>Hotline:</b> 0385 437 503</p>
        <p><b>Website:</b> www.comlangvong.vn</p>
        <p><b>Mạng xã hội:</b> facebook.com/comlangvong</p>
    </div>
    """, unsafe_allow_html=True)

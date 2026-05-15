import streamlit as st

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide"
)

params = st.query_params
page = params.get("page", "thongtin")

# =========================
# CSS GIAO DIỆN WEBSITE
# =========================
st.markdown("""
<style>

#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}
[data-testid="stDecoration"] {display: none !important;}
[data-testid="stStatusWidget"] {display: none !important;}

html {
    scroll-behavior: smooth;
    overflow-x: hidden;
}

body {
    margin: 0;
    padding: 0;
    background: #fffdf7;
    overflow-x: hidden;
}

* {
    box-sizing: border-box;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* =========================
HEADER / THANH MENU
========================= */
.header {
    position: sticky;
    top: 0;
    z-index: 999;
    background: white;
    margin: 14px;
    padding: 14px 28px;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 28px;
    width: calc(100% - 28px);
}

.logo {
    font-size: 28px;
    font-weight: 800;
    color: #2e7d32;
    white-space: nowrap;
}

.nav {
    display: flex;
    gap: 22px;
    align-items: center;
}

.nav a {
    text-decoration: none;
    color: white;
    background: #2e7d32;
    font-weight: 700;
    font-size: 14px;
    padding: 12px 18px;
    border-radius: 8px;
}

/* NÚT 3 GẠCH */
#menu-toggle {
    display: none;
}

.hamburger {
    display: none;
    font-size: 30px;
    cursor: pointer;
    color: #333;
}

.nav a:hover {
    background: #256b29;
    color: white;
}
.order-btn {
    background: #2e7d32;
    color: white !important;
    padding: 10px 16px;
    border-radius: 999px;
}

/* =========================
HERO BANNER
========================= */
.hero {
    min-height: 620px;
    margin: 0 14px;
    border-radius: 26px;
    background:
        linear-gradient(rgba(0,0,0,0.35), rgba(0,0,0,0.35)),
        url("http://tuhaoviet.vn/UploadImages/News/hinh-anh-com-lang-vong.jpg");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    padding: 60px;
    box-sizing: border-box;
    color: white;
}

.hero-box {
    max-width: 680px;
}

.hero-small {
    font-size: 18px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 12px;
}

.hero h1 {
    font-size: 64px;
    line-height: 1.1;
    margin: 0 0 18px 0;
}

.hero p {
    font-size: 20px;
    line-height: 1.7;
    margin-bottom: 30px;
}

.hero-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}

.btn-main {
    background: #2e7d32;
    color: white;
    padding: 14px 24px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
}

.btn-light {
    background: white;
    color: #2e7d32;
    padding: 14px 24px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
}

/* =========================
SECTION CHUNG
========================= */
.section {
    max-width: 1180px;
    margin: 80px auto;
    padding: 0 28px;
}

.section-title {
    text-align: center;
    margin-bottom: 40px;
}

.section-title p {
    color: #2e7d32;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.section-title h2 {
    font-size: 42px;
    margin: 0;
    color: #222;
}

/* =========================
CARD GIỚI THIỆU
========================= */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 22px;
}

.feature-card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.08);
    text-align: center;
}

.feature-icon {
    font-size: 42px;
    margin-bottom: 12px;
}

.feature-card h3 {
    color: #2e7d32;
    margin-bottom: 10px;
}

.feature-card p {
    color: #555;
    line-height: 1.7;
}

/* =========================
CÂU CHUYỆN SẢN PHẨM
========================= */
.story {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 45px;
    align-items: center;
}

.story img {
    width: 100%;
    border-radius: 24px;
    box-shadow: 0 8px 26px rgba(0,0,0,0.12);
}

.story-text h2 {
    font-size: 40px;
    color: #222;
    margin-bottom: 18px;
}

.story-text p {
    line-height: 1.9;
    color: #444;
    font-size: 17px;
}

/* =========================
SẢN PHẨM NỔI BẬT
========================= */
.product-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

.product-card {
    background: white;
    border-radius: 22px;
    overflow: hidden;
    box-shadow: 0 6px 22px rgba(0,0,0,0.08);
}

.product-card img {
    width: 100%;
    height: 230px;
    object-fit: cover;
}

.product-info {
    padding: 22px;
}

.product-info h3 {
    color: #2e7d32;
    margin-top: 0;
}

.product-info p {
    color: #555;
    line-height: 1.7;
}

/* =========================
TRUY XUẤT NGUỒN GỐC
========================= */
.trace-box {
    background: #f1f8e9;
    padding: 36px;
    border-radius: 24px;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
}

.trace-item {
    background: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.06);
}

.trace-item h3 {
    color: #2e7d32;
    margin-top: 0;
}

/* =========================
GALLERY
========================= */
.gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
}

.gallery img {
    width: 100%;
    height: 260px;
    object-fit: cover;
    border-radius: 20px;
}

/* =========================
LIÊN HỆ
========================= */
.contact {
    background: #2e7d32;
    color: white;
    border-radius: 28px;
    padding: 50px;
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 30px;
    align-items: center;
}

.contact h2 {
    font-size: 40px;
    margin-top: 0;
}

.contact p {
    font-size: 17px;
    line-height: 1.8;
}

.contact-card {
    background: white;
    color: #222;
    padding: 28px;
    border-radius: 20px;
}

.contact-card a {
    color: #2e7d32;
    font-weight: 700;
    text-decoration: none;
}

/* =========================
NÚT GỌI / ZALO NỔI
========================= */
.floating-contact {
    position: fixed;
    bottom: 28px;
    right: 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 9999;
}

.float-btn {
    width: 52px;
    height: 52px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: white;
    font-size: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}

.call-btn {
    background: #2e7d32;
}

.zalo-btn {
    background: #0084ff;
}

/* =========================
FOOTER
========================= */
.footer {
    background: #111;
    color: white;
    padding: 45px 28px;
    margin-top: 80px;
}

.footer-inner {
    max-width: 1180px;
    margin: auto;
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    gap: 28px;
}

.footer h3 {
    color: white;
}

.footer p,
.footer a {
    color: #ddd;
    text-decoration: none;
    line-height: 1.8;
}

.copy {
    text-align: center;
    color: #aaa;
    margin-top: 35px;
    font-size: 14px;
}

/* =========================
MOBILE
========================= */
@media (max-width: 900px) {
   .header {
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
}

.hamburger {
    display: block;
}

.nav {
    display: none;
    width: 100%;
    flex-direction: column;
    gap: 12px;
    margin-top: 15px;
}

#menu-toggle:checked ~ .nav {
    display: flex;
}

.nav a {
    width: 100%;
    text-align: center;
    box-sizing: border-box;
}

    .hero {
        min-height: 560px;
        padding: 36px 24px;
    }

    .hero h1 {
        font-size: 42px;
    }

    .hero p {
        font-size: 17px;
    }

    .feature-grid,
    .product-grid,
    .trace-box,
    .gallery,
    .story,
    .contact,
    .footer-inner {
        grid-template-columns: 1fr;
    }

    .section {
        margin: 55px auto;
    }

    .section-title h2 {
        font-size: 32px;
    }

    .contact {
        padding: 32px 24px;
    }

    .contact h2 {
        font-size: 32px;
    }

    .logo {
        font-size: 25px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER / MENU WEBSITE
# =========================
st.markdown("""
<div class="header">

<input type="checkbox" id="menu-toggle">

<div class="logo">🌾 Cốm Làng Vòng</div>

<label for="menu-toggle" class="hamburger">☰</label>

<div class="nav">
<a href="?page=thongtin" target="_self">Thông tin sản phẩm</a>
<a href="?page=truyxuat" target="_self">Truy xuất nguồn gốc</a>
<a href="?page=chatluong" target="_self">Chất lượng & chứng nhận</a>
<a href="?page=truyenthong" target="_self">Nội dung truyền thông</a>
<a href="?page=baobi" target="_self">Thông tin bao bì</a>
</div>

</div>
""", unsafe_allow_html=True)

# =========================
# HERO BANNER
# =========================
# =========================
# TRANG THÔNG TIN SẢN PHẨM
# =========================
if page == "thongtin":

   st.markdown("""
<section class="hero">
    <div class="hero-box">
        <div class="hero-small">Đặc sản mùa thu Hà Nội</div>
        <h1>Cốm Làng Vòng</h1>
        <p>
            Hạt cốm xanh non, dẻo thơm, thanh nhẹ — thức quà truyền thống gói trọn hương vị
            tinh tế của đất kinh kỳ.
        </p>
    </div>
</section>
""", unsafe_allow_html=True)

    st.markdown("""
    PHẦN GIỚI THIỆU NHANH
    """, unsafe_allow_html=True)

    st.markdown("""
    PHẦN SẢN PHẨM
    """, unsafe_allow_html=True)

# =========================
# TRANG TRUY XUẤT
# =========================
elif page == "truyxuat":

    st.markdown("""
    PHẦN TRUY XUẤT
    """, unsafe_allow_html=True)

# =========================
# TRANG CHẤT LƯỢNG
# =========================
elif page == "chatluong":

    st.markdown("""
    PHẦN CHẤT LƯỢNG
    """, unsafe_allow_html=True)

# =========================
# TRANG TRUYỀN THÔNG
# =========================
elif page == "truyenthong":

    st.markdown("""
    PHẦN CÂU CHUYỆN
    """, unsafe_allow_html=True)

    st.markdown("""
    PHẦN HÌNH ẢNH
    """, unsafe_allow_html=True)

# =========================
# TRANG BAO BÌ
# =========================
elif page == "baobi":

    st.markdown("""
    PHẦN BAO BÌ
    """, unsafe_allow_html=True)

# =========================
# NÚT GỌI / ZALO NỔI
# =========================
st.markdown("""
<div class="floating-contact">
    <a href="tel:0385437503" class="float-btn call-btn">📞</a>
    <a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">💬</a>
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER CUỐI TRANG
# =========================
st.markdown("""
<footer class="footer">
    <div class="footer-inner">
        <div>
            <h3>🌾 Cốm Làng Vòng</h3>
            <p>
                Đặc sản truyền thống Hà Nội, mang hương vị thanh tao của lúa nếp non
                và nét đẹp văn hóa ẩm thực đất kinh kỳ.
            </p>
        </div>

        <div>
            <h3>Danh mục</h3>
            <p><a href="#trangchu" target="_self">Trang chủ</a></p>
            <p><a href="#cauchuyen" target="_self">Câu chuyện</a></p>
            <p><a href="#sanpham" target="_self">Sản phẩm</a></p>
            <p><a href="#truyxuat" target="_self">Truy xuất</a></p>
        </div>

        <div>
            <h3>Liên hệ</h3>
            <p>📍 Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội</p>
            <p>📞 0385 437 503</p>
            <p>💬 Zalo: 0385 437 503</p>
        </div>
    </div>

    <div class="copy">
        © 2026 Cốm Làng Vòng. All rights reserved.
    </div>
</footer>
""", unsafe_allow_html=True)

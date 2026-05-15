import streamlit as st
from pathlib import Path
import base64

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide"
)

# =========================
# HÀM ĐỌC ẢNH LOCAL
# =========================
def image_to_base64(image_name):
    image_path = Path(image_name)

    if image_path.exists():
        img_bytes = image_path.read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return f"data:image/jpeg;base64,{encoded}"

    return ""


# =========================
# LOAD ẢNH
# =========================
hero_img = image_to_base64("Com tong quan 1.jpg")
img_1 = image_to_base64("Com tong quan.jpg")
img_2 = image_to_base64("Com tong quan 1.jpg")
img_3 = image_to_base64("Com tong quan 2.jpg")
img_4 = image_to_base64("Com tong quan 3.jpg")

# =========================
# LẤY TRANG HIỆN TẠI
# =========================
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

html, body {
    overflow-x: hidden;
    margin: 0;
    padding: 0;
    background: #f6f6f6;
}

.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* =========================
HEADER
========================= */
.header {
    position: sticky;
    top: 0;
    z-index: 999;
    background: white;
    margin: 14px;
    padding: 16px 28px;
    border-radius: 20px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);

    display: flex;
    align-items: center;
    justify-content: space-between;
}

.logo {
    font-size: 30px;
    font-weight: 800;
    color: #2e7d32;
}

/* MENU */
.nav {
    display: flex;
    gap: 14px;
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

.nav a:hover {
    background: #256b29;
}

/* MOBILE MENU */
#menu-toggle {
    display: none;
}

.hamburger {
    display: none;
    font-size: 32px;
    cursor: pointer;
}

/* =========================
HERO
========================= */
.hero {
    position: relative;
    width: calc(100% - 28px);
    height: 340px;
    margin: 0 14px;
    border-radius: 26px;
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 40px;
    box-sizing: border-box;
    color: white;
}

.hero-bg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background: rgba(0,0,0,0.38);
}

.hero-box {
    position: relative;
    z-index: 2;
    max-width: 320px;
    margin-top: 40px;
}

.hero-small {
    font-size: 14px;
    letter-spacing: 1px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 10px;
}

.hero h1 {
    font-size: 45px;
    line-height: 1.1;
    margin-bottom: 14px;
}

.hero p {
    font-size: 13px;
    line-height: 1.7;
}

/* =========================
SECTION
========================= */
.section {
    max-width: 1180px;
    margin: 80px auto;
    padding: 0 24px;
}

.section-title {
    text-align: center;
    margin-bottom: 40px;
}

.section-title p {
    color: #2e7d32;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 2px;
}

.section-title h2 {
    font-size: 44px;
    color: #222;
}

/* =========================
FEATURE
========================= */
.feature-grid {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 22px;
}

.feature-card {
    background: white;
    padding: 28px;
    border-radius: 22px;
    text-align: center;
    box-shadow: 0 6px 22px rgba(0,0,0,0.08);
}

.feature-icon {
    font-size: 42px;
    margin-bottom: 14px;
}

.feature-card h3 {
    color: #2e7d32;
}

.feature-card p {
    color: #555;
    line-height: 1.8;
}

/* =========================
PRODUCT
========================= */
.product-grid {
    display: grid;
    grid-template-columns: repeat(3,1fr);
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
    height: 240px;
    object-fit: cover;
}

.product-info {
    padding: 22px;
}

.product-info h3 {
    color: #2e7d32;
}

/* =========================
TRUY XUẤT
========================= */
.trace-box {
    background: #f1f8e9;
    padding: 36px;
    border-radius: 24px;

    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 22px;
}

.trace-item {
    background: white;
    padding: 24px;
    border-radius: 18px;
}

.trace-item h3 {
    color: #2e7d32;
}

/* =========================
STORY
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
}

.story-text h2 {
    font-size: 40px;
    color: #222;
}

.story-text p {
    line-height: 1.9;
    color: #444;
}

/* =========================
GALLERY
========================= */
.gallery {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 18px;
}

.gallery img {
    width: 100%;
    height: 260px;
    object-fit: cover;
    border-radius: 20px;
}

/* =========================
FLOAT BUTTON
========================= */
.floating-contact {
    position: fixed;
    right: 18px;
    bottom: 28px;

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
    align-items: center;
    justify-content: center;

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
}

/* =========================
MOBILE
========================= */
@media (max-width: 900px){

.header {
    flex-wrap: wrap;
}

.hamburger {
    display: block;
}

.nav {
    display: none;
    width: 100%;
    flex-direction: column;
    gap: 12px;
    margin-top: 16px;
}

#menu-toggle:checked ~ .nav {
    display: flex;
}

.nav a {
    width: 100%;
    text-align: center;
}

.hero {
    height: 320px;
    padding: 24px;
}

.hero h1 {
    font-size: 34px;
}

.hero p {
    font-size: 14px;
}

.hero-box {
    max-width: 220px;
    margin-top: 20px;
}

.feature-grid,
.product-grid,
.trace-box,
.story,
.gallery,
.footer-inner {
    grid-template-columns: 1fr;
}

.section-title h2 {
    font-size: 34px;
}

.logo {
    font-size: 26px;
}

}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header">

<input type="checkbox" id="menu-toggle">

<div class="logo">
🌾 Cốm Làng Vòng
</div>

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
# THÔNG TIN SẢN PHẨM
# =========================
if page == "thongtin":

    st.markdown(f"""
<section class="hero">

<img src="{hero_img}" class="hero-bg">

<div class="hero-overlay"></div>

<div class="hero-box">

<div class="hero-small">
Đặc sản mùa thu Hà Nội
</div>

<h1>
Cốm Làng Vòng
</h1>

<p>
Hạt cốm xanh non, dẻo thơm, thanh nhẹ — thức quà truyền thống gói trọn
hương vị tinh tế của đất kinh kỳ.
</p>

</div>

</section>
""", unsafe_allow_html=True)

    st.markdown("""
<section class="section">

<div class="section-title">
<p>Giá trị nổi bật</p>
<h2>Vì sao chọn Cốm Làng Vòng?</h2>
</div>

<div class="feature-grid">

<div class="feature-card">
<div class="feature-icon">🌾</div>
<h3>Tên sản phẩm</h3>
<p>
Cốm Làng Vòng là đặc sản truyền thống nổi tiếng của Hà Nội.
</p>
</div>

<div class="feature-card">
<div class="feature-icon">🏷️</div>
<h3>Mã sản phẩm</h3>
<p>
Mã sản phẩm mẫu: COM-LV-001.
</p>
</div>

<div class="feature-card">
<div class="feature-icon">🌿</div>
<h3>Thương hiệu</h3>
<p>
Gắn với làng nghề lâu đời và nét đẹp văn hóa ẩm thực Hà Nội.
</p>
</div>

<div class="feature-card">
<div class="feature-icon">📞</div>
<h3>Đặt hàng</h3>
<p>
Liên hệ nhanh qua hotline hoặc Zalo.
</p>
</div>

</div>

</section>
""", unsafe_allow_html=True)

    st.markdown(f"""
<section class="section">

<div class="section-title">
<p>Sản phẩm</p>
<h2>Những món nổi bật</h2>
</div>

<div class="product-grid">

<div class="product-card">
<img src="{img_1}">
<div class="product-info">
<h3>Cốm tươi</h3>
<p>Hạt cốm mềm dẻo, thơm nhẹ.</p>
</div>
</div>

<div class="product-card">
<img src="{img_2}">
<div class="product-info">
<h3>Bánh cốm</h3>
<p>Bánh truyền thống với nhân đậu xanh ngọt dịu.</p>
</div>
</div>

<div class="product-card">
<img src="{img_3}">
<div class="product-info">
<h3>Chả cốm</h3>
<p>Món ăn quen thuộc trong bữa cơm Việt.</p>
</div>
</div>

</div>

</section>
""", unsafe_allow_html=True)

# =========================
# TRUY XUẤT
# =========================
elif page == "truyxuat":

    st.markdown("""
<section class="section">

<div class="section-title">
<p>Thông tin sản phẩm</p>
<h2>Truy xuất nguồn gốc</h2>
</div>

<div class="trace-box">

<div class="trace-item">
<h3>🌾 Nguồn nguyên liệu</h3>
<p>
Lúa nếp non được chọn đúng thời điểm thu hoạch.
</p>
</div>

<div class="trace-item">
<h3>📍 Khu vực sản xuất</h3>
<p>
Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội.
</p>
</div>

<div class="trace-item">
<h3>🏷️ Mã lô hàng</h3>
<p>
Mã lô mẫu: LV-2026-001.
</p>
</div>

</div>

</section>
""", unsafe_allow_html=True)

# =========================
# CHẤT LƯỢNG
# =========================
elif page == "chatluong":

    st.markdown("""
<section class="section">

<div class="section-title">
<p>Chất lượng</p>
<h2>Chất lượng & chứng nhận</h2>
</div>

<div class="feature-grid">

<div class="feature-card">
<div class="feature-icon">🏅</div>
<h3>OCOP</h3>
<p>Sản phẩm phù hợp định hướng phát triển đặc sản địa phương.</p>
</div>

<div class="feature-card">
<div class="feature-icon">🔍</div>
<h3>Kiểm định</h3>
<p>Quy trình sản xuất chú trọng vệ sinh và chất lượng.</p>
</div>

<div class="feature-card">
<div class="feature-icon">🍃</div>
<h3>Hương vị</h3>
<p>Giữ được mùi thơm lúa non tự nhiên.</p>
</div>

<div class="feature-card">
<div class="feature-icon">✅</div>
<h3>An toàn</h3>
<p>Bảo quản và đóng gói đúng tiêu chuẩn.</p>
</div>

</div>

</section>
""", unsafe_allow_html=True)

# =========================
# TRUYỀN THÔNG
# =========================
elif page == "truyenthong":

    st.markdown(f"""
<section class="section story">

<div>
<img src="{img_4}">
</div>

<div class="story-text">

<p style="color:#2e7d32; font-weight:700;">
Câu chuyện sản phẩm
</p>

<h2>
Thức quà thanh tao của mùa thu Hà Nội
</h2>

<p>
Cốm Làng Vòng là một phần ký ức của Hà Nội,
gắn liền với hương lúa non và mùa thu đất kinh kỳ.
</p>

<p>
Cốm thường được gói trong lá sen để giữ hương thơm tự nhiên.
</p>

</div>

</section>
""", unsafe_allow_html=True)

    st.markdown(f"""
<section class="section">

<div class="section-title">
<p>Thư viện</p>
<h2>Hình ảnh sản phẩm</h2>
</div>

<div class="gallery">
<img src="{img_1}">
<img src="{img_2}">
<img src="{img_3}">
</div>

</section>
""", unsafe_allow_html=True)

# =========================
# BAO BÌ
# =========================
elif page == "baobi":

    st.markdown("""
<section class="section">

<div class="section-title">
<p>Bao bì</p>
<h2>Thông tin bao bì</h2>
</div>

<div class="feature-grid">

<div class="feature-card">
<div class="feature-icon">🖨️</div>
<h3>Mực in</h3>
<p>Mực in rõ nét và phù hợp bao bì thực phẩm.</p>
</div>

<div class="feature-card">
<div class="feature-icon">📦</div>
<h3>Giấy bao bì</h3>
<p>Giúp bảo quản sản phẩm tốt hơn.</p>
</div>

<div class="feature-card">
<div class="feature-icon">♻️</div>
<h3>Thu hồi bao bì</h3>
<p>Khuyến khích tái sử dụng và phân loại.</p>
</div>

<div class="feature-card">
<div class="feature-icon">🌿</div>
<h3>Thiết kế</h3>
<p>Sử dụng màu xanh cốm và họa tiết lá sen.</p>
</div>

</div>

</section>
""", unsafe_allow_html=True)

# =========================
# FLOAT BUTTON
# =========================
st.markdown("""
<div class="floating-contact">

<a href="tel:0385437503" class="float-btn call-btn">
📞
</a>

<a href="https://zalo.me/0385437503"
target="_blank"
class="float-btn zalo-btn">
💬
</a>

</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown("""
<footer class="footer">

<div class="footer-inner">

<div>
<h3>🌾 Cốm Làng Vòng</h3>

<p>
Đặc sản truyền thống Hà Nội,
mang hương vị thanh tao của lúa nếp non.
</p>
</div>

<div>
<h3>Danh mục</h3>

<p><a href="?page=thongtin">Thông tin sản phẩm</a></p>
<p><a href="?page=truyxuat">Truy xuất nguồn gốc</a></p>
<p><a href="?page=chatluong">Chất lượng & chứng nhận</a></p>
<p><a href="?page=truyenthong">Nội dung truyền thông</a></p>
<p><a href="?page=baobi">Thông tin bao bì</a></p>
</div>

<div>
<h3>Liên hệ</h3>

<p>📍 Làng Vòng, Hà Nội</p>
<p>📞 0385 437 503</p>
<p>💬 Zalo: 0385 437 503</p>
</div>

</div>

<div class="copy">
© 2026 Cốm Làng Vòng. All rights reserved.
</div>

</footer>
""", unsafe_allow_html=True)

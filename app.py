import streamlit as st

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide"
)

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
}

body {
    margin: 0;
    padding: 0;
    background: #fffdf7;
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
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);

    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 18px;
}

.logo {
    font-size: 30px;
    font-weight: 800;
    color: #2e7d32;
}

.nav {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}

.nav a {
    text-decoration: none;
    color: white;
    background: #2e7d32;
    padding: 10px 16px;
    border-radius: 999px;
    font-size: 14px;
    font-weight: 700;
}

.nav a:hover {
    background: #256b29;
}

/* =========================
HERO
========================= */
.hero {
    margin: 0 14px;
    min-height: 620px;
    border-radius: 28px;

    background:
    linear-gradient(rgba(0,0,0,0.38), rgba(0,0,0,0.38)),
    url("https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=1600&q=80");

    background-size: cover;
    background-position: center;

    display: flex;
    align-items: center;

    padding: 60px;
    box-sizing: border-box;

    color: white;
}

.hero-box {
    max-width: 700px;
}

.hero-small {
    font-size: 18px;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 12px;
    letter-spacing: 2px;
}

.hero h1 {
    font-size: 68px;
    line-height: 1.1;
    margin-bottom: 18px;
}

.hero p {
    font-size: 20px;
    line-height: 1.8;
}

.hero-buttons {
    margin-top: 30px;
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
}

.btn-main {
    background: #2e7d32;
    color: white;
    text-decoration: none;
    padding: 14px 24px;
    border-radius: 999px;
    font-weight: 700;
}

.btn-light {
    background: white;
    color: #2e7d32;
    text-decoration: none;
    padding: 14px 24px;
    border-radius: 999px;
    font-weight: 700;
}

/* =========================
SECTION
========================= */
.section {
    max-width: 1180px;
    margin: 90px auto;
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
    margin-top: 10px;
}

/* =========================
FEATURE CARD
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
STORY
========================= */
.story {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 50px;
    align-items: center;
}

.story img {
    width: 100%;
    border-radius: 24px;
}

.story-text h2 {
    font-size: 42px;
    color: #222;
}

.story-text p {
    line-height: 1.9;
    color: #444;
    font-size: 17px;
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
TRACEABILITY
========================= */
.trace-grid {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 22px;
}

.trace-card {
    background: #f1f8e9;
    padding: 28px;
    border-radius: 22px;
}

.trace-card h3 {
    color: #2e7d32;
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
    border-radius: 22px;
}

/* =========================
CONTACT
========================= */
.contact {
    background: #2e7d32;
    color: white;
    border-radius: 28px;
    padding: 50px;

    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 30px;
}

.contact h2 {
    font-size: 42px;
}

.contact p {
    line-height: 1.9;
}

.contact-box {
    background: white;
    color: #222;
    padding: 28px;
    border-radius: 22px;
}

.contact-box a {
    color: #2e7d32;
    text-decoration: none;
    font-weight: 700;
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
    gap: 12px;
    z-index: 9999;
}

.float-btn {
    width: 54px;
    height: 54px;
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
    margin-top: 90px;
    padding: 50px 24px;
}

.footer-inner {
    max-width: 1180px;
    margin: auto;

    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    gap: 30px;
}

.footer p,
.footer a {
    color: #ddd;
    text-decoration: none;
    line-height: 1.9;
}

.copy {
    text-align: center;
    margin-top: 40px;
    color: #aaa;
}

/* =========================
MOBILE
========================= */
@media (max-width: 900px){

.hero {
    min-height: 520px;
    padding: 34px 24px;
}

.hero h1 {
    font-size: 42px;
}

.hero p {
    font-size: 17px;
}

.feature-grid,
.story,
.product-grid,
.trace-grid,
.gallery,
.contact,
.footer-inner {
    grid-template-columns: 1fr;
}

.section-title h2 {
    font-size: 34px;
}

.logo {
    font-size: 26px;
}

.nav {
    justify-content: center;
}

.nav a {
    font-size: 13px;
    padding: 9px 14px;
}

}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div class="header">

    <div class="logo">
        🌾 Cốm Làng Vòng
    </div>

    <div class="nav">
        <a href="#trangchu">Trang chủ</a>
        <a href="#cauchuyen">Câu chuyện</a>
        <a href="#sanpham">Sản phẩm</a>
        <a href="#truyxuat">Truy xuất</a>
        <a href="#hinhanh">Hình ảnh</a>
        <a href="#lienhe">Liên hệ</a>
    </div>

</div>
""", unsafe_allow_html=True)

# =========================
# HERO
# =========================
st.markdown("""
<section class="hero" id="trangchu">

    <div class="hero-box">

        <div class="hero-small">
            Đặc sản mùa thu Hà Nội
        </div>

        <h1>Cốm Làng Vòng</h1>

        <p>
            Hương thơm lúa non, vị ngọt thanh và màu xanh dịu —
            thức quà tinh tế mang đậm dấu ấn văn hóa Hà Nội.
        </p>

        <div class="hero-buttons">
            <a href="#sanpham" class="btn-main">Xem sản phẩm</a>
            <a href="#lienhe" class="btn-light">Liên hệ ngay</a>
        </div>

    </div>

</section>
""", unsafe_allow_html=True)

# =========================
# FEATURE
# =========================
st.markdown("""
<section class="section">

    <div class="section-title">
        <p>Giá trị nổi bật</p>
        <h2>Vì sao chọn Cốm Làng Vòng?</h2>
    </div>

    <div class="feature-grid">

        <div class="feature-card">
            <div class="feature-icon">🌾</div>
            <h3>Truyền thống</h3>
            <p>
                Gắn liền với làng nghề lâu đời của Hà Nội.
            </p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🍃</div>
            <h3>Nguyên liệu chọn lọc</h3>
            <p>
                Lúa nếp non được chọn đúng thời điểm để giữ độ dẻo thơm.
            </p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🏅</div>
            <h3>Chất lượng</h3>
            <p>
                Chú trọng quy trình sạch và thông tin sản phẩm rõ ràng.
            </p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">📞</div>
            <h3>Dễ đặt hàng</h3>
            <p>
                Liên hệ nhanh qua hotline hoặc Zalo.
            </p>
        </div>

    </div>

</section>
""", unsafe_allow_html=True)

# =========================
# STORY
# =========================
st.markdown("""
<section class="section story" id="cauchuyen">

    <div>
        <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80">
    </div>

    <div class="story-text">

        <p style="color:#2e7d32; font-weight:700; text-transform:uppercase;">
            Câu chuyện sản phẩm
        </p>

        <h2>
            Thức quà thanh tao của mùa thu Hà Nội
        </h2>

        <p>
            Cốm Làng Vòng không chỉ là món ăn mà còn là một phần ký ức của Hà Nội.
            Từ những hạt lúa nếp non, người thợ rang, giã và sàng sảy nhiều lần
            để tạo nên hạt cốm mỏng, dẻo và thơm.
        </p>

        <p>
            Cốm thường được gói trong lá sen để giữ hương thơm tự nhiên,
            tạo nên nét rất riêng của ẩm thực đất kinh kỳ.
        </p>

    </div>

</section>
""", unsafe_allow_html=True)

# =========================
# PRODUCT
# =========================
st.markdown("""
<section class="section" id="sanpham">

    <div class="section-title">
        <p>Sản phẩm</p>
        <h2>Những món nổi bật từ cốm</h2>
    </div>

    <div class="product-grid">

        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1606787366850-de6330128bfc?auto=format&fit=crop&w=1000&q=80">

            <div class="product-info">
                <h3>Cốm tươi</h3>

                <p>
                    Hạt cốm mềm dẻo, thơm nhẹ, phù hợp ăn trực tiếp
                    hoặc dùng làm quà biếu.
                </p>
            </div>
        </div>

        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1602663491496-73f07481dbea?auto=format&fit=crop&w=1000&q=80">

            <div class="product-info">
                <h3>Bánh cốm</h3>

                <p>
                    Món bánh truyền thống với lớp vỏ dẻo thơm
                    và nhân đậu xanh ngọt dịu.
                </p>
            </div>
        </div>

        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1000&q=80">

            <div class="product-info">
                <h3>Chả cốm</h3>

                <p>
                    Sự kết hợp giữa cốm và thịt tạo nên món ăn đậm vị,
                    quen thuộc trong bữa cơm Việt.
                </p>
            </div>
        </div>

    </div>

</section>
""", unsafe_allow_html=True)

# =========================
# TRUY XUẤT
# =========================
st.markdown("""
<section class="section" id="truyxuat">

    <div class="section-title">
        <p>Thông tin sản phẩm</p>
        <h2>Truy xuất nguồn gốc</h2>
    </div>

    <div class="trace-grid">

        <div class="trace-card">
            <h3>🌾 Nguồn nguyên liệu</h3>

            <p>
                Lúa nếp non được chọn khi hạt còn ngậm sữa,
                giúp giữ hương thơm và độ dẻo đặc trưng.
            </p>
        </div>

        <div class="trace-card">
            <h3>📍 Khu vực sản xuất</h3>

            <p>
                Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội —
                nơi nổi tiếng với nghề làm cốm truyền thống.
            </p>
        </div>

        <div class="trace-card">
            <h3>🏷️ Mã lô hàng</h3>

            <p>
                Mã lô mẫu: LV-2026-001.
                Thông tin sản xuất và hạn sử dụng được cập nhật trên bao bì.
            </p>
        </div>

    </div>

</section>
""", unsafe_allow_html=True)

# =========================
# GALLERY
# =========================
st.markdown("""
<section class="section" id="hinhanh">

    <div class="section-title">
        <p>Thư viện</p>
        <h2>Hình ảnh Cốm Làng Vòng</h2>
    </div>

    <div class="gallery">

        <img src="https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=1000&q=80">

        <img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=1000&q=80">

        <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1000&q=80">

    </div>

</section>
""", unsafe_allow_html=True)

# =========================
# CONTACT
# =========================
st.markdown("""
<section class="section contact" id="lienhe">

    <div>

        <h2>Liên hệ đặt hàng</h2>

        <p>
            Khách hàng có thể liên hệ để được tư vấn sản phẩm,
            giá bán và phương thức giao hàng.
        </p>

        <p>
            Cốm Làng Vòng phù hợp làm quà biếu,
            sử dụng trong gia đình hoặc chế biến nhiều món ăn truyền thống.
        </p>

    </div>

    <div class="contact-box">

        <h3>🌾 Cốm Làng Vòng</h3>

        <p>
            📍 Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội
        </p>

        <p>
            📞 <a href="tel:0385437503">0385 437 503</a>
        </p>

        <p>
            💬 <a href="https://zalo.me/0385437503" target="_blank">
            Chat Zalo
            </a>
        </p>

        <p>
            📘 Facebook: Cốm Làng Vòng
        </p>

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
                mang hương vị thanh tao của lúa nếp non
                và nét đẹp văn hóa ẩm thực đất kinh kỳ.
            </p>
        </div>

        <div>
            <h3>Danh mục</h3>

            <p><a href="#trangchu">Trang chủ</a></p>
            <p><a href="#cauchuyen">Câu chuyện</a></p>
            <p><a href="#sanpham">Sản phẩm</a></p>
            <p><a href="#truyxuat">Truy xuất</a></p>
        </div>

        <div>
            <h3>Liên hệ</h3>

            <p>📍 Làng Vòng, Cầu Giấy, Hà Nội</p>
            <p>📞 0385 437 503</p>
            <p>💬 Zalo: 0385 437 503</p>
        </div>

    </div>

    <div class="copy">
        © 2026 Cốm Làng Vòng. All rights reserved.
    </div>

</footer>
""", unsafe_allow_html=True)

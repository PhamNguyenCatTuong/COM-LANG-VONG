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
    justify-content: space-between;
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
    color: #333;
    font-weight: 600;
    font-size: 15px;
}

.nav a:hover {
    color: #2e7d32;
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
        flex-direction: column;
        align-items: flex-start;
        gap: 16px;
    }

    .nav {
        flex-wrap: wrap;
        gap: 12px;
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
    <div class="logo">🌾 Cốm Làng Vòng</div>

    <div class="nav">
        <a href="#trangchu" target="_self">Trang chủ</a>
        <a href="#cauchuyen" target="_self">Câu chuyện</a>
        <a href="#sanpham" target="_self">Sản phẩm</a>
        <a href="#truyxuat" target="_self">Truy xuất</a>
        <a href="#hinhanh" target="_self">Hình ảnh</a>
        <a href="#lienhe" target="_self" class="order-btn">Liên hệ</a>
    </div>
</div>
""", unsafe_allow_html=True)

# =========================
# HERO BANNER
# =========================
st.markdown("""
<section class="hero" id="trangchu">
    <div class="hero-box">
        <div class="hero-small">Đặc sản mùa thu Hà Nội</div>
        <h1>Cốm Làng Vòng</h1>
        <p>
            Hạt cốm xanh non, dẻo thơm, thanh nhẹ — thức quà truyền thống gói trọn hương vị
            tinh tế của đất kinh kỳ.
        </p>
        <div class="hero-actions">
            <a href="#sanpham" class="btn-main" target="_self">Xem sản phẩm</a>
            <a href="#lienhe" class="btn-light" target="_self">Đặt hàng ngay</a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# GIỚI THIỆU NHANH
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
            <p>Gắn với làng nghề lâu đời, mang đậm dấu ấn ẩm thực Hà Nội.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🍃</div>
            <h3>Nguyên liệu chọn lọc</h3>
            <p>Làm từ lúa nếp non, chọn đúng thời điểm để giữ độ dẻo và hương thơm.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">✅</div>
            <h3>Thông tin rõ ràng</h3>
            <p>Có thông tin sản phẩm, mã lô hàng, nguồn nguyên liệu và khu vực sản xuất.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">📞</div>
            <h3>Dễ đặt hàng</h3>
            <p>Khách hàng có thể liên hệ nhanh qua hotline hoặc Zalo.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# CÂU CHUYỆN SẢN PHẨM
# =========================
st.markdown("""
<section class="section story" id="cauchuyen">
    <div>
        <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=80">
    </div>

    <div class="story-text">
        <p style="color:#2e7d32; font-weight:700; text-transform:uppercase;">Câu chuyện sản phẩm</p>
        <h2>Thức quà thanh tao của mùa thu Hà Nội</h2>
        <p>
            Cốm Làng Vòng không chỉ là món ăn, mà còn là ký ức của Hà Nội. Từ những hạt lúa nếp non,
            người thợ rang, giã, sàng sảy nhiều lần để tạo nên hạt cốm mỏng, dẻo, thơm và có màu xanh dịu.
        </p>
        <p>
            Cốm thường được gói trong lá sen để giữ hương thơm tự nhiên. Khi thưởng thức, người ta ăn chậm,
            nhai nhẹ để cảm nhận vị ngọt thanh và hương lúa non lan dần.
        </p>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# SẢN PHẨM NỔI BẬT
# =========================
st.markdown("""
<section class="section" id="sanpham">
    <div class="section-title">
        <p>Sản phẩm</p>
        <h2>Những món từ cốm</h2>
    </div>

    <div class="product-grid">
        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1606787366850-de6330128bfc?auto=format&fit=crop&w=1000&q=80">
            <div class="product-info">
                <h3>Cốm tươi</h3>
                <p>Hạt cốm mềm dẻo, thơm nhẹ, phù hợp ăn trực tiếp hoặc dùng làm quà biếu.</p>
            </div>
        </div>

        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1602663491496-73f07481dbea?auto=format&fit=crop&w=1000&q=80">
            <div class="product-info">
                <h3>Bánh cốm</h3>
                <p>Món bánh truyền thống có vỏ dẻo thơm, nhân đậu xanh ngọt dịu.</p>
            </div>
        </div>

        <div class="product-card">
            <img src="https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1000&q=80">
            <div class="product-info">
                <h3>Chả cốm</h3>
                <p>Sự kết hợp giữa cốm và thịt tạo nên món ăn đậm vị, quen thuộc trong bữa cơm Việt.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# TRUY XUẤT NGUỒN GỐC
# =========================
st.markdown("""
<section class="section" id="truyxuat">
    <div class="section-title">
        <p>Thông tin sản phẩm</p>
        <h2>Truy xuất nguồn gốc</h2>
    </div>

    <div class="trace-box">
        <div class="trace-item">
            <h3>🌾 Nguồn nguyên liệu</h3>
            <p>Lúa nếp non chọn lọc, thu hoạch khi hạt còn ngậm sữa để giữ vị ngọt thanh và độ dẻo.</p>
        </div>

        <div class="trace-item">
            <h3>📍 Khu vực sản xuất</h3>
            <p>Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội — nơi gắn với nghề làm cốm truyền thống.</p>
        </div>

        <div class="trace-item">
            <h3>🏷️ Mã lô hàng</h3>
            <p>Mã lô mẫu: LV-2026-001. Ngày sản xuất và hạn sử dụng được cập nhật trên bao bì.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# CHẤT LƯỢNG & BAO BÌ
# =========================
st.markdown("""
<section class="section">
    <div class="section-title">
        <p>Chất lượng</p>
        <h2>Cam kết sản phẩm</h2>
    </div>

    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🏅</div>
            <h3>OCOP</h3>
            <p>Định hướng phát triển theo sản phẩm đặc trưng địa phương.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h3>Kiểm định</h3>
            <p>Chú trọng nguyên liệu rõ ràng, quy trình sạch và bảo quản đúng cách.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">📦</div>
            <h3>Bao bì</h3>
            <p>Thiết kế nhận diện xanh cốm, rõ tên sản phẩm, mã lô và thông tin liên hệ.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">♻️</div>
            <h3>Thu hồi bao bì</h3>
            <p>Khuyến khích phân loại, tái sử dụng và xử lý bao bì đúng cách.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# HÌNH ẢNH SẢN PHẨM
# =========================
st.markdown("""
<section class="section" id="hinhanh">
    <div class="section-title">
        <p>Thư viện</p>
        <h2>Hình ảnh Cốm Làng Vòng</h2>
    </div>

    <div class="gallery">
        <img src="https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=1000&q=80">
        <img src="https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1000&q=80">
        <img src="https://images.unsplash.com/photo-1464226184884-fa280b87c399?auto=format&fit=crop&w=1000&q=80">
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# LIÊN HỆ ĐẶT HÀNG
# =========================
st.markdown("""
<section class="section contact" id="lienhe">
    <div>
        <h2>Liên hệ đặt hàng</h2>
        <p>
            Khách hàng có thể liên hệ để được tư vấn sản phẩm, giá bán, đóng gói quà biếu
            và phương thức giao hàng.
        </p>
        <p>
            Cốm Làng Vòng phù hợp làm quà tặng, dùng trong gia đình hoặc chế biến thành các món ăn truyền thống.
        </p>
    </div>

    <div class="contact-card">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p>📍 Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội</p>
        <p>📞 <a href="tel:0385437503">0385 437 503</a></p>
        <p>💬 <a href="https://zalo.me/0385437503" target="_blank">Chat Zalo</a></p>
        <p>📘 Facebook: Cốm Làng Vòng</p>
    </div>
</section>
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

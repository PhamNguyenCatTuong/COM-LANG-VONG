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

    return "https://images.unsplash.com/photo-1605000797499-95a51c5269ae?auto=format&fit=crop&w=1600&q=80"


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

/* HEADER */
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

.nav a:hover {
    background: #256b29;
    color: white;
}

#menu-toggle {
    display: none;
}

.hamburger {
    display: none;
    font-size: 30px;
    cursor: pointer;
    color: #333;
}

/* HERO */
.hero {
    min-height: 620px;
    margin: 0 14px;
    border-radius: 26px;
    position: relative;
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 60px;
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

/* SECTION */
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

/* CARD */
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

/* PRODUCT */
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

/* TRACE */
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

/* STORY */
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

/* GALLERY */
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

/* FLOAT BUTTON */
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

/* FOOTER */
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

/* MOBILE */
@media (max-width: 900px) {
    .header {
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        padding: 14px 18px;
        gap: 10px;
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
    .footer-inner {
        grid-template-columns: 1fr;
    }

    .section {
        margin: 55px auto;
        padding: 0 18px;
    }

    .section-title h2 {
        font-size: 32px;
    }

    .logo {
        font-size: 25px;
    }
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER / MENU
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
# TRANG THÔNG TIN SẢN PHẨM
# =========================
if page == "thongtin":

    st.markdown(f"""
<section class="hero">
    <img src="{hero_img}" class="hero-bg">
    <div class="hero-overlay"></div>

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
<section class="section">
    <div class="section-title">
        <p>Giá trị nổi bật</p>
        <h2>Vì sao chọn Cốm Làng Vòng?</h2>
    </div>

    <div class="feature-grid">
        <div class="feature-card">
            <div class="feature-icon">🌾</div>
            <h3>Tên sản phẩm</h3>
            <p>Cốm Làng Vòng là đặc sản truyền thống của Hà Nội, nổi bật với màu xanh non và hương thơm dịu.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🏷️</div>
            <h3>Mã sản phẩm</h3>
            <p>Mã sản phẩm mẫu: COM-LV-001, giúp khách hàng dễ nhận diện và tra cứu thông tin.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🌿</div>
            <h3>Thương hiệu</h3>
            <p>Thương hiệu gắn với làng nghề lâu đời, thể hiện nét tinh tế trong văn hóa ẩm thực Hà Nội.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">📞</div>
            <h3>Dễ đặt hàng</h3>
            <p>Khách hàng có thể liên hệ nhanh qua hotline hoặc Zalo để được tư vấn.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

    st.markdown(f"""
<section class="section">
    <div class="section-title">
        <p>Sản phẩm</p>
        <h2>Những món từ cốm</h2>
    </div>

    <div class="product-grid">
        <div class="product-card">
            <img src="{img_1}">
            <div class="product-info">
                <h3>Cốm tươi</h3>
                <p>Hạt cốm mềm dẻo, thơm nhẹ, phù hợp ăn trực tiếp hoặc dùng làm quà biếu.</p>
            </div>
        </div>

        <div class="product-card">
            <img src="{img_2}">
            <div class="product-info">
                <h3>Bánh cốm</h3>
                <p>Món bánh truyền thống có vỏ dẻo thơm, nhân đậu xanh ngọt dịu.</p>
            </div>
        </div>

        <div class="product-card">
            <img src="{img_3}">
            <div class="product-info">
                <h3>Chả cốm</h3>
                <p>Sự kết hợp giữa cốm và thịt tạo nên món ăn đậm vị, quen thuộc trong bữa cơm Việt.</p>
            </div>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# TRANG TRUY XUẤT
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
# TRANG CHẤT LƯỢNG
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
            <h3>Chứng nhận OCOP</h3>
            <p>Sản phẩm phù hợp định hướng phát triển theo nhóm đặc sản địa phương.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🔍</div>
            <h3>Kiểm định chất lượng</h3>
            <p>Chú trọng nguyên liệu rõ nguồn gốc, quy trình sạch và bảo quản đúng cách.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">✅</div>
            <h3>An toàn sản phẩm</h3>
            <p>Sản phẩm cần được đóng gói sạch, hạn chế tiếp xúc trực tiếp với môi trường bên ngoài.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🍃</div>
            <h3>Hương vị tự nhiên</h3>
            <p>Giữ hương thơm lúa non, vị ngọt thanh và độ dẻo đặc trưng của cốm.</p>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# TRANG TRUYỀN THÔNG
# =========================
elif page == "truyenthong":

    st.markdown(f"""
<section class="section story">
    <div>
        <img src="{img_4}">
    </div>

    <div class="story-text">
        <p style="color:#2e7d32; font-weight:700; text-transform:uppercase;">Câu chuyện sản phẩm</p>
        <h2>Thức quà thanh tao của mùa thu Hà Nội</h2>
        <p>
            Cốm Làng Vòng không chỉ là món ăn, mà còn là ký ức của Hà Nội.
            Từ những hạt lúa nếp non, người thợ rang, giã, sàng sảy nhiều lần để tạo nên hạt cốm mỏng, dẻo, thơm.
        </p>
        <p>
            Cốm thường được gói trong lá sen để giữ hương thơm tự nhiên.
            Khi thưởng thức, người ta ăn chậm để cảm nhận vị ngọt thanh và hương lúa non.
        </p>
    </div>
</section>
""", unsafe_allow_html=True)

    st.markdown(f"""
<section class="section">
    <div class="section-title">
        <p>Thư viện</p>
        <h2>Hình ảnh Cốm Làng Vòng</h2>
    </div>

    <div class="gallery">
        <img src="{img_1}">
        <img src="{img_2}">
        <img src="{img_3}">
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# TRANG BAO BÌ
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
            <p>Mực in cần rõ nét, bền màu và phù hợp với bao bì thực phẩm.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">📦</div>
            <h3>Giấy bao bì</h3>
            <p>Bao bì cần sạch, chắc chắn, giúp hạn chế ẩm và bảo vệ sản phẩm khi vận chuyển.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">♻️</div>
            <h3>Thu hồi bao bì</h3>
            <p>Khuyến khích phân loại, tái sử dụng và xử lý bao bì đúng cách sau khi dùng.</p>
        </div>

        <div class="feature-card">
            <div class="feature-icon">🌿</div>
            <h3>Thiết kế nhận diện</h3>
            <p>Có thể sử dụng màu xanh cốm, họa tiết lá sen để tăng tính nhận diện thương hiệu.</p>
        </div>
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
# FOOTER
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
            <p><a href="?page=thongtin" target="_self">Thông tin sản phẩm</a></p>
            <p><a href="?page=truyxuat" target="_self">Truy xuất nguồn gốc</a></p>
            <p><a href="?page=chatluong" target="_self">Chất lượng & chứng nhận</a></p>
            <p><a href="?page=truyenthong" target="_self">Nội dung truyền thông</a></p>
            <p><a href="?page=baobi" target="_self">Thông tin bao bì</a></p>
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

import streamlit as st

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Trang mặc định khi mở link / quét mã QR
page = st.query_params.get("page", "thong-tin-san-pham")

PAGES = {
    "thong-tin-san-pham": "Thông tin sản phẩm",
    "truy-xuat": "Truy xuất nguồn gốc",
    "truyen-thong": "Nội dung truyền thống",
    "chat-luong": "Chất lượng & chứng nhận",
    "bao-bi": "Bao bì",
    "lien-he": "Thông tin liên hệ",
}

if page not in PAGES:
    page = "thong-tin-san-pham"

BANNER_IMAGE = "https://images.unsplash.com/photo-1536304993881-ff6e9eefa2a6?auto=format&fit=crop&w=2200&q=90"

# =========================
# CSS GIAO DIỆN WEBSITE
# =========================
st.markdown(f"""
<style>

#MainMenu {{visibility: hidden;}}
header {{visibility: hidden;}}
footer {{visibility: hidden;}}
[data-testid="stToolbar"] {{display: none !important;}}
[data-testid="stDecoration"] {{display: none !important;}}
[data-testid="stStatusWidget"] {{display: none !important;}}

html {{
    scroll-behavior: smooth;
    overflow-x: hidden;
}}

body {{
    margin: 0;
    padding: 0;
    background: #fffdf7;
    overflow-x: hidden;
}}

* {{
    box-sizing: border-box;
}}

.block-container {{
    padding: 0 !important;
    max-width: 100% !important;
    overflow-x: hidden;
}}

/* =========================
HEADER / MENU 2 GẠCH
========================= */
.header {{
    position: sticky;
    top: 0;
    z-index: 999;
    background: white;
    margin: 14px;
    padding: 14px 22px;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    display: flex;
    align-items: center;
    justify-content: space-between;
}}

.logo {{
    font-size: 26px;
    font-weight: 800;
    color: #2e7d32;
    white-space: nowrap;
}}

.menu-wrap {{
    position: relative;
}}

.menu-wrap summary {{
    list-style: none;
    cursor: pointer;
    width: 46px;
    height: 40px;
    border-radius: 12px;
    background: #2e7d32;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 7px;
    padding: 0 10px;
}}

.menu-wrap summary::-webkit-details-marker {{
    display: none;
}}

.menu-wrap summary span {{
    display: block;
    height: 3px;
    background: white;
    border-radius: 10px;
}}

.menu-panel {{
    position: absolute;
    right: 0;
    top: 54px;
    width: 340px;
    max-width: calc(100vw - 28px);
    background: #542354;
    color: white;
    border-radius: 20px;
    padding: 18px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.22);
}}

.menu-group {{
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.35);
}}

.menu-group:last-child {{
    border-bottom: none;
}}

.menu-title {{
    display: block;
    color: white !important;
    text-decoration: none;
    font-size: 18px;
    font-weight: 800;
    text-transform: uppercase;
    margin-bottom: 8px;
}}

.sub-menu {{
    display: grid;
    gap: 5px;
    padding-left: 12px;
}}

.sub-menu a {{
    color: rgba(255,255,255,0.92) !important;
    text-decoration: none;
    font-size: 15px;
}}

.sub-menu a:hover,
.menu-title:hover {{
    color: #f7d77b !important;
}}

/* =========================
HERO BANNER
========================= */
.hero {{
    min-height: 620px;
    margin: 0 14px;
    border-radius: 26px;
    background:
        linear-gradient(rgba(0,0,0,0.25), rgba(0,0,0,0.45)),
        url("{BANNER_IMAGE}");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: flex-end;
    padding: 60px;
    color: white;
}}

.hero-box {{
    max-width: 650px;
    background: rgba(0,0,0,0.28);
    padding: 24px 28px;
    border-radius: 22px;
    backdrop-filter: blur(2px);
}}

.hero-small {{
    font-size: 16px;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 8px;
}}

.hero h1 {{
    font-size: 58px;
    line-height: 1.05;
    margin: 0 0 10px 0;
}}

.hero p {{
    font-size: 19px;
    line-height: 1.45;
    margin: 0 0 20px 0;
}}

.hero-actions {{
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}}

.btn-main,
.btn-light {{
    padding: 13px 22px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
}}

.btn-main {{
    background: #2e7d32;
    color: white !important;
}}

.btn-light {{
    background: white;
    color: #2e7d32 !important;
}}

/* =========================
SECTION CHUNG
========================= */
.section {{
    max-width: 1180px;
    margin: 70px auto;
    padding: 0 28px;
}}

.section-title {{
    text-align: center;
    margin-bottom: 34px;
}}

.section-title p {{
    color: #2e7d32;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 8px;
}}

.section-title h2 {{
    font-size: 42px;
    margin: 0;
    color: #222;
}}

.feature-grid,
.product-grid,
.trace-box,
.gallery {{
    display: grid;
    gap: 22px;
}}

.feature-grid {{
    grid-template-columns: repeat(4, 1fr);
}}

.product-grid,
.trace-box,
.gallery {{
    grid-template-columns: repeat(3, 1fr);
}}

.feature-card,
.product-card,
.trace-item,
.contact-card {{
    background: white;
    border-radius: 20px;
    box-shadow: 0 6px 22px rgba(0,0,0,0.08);
}}

.feature-card,
.trace-item,
.contact-card {{
    padding: 26px;
}}

.feature-card {{
    text-align: center;
}}

.feature-icon {{
    font-size: 42px;
    margin-bottom: 12px;
}}

.feature-card h3,
.product-info h3,
.trace-item h3,
.contact-card h3 {{
    color: #2e7d32;
    margin-top: 0;
}}

.feature-card p,
.product-info p,
.trace-item p {{
    color: #555;
    line-height: 1.7;
}}

.product-card {{
    overflow: hidden;
}}

.product-card img,
.gallery img {{
    width: 100%;
    object-fit: cover;
}}

.product-card img {{
    height: 230px;
}}

.product-info {{
    padding: 22px;
}}

.gallery img {{
    height: 260px;
    border-radius: 20px;
}}

.story {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 45px;
    align-items: center;
}}

.story img {{
    width: 100%;
    border-radius: 24px;
    box-shadow: 0 8px 26px rgba(0,0,0,0.12);
}}

.story-text h2 {{
    font-size: 40px;
    color: #222;
    margin-bottom: 18px;
}}

.story-text p {{
    line-height: 1.85;
    color: #444;
    font-size: 17px;
}}

.contact {{
    background: #2e7d32;
    color: white;
    border-radius: 28px;
    padding: 50px;
    display: grid;
    grid-template-columns: 1.3fr 1fr;
    gap: 30px;
    align-items: center;
}}

.contact h2 {{
    font-size: 40px;
    margin-top: 0;
}}

.contact p {{
    font-size: 17px;
    line-height: 1.8;
}}

.contact-card {{
    color: #222;
    min-height: 260px;
    display: block;
}}

.contact-card p {{
    color: #333;
    margin: 11px 0;
}}

.contact-card a {{
    color: #2e7d32 !important;
    font-weight: 700;
    text-decoration: none;
}}

.floating-contact {{
    position: fixed;
    bottom: 28px;
    right: 18px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 9999;
}}

.float-btn {{
    width: 52px;
    height: 52px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: white !important;
    font-size: 24px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25);
}}

.call-btn {{background: #2e7d32;}}
.zalo-btn {{background: #0084ff;}}

.footer {{
    background: #111;
    color: white;
    padding: 45px 28px;
    margin-top: 80px;
}}

.footer-inner {{
    max-width: 1180px;
    margin: auto;
    display: grid;
    grid-template-columns: 1.5fr 1fr 1fr;
    gap: 28px;
}}

.footer h3 {{color: white;}}

.footer p,
.footer a {{
    color: #ddd !important;
    text-decoration: none;
    line-height: 1.8;
}}

.copy {{
    text-align: center;
    color: #aaa;
    margin-top: 35px;
    font-size: 14px;
}}

/* =========================
MOBILE
========================= */
@media (max-width: 900px) {{
    html,
    body {{
        width: 100%;
        max-width: 100%;
        overflow-x: hidden;
    }}

    .header {{
        margin: 10px;
        padding: 12px 14px;
    }}

    .logo {{
        font-size: 21px;
    }}

    .hero {{
        min-height: 560px;
        margin: 0 10px;
        padding: 18px;
        align-items: flex-end;
        background-position: center;
    }}

    .hero-box {{
        max-width: 82%;
        padding: 14px 16px;
        border-radius: 16px;
    }}

    .hero-small {{
        font-size: 11px;
        line-height: 1.15;
        letter-spacing: 1px;
        margin-bottom: 5px;
    }}

    .hero h1 {{
        font-size: 29px;
        line-height: 1;
        margin-bottom: 6px;
    }}

    .hero p {{
        font-size: 13px;
        line-height: 1.28;
        margin-bottom: 10px;
    }}

    .btn-main,
    .btn-light {{
        padding: 9px 13px;
        font-size: 13px;
    }}

    .feature-grid,
    .product-grid,
    .trace-box,
    .gallery,
    .story,
    .contact,
    .footer-inner {{
        grid-template-columns: 1fr;
    }}

    .section {{
        margin: 50px auto;
        padding: 0 18px;
    }}

    .section-title h2 {{
        font-size: 30px;
    }}

    .contact {{
        padding: 30px 20px;
    }}

    .contact h2 {{
        font-size: 30px;
    }}
}}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER / MENU WEBSITE
# =========================
def change_page(page_key):
    st.query_params["page"] = page_key
    st.rerun()

st.markdown("""
<style>
.menu-top-row {
    position: sticky;
    top: 0;
    z-index: 999;
    background: white;
    margin: 14px;
    padding: 14px 22px;
    border-radius: 18px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
}
.menu-label {
    font-size: 26px;
    font-weight: 800;
    color: #2e7d32;
    white-space: nowrap;
    padding-top: 7px;
}
div[data-testid="stPopover"] button {
    background: #2e7d32 !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: 800 !important;
    min-height: 42px !important;
}
div[data-testid="stPopoverBody"] {
    background: #542354;
    border-radius: 18px;
    padding: 16px;
}
div[data-testid="stPopoverBody"] p,
div[data-testid="stPopoverBody"] label {
    color: white !important;
}
div[data-testid="stPopoverBody"] .stButton button {
    width: 100%;
    background: transparent !important;
    color: white !important;
    border: 1px solid rgba(255,255,255,0.28) !important;
    border-radius: 12px !important;
    text-align: left !important;
    justify-content: flex-start !important;
    margin-bottom: 4px;
}
div[data-testid="stPopoverBody"] .stButton button:hover {
    border-color: #f7d77b !important;
    color: #f7d77b !important;
}
.menu-main-text {
    color: white;
    font-size: 17px;
    font-weight: 800;
    text-transform: uppercase;
    margin: 12px 0 5px 0;
}
.menu-sub-text {
    color: rgba(255,255,255,0.85);
    font-size: 13px;
    margin: -2px 0 6px 0;
}
@media (max-width: 900px) {
    .menu-top-row { margin: 10px; padding: 12px 14px; }
    .menu-label { font-size: 21px; padding-top: 8px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="menu-top-row">', unsafe_allow_html=True)
menu_col_1, menu_col_2 = st.columns([0.78, 0.22], vertical_alignment="center")
with menu_col_1:
    st.markdown('<div class="menu-label">🌾 Cốm Làng Vòng</div>', unsafe_allow_html=True)
with menu_col_2:
    with st.popover("☰ Menu", use_container_width=True):
        st.markdown('<div class="menu-main-text">Thông tin sản phẩm</div><div class="menu-sub-text">Tên sản phẩm · Mã sản phẩm · Thương hiệu</div>', unsafe_allow_html=True)
        if st.button("Mở trang Thông tin sản phẩm", key="menu_thong_tin", use_container_width=True):
            change_page("thong-tin-san-pham")

        st.markdown('<div class="menu-main-text">Truy xuất nguồn gốc</div><div class="menu-sub-text">Nguồn nguyên liệu · Khu vực sản xuất · Mã lô hàng</div>', unsafe_allow_html=True)
        if st.button("Mở trang Truy xuất nguồn gốc", key="menu_truy_xuat", use_container_width=True):
            change_page("truy-xuat")

        st.markdown('<div class="menu-main-text">Nội dung truyền thống</div><div class="menu-sub-text">Câu chuyện sản phẩm · Hình ảnh · Video giới thiệu</div>', unsafe_allow_html=True)
        if st.button("Mở trang Nội dung truyền thống", key="menu_truyen_thong", use_container_width=True):
            change_page("truyen-thong")

        st.markdown('<div class="menu-main-text">Chất lượng & chứng nhận</div><div class="menu-sub-text">Chứng nhận OCOP · Kiểm định chất lượng</div>', unsafe_allow_html=True)
        if st.button("Mở trang Chất lượng & chứng nhận", key="menu_chat_luong", use_container_width=True):
            change_page("chat-luong")

        st.markdown('<div class="menu-main-text">Bao bì</div><div class="menu-sub-text">Mực · Giấy · Thời gian thu hồi</div>', unsafe_allow_html=True)
        if st.button("Mở trang Bao bì", key="menu_bao_bi", use_container_width=True):
            change_page("bao-bi")

        st.markdown('<div class="menu-main-text">Thông tin liên hệ</div><div class="menu-sub-text">Website · Hotline · Mạng xã hội</div>', unsafe_allow_html=True)
        if st.button("Mở trang Thông tin liên hệ", key="menu_lien_he", use_container_width=True):
            change_page("lien-he")
st.markdown('</div>', unsafe_allow_html=True)

# =========================
# HERO BANNER
# =========================
st.markdown("""
<section class="hero">
    <div class="hero-box">
        <div class="hero-small">Đặc sản mùa thu Hà Nội</div>
        <h1>Cốm Làng Vòng</h1>
        <p>
            Hạt cốm xanh non, dẻo thơm, thanh nhẹ — thức quà truyền thống gói trọn hương vị
            tinh tế của đất kinh kỳ.
        </p>
        <div class="hero-actions">
            <a href="?page=thong-tin-san-pham" class="btn-main" target="_self">Thông tin sản phẩm</a>
            <a href="?page=lien-he" class="btn-light" target="_self">Liên hệ đặt hàng</a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

# =========================
# 6 TRANG RIÊNG THEO MENU LỚN
# =========================
if page == "thong-tin-san-pham":
    st.markdown("""
    <section class="section" id="ten-san-pham">
        <div class="section-title">
            <p>Thông tin sản phẩm</p>
            <h2>Cốm Làng Vòng</h2>
        </div>

        <div class="product-grid">
            <div class="trace-item" id="ten-san-pham">
                <h3>🌾 Tên sản phẩm</h3>
                <p>Cốm Làng Vòng — đặc sản truyền thống Hà Nội, làm từ lúa nếp non.</p>
            </div>

            <div class="trace-item" id="ma-san-pham">
                <h3>🏷️ Mã sản phẩm</h3>
                <p>COM-LV-001. Mã có thể dùng để in trên tem, bao bì hoặc mã QR truy xuất.</p>
            </div>

            <div class="trace-item" id="thuong-hieu">
                <h3>✅ Thương hiệu</h3>
                <p>Cốm Làng Vòng — nhận diện xanh cốm, gắn với văn hóa ẩm thực Hà Nội.</p>
            </div>
        </div>
    </section>

    <section class="section">
        <div class="section-title">
            <p>Sản phẩm</p>
            <h2>Những món từ cốm</h2>
        </div>

        <div class="product-grid">
            <div class="product-card">
                <img src="https://langcomvong.com/uploads/images/com-lang-vong%281%29.jpg">
                <div class="product-info">
                    <h3>Cốm tươi</h3>
                    <p>Hạt cốm mềm dẻo, thơm nhẹ, phù hợp ăn trực tiếp hoặc dùng làm quà biếu.</p>
                </div>
            </div>

            <div class="product-card">
                <img src="https://langcomvong.com/uploads/images/banh-com.jpg">
                <div class="product-info">
                    <h3>Bánh cốm</h3>
                    <p>Món bánh truyền thống có vỏ dẻo thơm, nhân đậu xanh ngọt dịu.</p>
                </div>
            </div>

            <div class="product-card">
                <img src="https://langcomvong.com/uploads/images/cha-com.jpg">
                <div class="product-info">
                    <h3>Chả cốm</h3>
                    <p>Sự kết hợp giữa cốm và thịt tạo nên món ăn đậm vị, quen thuộc trong bữa cơm Việt.</p>
                </div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

elif page == "truy-xuat":
    st.markdown("""
    <section class="section">
        <div class="section-title">
            <p>Thông tin sản phẩm</p>
            <h2>Truy xuất nguồn gốc</h2>
        </div>

        <div class="trace-box">
            <div class="trace-item" id="nguon-nguyen-lieu">
                <h3>🌾 Nguồn nguyên liệu</h3>
                <p>Lúa nếp non chọn lọc, thu hoạch khi hạt còn ngậm sữa để giữ vị ngọt thanh và độ dẻo.</p>
            </div>

            <div class="trace-item" id="khu-vuc-san-xuat">
                <h3>📍 Khu vực sản xuất</h3>
                <p>Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội — nơi gắn với nghề làm cốm truyền thống.</p>
            </div>

            <div class="trace-item" id="ma-lo-hang">
                <h3>🏷️ Mã lô hàng</h3>
                <p>Mã lô mẫu: LV-2026-001. Ngày sản xuất và hạn sử dụng được cập nhật trên bao bì.</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

elif page == "truyen-thong":
    st.markdown("""
    <section class="section story" id="cau-chuyen">
        <div>
            <img src="https://langcomvong.com/uploads/images/com-lang-vong%281%29.jpg">
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

    <section class="section" id="hinh-anh">
        <div class="section-title">
            <p>Thư viện</p>
            <h2>Hình ảnh Cốm Làng Vòng</h2>
        </div>

        <div class="gallery">
            <img src="https://langcomvong.com/uploads/images/com-lang-vong%281%29.jpg">
            <img src="https://langcomvong.com/uploads/images/com-tuoi.jpg">
            <img src="https://langcomvong.com/uploads/images/xoi-com.jpg">
        </div>
    </section>

    <section class="section" id="video">
        <div class="section-title">
            <p>Video giới thiệu</p>
            <h2>Không gian dành cho video sản phẩm</h2>
        </div>
        <div class="trace-item">
            <p>Có thể gắn video giới thiệu quy trình làm cốm, đóng gói sản phẩm hoặc hướng dẫn quét mã truy xuất tại đây.</p>
        </div>
    </section>
    """, unsafe_allow_html=True)

elif page == "chat-luong":
    st.markdown("""
    <section class="section">
        <div class="section-title">
            <p>Chất lượng</p>
            <h2>Chất lượng & chứng nhận</h2>
        </div>

        <div class="feature-grid">
            <div class="feature-card" id="ocop">
                <div class="feature-icon">🏅</div>
                <h3>Chứng nhận OCOP</h3>
                <p>Định hướng phát triển theo sản phẩm đặc trưng địa phương.</p>
            </div>

            <div class="feature-card" id="kiem-dinh">
                <div class="feature-icon">🔍</div>
                <h3>Kiểm định chất lượng</h3>
                <p>Chú trọng nguyên liệu rõ ràng, quy trình sạch và bảo quản đúng cách.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">✅</div>
                <h3>Thông tin rõ ràng</h3>
                <p>Có thông tin sản phẩm, mã lô hàng, nguồn nguyên liệu và khu vực sản xuất.</p>
            </div>

            <div class="feature-card">
                <div class="feature-icon">🍃</div>
                <h3>Nguyên liệu chọn lọc</h3>
                <p>Làm từ lúa nếp non, chọn đúng thời điểm để giữ độ dẻo và hương thơm.</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

elif page == "bao-bi":
    st.markdown("""
    <section class="section">
        <div class="section-title">
            <p>Bao bì</p>
            <h2>Thông tin bao bì sản phẩm</h2>
        </div>

        <div class="trace-box">
            <div class="trace-item" id="muc">
                <h3>🖨️ Mực</h3>
                <p>Ưu tiên mực in rõ nét, bền màu, phù hợp thông tin tem nhãn, mã QR và nhận diện thương hiệu.</p>
            </div>

            <div class="trace-item" id="giay">
                <h3>📄 Giấy</h3>
                <p>Sử dụng giấy bao bì có độ cứng phù hợp, dễ in thông tin sản phẩm, hướng đến khả năng tái chế.</p>
            </div>

            <div class="trace-item" id="thoi-gian-thu-hoi">
                <h3>♻️ Thời gian thu hồi</h3>
                <p>Khuyến khích thu hồi hoặc phân loại bao bì sau khi sử dụng. Thời gian thu hồi dự kiến có thể cập nhật theo từng chương trình.</p>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

elif page == "lien-he":
    st.markdown("""
    <section class="section contact">
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
            <p id="website">🌐 Website: comlangvong.vn</p>
            <p id="hotline">📞 Hotline: <a href="tel:0385437503">0385 437 503</a></p>
            <p>💬 Zalo: <a href="https://zalo.me/0385437503" target="_blank">0385 437 503</a></p>
            <p id="mang-xa-hoi">📘 Facebook: Cốm Làng Vòng</p>
            <p>📍 Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội</p>
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
            <p><a href="?page=thong-tin-san-pham" target="_self">Thông tin sản phẩm</a></p>
            <p><a href="?page=truy-xuat" target="_self">Truy xuất nguồn gốc</a></p>
            <p><a href="?page=truyen-thong" target="_self">Nội dung truyền thống</a></p>
            <p><a href="?page=bao-bi" target="_self">Bao bì</a></p>
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

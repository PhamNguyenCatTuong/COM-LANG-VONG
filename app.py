import base64
import json
import mimetypes
import sqlite3
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CỐM LÀNG VÒNG", layout="wide")

params = st.query_params
page = params.get("page", "thongtinsp")

APP_DIR = Path(__file__).resolve().parent


def resolve_asset_path(file_name):
    """Return absolute path for an image placed next to app.py."""
    return APP_DIR / file_name


def image_to_data_uri(file_name):
    """Convert local image file to data URI for HTML components."""
    image_path = resolve_asset_path(file_name)

    if not image_path.exists():
        return file_name

    mime_type, _ = mimetypes.guess_type(image_path.name)
    mime_type = mime_type or "image/jpeg"
    encoded = base64.b64encode(image_path.read_bytes()).decode("utf-8")

    return f"data:{mime_type};base64,{encoded}"


CERTIFICATES = [
    {
        "image": 'CBSP.jpg',
        "title": 'Tự công bố sản phẩm',
        "desc": 'Giấy xác nhận tự công bố sản phẩm Cốm Làng Vòng theo quy định an toàn thực phẩm.',
    },
    {
        "image": 'KQKN.jpg',
        "title": 'Phiếu kiểm nghiệm',
        "desc": 'Kết quả kiểm nghiệm các chỉ tiêu an toàn thực phẩm của sản phẩm.',
    },
    {
        "image": 'OCOP.JPEG',
        "title": 'Chứng nhận OCOP 4 sao',
        "desc": 'Chứng nhận sản phẩm OCOP đạt 4 sao năm 2022.',
    },
    {
        "image": 'HACCP.JPEG',
        "title": 'Chứng nhận HACCP',
        "desc": 'Chứng nhận hệ thống phân tích mối nguy và kiểm soát điểm tới hạn.',
    },
    {
        "image": 'GMP.jpg',
        "title": 'Chứng nhận GMP',
        "desc": 'Chứng nhận thực hành sản xuất tốt trong sản xuất thực phẩm.',
    },
    {
        "image": 'ATTP.JPEG',
        "title": 'Chứng nhận an toàn thực phẩm',
        "desc": 'Chứng nhận cơ sở đủ điều kiện an toàn thực phẩm.',
    },
]

banner_image = image_to_data_uri("Banner com.jpg")

st.markdown("""
<style>
* { box-sizing: border-box; }
html, body { margin: 0; padding: 0; overflow-x: hidden; }
img { max-width: 100%; height: auto; }

#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}

.block-container {
    max-width: 1180px !important;
    padding-left: clamp(8px, 2vw, 16px) !important;
    padding-right: clamp(8px, 2vw, 16px) !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    overflow-x: hidden;
}

.topbar {
    position: relative;
    background: white;
    padding: clamp(10px, 2vw, 15px);
    border-radius: 15px;
    margin: 10px auto;
    width: 100%;
    z-index: 999;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.top-row { display: flex; justify-content: space-between; align-items: center; gap: 10px; }
.logo {
    font-size: clamp(32px, 8vw, 48px);
    font-weight: 900;
    color: #2e7d32;
    white-space: nowrap;
}
.hamburger { font-size: clamp(22px, 5vw, 28px); cursor: pointer; }
#menu-toggle { display: none; }
.menu { display: none; flex-direction: column; gap: 5px; margin-top: 10px; }
#menu-toggle:checked ~ .menu { display: flex; }
.dropdown { position: relative; background: white; border-radius: 8px; overflow: hidden; }
.dropbtn {
    background: #2e7d32; color: white; border: none; cursor: pointer;
    width: 100%; text-align: left; border-radius: 8px 8px 0 0;
    font-size: clamp(12px, 3.1vw, 15px); padding: clamp(7px, 1.9vw, 10px) 12px;
}
.dropdown-content { display: none; background: white; min-width: 230px; border-radius: 0 0 8px 8px; overflow: hidden; box-shadow: 0 4px 10px rgba(0,0,0,0.12); z-index: 9999; }
.dropdown-content a { display: block; padding: clamp(6px, 1.8vw, 11px) 12px; text-decoration: none; color: #333; border-bottom: 1px solid #eee; font-size: clamp(11px, 2.9vw, 14px); line-height: 1.15; }
.dropdown-content a:hover { background: #f1f8e9; }
.dropdown:hover .dropdown-content { display: block; }

.hero-banner {
    width: 100%;
    min-height: clamp(290px, 58vw, 470px);
    border-radius: clamp(16px, 4vw, 22px);
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: center;
    background:
        linear-gradient(90deg, rgba(0,0,0,0.68) 0%, rgba(0,0,0,0.42) 44%, rgba(0,0,0,0.08) 100%),
        url("__BANNER_IMAGE__");
    background-size: cover;
    background-position: center;
    margin: 12px auto 0 auto;
}
.hero-content {
    width: min(48%, 560px);
    padding-left: clamp(24px, 6vw, 60px);
    padding-right: 6px;
    padding-top: 120px;
    color: white;
}
.hero-small { font-size: clamp(9px, 2.5vw, 17px); font-weight: 700; letter-spacing: clamp(0.7px, 0.25vw, 1.8px); text-transform: uppercase; margin-bottom: -6px; line-height: 1; white-space: nowrap; }
.hero-content h1 { font-size: clamp(28px, 8.2vw, 56px); line-height: 1.04; margin: 0 0 -15px 0; }
.hero-content p { font-size: clamp(12px, 3.4vw, 20px); line-height: 1.32; margin: 0 0 clamp(12px, 3vw, 18px) 0; }
.hero-actions { display: flex; gap: clamp(7px, 2vw, 12px); flex-wrap: nowrap; }
.hero-btn {
    padding: 16px 32px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 800;
    display: inline-block;
    font-size: 18px;
    white-space: nowrap;
}
.hero-btn.order { background: #2e7d32; color: white; }
.hero-btn.call { background: white; color: #2e7d32; }

.content { max-width: 850px; margin: auto; padding: clamp(12px, 3vw, 20px); line-height: 1.75; font-size: clamp(14px, 3vw, 16px); overflow-x: hidden; }
.page-title { text-align: center; font-size: clamp(17px, 4.2vw, 34px); line-height: 1.2; margin: clamp(14px, 4vw, 24px) auto clamp(10px, 3vw, 18px) auto; white-space: normal; max-width: 100%; overflow-wrap: normal; }
.page-title.small-title {
    font-size: clamp(18px, 4vw, 30px);
}

.card, .card2 { padding: clamp(14px, 3vw, 20px); border-radius: 14px; margin-top: 18px; overflow-wrap: anywhere; }
.card { background: #f1f8e9; }
.card2 { background: #e8f5e9; }
.card h3, .card2 h3 { font-size: clamp(17px, 4vw, 22px); line-height: 1.25; margin-top: 0; }

.floating-contact { position: fixed; bottom: 50px; right: clamp(8px, 2vw, 15px); display: flex; flex-direction: column; gap: 10px; z-index: 9999; }
.float-btn { width: clamp(40px, 10vw, 48px); height: clamp(40px, 10vw, 48px); border-radius: 50%; display: flex; justify-content: center; align-items: center; text-decoration: none; color: white; font-size: clamp(18px, 5vw, 22px); box-shadow: 0 4px 10px rgba(0,0,0,0.2); }
.call-btn { background: #2e7d32; }
.zalo-btn { background: #0084ff; }
.footer-full { width: 100%; background: #000; color: white; padding: 10px; margin-top: 40px; border-radius: 0; }
.footer-content { max-width: 850px; margin: auto; text-align: center; }
.footer-content a { color: white; text-decoration: none; }

/* ===== PRODUCT ===== */

.product-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 22px;
    margin-top: 20px;
}

.product-card {
    background: white;
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    display: flex;
    flex-direction: column;
    height: 100%;
}

.product-card img {
    width: 100%;
    height: 260px;
    object-fit: cover;
}

.product-info {
    padding: 16px;
    display: flex;
    flex-direction: column;
    flex: 1;
}

.product-info h3 {
    margin: 0 0 8px 0;
    color: #1f2937;
    font-size: 20px;
}

.product-info p {
    font-size: 14px;
    line-height: 1.45;
}

.product-weight {
    margin-top: auto;
}

.product-price {
    font-size: 24px;
    font-weight: 900;
    color: #1f2937;
    margin: 8px 0 12px;
}

.buy-btn {
    width: fit-content;
    background: #2e7d32;
    color: white !important;
    padding: 10px 20px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 800;
}

@media (min-width: 768px) {
    .topbar { display: flex; align-items: center; gap: 20px; }
    .hamburger { display: none; }
    .menu { display: flex !important; flex-direction: row; flex-wrap: wrap; margin-top: 0; }
    .dropbtn { width: auto; text-align: center; border-radius: 8px; } 
    .dropdown-content { position: absolute; border-radius: 10px; }
}

@media (max-width: 768px) {
    .logo {
        font-size: 34px;
    }
    .block-container { max-width: 100% !important; }
    .topbar { margin: 6px auto; padding: 10px; }
    .dropdown-content { display: block !important; position: relative; width: 100%; min-width: 0; box-shadow: none; }
    .hero-banner { min-height: clamp(300px, 86vw, 380px); margin-top: 10px; }
    .hero-content {
        width: 72%;
        padding-left: 22px;
        padding-top: 140px;
    }
    .hero-content h1 {
        font-size: clamp(34px, 9vw, 48px);
        white-space: nowrap;
        line-height: 1;
    }
    .hero-content p { font-size: clamp(12px, 3.4vw, 14px); }
    .hero-btn {
        padding: 14px 24px;
        font-size: 16px;
    }
    .page-title {
        font-size: clamp(16px, 4.1vw, 19px);
        white-space: nowrap;
    }
    .page-title.small-title {
        font-size: 35px !important;
        white-space: nowrap;
        letter-spacing: 0;
        width: 100%;
        text-align: center !important;
        margin-left: auto !important;
        margin-right: auto !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
        left: 0;
        right: 0;
        position: relative;
    }
    .product-grid {
        grid-template-columns: 1fr;
    }

    .product-card img {
        height: 230px;
    }
}
}
</style>
""".replace("__BANNER_IMAGE__", image_to_data_uri("Banner com.jpg")), unsafe_allow_html=True)

st.markdown("""
<div class="topbar">
<input type="checkbox" id="menu-toggle">
<div class="top-row">
    <div class="logo">🌾 Cốm Làng Vòng</div>
    <label for="menu-toggle" class="hamburger">☰</label>
</div>
<div class="menu">
<div class="dropdown">
    <a href="?page=thongtinsp" target="_self" style="text-decoration:none;"><button class="dropbtn">Thông tin sản phẩm</button></a>
    <div class="dropdown-content">
        <a href="?page=tensp_masp" target="_self">Tên & mã sản phẩm</a>
        <a href="?page=thuonghieu" target="_self">Thương hiệu</a>
        <a href="?page=sanpham" target="_self">Sản phẩm</a>
    </div>
</div>
<div class="dropdown">
    <a href="?page=truyxuat" target="_self" style="text-decoration:none;"><button class="dropbtn">Truy xuất nguồn gốc</button></a>
    <div class="dropdown-content">
        <a href="?page=nguyenlieu" target="_self">Nguồn nguyên liệu</a>
        <a href="?page=khuvuc" target="_self">Khu vực sản xuất</a>
        <a href="?page=malo" target="_self">Mã lô hàng</a>
    </div>
</div>
<div class="dropdown">
    <a href="?page=chatluong" target="_self" style="text-decoration:none;"><button class="dropbtn">Chất lượng & chứng nhận</button></a>
</div>
<div class="dropdown">
    <a href="?page=truyenthong" target="_self" style="text-decoration:none;"><button class="dropbtn">Nội dung truyền thông</button></a>
    <div class="dropdown-content">
        <a href="?page=cauchuyen" target="_self">Câu chuyện sản phẩm</a>
        <a href="?page=video" target="_self">Video giới thiệu</a>
    </div>
</div>
<div class="dropdown">
    <a href="?page=baobi" target="_self" style="text-decoration:none;"><button class="dropbtn">Thông tin bao bì</button></a>
    <div class="dropdown-content">
        <a href="?page=muc_giay" target="_self">Mực & giấy bao bì</a>
        <a href="?page=thuhoi" target="_self">Chính sách thu hồi</a>
    </div>
</div>
</div>
</div>
<section class="hero-banner">
    <div class="hero-content">
        <div class="hero-small">Đặc sản mùa thu Hà Nội</div>
        <h1>Cốm Làng Vòng</h1>
        <p>Hương vị truyền thống của Hà Nội với hạt cốm dẻo thơm.</p>
        <div class="hero-actions">
            <a href="#dathang" class="hero-btn order" target="_self">Đặt hàng ngay</a>
            <a href="tel:0385437503" class="hero-btn call">Gọi tư vấn</a>
        </div>
    </div>
</section>
""", unsafe_allow_html=True)

st.markdown("<div class='content'>", unsafe_allow_html=True)

PRODUCTS = [

    {
        "name": "Bánh Cốm Truyền Thống",
        "price": "65.000đ",
        "weight": "250g / hộp",
        "image": "Banh com.jpg",
        "desc": "Bánh cốm dẻo thơm với nhân đậu xanh truyền thống Hà Nội."
    },

    {
        "name": "Bánh Chưng Cốm",
        "price": "180.000đ",
        "weight": "700g",
        "image": "banh trung com.jpg",
        "desc": "Bánh chưng kết hợp cốm xanh tạo hương vị độc đáo."
    },

    {
        "name": "Bánh Trung Thu Cốm",
        "price": "95.000đ",
        "weight": "180g",
        "image": "Banh trung thu com.jpg",
        "desc": "Bánh trung thu nhân cốm mềm dẻo, thơm vị mùa thu Hà Nội."
    },

    {
        "name": "Bánh Xu Xê Cốm",
        "price": "55.000đ",
        "weight": "6 cái / hộp",
        "image": "Banh xu xe com.jpg",
        "desc": "Bánh xu xê vị cốm thanh nhẹ, dẻo ngọt vừa phải."
    },

    {
        "name": "Bia Cốm Hà Nội",
        "price": "35.000đ",
        "weight": "330ml",
        "image": "bia com.jpg",
        "desc": "Dòng bia thủ công mang hương thơm nhẹ từ cốm non."
    },

    {
        "name": "Cốm Mộc",
        "price": "120.000đ",
        "weight": "500g",
        "image": "com moc.jpg",
        "desc": "Cốm tươi nguyên bản dẻo thơm, chuẩn vị làng Vòng."
    },

    {
        "name": "Cốm Xào Dừa",
        "price": "85.000đ",
        "weight": "300g",
        "image": "com xao dua.jpg",
        "desc": "Cốm xào cùng dừa non tạo vị béo ngọt hấp dẫn."
    },

    {
        "name": "Mochi Cốm",
        "price": "75.000đ",
        "weight": "6 bánh / hộp",
        "image": "mochi com.png",
        "desc": "Mochi nhân cốm mềm mịn, hiện đại nhưng vẫn đậm chất Việt."
    },

    {
        "name": "Sữa Chua Cốm",
        "price": "45.000đ",
        "weight": "4 hũ",
        "image": "sua chua com.png",
        "desc": "Sữa chua kết hợp cốm non tạo vị thanh mát độc đáo."
    },

    {
        "name": "Tôm Tẩm Cốm",
        "price": "140.000đ",
        "weight": "500g",
        "image": "tom tam com.jpg",
        "desc": "Tôm chiên giòn phủ cốm xanh thơm bùi đặc trưng."
    },

    {
        "name": "Trà Sen Cốm",
        "price": "160.000đ",
        "weight": "200g",
        "image": "tra sen.jpg",
        "desc": "Trà sen ướp hương cốm thanh tao, đậm chất Hà Nội."
    },

    {
        "name": "Xôi Cốm",
        "price": "50.000đ",
        "weight": "1 suất",
        "image": "xoi com.jpg",
        "desc": "Xôi cốm dẻo thơm ăn kèm dừa tươi và đậu xanh."
    }
]

PAGE_DATABASE = {
    "thongtinsp": {"title": "Thông tin sản phẩm", "type": "group", "items": ["tensp_masp", "thuonghieu", "sanpham"]},
    "tensp_masp": {"title": "Tên & mã sản phẩm", "card_class": "card", "card_title": "🌾 Thông tin nhận diện sản phẩm", "fields": {"Tên sản phẩm": "Cốm Làng Vòng", "Mã sản phẩm": "COM-LV-001", "Loại sản phẩm": "Thực phẩm truyền thống", "Dòng sản phẩm": "Cốm truyền thống"}, "paragraphs": ["Thông tin tên và mã sản phẩm giúp khách hàng nhận diện, tra cứu và truy xuất sản phẩm nhanh chóng."]},
    "thuonghieu": {"title": "Thương hiệu", "card_class": "card", "card_title": "🌿 Thương hiệu Cốm Làng Vòng", "paragraphs": ["Cốm Làng Vòng là thương hiệu gắn với làng nghề truyền thống Hà Nội.", "Sản phẩm đại diện cho nét tinh tế và văn hóa ẩm thực Thủ đô."]},
    "sanpham": {
        "title": "Sản phẩm",
        "type": "products"
    },
    "truyxuat": {"title": "Truy xuất nguồn gốc", "type": "group", "items": ["nguyenlieu", "khuvuc", "malo"]},
    "nguyenlieu": {"title": "Nguồn nguyên liệu", "card_class": "card2", "card_title": "🌾 Lúa nếp non", "paragraphs": ["Nguyên liệu chính là lúa nếp non được chọn lọc kỹ lưỡng.", "Lúa được sàng lọc, loại bỏ hạt lép trước khi rang và giã để tạo nên hạt cốm dẻo thơm."]},
    "khuvuc": {"title": "Khu vực sản xuất", "card_class": "card2", "card_title": "📍 Làng Vòng - Hà Nội", "paragraphs": ["Sản phẩm được sản xuất tại làng nghề truyền thống Làng Vòng.", "Đây là địa danh nổi tiếng với nghề làm cốm lâu đời của Hà Nội."]},
    "malo": {"title": "Mã lô hàng", "card_class": "card2", "card_title": "🏷️ Thông tin lô hàng", "fields": {"Mã lô": "LV-2026-001", "Ngày sản xuất": "Cập nhật trên bao bì sản phẩm", "Hạn sử dụng": "Cập nhật theo từng loại sản phẩm"}},
    "chatluong": {"title": "Chất lượng & chứng nhận", "type": "custom_cert"},
    "truyenthong": {"title": "Nội dung truyền thông", "type": "group", "items": ["cauchuyen", "hinhanh", "video"]},
    "cauchuyen": {"title": "Câu chuyện sản phẩm", "card_class": "card", "card_title": "🍃 Câu chuyện Cốm Làng Vòng", "paragraphs": ["Cốm Làng Vòng là một phần ký ức mùa thu Hà Nội.", "Mỗi hạt cốm là kết quả của quá trình chọn lúa, rang, giã và sàng sảy công phu."]},
    "hinhanh": {"title": "Hình ảnh", "type": "images", "intro": "Hình ảnh sản phẩm:", "images": ["Com tong quan.jpg", "Com tong quan 1.jpg", "Com tong quan 2.jpg"]},
    "video": {"title": "Video giới thiệu", "card_class": "card", "card_title": "🎬 Video giới thiệu", "videos": ["https://www.youtube.com/watch?v=_q38xqZFuKE"]},
    "baobi": {"title": "Thông tin bao bì", "type": "group", "items": ["muc_giay", "thuhoi"]},
    "muc_giay": {"title": "Mực & giấy bao bì", "card_class": "card2", "card_title": "📦 Thông tin chất liệu bao bì", "paragraphs": ["Bao bì sử dụng giấy sạch, chắc chắn và phù hợp với thực phẩm.", "Mực in cần rõ nét, bền màu, thể hiện đầy đủ tên sản phẩm, mã lô hàng, hạn sử dụng và thông tin truy xuất.", "Thiết kế nên dùng màu xanh cốm, họa tiết lá sen để tăng khả năng nhận diện thương hiệu."]},
    "thuhoi": {"title": "Chính sách thu hồi", "card_class": "card2", "card_title": "♻️ Chính sách thu hồi", "paragraphs": ["Khuyến khích phân loại và tái chế bao bì sau sử dụng."], "bullets": ["Không vứt bao bì ra môi trường.", "Phân loại bao bì giấy, túi, hộp sau khi dùng.", "Ưu tiên sử dụng bao bì thân thiện với môi trường."]}
}

def create_database():
    conn = sqlite3.connect(":memory:")
    conn.execute("""CREATE TABLE pages (page_id TEXT PRIMARY KEY, title TEXT, page_type TEXT, card_class TEXT, card_title TEXT, intro TEXT, group_items TEXT)""")
    conn.execute("""CREATE TABLE page_fields (page_id TEXT, field_name TEXT, field_value TEXT, sort_order INTEGER)""")
    conn.execute("""CREATE TABLE page_paragraphs (page_id TEXT, content TEXT, sort_order INTEGER)""")
    conn.execute("""CREATE TABLE page_bullets (page_id TEXT, content TEXT, sort_order INTEGER)""")
    conn.execute("""CREATE TABLE page_images (page_id TEXT, image_path TEXT, sort_order INTEGER)""")
    for page_id, data in PAGE_DATABASE.items():
        conn.execute("INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?)", (page_id, data.get("title", ""), data.get("type", "content"), data.get("card_class", "card"), data.get("card_title", ""), data.get("intro", ""), ",".join(data.get("items", []))))
        for idx, (name, value) in enumerate(data.get("fields", {}).items(), start=1):
            conn.execute("INSERT INTO page_fields VALUES (?, ?, ?, ?)", (page_id, name, value, idx))
        for idx, paragraph in enumerate(data.get("paragraphs", []), start=1):
            conn.execute("INSERT INTO page_paragraphs VALUES (?, ?, ?)", (page_id, paragraph, idx))
        for idx, bullet in enumerate(data.get("bullets", []), start=1):
            conn.execute("INSERT INTO page_bullets VALUES (?, ?, ?)", (page_id, bullet, idx))
        for idx, image in enumerate(data.get("images", []), start=1):
            conn.execute("INSERT INTO page_images VALUES (?, ?, ?)", (page_id, image, idx))
    conn.commit()
    return conn

def fetch_page(conn, page_id):
    cur = conn.cursor()
    cur.execute("SELECT page_id, title, page_type, card_class, card_title, intro, group_items FROM pages WHERE page_id = ?", (page_id,))
    row = cur.fetchone()
    if not row: return None
    page_data = {"page_id": row[0], "title": row[1], "type": row[2], "card_class": row[3], "card_title": row[4], "intro": row[5], "fields": [], "paragraphs": [], "bullets": [], "images": [], "group_items": row[6].split(",") if row[6] else []}
    cur.execute("SELECT field_name, field_value FROM page_fields WHERE page_id = ? ORDER BY sort_order", (page_id,)); page_data["fields"] = cur.fetchall()
    cur.execute("SELECT content FROM page_paragraphs WHERE page_id = ? ORDER BY sort_order", (page_id,)); page_data["paragraphs"] = [item[0] for item in cur.fetchall()]
    cur.execute("SELECT content FROM page_bullets WHERE page_id = ? ORDER BY sort_order", (page_id,)); page_data["bullets"] = [item[0] for item in cur.fetchall()]
    cur.execute("SELECT image_path FROM page_images WHERE page_id = ? ORDER BY sort_order", (page_id,)); page_data["images"] = [item[0] for item in cur.fetchall()]
    return page_data

def render_certificate_page():
    html = """
    <style>
    html, body { margin:0; padding:0; overflow:hidden; font-family:Arial, sans-serif; }
    .cert-shell { width:100%; position:relative; padding:0 38px; box-sizing:border-box; }
    .cert-track { display:flex; gap:14px; overflow-x:auto; scroll-snap-type:x mandatory; scroll-behavior:smooth; padding:6px 0 16px 0; }
    .cert-track::-webkit-scrollbar { height:6px; }
    .cert-track::-webkit-scrollbar-thumb { background:#cfcfcf; border-radius:999px; }
    .cert-card { flex:0 0 min(76vw, 340px); scroll-snap-align:center; background:#f1f8e9; border-radius:18px; padding:12px; box-shadow:0 4px 14px rgba(0,0,0,.08); box-sizing:border-box; }
    .cert-card img { width:100%; height:300px; object-fit:contain; background:white; border-radius:14px; display:block; }
    .cert-card h3 { color:#2e7d32; font-size:18px; line-height:1.2; text-align:center; margin:12px 0 6px 0; }
    .cert-card p { font-size:14px; line-height:1.45; text-align:center; margin:0; color:#444; }
    .cert-btn { position:absolute; top:145px; transform:translateY(-50%); width:34px; height:34px; border-radius:50%; border:0; background:#2e7d32; color:white; font-size:24px; line-height:34px; cursor:pointer; z-index:5; }
    .cert-prev { left:0; } .cert-next { right:0; }
    @media (max-width:480px) { .cert-shell { padding:0 30px; } .cert-card { flex-basis:78vw; padding:10px; } .cert-card img { height:250px; } .cert-card h3 { font-size:16px; } .cert-card p { font-size:12.5px; } .cert-btn { width:30px; height:30px; font-size:20px; top:125px; } }
    </style>
    <div class="cert-shell">
      <div class="cert-track" id="certTrack">
    """
    for cert in CERTIFICATES:
        html += f"""
        <div class="cert-card">
            <img src="{image_to_data_uri(cert['image'])}" alt="{cert['title']}">
            <h3>{cert['title']}</h3>
            <p>{cert['desc']}</p>
        </div>
        """
    html += """
      </div>
    </div>
    """
    components.html(html, height=440, scrolling=False)

def render_products():
    html = "<div class='product-grid'>"

    for product in PRODUCTS:
        html += f"""
        <div class="product-card">
            <img src="{image_to_data_uri(product['image'])}" alt="{product['name']}">

            <div class="product-info">
                <h3>{product['name']}</h3>
                <p>{product['desc']}</p>
                <p class="product-weight">⚖️ Định lượng: {product['weight']}</p>
                <div class="product-price">💰 {product['price']}</div>
                <a href="tel:0385437503" class="buy-btn">Đặt hàng</a>
            </div>
        </div>
        """

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_products():
    cols = st.columns(2)

    for index, product in enumerate(PRODUCTS):

        with cols[index % 2]:

            image_path = resolve_asset_path(product["image"])

            if image_path.exists():
                st.image(str(image_path), use_container_width=True)

            st.markdown(f"### {product['name']}")

            st.markdown(product["desc"])

            st.markdown(
                f"**⚖️ Định lượng:** {product['weight']}"
            )

            st.markdown(
                f"## 💰 {product['price']}"
            )

            st.markdown(
                "<a href='tel:0385437503' class='buy-btn'>Đặt hàng</a>",
                unsafe_allow_html=True
            )

            st.markdown("---")
    
def render_page(page_data):
    special_titles = [
    "Chất lượng & chứng nhận",
    "Nội dung truyền thông"
    ]
    
    title_class = "page-title small-title" if page_data["title"] in special_titles else "page-title"
    st.markdown(f"<h1 class='{title_class}'>{page_data['title']}</h1>", unsafe_allow_html=True)
    if page_data["type"] == "custom_cert":
        render_certificate_page(); return
    if page_data["type"] == "group":

        for child_page_id in page_data["group_items"]:
    
            child_data = fetch_page(conn, child_page_id)
    
            if not child_data:
                continue
    
            if child_data["type"] == "products":
    
                st.markdown("""
                <div class="card">
                    <h3>🌾 Sản phẩm</h3>
                    <p>Khám phá các sản phẩm đặc sản từ cốm Làng Vòng.</p>
                    <a href="?page=sanpham" target="_self">
                        Xem chi tiết →
                    </a>
                </div>
                """, unsafe_allow_html=True)
    
            else:

                html = f"<div class='{child_data.get('card_class', 'card')}'>"
            
                if child_data.get("card_title"):
                    html += f"<h3>{child_data['card_title']}</h3>"
            
                for name, value in child_data.get("fields", []):
                    html += f"<p><b>{name}:</b> {value}</p>"
            
                for p in child_data.get("paragraphs", []):
                    html += f"<p>{p}</p>"
            
                html += f"<p><a href='?page={child_page_id}' target='_self'>Xem chi tiết →</a></p>"
            
                html += "</div>"
            
                st.markdown(html, unsafe_allow_html=True)
    
        return
    if page_data["type"] == "products":
        render_products()
        return
    if page_data["type"] == "videos":
        for video in page_data["videos"]:
            st.video(video)
        return
    if page_data["type"] == "images":
        st.write(page_data["intro"])
        for image_path in page_data["images"]:
            full_path = resolve_asset_path(image_path)
            if full_path.exists():
                st.image(str(full_path), use_container_width=True)
            else:
                st.warning(f"Không tìm thấy ảnh: {image_path}")
        return
    render_content_card(page_data)

conn = create_database()
current_page = fetch_page(conn, page)
if current_page: render_page(current_page)
else:
    st.markdown("<h1 class='page-title'>Trang không tồn tại</h1>", unsafe_allow_html=True)
    st.write("Vui lòng chọn lại mục trong menu.")

st.markdown("""
<div class="floating-contact">
    <a href="tel:0385437503" class="float-btn call-btn">📞</a>
    <a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">💬</a>
</div>
</div>
<div class="footer-full" id="dathang">
    <div class="footer-content">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p>📍 Địa chỉ: Số 36, ngõ 63 Xuân Thủy, Cầu Giấy, Hà Nội</p>
        <p>📞 <a href="tel:0385437503">0385 437 503</a></p>
        <p>💬 <a href="https://zalo.me/0385437503" target="_blank">Chat Zalo</a></p>
        <p style="margin-top:15px; font-size:13px; color:#ccc;">© 2026 Cốm Làng Vòng. All rights reserved.</p>
    </div>
</div>
""", unsafe_allow_html=True)

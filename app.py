import base64
import mimetypes
import sqlite3
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="CỐM LÀNG VÒNG", layout="wide")

params = st.query_params
page = params.get("page", "gioithieu")

APP_DIR = Path(__file__).resolve().parent


def resolve_asset_path(file_name):
    """Return absolute path for a file placed next to app.py."""
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
        "image": "CBSP.jpg",
        "title": "Tự công bố sản phẩm",
        "desc": "Giấy xác nhận tự công bố sản phẩm Cốm Làng Vòng theo quy định an toàn thực phẩm.",
    },
    {
        "image": "KQKN.jpg",
        "title": "Phiếu kiểm nghiệm",
        "desc": "Kết quả kiểm nghiệm các chỉ tiêu an toàn thực phẩm của sản phẩm.",
    },
    {
        "image": "OCOP.JPEG",
        "title": "Chứng nhận OCOP 4 sao",
        "desc": "Chứng nhận sản phẩm OCOP đạt 4 sao năm 2022.",
    },
    {
        "image": "HACCP.JPEG",
        "title": "Chứng nhận HACCP",
        "desc": "Chứng nhận hệ thống phân tích mối nguy và kiểm soát điểm tới hạn.",
    },
    {
        "image": "GMP.jpg",
        "title": "Chứng nhận GMP",
        "desc": "Chứng nhận thực hành sản xuất tốt trong sản xuất thực phẩm.",
    },
    {
        "image": "ATTP.JPEG",
        "title": "Chứng nhận an toàn thực phẩm",
        "desc": "Chứng nhận cơ sở đủ điều kiện an toàn thực phẩm.",
    },
]

PRODUCTS = [
    {
        "category": "Sản phẩm phổ biến",
        "name": "Bánh Cốm Truyền Thống",
        "price": "65.000đ",
        "weight": "250g / hộp",
        "image": "Banh com.jpg",
        "desc": "Lớp vỏ cốm xanh mềm dẻo ôm trọn phần nhân đậu xanh sên nhuyễn cùng dừa nạo. Khi thưởng thức cảm nhận rõ vị ngọt thanh, thơm mùi lúa non đặc trưng của mùa thu Hà Nội.",
    },
    {
        "category": "Sản phẩm đặc biệt",
        "name": "Bánh Chưng Cốm",
        "price": "180.000đ",
        "weight": "700g",
        "image": "banh trung com.jpg",
        "desc": "Nếp dẻo kết hợp cốm non tạo nên hương thơm dịu nhẹ rất riêng. Nhân đậu xanh và thịt được nêm vừa vị, mang cảm giác ấm áp và đậm chất truyền thống.",
    },
    {
        "category": "Sản phẩm đặc biệt",
        "name": "Bánh Trung Thu Cốm",
        "price": "95.000đ",
        "weight": "180g",
        "image": "Banh trung thu com.jpg",
        "desc": "Phần nhân cốm mềm mịn hòa quyện cùng vị béo nhẹ của hạt sen và dừa sợi. Vỏ bánh nướng thơm bơ tạo hậu vị thanh tao, không quá ngọt.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Bánh Xu Xê Cốm",
        "price": "55.000đ",
        "weight": "6 cái / hộp",
        "image": "Banh xu xe com.jpg",
        "desc": "Bánh có lớp vỏ trong dẻo dai cùng nhân đậu xanh cốm thơm nhẹ. Khi ăn cảm nhận độ mềm mát và vị ngọt thanh rất dễ chịu.",
    },
    {
        "category": "Sản phẩm đặc biệt",
        "name": "Bia Cốm Hà Nội",
        "price": "35.000đ",
        "weight": "330ml",
        "image": "bia com.jpg",
        "desc": "Dòng bia thủ công mang hương thơm thoang thoảng của cốm non. Vị bia nhẹ, hậu vị mượt và dễ uống, thích hợp cho những buổi gặp gỡ cuối tuần.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Cốm Mộc",
        "price": "120.000đ",
        "weight": "500g",
        "image": "com moc.jpg",
        "desc": "Những hạt cốm xanh mềm được làm từ nếp non tuyển chọn, giữ trọn độ dẻo và hương thơm tự nhiên. Khi nhai cảm nhận vị ngọt dịu lan tỏa rất đặc trưng.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Cốm Xào Dừa",
        "price": "85.000đ",
        "weight": "300g",
        "image": "com xao dua.jpg",
        "desc": "Cốm được xào cùng dừa non và đường phèn tạo độ dẻo béo hấp dẫn. Mùi thơm của lá sen và cốm quyện lại mang cảm giác rất Hà Nội.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Mochi Cốm",
        "price": "75.000đ",
        "weight": "6 bánh / hộp",
        "image": "mochi com.png",
        "desc": "Lớp mochi mềm dai kết hợp nhân kem cốm béo nhẹ tạo cảm giác mát lạnh khi thưởng thức. Hương cốm thanh thoát giúp món bánh không bị ngấy.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Sữa Chua Cốm",
        "price": "45.000đ",
        "weight": "4 hũ",
        "image": "sua chua com.png",
        "desc": "Sữa chua mịn kết hợp cốm non tạo vị chua ngọt hài hòa. Từng muỗng mang hương thơm dịu nhẹ và cảm giác thanh mát rất dễ ăn.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Tôm Tẩm Cốm",
        "price": "140.000đ",
        "weight": "500g",
        "image": "tom tam com.jpg",
        "desc": "Tôm tươi được phủ lớp cốm xanh rồi chiên vàng giòn. Khi ăn cảm nhận lớp vỏ thơm bùi hòa cùng vị ngọt tự nhiên của tôm.",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Xôi Cốm",
        "price": "50.000đ",
        "weight": "1 suất",
        "image": "xoi com.jpg",
        "desc": "Xôi được nấu từ cốm non dẻo mềm kết hợp đậu xanh và dừa sợi. Hương thơm bùi béo hòa quyện tạo cảm giác vừa dân dã vừa tinh tế.",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Ô Mai Sấu Hà Nội",
        "price": "70.000đ",
        "weight": "250g / hộp",
        "image": "omai sau.jpg",
        "desc": "Ô mai sấu có vị chua ngọt hài hòa, thơm mùi gừng nhẹ và rất hợp dùng làm quà Hà Nội.",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Trà Sen Tây Hồ",
        "price": "220.000đ",
        "weight": "100g",
        "image": "tra sen.jpg",
        "desc": "Trà sen ướp hương thanh tao, hậu vị dịu ngọt, phù hợp thưởng thức cùng các món bánh truyền thống.",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Bánh Tôm Hồ Tây",
        "price": "90.000đ",
        "weight": "1 phần",
        "image": "banh tom ho tay.jpg",
        "desc": "Bánh tôm giòn rụm, thơm béo, là món ăn gắn với ký ức ẩm thực Hồ Tây.",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Chả Cá Lã Vọng",
        "price": "180.000đ",
        "weight": "1 phần",
        "image": "cha ca la vong.jpg",
        "desc": "Chả cá thơm nghệ, ăn cùng thì là, hành và bún, mang hương vị đặc trưng của Hà Nội.",
    },

]

if "cart" not in st.session_state:
    st.session_state.cart = {}

add_cart = params.get("add_cart", None)

if add_cart is not None:
    try:
        product_index = int(add_cart)

        if 0 <= product_index < len(PRODUCTS):
            key = str(product_index)
            st.session_state.cart[key] = st.session_state.cart.get(key, 0) + 1

        st.query_params.clear()
        st.query_params["page"] = page or "sanpham"
        if page == "chitietsp":
            st.query_params["product"] = str(product_index)
        st.rerun()

    except (TypeError, ValueError):
        pass

cart_count = sum(st.session_state.cart.values())

PAGE_DATABASE = {
    "gioithieu": {
        "title": "Giới thiệu",
        "type": "group",
        "items": ["cauchuyen", "video"],
    },
    "quytrinh": {
        "title": "Quy trình & nguồn gốc",
        "type": "group",
        "items": ["nguyenlieu", "khuvuc"],
    },
    "sanpham_main": {
        "title": "Sản phẩm",
        "type": "group",
        "items": ["sanpham", "thuonghieu", "tensp_masp"],
    },
    "baobi_main": {
        "title": "Bao bì & bảo quản",
        "type": "group",
        "items": ["muc_giay", "thuhoi"],
    },
    "giohang": {
        "title": "Giỏ hàng",
        "type": "custom_cart",
    },

    # Legacy groups kept for old links.
    "thongtinsp": {
        "title": "Thông tin sản phẩm",
        "type": "group",
        "items": ["sanpham", "thuonghieu", "tensp_masp"],
    },
    "truyxuat": {
        "title": "Truy xuất nguồn gốc",
        "type": "group",
        "items": ["nguyenlieu", "khuvuc", "malo"],
    },
    "truyenthong": {
        "title": "Nội dung truyền thông",
        "type": "group",
        "items": ["cauchuyen", "video"],
    },
    "baobi": {
        "title": "Thông tin bao bì",
        "type": "group",
        "items": ["muc_giay", "thuhoi"],
    },

    "cauchuyen": {
        "title": "Câu chuyện Cốm Làng Vòng",
        "card_class": "card",
        "card_title": "🍃 Câu chuyện Cốm Làng Vòng",
        "paragraphs": [
            "Cốm Làng Vòng là một thức quà truyền thống gắn liền với mùa thu Hà Nội. Hương cốm non, màu xanh dịu và vị ngọt thanh đã trở thành một phần ký ức quen thuộc của nhiều thế hệ người Việt.",
            "Từ những hạt lúa nếp non được chọn lọc kỹ, người làm cốm phải trải qua nhiều công đoạn thủ công như rang, giã, sàng sảy và ủ lá sen. Mỗi công đoạn đều cần sự tỉ mỉ, kinh nghiệm và cảm nhận tinh tế của người thợ.",
            "Không chỉ là một món ăn, cốm còn là biểu tượng của sự thanh nhã trong văn hóa ẩm thực Hà Nội. Cốm thường được dùng làm quà biếu, dùng trong mâm lễ, cưới hỏi hoặc thưởng thức cùng chuối chín, trà sen.",
            "Ngày nay, Cốm Làng Vòng được phát triển thành nhiều sản phẩm mới như bánh cốm, xôi cốm, cốm xào, mochi cốm và các món quà đặc sản. Dù có nhiều biến tấu, giá trị cốt lõi vẫn là giữ được hương vị mộc mạc, dẻo thơm và tinh thần truyền thống.",
            "Chúng tôi mong muốn đưa hương vị cốm truyền thống đến gần hơn với người tiêu dùng hiện đại, đồng thời giữ gìn nét đẹp làng nghề và câu chuyện văn hóa của Hà Nội."
        ],
        "images": [
            "Hinh 1.jpg",
        ],

        "bullets": [
            "Nguồn cảm hứng từ làng nghề Cốm Làng Vòng lâu đời.",
            "Giữ tinh thần thủ công, mộc mạc và tinh tế.",
            "Kết hợp truyền thống với cách trình bày hiện đại.",
            "Phù hợp làm quà biếu, quà du lịch và đặc sản Hà Nội.",
            "Tôn trọng chất lượng, nguồn gốc và trải nghiệm của người tiêu dùng."
        ],
    },
    "video": {
        "title": "Hành trình hương cốm",
        "type": "custom_video",
        "card_title": "🎬 Hành trình hương cốm",
        "paragraphs": [
            "Tái hiện nét đẹp truyền thống và tinh hoa ẩm thực từ cốm Làng Vòng."
        ],
    },
    "sanpham": {
        "title": "Sản phẩm",
        "type": "products",
        "card_title": "🌾 Danh sách sản phẩm",
        "paragraphs": [
            "Khám phá các sản phẩm đặc sản từ cốm Làng Vòng, kèm giá bán và định lượng."
        ],
    },
    "thuonghieu": {
        "title": "Thương hiệu",
        "card_class": "card",
        "card_title": "🌿 Thương hiệu Cốm Làng Vòng",
        "paragraphs": [
            "Cốm Làng Vòng là thương hiệu gắn với làng nghề truyền thống Hà Nội.",
            "Sản phẩm đại diện cho nét tinh tế và văn hóa ẩm thực Thủ đô.",
        ],
    },
    "tensp_masp": {
        "title": "Tên & mã sản phẩm",
        "card_class": "card",
        "card_title": "🌾 Thông tin nhận diện sản phẩm",
        "fields": {
            "Tên sản phẩm": "Cốm Làng Vòng",
            "Mã sản phẩm": "COM-LV-001",
            "Loại sản phẩm": "Thực phẩm truyền thống",
            "Dòng sản phẩm": "Cốm truyền thống",
        },
        "paragraphs": [
            "Thông tin tên và mã sản phẩm giúp khách hàng nhận diện, tra cứu và truy xuất sản phẩm nhanh chóng."
        ],
    },
    "nguyenlieu": {
        "title": "Nguồn nguyên liệu",
        "card_class": "card2",
        "card_title": "🌾 Nguồn nguyên liệu làm cốm",
        "paragraphs": [
            "Cốm Làng Vòng được tạo nên từ những hạt lúa nếp non còn ngậm sữa, được thu hoạch đúng thời điểm để giữ độ dẻo mềm và hương thơm tự nhiên.",
            "Người làm cốm phải chọn lọc kỹ từng bó lúa, loại bỏ hạt lép, hạt sâu và tạp chất để giữ lại phần nguyên liệu đạt chất lượng tốt nhất.",
            "Lúa sau khi thu hoạch cần được đưa vào sơ chế sớm để giữ màu xanh non, vị ngọt thanh và mùi thơm đặc trưng của cốm Hà Nội.",
        ],
        "bullets": [
            "Chọn hạt lúa nếp non đạt độ sữa thích hợp.",
            "Ưu tiên nguyên liệu canh tác an toàn.",
            "Thu hoạch đúng mùa để giữ độ dẻo và màu xanh.",
            "Sơ chế nhanh để bảo toàn hương thơm tự nhiên.",
        ],
        "images": [
            "Com tong quan 3.jpg",
            "hat com tuoi.jpg",
            "me com lang vong.jpg",
        ],
    },

    "khuvuc": {
        "title": "Khu vực sản xuất",
        "card_class": "card2",
        "card_title": "📍 Khu vực sản xuất & chế biến",
        "images": [
            "rang com.jpg",
            "gia com.jpg",
            "sang com.jpg",
        ],
        "paragraphs": [
            "Sản phẩm được chế biến theo phương pháp truyền thống gắn với nghề làm cốm Làng Vòng, Hà Nội.",
            "Khu vực sản xuất cần đảm bảo sạch sẽ, khô thoáng, tách biệt với nguồn ô nhiễm và có dụng cụ chuyên dùng cho thực phẩm.",
            "Các công đoạn rang, giã, sàng, đóng gói được kiểm soát nhằm giữ hương vị cốm và đảm bảo an toàn cho người tiêu dùng.",
        ],
        "fields": {
            "Khu vực": "Làng Vòng - Cầu Giấy - Hà Nội",
            "Hình thức sản xuất": "Kết hợp phương pháp truyền thống và kiểm soát vệ sinh an toàn thực phẩm",
            "Điều kiện sản xuất": "Sạch sẽ, khô thoáng, dụng cụ tiếp xúc thực phẩm được vệ sinh định kỳ",
        },
    },

    "chatluong": {
        "title": "Chất lượng & chứng nhận",
        "type": "custom_cert",
        "card_title": "✅ Chất lượng & chứng nhận",
        "paragraphs": [
            "Các chứng nhận và hồ sơ kiểm nghiệm giúp khách hàng yên tâm hơn về chất lượng sản phẩm."
        ],
    },
    "muc_giay": {
        "title": "Mực & giấy bao bì",
        "card_class": "card2",
        "card_title": "📦 Thông tin chất liệu bao bì",
        "paragraphs": [
            "Bao bì sử dụng giấy sạch, chắc chắn và phù hợp với thực phẩm.",
            "Mực in cần rõ nét, bền màu, thể hiện đầy đủ tên sản phẩm, mã lô hàng, hạn sử dụng và thông tin truy xuất.",
            "Thiết kế nên dùng màu xanh cốm, họa tiết lá sen để tăng khả năng nhận diện thương hiệu.",
        ],
    },
    "thuhoi": {
        "title": "Chính sách thu hồi",
        "card_class": "card2",
        "card_title": "♻️ Chính sách thu hồi",
        "paragraphs": ["Khuyến khích phân loại và tái chế bao bì sau sử dụng."],
        "bullets": [
            "Không vứt bao bì ra môi trường.",
            "Phân loại bao bì giấy, túi, hộp sau khi dùng.",
            "Ưu tiên sử dụng bao bì thân thiện với môi trường.",
        ],
    },
}

st.markdown(
    """
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
    background: #2e7d32;
    color: white;
    border: none;
    cursor: pointer;
    width: 100%;
    text-align: left;
    border-radius: 8px 8px 0 0;
    font-size: clamp(12px, 3.1vw, 15px);
    padding: clamp(7px, 1.9vw, 10px) 12px;
}

.dropdown-content {
    display: none;
    background: white;
    min-width: 230px;
    border-radius: 0 0 8px 8px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    z-index: 9999;
}

.dropdown-content a {
    display: block;
    padding: clamp(6px, 1.8vw, 11px) 12px;
    text-decoration: none;
    color: #333;
    border-bottom: 1px solid #eee;
    font-size: clamp(11px, 2.9vw, 14px);
    line-height: 1.15;
}

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
    width: min(72%, 720px);
    padding-left: clamp(24px, 6vw, 60px);
    padding-right: 6px;
    padding-top: 120px;
    color: white;
}

.hero-small {
    font-size: clamp(9px, 2.5vw, 17px);
    font-weight: 700;
    letter-spacing: clamp(0.7px, 0.25vw, 1.8px);
    text-transform: uppercase;
    margin-bottom: -6px;
    line-height: 1;
    white-space: nowrap;
}

.hero-content h1 {
    font-size: clamp(28px, 8.2vw, 56px);
    line-height: 1.04;
    margin: 0 0 -15px 0;
    white-space: nowrap;
}

.hero-content p {
    font-size: clamp(12px, 3.4vw, 20px);
    line-height: 1.32;
    margin: 0 0 clamp(12px, 3vw, 18px) 0;
}

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

.content {
    max-width: 850px;
    margin: auto;
    padding: clamp(12px, 3vw, 20px);
    line-height: 1.75;
    font-size: clamp(14px, 3vw, 16px);
    overflow-x: hidden;
}

.page-title {
    text-align: center;
    font-size: clamp(17px, 4.2vw, 34px);
    line-height: 1.2;
    margin: clamp(14px, 4vw, 24px) auto clamp(10px, 3vw, 18px) auto;
    white-space: normal;
    max-width: 100%;
    overflow-wrap: normal;
}

.page-title.small-title { font-size: clamp(18px, 4vw, 30px); }

.card, .card2 {
    padding: clamp(14px, 3vw, 20px);
    border-radius: 14px;
    margin-top: 18px;
    overflow-wrap: anywhere;
}

.card { background: #f1f8e9; }
.card2 { background: #e8f5e9; }

.card h3, .card2 h3 {
    font-size: clamp(17px, 4vw, 22px);
    line-height: 1.25;
    margin-top: 0;
}

.product-section { margin-top: 28px; }
.product-section-title {
    font-size: 26px;
    color: #2e7d32;
    margin: 18px 0 12px;
}
.product-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 16px;
    margin-top: 10px;
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

.product-card img, .product-image-placeholder {
    width: 100%;
    height: 170px;
    object-fit: cover;
    display: flex;
    align-items: center;
    justify-content: center;
    background: #f1f8e9;
    color: #2e7d32;
    font-weight: 800;
    text-align: center;
    padding: 10px;
}


.product-card-link {
    display: block;
    text-decoration: none;
    color: inherit;
}
.product-card-link:hover h3 { color: #2e7d32; }
.product-card:hover { transform: translateY(-2px); transition: transform .2s ease, box-shadow .2s ease; box-shadow: 0 8px 22px rgba(0,0,0,0.12); }
.product-detail {
    display: grid;
    grid-template-columns: minmax(280px, 46%) 1fr;
    gap: 28px;
    background: #fffdf4;
    border-radius: 22px;
    padding: 20px;
    margin-top: 18px;
    align-items: start;
}
.product-detail-image img, .product-detail-image .product-image-placeholder {
    width: 100%;
    height: 430px;
    object-fit: cover;
    border-radius: 20px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.12);
}
.product-detail-info h2 { margin: 0 0 10px; color: #17351f; font-size: clamp(26px, 4vw, 42px); }
.product-detail-price { font-size: 30px; font-weight: 900; color: #1f2937; margin: 10px 0 16px; }
.product-summary { background:#f1f8e9; border-radius:16px; padding:14px 16px; margin:14px 0; }
.product-summary p { margin: 6px 0; }
.detail-block { background: #f1f8e9; border-radius: 16px; padding: 18px 20px; margin-top: 18px; }
.detail-block h3 { margin: 0 0 10px; color: #2e7d32; font-size: 22px; }
.detail-block ul, .detail-block ol { margin: 0; padding-left: 22px; }
.detail-block li { margin: 6px 0; }
.back-products { display:inline-block; margin-top:16px; color:#2e7d32; font-weight:900; text-decoration:none; }
.process-sketch { display:grid; grid-template-columns: repeat(4, minmax(0,1fr)); gap:12px; margin:14px 0 18px; }
.process-step { background:white; border:2px dashed #9ccc65; border-radius:16px; padding:14px 10px; text-align:center; min-height:128px; display:flex; flex-direction:column; justify-content:center; box-shadow:0 4px 12px rgba(0,0,0,.06); }
.process-icon { font-size:34px; line-height:1.1; margin-bottom:8px; }
.process-label { font-size:13px; font-weight:800; color:#244128; }
.product-tabs-title { color:#14782e; font-size:22px; border-bottom:3px solid #14782e; padding-bottom:8px; margin:24px 0 16px; text-transform:uppercase; }
.compact-product-grid { display:grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap:16px; margin-bottom:20px; }
.compact-product-card { text-decoration:none; color:inherit; display:block; }
.compact-product-card img, .compact-product-card .product-image-placeholder { width:100%; height:180px; object-fit:cover; border-radius:0; box-shadow:none; }
.compact-product-card h4 { color:#14782e; margin:8px 0 4px; font-size:15px; }
.compact-product-card .compact-price { color:red; font-weight:900; margin-bottom:8px; }
.compact-actions { display:flex; gap:6px; flex-wrap:wrap; }
.compact-actions a { text-decoration:none; color:white !important; background:#f97316; padding:8px 12px; font-size:12px; font-weight:800; }
.compact-actions a:last-child { background:#14782e; }

@media (max-width: 768px) {
    .product-detail { grid-template-columns: 1fr; padding: 12px; gap: 14px; }
    .product-detail-image img, .product-detail-image .product-image-placeholder { height: 260px; }
    .process-sketch { grid-template-columns: repeat(2, minmax(0,1fr)); }
    .compact-product-grid { grid-template-columns: repeat(2, minmax(0,1fr)); gap:12px; }
    .compact-product-card img, .compact-product-card .product-image-placeholder { height:135px; }
}

.product-info {
    padding: 12px;
    display: flex;
    flex-direction: column;
    flex: 1;
}

.product-info h3 {
    margin: 0 0 8px 0;
    color: #1f2937;
    font-size: 17px;
}

.product-info p {
    font-size: 14px;
    line-height: 1.45;
}

.product-weight { margin-top: auto; font-weight: 600; }

.product-price {
    font-size: 20px;
    font-weight: 900;
    color: #1f2937;
    margin: 8px 0 12px;
}

.product-actions { display:flex; gap:8px; flex-wrap:wrap; align-items:center; }
.buy-btn, .cart-add-btn {
    width: fit-content;
    background: #2e7d32;
    color: white !important;
    padding: 9px 14px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 800;
    font-size: 13px;
}

.product-actions {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    align-items: center;
}

.cart-btn {
    width: fit-content;
    background: #ff9800;
    color: white !important;
    padding: 10px 16px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 800;
    border: none;
    cursor: pointer;
}

.cart-add-btn { background:#f59e0b; }
.cart-link {
    text-decoration:none;
    color:#2e7d32;
    font-weight:900;
    font-size:22px;
    white-space:nowrap;
}
.cart-badge {
    background:#f59e0b;
    color:white;
    border-radius:999px;
    padding:2px 7px;
    font-size:12px;
    vertical-align:top;
}
.cart-menu-btn {
    text-decoration:none;
    color:#2e7d32;
    font-weight:900;
    padding: 9px 12px;
    white-space: nowrap;
}

.cart-list { display:grid; gap:10px; margin-top:16px; }
.cart-item { background:#f1f8e9; border-radius:14px; padding:12px 14px; }

.floating-contact {
    position: fixed;
    bottom: 50px;
    right: clamp(8px, 2vw, 15px);
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 9999;
}

.float-btn {
    width: clamp(40px, 10vw, 48px);
    height: clamp(40px, 10vw, 48px);
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: white;
    font-size: clamp(18px, 5vw, 22px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.call-btn { background: #2e7d32; }
.zalo-btn { background: #0084ff; }

.footer-full {
    width: 100%;
    background: #000;
    color: white;
    padding: 10px;
    margin-top: 40px;
    border-radius: 0;
}

.footer-content { max-width: 850px; margin: auto; text-align: center; }
.footer-content a { color: white; text-decoration: none; }

@media (min-width: 768px) {
    .topbar { display: flex; align-items: center; gap: 20px; }
    .hamburger { display: none; }
    .menu { display: flex !important; flex-direction: row; flex-wrap: wrap; margin-top: 0; }
    .dropbtn { width: auto; text-align: center; border-radius: 8px; }
    .dropdown-content { position: absolute; border-radius: 10px; }
}

@media (max-width: 768px) {
    .logo { font-size: 34px; }
    .block-container { max-width: 100% !important; }
    .topbar { margin: 6px auto; padding: 10px; }
    .dropdown-content {
        display: block !important;
        position: relative;
        width: 100%;
        min-width: 0;
        box-shadow: none;
        border-radius: 0 0 8px 8px;
        margin-top: 0;
    }

    .dropdown-content a {
        background: #f7fff5;
        color: #2e7d32;
        padding-left: 24px;
        font-weight: 600;
    }

    .dropdown-content a:hover {
        background: #e8f5e9;
    }

    .dropdown {
        margin-bottom: 6px;
    }
    .hero-banner { min-height: clamp(300px, 86vw, 380px); margin-top: 10px; }
    .hero-content { width: 78%; padding-left: 22px; padding-top: 140px; }
    .hero-content h1 { font-size: clamp(34px, 9vw, 48px); white-space: nowrap; line-height: 1; }
    .hero-content p { font-size: clamp(12px, 3.4vw, 14px); }
    .hero-btn { padding: 14px 24px; font-size: 16px; }
    .page-title { font-size: clamp(16px, 4.1vw, 19px); white-space: nowrap; }
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
        position: relative;
    }
    .product-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
    .product-card img, .product-image-placeholder { height: 135px; }
    .product-info h3 { font-size: 15px; }
    .product-info p { font-size: 12px; }
    .product-price { font-size: 17px; }
    .buy-btn, .cart-add-btn { font-size: 12px; padding: 8px 10px; }
}
.origin-page {
    background: #fffdf4;
    border-radius: 22px;
    padding: 20px;
    margin-top: 20px;
}

.origin-row {
    display: grid;
    grid-template-columns: 330px 1fr;
    gap: 22px;
    padding: 26px 0;
    border-bottom: 1px solid #d9e5d0;
}

.origin-row:last-child {
    border-bottom: none;
}

.origin-text h2 {
    color: #1b5e20;
    margin: 0 0 8px;
    font-size: 28px;
}

.origin-text h4 {
    color: #2e7d32;
    font-style: italic;
    margin: 0 0 16px;
    font-size: 18px;
}

.origin-text p,
.origin-text li {
    font-size: 15px;
    line-height: 1.6;
}

.origin-text ul {
    padding-left: 20px;
}

.origin-gallery {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 18px;
}

.origin-gallery img {
    width: 100%;
    aspect-ratio: 1/1;   /* ảnh vuông, đều nhau */
    object-fit: cover;
    border-radius: 18px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.12);
    transition: transform 0.3s ease;
}

.origin-gallery img:hover {
    transform: translateY(-4px);
}

@media (max-width: 768px) {
    .origin-page {
        padding: 12px;
    }

    .origin-row {
        grid-template-columns: 1fr;
        gap: 14px;
        padding: 20px 0;
    }

    .origin-text h2 {
        font-size: 22px;
    }

    .origin-gallery {
        grid-template-columns: repeat(3, 1fr); /* 3 cột trên điện thoại */
        gap: 8px;
    }

    .origin-gallery img {
        height: auto;
        border-radius: 12px;
    }
}

.story-layout {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 42px;
    align-items: center;
    padding: 30px 10px;
}

.story-left {
    padding-right: 10px;
}

.story-mini-badge {
    display: inline-block;
    background: #e6f4ea;
    color: #2e7d32;
    padding: 8px 16px;
    border-radius: 999px;
    font-weight: 800;
    margin-bottom: 20px;
}

.story-left h1 {
    font-size: clamp(42px, 5vw, 70px);
    line-height: 1.05;
    color: #17351f;
    margin-bottom: 24px;
}

.story-desc {
    font-size: 18px;
    line-height: 1.8;
    color: #425344;
    margin-bottom: 30px;
}

.story-features {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 30px;
}

.story-feature {
    background: #f4f8f1;
    border-radius: 18px;
    padding: 16px;
    font-weight: 700;
    color: #244128;
    border: 1px solid #dce8d8;
}

.story-quote {
    border-left: 5px solid #2e7d32;
    padding-left: 18px;
    font-size: 20px;
    line-height: 1.7;
    color: #29432d;
    font-style: italic;
}

.story-right img {
    width: 100%;
    height: 720px;
    object-fit: cover;
    border-radius: 28px;
    box-shadow: 0 12px 40px rgba(0,0,0,0.12);
}

@media (max-width: 768px) {

    .story-layout {
        grid-template-columns: 1.05fr 0.95fr;
        gap: 10px;
        padding: 14px 4px;
        align-items: center;
    }

    .story-left h1 {
        font-size: 24px;
        margin-bottom: 10px;
    }

    .story-mini-badge {
        font-size: 11px;
        padding: 6px 10px;
        margin-bottom: 10px;
    }

    .story-desc {
        font-size: 13px;
        line-height: 1.55;
        margin-bottom: 12px;
    }

    .story-features {
        grid-template-columns: 1fr;
        gap: 7px;
        margin-bottom: 12px;
    }

    .story-feature {
        font-size: 12px;
        padding: 8px;
        border-radius: 12px;
    }

    .story-quote {
        font-size: 13px;
        line-height: 1.5;
        padding-left: 10px;
    }

    .story-right img {
        height: 360px;
        border-radius: 18px;
    }
}

</style>
""".replace("__BANNER_IMAGE__", image_to_data_uri("Banner com.jpg")),
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="topbar">
<input type="checkbox" id="menu-toggle">
<div class="top-row">
<div class="logo">🌾 Cốm Làng Vòng</div>
<a href="?page=giohang" target="_self" class="cart-link">🛒 <span class="cart-badge">__CART_COUNT__</span></a>
<label for="menu-toggle" class="hamburger">☰</label>
</div>
<div class="menu">
<div class="dropdown"><a href="?page=gioithieu" target="_self" style="text-decoration:none;"><button class="dropbtn">Giới thiệu</button></a><div class="dropdown-content"><a href="?page=cauchuyen" target="_self">Câu chuyện Cốm Làng Vòng</a><a href="?page=video" target="_self">Hành trình hương cốm</a></div></div>
<div class="dropdown"><a href="?page=quytrinh" target="_self" style="text-decoration:none;"><button class="dropbtn">Quy trình & nguồn gốc</button></a><div class="dropdown-content"><a href="?page=nguyenlieu" target="_self">Nguồn nguyên liệu</a><a href="?page=khuvuc" target="_self">Khu vực sản xuất</a></div></div>
<div class="dropdown"><a href="?page=sanpham_main" target="_self" style="text-decoration:none;"><button class="dropbtn">Sản phẩm</button></a><div class="dropdown-content"><a href="?page=sanpham" target="_self">Danh sách sản phẩm</a><a href="?page=thuonghieu" target="_self">Thương hiệu</a><a href="?page=tensp_masp" target="_self">Tên & mã sản phẩm</a></div></div>
<div class="dropdown"><a href="?page=chatluong" target="_self" style="text-decoration:none;"><button class="dropbtn">Chất lượng</button></a></div>
<div class="dropdown"><a href="?page=baobi_main" target="_self" style="text-decoration:none;"><button class="dropbtn">Bao bì & bảo quản</button></a><div class="dropdown-content"><a href="?page=muc_giay" target="_self">Mực & giấy bao bì</a><a href="?page=thuhoi" target="_self">Chính sách thu hồi</a></div></div>
<a href="?page=giohang" target="_self" class="cart-menu-btn">🛒 Giỏ hàng (__CART_COUNT__)</a>
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
""".replace("__CART_COUNT__", str(cart_count)),
    unsafe_allow_html=True,
)

st.markdown("<div class='content'>", unsafe_allow_html=True)


def create_database():
    conn = sqlite3.connect(":memory:")
    conn.execute(
        """CREATE TABLE pages (
            page_id TEXT PRIMARY KEY,
            title TEXT,
            page_type TEXT,
            card_class TEXT,
            card_title TEXT,
            intro TEXT,
            group_items TEXT
        )"""
    )
    conn.execute(
        """CREATE TABLE page_fields (
            page_id TEXT,
            field_name TEXT,
            field_value TEXT,
            sort_order INTEGER
        )"""
    )
    conn.execute(
        """CREATE TABLE page_paragraphs (
            page_id TEXT,
            content TEXT,
            sort_order INTEGER
        )"""
    )
    conn.execute(
        """CREATE TABLE page_bullets (
            page_id TEXT,
            content TEXT,
            sort_order INTEGER
        )"""
    )
    conn.execute(
        """CREATE TABLE page_images (
            page_id TEXT,
            image_path TEXT,
            sort_order INTEGER
        )"""
    )

    for page_id, data in PAGE_DATABASE.items():
        conn.execute(
            "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                page_id,
                data.get("title", ""),
                data.get("type", "content"),
                data.get("card_class", "card"),
                data.get("card_title", ""),
                data.get("intro", ""),
                ",".join(data.get("items", [])),
            ),
        )

        for idx, (name, value) in enumerate(data.get("fields", {}).items(), start=1):
            conn.execute(
                "INSERT INTO page_fields VALUES (?, ?, ?, ?)",
                (page_id, name, value, idx),
            )

        for idx, paragraph in enumerate(data.get("paragraphs", []), start=1):
            conn.execute(
                "INSERT INTO page_paragraphs VALUES (?, ?, ?)",
                (page_id, paragraph, idx),
            )

        for idx, bullet in enumerate(data.get("bullets", []), start=1):
            conn.execute(
                "INSERT INTO page_bullets VALUES (?, ?, ?)",
                (page_id, bullet, idx),
            )

        for idx, image in enumerate(data.get("images", []), start=1):
            conn.execute(
                "INSERT INTO page_images VALUES (?, ?, ?)",
                (page_id, image, idx),
            )

    conn.commit()
    return conn


def fetch_page(conn, page_id):
    cur = conn.cursor()
    cur.execute(
        """SELECT page_id, title, page_type, card_class, card_title, intro, group_items
           FROM pages
           WHERE page_id = ?""",
        (page_id,),
    )
    row = cur.fetchone()

    if not row:
        return None

    page_data = {
        "page_id": row[0],
        "title": row[1],
        "type": row[2],
        "card_class": row[3],
        "card_title": row[4],
        "intro": row[5],
        "fields": [],
        "paragraphs": [],
        "bullets": [],
        "images": [],
        "group_items": row[6].split(",") if row[6] else [],
    }

    cur.execute(
        "SELECT field_name, field_value FROM page_fields WHERE page_id = ? ORDER BY sort_order",
        (page_id,),
    )
    page_data["fields"] = cur.fetchall()

    cur.execute(
        "SELECT content FROM page_paragraphs WHERE page_id = ? ORDER BY sort_order",
        (page_id,),
    )
    page_data["paragraphs"] = [item[0] for item in cur.fetchall()]

    cur.execute(
        "SELECT content FROM page_bullets WHERE page_id = ? ORDER BY sort_order",
        (page_id,),
    )
    page_data["bullets"] = [item[0] for item in cur.fetchall()]

    cur.execute(
        "SELECT image_path FROM page_images WHERE page_id = ? ORDER BY sort_order",
        (page_id,),
    )
    page_data["images"] = [item[0] for item in cur.fetchall()]

    return page_data


def render_content_card(page_data, detail_link=None, show_full=False):
    html = f"<div class='{page_data.get('card_class', 'card')}'>"

    if page_data.get("card_title"):
        html += f"<h3>{page_data['card_title']}</h3>"
    else:
        html += f"<h3>{page_data.get('title', '')}</h3>"

    for name, value in page_data.get("fields", []):
        html += f"<p><b>{name}:</b> {value}</p>"

    if show_full:

        for paragraph in page_data.get("paragraphs", []):
            html += f"<p>{paragraph}</p>"

        if page_data.get("images"):

            html += '<div class="origin-gallery">'

            for image in page_data.get("images", []):
                html += f'<img src="{image_to_data_uri(image)}">'

            html += '</div>'

        if page_data.get("bullets"):
            html += "<ul>"

            for bullet in page_data["bullets"]:
                html += f"<li>{bullet}</li>"

            html += "</ul>"
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

def render_story_page():
    story_image = image_to_data_uri("Hinh 1.jpg")

    html = f"""<div class="story-layout">
<div class="story-left">
<div class="story-mini-badge">🍃 Di sản ẩm thực Hà Nội</div>
<h1>Câu chuyện<br>Cốm Làng Vòng</h1>
<p class="story-desc">
Từ hạt lúa nếp non còn ngậm sữa, qua đôi tay người thợ làng nghề,
cốm trở thành thức quà thanh nhã của mùa thu Hà Nội.
</p>
<div class="story-features">
<div class="story-feature">🌾 Lúa nếp non tuyển chọn</div>
<div class="story-feature">🔥 Rang thủ công giữ hương</div>
<div class="story-feature">🥢 Giã, sàng tỉ mỉ</div>
<div class="story-feature">🍃 Gói trong hương lá sen</div>
</div>
<div class="story-quote">“Cốm không chỉ là món ăn, mà còn là ký ức mùa thu Hà Nội.”</div>
</div>
<div class="story-right">
<img src="{story_image}">
</div>
</div>"""

    st.markdown(html, unsafe_allow_html=True)


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
@media (max-width:480px) { .cert-shell { padding:0 8px; } .cert-card { flex-basis:78vw; padding:10px; } .cert-card img { height:250px; } .cert-card h3 { font-size:16px; } .cert-card p { font-size:12.5px; } }
</style>
<div class="cert-shell">
<div class="cert-track" id="certTrack">
"""
    for cert in CERTIFICATES:
        html += (
            f'<div class="cert-card">'
            f'<img src="{image_to_data_uri(cert["image"])}" alt="{cert["title"]}">'
            f"<h3>{cert['title']}</h3>"
            f"<p>{cert['desc']}</p>"
            f"</div>"
        )

    html += """
</div>
</div>
"""
    components.html(html, height=440, scrolling=False)


def render_product_image(product):
    image_path = resolve_asset_path(product["image"])

    if image_path.exists():
        return f'<img src="{image_to_data_uri(product["image"])}" alt="{product["name"]}">'

    return f'<div class="product-image-placeholder">{product["name"]}</div>'


def build_product_story(product):
    """Return a short storytelling paragraph for each product detail page."""
    name = product.get("name", "sản phẩm")

    stories = {
        "Bánh Cốm Truyền Thống": "Bánh cốm truyền thống gợi nhớ những hộp bánh xanh được gói ghém cẩn thận trong các dịp cưới hỏi, lễ Tết và những lần người Hà Nội mang quà đi xa. Mỗi chiếc bánh là sự gặp gỡ giữa hạt cốm non dẻo thơm và nhân đậu xanh ngọt bùi, giữ lại nét thanh nhã của mùa thu Hà Nội.",
        "Bánh Chưng Cốm": "Bánh chưng cốm là cách kể mới của món bánh ngày Tết. Sắc xanh của cốm làm chiếc bánh trở nên mềm mại hơn, vừa quen thuộc như mâm cơm sum họp, vừa có hương thơm rất riêng của làng nghề Hà Nội.",
        "Bánh Trung Thu Cốm": "Bánh trung thu cốm mang hương mùa thu vào đêm rằm. Khi cắt bánh, mùi cốm dịu nhẹ hòa cùng vị ngọt của nhân tạo cảm giác ấm áp, như một món quà dành cho gia đình trong khoảnh khắc đoàn viên.",
        "Bánh Xu Xê Cốm": "Bánh xu xê cốm thường gắn với lời chúc trọn vẹn, đủ đầy. Lớp vỏ dẻo trong ôm lấy nhân cốm đậu xanh, tượng trưng cho sự hòa hợp và ngọt ngào trong những dịp vui.",
        "Bia Cốm Hà Nội": "Bia cốm Hà Nội là một biến tấu trẻ trung từ hương vị truyền thống. Vị bia nhẹ kết hợp hương cốm thoảng qua, tạo cảm giác vừa hiện đại vừa thân quen trong những cuộc gặp gỡ bạn bè.",
        "Cốm Mộc": "Cốm mộc là hình ảnh nguyên bản nhất của làng Vòng. Từ những hạt lúa nếp non được rang, giã và sàng bằng sự kiên nhẫn, cốm mộc giữ lại vị ngọt thanh và mùi thơm tự nhiên của đồng lúa Hà Nội.",
        "Cốm Xào Dừa": "Cốm xào dừa là món quà của sự khéo léo. Hạt cốm được xào chậm để giữ độ dẻo, quyện cùng dừa non béo nhẹ, tạo nên món ăn dân dã nhưng rất dễ khiến người thưởng thức nhớ lâu.",
        "Mochi Cốm": "Mochi cốm là cuộc gặp giữa cảm hứng Á Đông hiện đại và hương cốm Hà Nội. Lớp bánh mềm dai, nhân mát lạnh và mùi cốm nhẹ khiến sản phẩm phù hợp với những người trẻ muốn tìm một hương vị truyền thống theo cách mới.",
        "Sữa Chua Cốm": "Sữa chua cốm kể câu chuyện về sự tươi mát. Vị chua nhẹ của sữa chua làm nổi bật hương cốm non, tạo nên món tráng miệng gần gũi, dễ ăn và phù hợp với nhịp sống hiện đại.",
        "Tôm Tẩm Cốm": "Tôm tẩm cốm biến hạt cốm thành lớp áo giòn thơm cho món mặn. Khi chiên vàng, cốm ôm lấy vị ngọt của tôm, tạo nên món ăn vừa lạ miệng vừa mang dấu ấn ẩm thực Hà Nội.",
        "Trà Sen Cốm": "Trà sen cốm là câu chuyện của sự thư thái. Hương sen thanh tao gặp mùi cốm non dịu nhẹ, tạo nên chén trà thích hợp cho những lúc chậm lại và cảm nhận nét tinh tế của Hà Nội.",
        "Xôi Cốm": "Xôi cốm thường xuất hiện trong những buổi sáng se lạnh hoặc mâm lễ truyền thống. Vị dẻo của cốm, bùi của đậu xanh và béo của dừa gợi cảm giác ấm áp, thân thuộc như một phần ký ức phố cổ.",
        "Ô Mai Sấu Hà Nội": "Ô mai sấu Hà Nội gắn với những gói quà nhỏ mang vị chua, cay, mặn, ngọt hài hòa. Mỗi miếng ô mai như lưu lại chút nắng gió phố phường và thói quen nhâm nhi rất riêng của người Hà Nội.",
        "Trà Sen Tây Hồ": "Trà sen Tây Hồ là thức trà của sự cầu kỳ. Từng lớp hương sen được ướp vào trà để tạo mùi thơm sâu, dịu và sang, phù hợp để tiếp khách hoặc dùng cùng bánh truyền thống.",
        "Bánh Tôm Hồ Tây": "Bánh tôm Hồ Tây gợi nhớ những buổi chiều bên mặt nước, khi chiếc bánh vừa chiên xong còn giòn rụm và thơm nóng. Đây là món ăn mang màu sắc phố phường, vui vẻ và rất Hà Nội.",
        "Chả Cá Lã Vọng": "Chả cá Lã Vọng là câu chuyện về một món ăn lâu đời của Hà Nội. Hương nghệ, thì là và cá nóng trên chảo tạo nên trải nghiệm đậm đà, thường được nhớ đến trong những bữa ăn quây quần.",
    }

    return stories.get(
        name,
        f"{name} được phát triển từ cảm hứng gìn giữ hương vị truyền thống Hà Nội, kết hợp nguyên liệu quen thuộc với cách chế biến phù hợp hơn với người tiêu dùng hiện đại."
    )


def build_product_details(product):
    category = product.get("category", "")
    name = product.get("name", "")

    if "Bánh" in name:
        ingredients = ["Cốm non", "Đậu xanh", "Đường", "Dừa nạo hoặc nguyên liệu phối hợp theo từng dòng bánh", "Lá sen hoặc bao bì thực phẩm sạch"]
        process = ["Chọn cốm non và sơ chế nguyên liệu.", "Sên nhân đến khi mềm, dẻo và có mùi thơm.", "Tạo hình bánh, định lượng theo từng hộp hoặc từng chiếc.", "Đóng gói sạch, dán nhãn và bảo quản nơi khô mát."]
    elif "Trà" in name:
        ingredients = ["Trà chất lượng tốt", "Hương sen", "Hương cốm hoặc cốm non", "Bao bì kín mùi"]
        process = ["Chọn trà và nguyên liệu tạo hương.", "Ướp trà theo từng lớp để hương thấm đều.", "Sấy hoặc hong nhẹ để ổn định độ ẩm.", "Đóng gói kín để giữ hương thơm."]
    elif "Sữa Chua" in name:
        ingredients = ["Sữa chua", "Cốm non", "Đường hoặc siro nhẹ", "Hũ đựng thực phẩm"]
        process = ["Chuẩn bị sữa chua mịn và cốm non.", "Phối trộn cốm với sữa chua theo tỷ lệ phù hợp.", "Chiết vào hũ sạch.", "Bảo quản lạnh trước khi giao khách."]
    elif "Tôm" in name:
        ingredients = ["Tôm tươi", "Cốm xanh", "Bột áo", "Gia vị", "Dầu chiên"]
        process = ["Làm sạch tôm và ướp gia vị nhẹ.", "Phủ bột áo rồi lăn qua cốm xanh.", "Chiên vàng ở nhiệt độ phù hợp.", "Đóng gói hoặc dùng ngay khi còn nóng giòn."]
    elif "Bia" in name:
        ingredients = ["Nước", "Malt", "Hoa bia", "Men bia", "Hương cốm"]
        process = ["Nấu dịch malt.", "Ủ lên men với men bia.", "Tạo hương cốm nhẹ.", "Lọc, đóng chai/lon và bảo quản mát."]
    elif "Ô Mai" in name:
        ingredients = ["Quả sấu", "Đường", "Gừng", "Muối", "Gia vị ô mai"]
        process = ["Chọn sấu, làm sạch và sơ chế.", "Ướp đường, gừng và gia vị.", "Sên hoặc hong đến khi đạt độ dẻo.", "Đóng hộp kín để bảo quản."]
    elif "Chả Cá" in name:
        ingredients = ["Cá tươi", "Nghệ", "Thì là", "Hành", "Gia vị"]
        process = ["Sơ chế cá và thái miếng vừa ăn.", "Ướp cá với nghệ và gia vị.", "Nướng hoặc áp chảo sơ.", "Hoàn thiện cùng thì là, hành và dùng nóng."]
    elif "Bánh Tôm" in name:
        ingredients = ["Tôm", "Bột", "Khoai hoặc nguyên liệu tạo độ giòn", "Gia vị", "Dầu chiên"]
        process = ["Sơ chế tôm và nguyên liệu đi kèm.", "Pha bột có độ sánh phù hợp.", "Tạo hình bánh cùng tôm.", "Chiên vàng giòn và dùng nóng."]
    else:
        ingredients = ["Cốm non", "Đường", "Dừa", "Lá sen", "Nguyên liệu phụ theo từng sản phẩm"]
        process = ["Chọn cốm non đạt độ dẻo và hương thơm.", "Sơ chế nguyên liệu sạch.", "Chế biến theo phương pháp truyền thống hoặc hiện đại tùy sản phẩm.", "Định lượng, đóng gói và bảo quản đúng điều kiện."]

    if category == "Cốm truyền thống":
        storage = "Nên dùng sớm trong ngày hoặc bảo quản mát để giữ độ dẻo thơm của cốm."
    elif "đặc sản" in category.lower():
        storage = "Bảo quản theo đặc tính từng món; ưu tiên dùng khi còn tươi ngon."
    else:
        storage = "Bảo quản nơi khô mát hoặc ngăn mát tùy sản phẩm, tránh ánh nắng trực tiếp."

    return ingredients, process, storage


def render_products():
    categories = [
        "Sản phẩm phổ biến",
        "Sản phẩm đặc biệt",
        "Các đặc sản khác của Hà Nội",
    ]

    html = ""

    for category in categories:
        category_products = [
            (index, product)
            for index, product in enumerate(PRODUCTS)
            if product.get("category") == category
        ]

        if not category_products:
            continue

        html += f'<section class="product-section"><h2 class="product-section-title">{category}</h2>'
        html += '<div class="product-grid">'

        for index, product in category_products:
            detail_url = f"?page=chitietsp&product={index}"
            html += (
                f'<div class="product-card">'
                f'<a href="{detail_url}" target="_self" class="product-card-link">'
                f'{render_product_image(product)}'
                f'<div class="product-info">'
                f'<h3>{product["name"]}</h3>'
                f'<div class="product-price">💰 {product["price"]}</div>'
                f'</div>'
                f'</a>'
                f'<div class="product-info" style="padding-top:0;">'
                f'<div class="product-actions">'
                f'<a href="tel:0385437503" class="buy-btn">Đặt hàng</a>'
                f'<a href="?page=sanpham&add_cart={index}" target="_self" class="cart-btn">+ Giỏ hàng</a>'
                f'</div>'
                f'</div>'
                f'</div>'
            )

        html += "</div></section>"

    st.markdown(html, unsafe_allow_html=True)


def build_product_notes(product):
    name = product.get("name", "sản phẩm")
    return [
        f"Chọn nguyên liệu tươi, sạch để giữ đúng mùi vị của {name}.",
        "Không chế biến ở nhiệt quá cao trong thời gian dài để tránh mất hương cốm.",
        "Dụng cụ tiếp xúc thực phẩm cần được vệ sinh và để khô trước khi dùng.",
        "Nên dùng sớm sau khi mở bao bì để sản phẩm giữ được độ thơm ngon.",
    ]


def build_product_nutrition(product):
    name = product.get("name", "sản phẩm")
    if "Bia" in name:
        return ["Cung cấp năng lượng nhẹ từ malt.", "Có hương cốm dễ uống, nên dùng điều độ.", "Không phù hợp cho trẻ em và người cần kiêng đồ uống có cồn."]
    if "Trà" in name:
        return ["Ít năng lượng.", "Hương trà và sen giúp tạo cảm giác thư giãn.", "Có thể dùng cùng bánh cốm hoặc các món ngọt truyền thống."]
    if "Sữa Chua" in name:
        return ["Bổ sung lợi khuẩn từ sữa chua.", "Có vị chua ngọt dễ ăn.", "Phù hợp dùng lạnh như món tráng miệng."]
    if any(k in name for k in ["Tôm", "Chả Cá", "Bánh Tôm"]):
        return ["Có chất đạm từ nguyên liệu chính.", "Nên dùng kèm rau hoặc đồ chua để cân bằng vị.", "Món chiên/rán nên dùng vừa phải để tránh cảm giác ngấy."]
    return ["Cung cấp năng lượng từ tinh bột của cốm/nếp.", "Có vị ngọt dịu, phù hợp dùng làm món quà hoặc món ăn nhẹ.", "Nên dùng lượng vừa phải nếu cần kiểm soát đường hoặc tinh bột."]


def build_process_sketch(process):
    icons = ["🌾", "🥣", "🔥", "📦", "🍃", "✅"]
    labels = []
    for i, step in enumerate(process[:4]):
        short = step.split(".")[0]
        labels.append((icons[i % len(icons)], short))
    return "".join(
        f"<div class='process-step'><div class='process-icon'>{icon}</div><div class='process-label'>Bước {idx}: {label}</div></div>"
        for idx, (icon, label) in enumerate(labels, start=1)
    )


def render_compact_product_grid(indexes):
    html = '<div class="compact-product-grid">'
    for index in indexes:
        product = PRODUCTS[index]
        html += (
            f'<div class="compact-product-card">'
            f'<a href="?page=chitietsp&product={index}" target="_self" class="compact-product-card">'
            f'{render_product_image(product)}'
            f'<h4>{product["name"]}</h4>'
            f'<div class="compact-price">{product["price"]}</div>'
            f'</a>'
            f'<div class="compact-actions">'
            f'<a href="tel:0385437503">MUA NGAY</a>'
            f'<a href="?page=chitietsp&product={index}&add_cart={index}" target="_self">THÊM GIỎ HÀNG</a>'
            f'</div>'
            f'</div>'
        )
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def render_product_detail_page():
    product_param = params.get("product", "0")

    try:
        product_index = int(product_param)
    except (TypeError, ValueError):
        product_index = 0

    if product_index < 0 or product_index >= len(PRODUCTS):
        st.markdown("<h1 class='page-title'>Không tìm thấy sản phẩm</h1>", unsafe_allow_html=True)
        st.write("Vui lòng quay lại danh sách sản phẩm.")
        return

    if "viewed_products" not in st.session_state:
        st.session_state.viewed_products = []
    st.session_state.viewed_products = [i for i in st.session_state.viewed_products if i != product_index]
    st.session_state.viewed_products.insert(0, product_index)
    st.session_state.viewed_products = st.session_state.viewed_products[:8]

    product = PRODUCTS[product_index]
    ingredients, process, storage = build_product_details(product)
    story = build_product_story(product)
    notes = build_product_notes(product)
    nutrition = build_product_nutrition(product)

    ingredients_html = "".join(f"<li>{item}</li>" for item in ingredients)
    process_html = "".join(f"<li>{item}</li>" for item in process)
    notes_html = "".join(f"<li>{item}</li>" for item in notes)
    nutrition_html = "".join(f"<li>{item}</li>" for item in nutrition)
    sketch_html = build_process_sketch(process)

    html = (
        f"<a href='?page=sanpham' target='_self' class='back-products'>← Quay lại danh sách sản phẩm</a>"
        f"<div class='product-detail'>"
        f"<div class='product-detail-image'>{render_product_image(product)}</div>"
        f"<div class='product-detail-info'>"
        f"<h2>{product['name']}</h2>"
        f"<div class='product-detail-price'>💰 {product['price']}</div>"
        f"<div class='product-summary'>"
        f"<p><b>Danh mục:</b> {product['category']}</p>"
        f"<p><b>Định lượng:</b> {product['weight']}</p>"
        f"<p><b>Bảo quản:</b> {storage}</p>"
        f"</div>"
        f"<div class='product-actions'>"
        f"<a href='tel:0385437503' class='buy-btn'>Đặt hàng</a>"
        f"<a href='?page=chitietsp&product={product_index}&add_cart={product_index}' target='_self' class='cart-btn'>+ Giỏ hàng</a>"
        f"</div>"
        f"</div></div>"
        f"<div class='detail-block'><h3>Mô tả sản phẩm</h3><p>{story}</p><p>{product['desc']}</p></div>"
        f"<div class='detail-block'><h3>Cách làm {product['name']}</h3>"
        f"<h4>Nguyên liệu</h4><ul>{ingredients_html}</ul>"
        f"<h4>Các bước làm minh họa</h4><div class='process-sketch'>{sketch_html}</div>"
        f"<ol>{process_html}</ol></div>"
        f"<div class='detail-block'><h3>Các lưu ý khi làm {product['name']}</h3><ul>{notes_html}</ul></div>"
        f"<div class='detail-block'><h3>Giá trị dinh dưỡng của {product['name']}</h3><ul>{nutrition_html}</ul></div>"
    )

    st.markdown(html, unsafe_allow_html=True)

    same_category = [
        index for index, item in enumerate(PRODUCTS)
        if item.get("category") == product.get("category") and index != product_index
    ][:4]
    viewed = [index for index in st.session_state.viewed_products if index != product_index][:4]

    tab_related, tab_viewed = st.tabs(["Sản phẩm cùng chuyên mục", "Sản phẩm đã xem"])

    with tab_related:
        st.markdown("<h3 class='product-tabs-title'>Sản phẩm cùng chuyên mục</h3>", unsafe_allow_html=True)
        if same_category:
            render_compact_product_grid(same_category)
        else:
            st.info("Chưa có sản phẩm cùng chuyên mục.")

    with tab_viewed:
        st.markdown("<h3 class='product-tabs-title'>Sản phẩm đã xem</h3>", unsafe_allow_html=True)
        if viewed:
            render_compact_product_grid(viewed)
        else:
            st.info("Bạn chưa xem thêm sản phẩm nào khác.")


def render_origin_process_page():
    render_ingredient_page()
    render_production_area_page()
def render_ingredient_page():

    # Nguồn nguyên liệu
    img1 = image_to_data_uri("Com tong quan 3.jpg")
    img2 = image_to_data_uri("hat com tuoi.jpg")
    img3 = image_to_data_uri("me com lang vong.jpg")

    html = f"""<section class="origin-row">
<div class="origin-text">
<h2>🌾 Nguồn nguyên liệu làm cốm</h2>
<h4>Tinh túy từ hạt lúa nếp non</h4>
<p>Cốm Làng Vòng được tạo nên từ những hạt lúa nếp non còn ngậm sữa...</p>
<ul>
<li>🌾 Chọn lọc kỹ hạt lúa nếp non</li>
<li>🌿 Ưu tiên nguyên liệu an toàn</li>
<li>⏰ Thu hoạch đúng mùa</li>
<li>🍃 Sơ chế nhanh</li>
</ul>
</div>
<div class="origin-gallery">
<img src="{img1}">
<img src="{img2}">
<img src="{img3}">
</div>
</section>"""

    st.markdown(html, unsafe_allow_html=True)

def render_production_area_page():
    img4 = image_to_data_uri("rang com.jpg")
    img5 = image_to_data_uri("gia com.jpg")
    img6 = image_to_data_uri("sang com.jpg")

    html = f"""<section class="origin-row">
<div class="origin-text">
<h2>📍 Khu vực sản xuất & chế biến</h2>
<h4>Làng Vòng – nơi lưu giữ hương vị truyền thống</h4>
<p>Các công đoạn rang, giã, sàng được thực hiện cẩn thận...</p>
<ul>
<li>🔥 Rang cốm thủ công</li>
<li>🥢 Giã cốm đều tay</li>
<li>🍃 Sàng sảy kỹ</li>
<li>📦 Đóng gói sạch</li>
</ul>
</div>
<div class="origin-gallery">
<img src="{img4}">
<img src="{img5}">
<img src="{img6}">
</div>
</section>"""

    st.markdown(html, unsafe_allow_html=True)

def render_cart_page():
    st.markdown("<h1 class='page-title'>🛒 Giỏ hàng</h1>", unsafe_allow_html=True)

    if "cart" not in st.session_state or not st.session_state.cart:
        st.info("Giỏ hàng của bạn đang trống.")
        return

    html = '<div class="product-grid">'

    for product_index, quantity in st.session_state.cart.items():
        product = PRODUCTS[int(product_index)]

        html += (
            f'<div class="product-card">'
            f'{render_product_image(product)}'
            f'<div class="product-info">'
            f'<h3>{product["name"]}</h3>'
            f'<p>{product["desc"]}</p>'
            f'<p class="product-weight">⚖️ {product["weight"]}</p>'
            f'<div class="product-price">💰 {product["price"]}</div>'
            f'<p><b>Số lượng:</b> {quantity}</p>'
            f'<a href="tel:0385437503" class="buy-btn">Đặt hàng</a>'
            f'</div>'
            f'</div>'
        )

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


def render_video_page():
    st.markdown(
        """
<div class="card">
<h3>🎬 Hành trình hương cốm</h3>
<p>Video tái hiện nét đẹp truyền thống của cốm Làng Vòng — từ những hạt nếp non xanh mướt đến quy trình chế biến thủ công mang đậm dấu ấn Hà Nội xưa.</p>
<p>Mỗi thức quà từ cốm không chỉ là một món ăn, mà còn là hương vị của mùa thu Hà Nội, của ký ức và sự tinh tế trong văn hoá ẩm thực Việt.</p>
</div>
""",
        unsafe_allow_html=True,
    )
    st.video("https://www.youtube.com/watch?v=_q38xqZFuKE")


def render_page(page_data):
    special_titles = [
        "Chất lượng & chứng nhận",
        "Nội dung truyền thông",
    ]

    title_class = "page-title small-title" if page_data["title"] in special_titles else "page-title"
    st.markdown(f"<h1 class='{title_class}'>{page_data['title']}</h1>", unsafe_allow_html=True)

    if page_data["page_id"] == "cauchuyen":
        render_story_page()
        return
    if page_data["page_id"] == "quytrinh":
        render_origin_process_page()
        return
    if page_data["page_id"] == "nguyenlieu":
        render_ingredient_page()
        return
    if page_data["page_id"] == "khuvuc":
        render_production_area_page()
        return
    if page_data["type"] == "custom_cert":
        render_certificate_page()
        return

    if page_data["type"] in ["group", "full_content"]:
        for child_page_id in page_data.get("group_items", []):

            child_data = fetch_page(conn, child_page_id)

            if not child_data:
                continue

            render_content_card(child_data, show_full=True)

        return
    if page_data["type"] == "products":
        render_products()
        return

    if page_data["type"] == "custom_video":
        render_video_page()
        return

    if page_data["type"] == "custom_cart":
        render_cart_page()
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

    if page_data["page_id"] == "nguyenlieu":
        render_origin_process_page()
        return
    
    if page_data["page_id"] == "khuvuc":
        render_production_area_page()
        return

    render_content_card(page_data, show_full=True)


conn = create_database()
current_page = fetch_page(conn, page)

if page == "giohang":
    render_cart_page()

elif page == "chitietsp":
    render_product_detail_page()

elif current_page:
    render_page(current_page)

else:
    st.markdown("<h1 class='page-title'>Trang không tồn tại</h1>", unsafe_allow_html=True)
    st.write("Vui lòng chọn lại mục trong menu.")

st.markdown(
    """
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
""",
    unsafe_allow_html=True,
)

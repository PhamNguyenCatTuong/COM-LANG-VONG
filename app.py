import base64
import mimetypes
import sqlite3
from pathlib import Path
from html import escape

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
        "image": "CBSP.png",
        "title": "Tự công bố sản phẩm",
        "desc": "Giấy xác nhận tự công bố sản phẩm Cốm Làng Vòng theo quy định an toàn thực phẩm.",
    },
    {
        "image": "KQKN.png",
        "title": "Phiếu kiểm nghiệm",
        "desc": "Kết quả kiểm nghiệm các chỉ tiêu an toàn thực phẩm của sản phẩm.",
    },
    {
        "image": "OCOP.png",
        "title": "Chứng nhận OCOP 4 sao",
        "desc": "Chứng nhận sản phẩm OCOP đạt 4 sao năm 2022.",
    },
    {
        "image": "ATTP.png",
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
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Chả cốm",
        "price": "100.000đ",
        "weight": "500g",
        "image": "Cha com.jpg",
    },
    {
        "category": "Sản phẩm đặc biệt",
        "name": "Bánh Chưng Cốm",
        "price": "180.000đ",
        "weight": "700g",
        "image": "banh trung com.jpg",
    },
    {
        "category": "Sản phẩm đặc biệt",
        "name": "Bánh Trung Thu Cốm",
        "price": "95.000đ",
        "weight": "180g",
        "image": "Banh trung thu com.jpg",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Bánh Xu Xê Cốm",
        "price": "55.000đ",
        "weight": "6 cái / hộp",
        "image": "Banh xu xe com.jpg",
    },
    {
        "category": "Sản phẩm đặc biệt",
        "name": "Bia Cốm Hà Nội",
        "price": "35.000đ",
        "weight": "330ml",
        "image": "bia com.jpg",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Cốm Mộc",
        "price": "120.000đ",
        "weight": "500g",
        "image": "com moc.jpg",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Cốm Xào Dừa",
        "price": "85.000đ",
        "weight": "300g",
        "image": "com xao dua.jpg",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Mochi Cốm",
        "price": "75.000đ",
        "weight": "6 bánh / hộp",
        "image": "mochi com.png",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Sữa Chua Cốm",
        "price": "45.000đ",
        "weight": "4 hũ",
        "image": "sua chua com.png",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Tôm Tẩm Cốm",
        "price": "140.000đ",
        "weight": "500g",
        "image": "tom tam com.jpg",
    },
    {
        "category": "Sản phẩm phổ biến",
        "name": "Xôi Cốm",
        "price": "50.000đ",
        "weight": "1 suất",
        "image": "xoi com.jpg",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Ô Mai Sấu Hà Nội",
        "price": "70.000đ",
        "weight": "250g / hộp",
        "image": "o mai sau.jpg",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Trà Sen Tây Hồ",
        "price": "220.000đ",
        "weight": "100g",
        "image": "tra sen.jpg",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Chả Cá Lã Vọng",
        "price": "180.000đ",
        "weight": "1 phần",
        "image": "Cha ca la vong.jpg",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Bánh chả",
        "price": "55.000đ",
        "weight": "200gr",
        "image": "Banh cha.jpeg",
    },
    {
        "category": "Các đặc sản khác của Hà Nội",
        "name": "Chè lam",
        "price": "50.000đ",
        "weight": "1 hooojp 450gr",
        "image": "Che lam.jpg",
    },

]

PRODUCTION_AREAS = [
    {
        "area_id": "tiep_nhan",
        "title": "Khu tiếp nhận nguyên liệu",
        "subtitle": "Kiểm tra lúa nếp non trước khi sơ chế",
        "images": ["Com tong quan 3.jpg", "hat com tuoi.jpg"],
        "description": [
            "Nguyên liệu được tiếp nhận trong khu vực sạch, khô thoáng và tách biệt với khu đóng gói thành phẩm.",
            "Lúa nếp non được kiểm tra màu sắc, độ non, mùi thơm và loại bỏ tạp chất trước khi đưa vào quy trình làm cốm."
        ],
        "fields": {
            "Chức năng": "Tiếp nhận, phân loại và kiểm tra nguyên liệu đầu vào",
            "Yêu cầu vệ sinh": "Nền khô, dụng cụ sạch, có khay hoặc mẹt riêng cho nguyên liệu",
            "Điểm kiểm soát": "Loại bỏ hạt lép, hạt sâu, tạp chất và nguyên liệu không đạt"
        },
        "bullets": ["Kiểm tra độ non của hạt lúa", "Phân loại nguyên liệu trước khi rang", "Không để nguyên liệu tiếp xúc trực tiếp với nền", "Ghi nhận thời gian tiếp nhận để đảm bảo độ tươi"],
    },
    {
        "area_id": "rang_com",
        "title": "Khu rang cốm",
        "subtitle": "Giữ hương thơm và màu xanh tự nhiên",
        "images": ["rang com.jpg"],
        "description": [
            "Khu rang là nơi quyết định mùi thơm ban đầu của cốm. Người thợ cần kiểm soát lửa đều để hạt cốm chín tới mà không bị cháy.",
            "Dụng cụ rang phải được vệ sinh trước và sau mỗi mẻ để tránh lẫn tạp chất hoặc mùi lạ."
        ],
        "fields": {
            "Chức năng": "Rang lúa nếp non theo phương pháp truyền thống",
            "Yêu cầu vệ sinh": "Bếp, chảo rang và dụng cụ đảo cốm sạch, không bám mùi lạ",
            "Điểm kiểm soát": "Nhiệt độ, thời gian rang và độ chín của hạt"
        },
        "bullets": ["Rang từng mẻ vừa đủ để cốm chín đều", "Đảo liên tục để tránh cháy cạnh", "Không dùng dụng cụ bị gỉ sét hoặc bám dầu mỡ", "Tách riêng nguyên liệu sống và nguyên liệu đã rang"],
    },
    {
        "area_id": "gia_sang",
        "title": "Khu giã và sàng sảy",
        "subtitle": "Tạo độ dẻo, sạch vỏ và đều hạt",
        "images": ["gia com.jpg", "sang com.jpg"],
        "description": [
            "Sau khi rang, cốm được giã và sàng nhiều lần để tách vỏ trấu, làm hạt mềm dẻo và đều hơn.",
            "Đây là công đoạn cần sự tỉ mỉ vì lực giã quá mạnh có thể làm nát hạt, còn quá nhẹ sẽ khó tách vỏ."
        ],
        "fields": {
            "Chức năng": "Giã, sàng và làm sạch cốm sau khi rang",
            "Yêu cầu vệ sinh": "Cối, chày, nia, sàng được làm sạch và để khô trước khi dùng",
            "Điểm kiểm soát": "Độ dẻo, độ sạch vỏ và kích thước hạt"
        },
        "bullets": ["Giã đều tay theo từng mẻ nhỏ", "Sàng bỏ trấu và hạt vỡ", "Không để cốm lẫn dị vật trong quá trình sàng", "Kiểm tra cảm quan trước khi chuyển sang đóng gói"],
    },
    {
        "area_id": "dong_goi",
        "title": "Khu đóng gói thành phẩm",
        "subtitle": "Bảo vệ hương cốm trước khi đến tay khách hàng",
        "images": ["Banh com.jpg", "com moc.jpg"],
        "description": [
            "Thành phẩm được đóng gói trong khu vực sạch, hạn chế bụi và côn trùng, giúp giữ hương thơm cũng như chất lượng sản phẩm.",
            "Bao bì cần có thông tin sản phẩm, định lượng, ngày sản xuất, hạn sử dụng và hướng dẫn bảo quản."
        ],
        "fields": {
            "Chức năng": "Cân định lượng, đóng gói, dán nhãn và hoàn thiện sản phẩm",
            "Yêu cầu vệ sinh": "Bàn đóng gói sạch, nhân sự dùng găng tay hoặc dụng cụ tiếp xúc thực phẩm",
            "Điểm kiểm soát": "Khối lượng, nhãn sản phẩm, bao bì kín và nguyên vẹn"
        },
        "bullets": ["Cân đúng định lượng từng sản phẩm", "Kiểm tra bao bì trước khi đóng gói", "Dán nhãn đầy đủ thông tin", "Tách riêng sản phẩm lỗi hoặc bao bì hỏng"],
    },
    {
        "area_id": "bao_quan",
        "title": "Khu bảo quản và xuất hàng",
        "subtitle": "Giữ sản phẩm khô mát, sạch và dễ truy xuất",
        "images": ["OCOP.JPEG", "ATTP.JPEG"],
        "description": [
            "Sản phẩm sau đóng gói được bảo quản ở nơi khô ráo, thoáng mát, tránh ánh nắng trực tiếp và nguồn nhiệt cao.",
            "Khu xuất hàng cần sắp xếp theo lô để dễ kiểm soát hạn sử dụng và truy xuất khi cần."
        ],
        "fields": {
            "Chức năng": "Lưu kho tạm, kiểm tra đơn hàng và xuất sản phẩm",
            "Yêu cầu vệ sinh": "Kệ bảo quản sạch, sản phẩm không đặt trực tiếp xuống nền",
            "Điểm kiểm soát": "Hạn sử dụng, mã lô, tình trạng bao bì và điều kiện nhiệt độ"
        },
        "bullets": ["Sắp xếp theo nguyên tắc nhập trước - xuất trước", "Tránh để gần hóa chất hoặc nguồn mùi mạnh", "Kiểm tra bao bì trước khi giao hàng", "Lưu thông tin lô hàng để hỗ trợ truy xuất"],
    },
]


# Parent menu pages are no longer standalone pages.
# Old parent URLs redirect to the first detailed submenu page.
PARENT_PAGE_REDIRECTS = {
    "gioithieu": "cauchuyen",
    "sanpham_main": "sanpham",
    "baobi_main": "muc_giay",
}
if page in PARENT_PAGE_REDIRECTS:
    st.query_params["page"] = PARENT_PAGE_REDIRECTS[page]
    st.rerun()

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
        viewed_query = params.get("viewed", "")
        if viewed_query:
            st.query_params["viewed"] = viewed_query
        st.rerun()

    except (TypeError, ValueError):
        pass

cart_count = sum(st.session_state.cart.values())


def get_viewed_products_from_url():
    """Lấy danh sách sản phẩm đã xem từ URL query params."""
    viewed_param = params.get("viewed", "")
    viewed_items = []

    for item in str(viewed_param).split(","):
        item = item.strip()
        if item.isdigit():
            idx = int(item)
            if 0 <= idx < len(PRODUCTS) and idx not in viewed_items:
                viewed_items.append(idx)

    return viewed_items


def get_current_viewed_query():
    """Trả về chuỗi viewed hiện tại để gắn vào tất cả link sản phẩm."""
    viewed_items = st.session_state.get("viewed_products", []) or get_viewed_products_from_url()
    return ",".join(str(i) for i in viewed_items if 0 <= int(i) < len(PRODUCTS))


def page_url(page_id, product_index=None, add_cart=None):
    """Tạo URL nội bộ và luôn giữ lại lịch sử sản phẩm đã xem."""
    parts = [f"page={page_id}"]

    if product_index is not None:
        parts.append(f"product={product_index}")

    if add_cart is not None:
        parts.append(f"add_cart={add_cart}")

    viewed_query = get_current_viewed_query()
    if viewed_query:
        parts.append(f"viewed={viewed_query}")

    return "?" + "&".join(parts)

PAGE_DATABASE = {
    "gioithieu": {
        "title": "Giới thiệu",
        "type": "group",
        "items": ["cauchuyen", "video"],
    },
    "quytrinh": {
        "title": "Quy trình & nguồn gốc",
        "type": "custom_origin_process",
        "items": ["nguyenlieu", "khuvuc"],
    },
    "sanpham_main": {
        "title": "Sản phẩm",
        "type": "group",
        "items": ["sanpham", "congthuc"],
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
        "items": ["sanpham", "congthuc"],
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
    "congthuc": {
        "title": "Công thức & Cách làm món ăn",
        "card_class": "card",
        "card_title": "🍽️ Công thức & Cách làm món ăn",
        "paragraphs": [
            "Chọn một sản phẩm trong danh sách để xem công thức, nguyên liệu chi tiết, các bước làm minh họa và lưu ý khi chế biến.",
            "Các công thức được trình bày theo từng món để khách hàng dễ theo dõi và thực hiện tại nhà.",
        ],
        "bullets": [
            "Bánh cốm, bánh xu xê cốm, bánh chưng cốm, bánh trung thu cốm.",
            "Cốm xào dừa, mochi cốm, sữa chua cốm, xôi cốm.",
            "Tôm tẩm cốm và các món đặc sản khác.",
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
    z-index: 10000;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    overflow: visible;
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

.menu {
    display: none;
    flex-direction: column;
    gap: 5px;
    margin-top: 10px;
    overflow: visible;
    width: 100%;
}
#menu-toggle:checked ~ .menu { display: flex; }

.dropdown {
    position: relative;
    background: white;
    border-radius: 8px;
    overflow: visible;
}

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
    overflow: visible;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    z-index: 10000;
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
.dropdown:hover .dropdown-content,
.dropdown:focus-within .dropdown-content {
    display: block;
}

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
    height: 250px;
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

.ingredient-card {
    background: white;
    border-radius: 18px;
    padding: 22px 24px;
    margin: 12px 0 18px;
    box-shadow: 0 4px 14px rgba(0,0,0,.06);
}
.ingredient-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 18px;
    flex-wrap: wrap;
    gap: 10px;
}
.ingredient-head h3 {
    margin: 0 !important;
    color: #17351f !important;
    font-size: 26px !important;
    font-weight: 900 !important;
}
.ingredient-serving {
    font-size: 18px;
    color: #666;
    font-weight: 700;
}
.ingredient-list {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.ingredient-main {
    font-size: 18px;
    color: #111827;
}
.ingredient-dot {
    font-size: 24px;
    margin-right: 6px;
}
.ingredient-name {
    font-weight: 600;
}
.ingredient-amount {
    color: #666;
    font-size: 14px;
    margin-left: 8px;
}
.ingredient-note {
    padding-left: 30px;
    color: #666;
    margin-top: 2px;
    font-size: 14px;
    line-height: 1.3;
}
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

@media (max-width: 1024px) {
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
    font-size: 12px;
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

@media (min-width: 1025px) {
    .topbar { display: flex; align-items: center; gap: 20px; }
    .hamburger { display: none; }
    .menu { display: flex !important; flex-direction: row; flex-wrap: wrap; margin-top: 0; }
    .dropbtn { width: auto; text-align: center; border-radius: 8px; }
    .dropdown-content {
        position: absolute;
        top: 100%;
        left: 0;
        border-radius: 10px;
    }

    .dropdown:hover .dropdown-content,
    .dropdown:focus-within .dropdown-content {
        display: block;
    }
}

@media (max-width: 1024px) {
    .logo { font-size: 34px; }
    .block-container { max-width: 100% !important; }
    .topbar { margin: 6px auto; padding: 10px; }
    .menu {
        display: none !important;
        flex-direction: column;
        width: 100%;
    }

    #menu-toggle:checked ~ .menu {
        display: flex !important;
    }

    .dropdown-content {
        display: block !important;
        position: relative;
        width: 100%;
        min-width: 0;
        box-shadow: none;
        border-radius: 0 0 8px 8px;
        margin-top: 0;
        overflow: visible;
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
        width: 100%;
        overflow: visible;
    }

    .dropbtn {
        width: 100%;
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

@media (max-width: 1024px) {
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

@media (max-width: 1024px) {

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


/* FIX MOBILE/ANDROID MENU */
@media (max-width: 1024px) {
    .topbar {
        overflow: visible !important;
        padding: 10px 12px !important;
    }

    .top-row {
        display: grid !important;
        grid-template-columns: minmax(0, 1fr) auto auto !important;
        align-items: center !important;
        gap: 8px !important;
        width: 100% !important;
    }

    .logo {
        min-width: 0 !important;
        font-size: clamp(24px, 7vw, 34px) !important;
        line-height: 1.1 !important;
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }

    .cart-link {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        font-size: 22px !important;
        flex-shrink: 0 !important;
    }

    .hamburger {
        display: inline-flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 42px !important;
        height: 42px !important;
        font-size: 30px !important;
        color: #2e7d32 !important;
        cursor: pointer !important;
        flex-shrink: 0 !important;
        z-index: 10001 !important;
    }

    .menu {
        display: none !important;
        width: 100% !important;
        margin-top: 10px !important;
    }

    #menu-toggle:checked ~ .menu {
        display: flex !important;
        flex-direction: column !important;
    }

    .dropdown-content {
        display: block !important;
        position: relative !important;
        width: 100% !important;
        min-width: 0 !important;
        box-shadow: none !important;
    }
}

@media (max-width: 430px) {
    .logo {
        font-size: clamp(22px, 6.6vw, 30px) !important;
    }

    .cart-link {
        font-size: 20px !important;
    }

    .hamburger {
        width: 40px !important;
        height: 40px !important;
        font-size: 28px !important;
    }
}


.recipe-shell {
    background: #fffdf4;
    border-radius: 24px;
    padding: 22px;
    margin-top: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,.08);
}

.recipe-quick-title {
    color: #17351f;
    font-size: 26px;
    margin: 0 0 14px;
}

.recipe-quick-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-bottom: 10px;
}

.recipe-quick-card {
    display: block;
    background: white;
    border: 1px solid #dce8d8;
    border-radius: 16px;
    padding: 12px 14px;
    text-decoration: none;
    color: #17351f !important;
    font-weight: 800;
    box-shadow: 0 4px 12px rgba(0,0,0,.06);
}

.recipe-quick-card span {
    display: block;
    color: #2e7d32;
    font-size: 13px;
    margin-top: 4px;
}

.recipe-book {
    position: relative;
    max-width: 920px;
    margin: 8px auto 0;
    min-height: 560px;
    perspective: 1800px;
}

.recipe-page {
    display: none;
    background: linear-gradient(90deg, #fff8df 0%, #fffdf4 48%, #f8edc8 50%, #fffdf4 52%, #fff8df 100%);
    border: 2px solid #d7b56d;
    border-radius: 22px;
    box-shadow: 0 14px 34px rgba(70,45,12,.22);
    padding: 28px;
    min-height: 560px;
    animation: pageFlip .45s ease;
}

.recipe-page.active {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 34px;
}

@keyframes pageFlip {
    from { transform: rotateY(-8deg); opacity: .55; }
    to { transform: rotateY(0deg); opacity: 1; }
}

.recipe-page-left,
.recipe-page-right {
    min-width: 0;
}

.recipe-page h3 {
    color: #1b5e20;
    font-size: 26px;
    margin: 0 0 10px;
}

.recipe-page h4 {
    color: #7a4b00;
    font-size: 18px;
    margin: 16px 0 8px;
}

.recipe-page ul,
.recipe-page ol {
    margin: 0;
    padding-left: 22px;
}

.recipe-page li {
    margin: 7px 0;
    line-height: 1.45;
}

.recipe-serving {
    display: inline-block;
    background: #e8f5e9;
    color: #2e7d32;
    border-radius: 999px;
    padding: 6px 12px;
    font-weight: 800;
    margin-bottom: 12px;
}

.recipe-open-detail {
    display: inline-block;
    background: #2e7d32;
    color: white !important;
    text-decoration: none;
    border-radius: 999px;
    padding: 10px 16px;
    font-weight: 900;
    margin-top: 14px;
}

.recipe-controls {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    margin-top: 16px;
}

.recipe-controls button {
    border: none;
    background: #2e7d32;
    color: white;
    border-radius: 999px;
    padding: 10px 18px;
    font-weight: 900;
    cursor: pointer;
}

.recipe-counter {
    font-weight: 900;
    color: #17351f;
}

@media (max-width: 1024px) {
    .recipe-quick-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .recipe-book {
        min-height: auto;
    }

    .recipe-page,
    .recipe-page.active {
        display: block;
        min-height: auto;
        padding: 20px;
        background: #fffdf4;
    }

    .recipe-page-left {
        border-bottom: 1px dashed #d7b56d;
        padding-bottom: 16px;
        margin-bottom: 16px;
    }
}

@media (max-width: 480px) {
    .recipe-shell {
        padding: 14px;
    }

    .recipe-quick-grid {
        grid-template-columns: 1fr;
    }

    .recipe-page h3 {
        font-size: 22px;
    }
}


/* FIX RECIPE BOOK FLIP - no JavaScript needed */
.recipe-radio {
    position: absolute;
    opacity: 0;
    pointer-events: none;
}

.recipe-book {
    position: relative;
    max-width: 920px;
    margin: 8px auto 0;
    min-height: 560px;
    perspective: 1800px;
}

.recipe-page {
    display: none !important;
    position: relative;
    background: linear-gradient(90deg, #fff8df 0%, #fffdf4 48%, #f8edc8 50%, #fffdf4 52%, #fff8df 100%);
    border: 2px solid #d7b56d;
    border-radius: 22px;
    box-shadow: 0 14px 34px rgba(70,45,12,.22);
    padding: 28px 66px;
    min-height: 560px;
    animation: pageFlip .45s ease;
    grid-template-columns: 1fr 1fr;
    gap: 34px;
}

#recipe-page-0:checked ~ .recipe-book .recipe-page-0,
#recipe-page-1:checked ~ .recipe-book .recipe-page-1,
#recipe-page-2:checked ~ .recipe-book .recipe-page-2,
#recipe-page-3:checked ~ .recipe-book .recipe-page-3,
#recipe-page-4:checked ~ .recipe-book .recipe-page-4,
#recipe-page-5:checked ~ .recipe-book .recipe-page-5,
#recipe-page-6:checked ~ .recipe-book .recipe-page-6,
#recipe-page-7:checked ~ .recipe-book .recipe-page-7,
#recipe-page-8:checked ~ .recipe-book .recipe-page-8,
#recipe-page-9:checked ~ .recipe-book .recipe-page-9,
#recipe-page-10:checked ~ .recipe-book .recipe-page-10,
#recipe-page-11:checked ~ .recipe-book .recipe-page-11,
#recipe-page-12:checked ~ .recipe-book .recipe-page-12,
#recipe-page-13:checked ~ .recipe-book .recipe-page-13,
#recipe-page-14:checked ~ .recipe-book .recipe-page-14,
#recipe-page-15:checked ~ .recipe-book .recipe-page-15,
#recipe-page-16:checked ~ .recipe-book .recipe-page-16,
#recipe-page-17:checked ~ .recipe-book .recipe-page-17,
#recipe-page-18:checked ~ .recipe-book .recipe-page-18,
#recipe-page-19:checked ~ .recipe-book .recipe-page-19 {
    display: grid !important;
}

.recipe-side-btn {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 20;
    width: 46px;
    height: 46px;
    border-radius: 50%;
    background: #2e7d32;
    color: white !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 900;
    cursor: pointer;
    box-shadow: 0 6px 16px rgba(0,0,0,.22);
    user-select: none;
}

.recipe-side-btn.prev {
    left: 12px;
}

.recipe-side-btn.next {
    right: 12px;
}

.recipe-page-number {
    position: absolute;
    bottom: 14px;
    left: 50%;
    transform: translateX(-50%);
    background: #fffdf4;
    color: #17351f;
    border: 1px solid #d7b56d;
    border-radius: 999px;
    padding: 5px 12px;
    font-weight: 900;
    font-size: 13px;
}

.recipe-controls {
    display: none !important;
}

@media (max-width: 1024px) {
    .recipe-book {
        min-height: auto !important;
        margin-top: 14px;
    }

    .recipe-page {
        min-height: 520px !important;
        padding: 22px 54px 48px !important;
        background: linear-gradient(90deg, #fff8df 0%, #fffdf4 48%, #f8edc8 50%, #fffdf4 52%, #fff8df 100%) !important;
        grid-template-columns: 1fr !important;
        gap: 14px !important;
    }

    #recipe-page-0:checked ~ .recipe-book .recipe-page-0,
    #recipe-page-1:checked ~ .recipe-book .recipe-page-1,
    #recipe-page-2:checked ~ .recipe-book .recipe-page-2,
    #recipe-page-3:checked ~ .recipe-book .recipe-page-3,
    #recipe-page-4:checked ~ .recipe-book .recipe-page-4,
    #recipe-page-5:checked ~ .recipe-book .recipe-page-5,
    #recipe-page-6:checked ~ .recipe-book .recipe-page-6,
    #recipe-page-7:checked ~ .recipe-book .recipe-page-7,
    #recipe-page-8:checked ~ .recipe-book .recipe-page-8,
    #recipe-page-9:checked ~ .recipe-book .recipe-page-9,
    #recipe-page-10:checked ~ .recipe-book .recipe-page-10,
    #recipe-page-11:checked ~ .recipe-book .recipe-page-11,
    #recipe-page-12:checked ~ .recipe-book .recipe-page-12,
    #recipe-page-13:checked ~ .recipe-book .recipe-page-13,
    #recipe-page-14:checked ~ .recipe-book .recipe-page-14,
    #recipe-page-15:checked ~ .recipe-book .recipe-page-15,
    #recipe-page-16:checked ~ .recipe-book .recipe-page-16,
    #recipe-page-17:checked ~ .recipe-book .recipe-page-17,
    #recipe-page-18:checked ~ .recipe-book .recipe-page-18,
    #recipe-page-19:checked ~ .recipe-book .recipe-page-19 {
        display: grid !important;
    }

    .recipe-page-left {
        border-bottom: 1px dashed #d7b56d;
        padding-bottom: 12px;
        margin-bottom: 4px;
    }

    .recipe-side-btn {
        width: 42px;
        height: 42px;
        font-size: 22px;
    }

    .recipe-side-btn.prev {
        left: 6px;
    }

    .recipe-side-btn.next {
        right: 6px;
    }
}

@media (max-width: 480px) {
    .recipe-page {
        padding: 18px 46px 46px !important;
        min-height: 560px !important;
        border-radius: 18px !important;
    }

    .recipe-page h3 {
        font-size: 21px !important;
    }

    .recipe-page h4 {
        font-size: 16px !important;
        margin: 10px 0 6px !important;
    }

    .recipe-page li {
        font-size: 13px !important;
        margin: 5px 0 !important;
    }

    .recipe-open-detail {
        padding: 9px 12px !important;
        font-size: 13px !important;
    }
}


.recipe-image-page {
    width: 100%;
    height: 100%;
    min-height: 520px;
    border-radius: 16px;
    overflow: hidden;
    background: #f7f1dc;
    display: flex;
    align-items: center;
    justify-content: center;
}

.recipe-image-page img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    background: #efe6d6;
}

.recipe-image-placeholder {
    width: 100%;
    height: 520px;
    border: 3px dashed #d7b56d;
    border-radius: 16px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #8a6a2f;
    font-size: 22px;
    font-weight: 800;
    background: rgba(255,255,255,0.45);
    text-align: center;
    padding: 20px;
}

@media (max-width: 768px) {
    .recipe-image-page,
    .recipe-image-placeholder {
        height: 460px;
        min-height: 460px;
    }
}


/* SKETCH STYLE FOR QUY TRINH & NGUON GOC */
.process-map-page {
    background: #fffdf4;
    border-radius: 26px;
    padding: clamp(18px, 4vw, 34px);
    margin-top: 20px;
    box-shadow: 0 10px 28px rgba(0,0,0,.08);
    border: 1px solid #e3ead8;
}
.process-map-head {
    display: grid;
    grid-template-columns: minmax(240px, 1fr) minmax(220px, 360px);
    gap: 20px;
    align-items: start;
    margin-bottom: 24px;
}
.process-map-intro h2 {
    margin: 0 0 10px;
    color: #17351f;
    font-size: clamp(26px, 4vw, 42px);
    line-height: 1.08;
}
.process-map-intro p {
    color: #425344;
    font-size: 17px;
    line-height: 1.7;
    margin: 0;
}
.process-note-card {
    background: #f1f8e9;
    border-radius: 18px;
    padding: 16px 18px;
    border-left: 5px solid #2e7d32;
}
.process-note-card h3 {
    margin: 0 0 8px;
    color: #2e7d32;
    font-size: 20px;
}
.process-note-card p {
    margin: 0;
    line-height: 1.55;
}
.process-flow {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 18px 26px;
    align-items: center;
    margin: 26px 0;
}
.flow-card {
    min-height: 126px;
    background: white;
    border: 2px solid #9ccc65;
    border-radius: 18px;
    padding: 16px 12px;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 7px 18px rgba(0,0,0,.08);
    position: relative;
}
.flow-card .flow-icon {
    font-size: 34px;
    line-height: 1;
    margin-bottom: 9px;
}
.flow-card h3 {
    margin: 0 0 6px;
    color: #17351f;
    font-size: 18px;
}
.flow-card p {
    margin: 0;
    color: #4b604d;
    font-size: 13px;
    line-height: 1.35;
}
.flow-arrow {
    font-size: 34px;
    color: #2e7d32;
    text-align: center;
    font-weight: 900;
}
.flow-arrow.down {
    grid-column: 4;
}
.process-bottom-note {
    margin-top: 24px;
    font-size: 20px;
    line-height: 1.65;
    color: #29432d;
    font-style: italic;
    border-top: 1px dashed #b6cfa7;
    padding-top: 18px;
}
.process-gallery-mini {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 18px;
}
.process-gallery-mini img {
    width: 100%;
    aspect-ratio: 4/3;
    object-fit: cover;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(0,0,0,.12);
}
@media (max-width: 1024px) {
    .process-map-head { grid-template-columns: 1fr; }
    .process-flow { grid-template-columns: 1fr; gap: 10px; }
    .flow-arrow, .flow-arrow.down { grid-column: auto; transform: rotate(90deg); }
    .flow-card { min-height: 110px; }
    .process-gallery-mini { grid-template-columns: repeat(3, 1fr); gap: 8px; }
    .process-bottom-note { font-size: 16px; }
}


/* Parent menu buttons with submenus are not direct links */
.dropbtn.parent-only {
    cursor: default;
}
.dropbtn.parent-only:focus {
    outline: none;
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
<div class="dropdown"><button class="dropbtn parent-only" type="button">Giới thiệu</button><div class="dropdown-content"><a href="?page=cauchuyen" target="_self">Câu chuyện Cốm Làng Vòng</a><a href="?page=video" target="_self">Hành trình hương cốm</a></div></div>
<div class="dropdown"><a href="?page=quytrinh" target="_self" style="text-decoration:none;"><button class="dropbtn">Quy trình & nguồn gốc</button></a></div>
<div class="dropdown"><button class="dropbtn parent-only" type="button">Sản phẩm</button><div class="dropdown-content"><a href="?page=sanpham" target="_self">Danh sách sản phẩm</a><a href="?page=congthuc" target="_self">Công thức & Cách làm món ăn</a></div></div>
<div class="dropdown"><a href="?page=chatluong" target="_self" style="text-decoration:none;"><button class="dropbtn">Chất lượng</button></a></div>
<div class="dropdown"><button class="dropbtn parent-only" type="button">Bao bì & bảo quản</button><div class="dropdown-content"><a href="?page=muc_giay" target="_self">Mực & giấy bao bì</a><a href="?page=thuhoi" target="_self">Chính sách thu hồi</a></div></div>
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
    conn.execute(
        """CREATE TABLE production_areas (
            area_id TEXT PRIMARY KEY,
            title TEXT,
            subtitle TEXT,
            description TEXT,
            function_text TEXT,
            hygiene_text TEXT,
            control_text TEXT,
            sort_order INTEGER
        )"""
    )
    conn.execute(
        """CREATE TABLE production_area_bullets (
            area_id TEXT,
            content TEXT,
            sort_order INTEGER
        )"""
    )
    conn.execute(
        """CREATE TABLE production_area_images (
            area_id TEXT,
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
        "Bánh Cốm Truyền Thống": "Bánh cốm ra đời từ thế kỷ 19, khi làng nghề làm cốm tại Hà Nội – đặc biệt là làng Vòng và làng Mễ Trì – bắt đầu nổi tiếng. Ban đầu, cốm được gói trong lá sen để ăn trực tiếp, nhưng với sự sáng tạo của người dân, món bánh cốm ra đời, kết hợp cốm với nhân đậu xanh ngọt bùi, trở thành món quà cưới hỏi không thể thiếu của người Việt.",
        "Bánh Chưng Cốm": "Bánh chưng cốm là cách kể mới của món bánh ngày Tết. Sắc xanh của cốm làm chiếc bánh trở nên mềm mại hơn, vừa quen thuộc như mâm cơm sum họp, vừa có hương thơm rất riêng của làng nghề Hà Nội.",
        "Bánh Trung Thu Cốm": "Bánh trung thu cốm mang hương mùa thu vào đêm rằm. Khi cắt bánh, mùi cốm dịu nhẹ hòa cùng vị ngọt của nhân tạo cảm giác ấm áp, như một món quà dành cho gia đình trong khoảnh khắc đoàn viên.",
        "Bánh Xu Xê Cốm": "Bánh xu xê (hay phu thê) là loại bánh ngọt cổ truyền mang ý nghĩa gắn kết tình cảm lứa đôi. Tại Làng Vòng (Hà Nội), món ăn này được biến tấu đầy tinh tế khi kết hợp vỏ bánh dẻo dai từ lá dứa cùng phần nhân cốm tươi, dừa sợi thơm lừng.",
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
            detail_url = page_url("chitietsp", product_index=index)
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




def render_recipe_book_page():
    """Render a Heyzine-like flipbook viewer using StPageFlip when available."""
    import json
    from urllib.parse import quote

    # Avoid Streamlit WebSocket errors by not embedding all flipbook pages as base64.
    # The page images are loaded from the public GitHub raw URL instead.
    raw_asset_base = "https://raw.githubusercontent.com/PhamNguyenCatTuong/COM-LANG-VONG/main/"

    recipe_pages = [
        {"name": "Chuyện bếp mùa Cốm", "file": "1.jpg"},
        {"name": "Chè cốm", "file": "2.jpg"},
        {"name": "Chả cốm", "file": "3.jpg"},
        {"name": "Cốm xào dừa/Tôm tẩm cốm chiên giòn", "file": "4.jpg"},
        {"name": "Bánh cốm nếp nương", "file": "5.jpg"},
        {"name": "Bánh xu xê cốm", "file": "6.jpg"},
        {"name": "Sữa chua cốm", "file": "7.jpg"},
        {"name": "Xôi cốm", "file": "8.jpg"},
        {"name": "Mochi cốm", "file": "9.jpg"},
        {"name": "Bánh trung thu nhân cốm", "file": "10.jpg"},
        {"name": "Bánh chưng nhân cốm", "file": "11.jpg"},
    ]

    pages_payload = []
    for item in recipe_pages:
        image_path = resolve_asset_path(item["file"])
        pages_payload.append(
            {
                "name": item["name"],
                "file": item["file"],
                "src": raw_asset_base + quote(item["file"]) if image_path.exists() else "",
                "exists": image_path.exists(),
            }
        )

    pages_json = json.dumps(pages_payload, ensure_ascii=False)

    html = """
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script src="https://cdn.jsdelivr.net/npm/page-flip@2.0.7/dist/js/page-flip.browser.min.js"></script>
<style>
* { box-sizing: border-box; }
html, body {
    margin: 0;
    padding: 0;
    overflow: hidden;
    background: transparent;
    font-family: Arial, Helvetica, sans-serif;
}
.viewer {
    width: 100%;
    min-height: 720px;
    padding: 8px 10px 10px;
    border-radius: 28px;
    background: transparent !important;
    
    position: relative;
    box-shadow: none !important;
}
.viewer-top {
    max-width: 1040px;
    margin: 0 auto 4px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
}
.viewer-title {
    min-width: 0;
}
.viewer-title h2 {
    margin: 0;
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(22px, 3.4vw, 34px);
    line-height: 1;
    
}
.viewer-title p {
    margin: 1px 0 0;
    
    font-size: 13px;
}
.toolbar {
    display: inline-flex;
    align-items: center;
    gap: 5px;
    padding: 4px;
    border-radius: 999px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.12);
    box-shadow: inset 0 1px 0 rgba(255,255,255,.1);
}
.tool-btn {
    width: 30px;
    height: 30px;
    border: 0;
    border-radius: 50%;
    background: rgba(255,255,255,.12);
    
    font-size: 18px;
    font-weight: 900;
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    transition: transform .16s ease, background .16s ease, opacity .16s ease;
}
.tool-btn:hover {
    background: rgba(255,255,255,.22);
    transform: translateY(-1px);
}
.tool-btn:disabled {
    opacity: .34;
    cursor: not-allowed;
    transform: none;
}
.book-stage {
    max-width: 1040px;
    margin: 0 auto;
    min-height: 285px;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    perspective: 2800px;
}
.book-shell {
    position: relative;

    width: min(100%, 980px);

    aspect-ratio: 2400 / 1400;

    height: auto;

    display: flex;
    align-items: center;
    justify-content: center;

    overflow: hidden;
}
.book-shell::before {
    content: none !important;
    display: none !important;
}
#book {
    width: 100%;
    height: 100%;
    position: relative;
}
.page {
    background: transparent !important;
    overflow: hidden;
    box-shadow: none !important;
}
.page::before {
    content: none !important;
    display: none !important;
}
.page img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    background: transparent !important;
    user-select: none;
    -webkit-user-drag: none;
}
.page.cover img {
    object-fit: contain;
}

/* Remove artificial cream/white sheet behind recipe spreads. */
.page,
.stf__item,
.stf__block {
    background: transparent !important;
}

.page img {
    background: transparent !important;
}

.page-placeholder {
    height: 100%;
    width: 100%;
    display: grid;
    place-items: center;
    padding: 30px;
    text-align: center;
    color: #7b5b2d;
    background: #fbf6e8;
    font-weight: 900;
    line-height: 1.5;
}
.side-nav {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    z-index: 30;
    width: 42px;
    height: 42px;
    border: 0;
    border-radius: 50%;
    background: rgba(15,17,18,.72);
    color: white;
    font-size: 30px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 12px 30px rgba(0,0,0,.38);
    backdrop-filter: blur(8px);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: .16s ease;
}
.side-nav:hover {
    background: rgba(46,125,50,.92);
    transform: translateY(-50%) scale(1.04);
}
.side-nav:disabled {
    opacity: .28;
    cursor: not-allowed;
    transform: translateY(-50%);
}
.side-nav.prev { left: 0; }
.side-nav.next { right: 0; }
.status-row {
    max-width: 1040px;
    margin: 6px auto 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 6px;
    
    font-size: 13px;
    font-weight: 800;
}
.page-label {
    
    max-width: 56%;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.counter-pill {
    flex-shrink: 0;
    border-radius: 999px;
    padding: 4px 10px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.12);
    
}
.progress {
    max-width: 1040px;
    height: 6px;
    margin: 6px auto 0;
    border-radius: 999px;
    background: rgba(255,255,255,.12);
    overflow: hidden;
}
.progress span {
    display: block;
    width: 0%;
    height: 100%;
    border-radius: 999px;
    background: linear-gradient(90deg, #d6b15e, #8bc34a);
    transition: width .32s ease;
}
.thumb-strip {
    max-width: 1040px;
    margin: 8px auto 0;
    display: flex;
    gap: 10px;
    overflow-x: auto;
    padding: 3px 4px 6px;
    scroll-snap-type: x proximity;
}
.thumb-strip::-webkit-scrollbar { height: 6px; }
.thumb-strip::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,.25);
    border-radius: 999px;
}
.thumb {
    flex: 0 0 68px;
    height: 48px;
    border: 2px solid transparent;
    border-radius: 10px;
    padding: 0;
    background: rgba(255,255,255,.1);
    overflow: hidden;
    cursor: pointer;
    scroll-snap-align: center;
    opacity: .65;
    transition: .16s ease;
}
.thumb img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
}
.thumb.active {
    opacity: 1;
    border-color: #d6b15e;
    box-shadow: 0 0 0 3px rgba(214,177,94,.18);
}
.thumb.missing-thumb {
    
    font-size: 11px;
    font-weight: 800;
}
.loading {
    position: absolute;
    inset: 0;
    display: grid;
    place-items: center;
    
    font-weight: 900;
    letter-spacing: .2px;
    z-index: 60;
    background: rgba(255,255,255,.12);
    backdrop-filter: blur(3px);
}
.viewer.fullscreen {
    min-height: 100vh;
    height: 100vh;
    border-radius: 0;
}
.viewer.fullscreen .book-stage { min-height: calc(100vh - 190px); }
.viewer.fullscreen .book-shell { height: calc(100vh - 240px); max-height: 820px; }
@media (max-width: 760px) {
    .viewer {
        min-height: 650px;
        padding: 6px;
        border-radius: 22px;
    }
    .viewer-top {
        flex-direction: column;
        align-items: stretch;
        text-align: center;
        margin-bottom: 2px;
    }
    .toolbar {
        align-self: center;
        transform: scale(.86);
    }
    .book-stage {
        min-height: 245px;
    }
    .book-shell {
        width: 100%;
        aspect-ratio: 2400 / 1400;
        height: auto;
    }
    .side-nav {
        width: 44px;
        height: 44px;
        font-size: 30px;
        background: rgba(15,17,18,.56);
    }
    .side-nav.prev { left: 4px; }
    .side-nav.next { right: 4px; }
    .status-row {
        justify-content: center;
        flex-wrap: wrap;
        text-align: center;
        gap: 8px;
    }
    .page-label {
        max-width: 100%;
        flex-basis: 100%;
    }
    .thumb { flex-basis: 58px; height: 42px; }
}
@media (max-width: 420px) {
    .book-shell {
        width: 100%;
        aspect-ratio: 2400 / 1400;
        height: auto;
    }
    .book-stage { min-height: 230px; }
    .viewer { min-height: 620px; }
}

/* COMPACT MOBILE FLIPBOOK SPACING */
.viewer-top { line-height: 1.05; }
.viewer-title h2 { margin-bottom: 0 !important; }
.viewer-title p { line-height: 1.15 !important; }
.toolbar { margin-top: 2px !important; margin-bottom: 2px !important; }
.book-stage { margin-top: 4px !important; margin-bottom: 4px !important; }
.status-row { margin-top: 6px !important; line-height: 1.1 !important; }
.progress { margin-top: 6px !important; }
.thumb-strip { margin-top: 8px !important; padding-bottom: 4px !important; }

@media (max-width: 760px) {
    .viewer-top { gap: 4px !important; }
    .viewer-title h2 { font-size: 30px !important; line-height: 1 !important; }
    .viewer-title p { font-size: 14px !important; margin-top: 2px !important; }
    .toolbar { transform: scale(.82) !important; transform-origin: center top !important; }
    .book-stage { min-height: 235px !important; }
    .status-row { margin-top: 4px !important; }
    .page-label { font-size: 18px !important; }
    .counter-pill { font-size: 16px !important; padding: 3px 9px !important; }
}


/* REMOVE DARK VIEWER BACKGROUND */
.viewer,
.book-stage,
.book-shell,
#book {
    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
}
.book-shell::before {
    content: none !important;
    display: none !important;
}



/* ONLY submenu compact spacing */
.submenu-list{
    gap:4px !important;
}
.submenu-item{
    min-height:34px !important;
    padding:8px 14px !important;
    margin-bottom:4px !important;
}


/* FIX PALE TEXT */
.viewer-title,
.viewer-title h1,
.viewer-title h2,
.viewer-subtitle,
.page-caption,
.page-label,
.counter-pill,
.toolbar,
.status-row{
    color:#17351f !important;
}

/* submenu text only */
.submenu-item,
.submenu-item .title,
.submenu-item .desc{
    color:#17351f !important;
}

</style>
</head>
<body>
<div class="viewer" id="viewer">
    <div class="viewer-top">
        <div class="viewer-title">
            <h2>Sổ Tay Công Thức Cốm</h2>
            <p>Kéo mép trang hoặc bấm mũi tên để lật sách</p>
        </div>
        <div class="toolbar">
            <button class="tool-btn" id="firstBtn" title="Trang đầu">⏮</button>
            <button class="tool-btn" id="prevBtnTop" title="Trang trước">‹</button>
            <button class="tool-btn" id="soundBtn" title="Bật/tắt âm">🔊</button>
            <button class="tool-btn" id="zoomBtn" title="Phóng to">＋</button>
            <button class="tool-btn" id="fullBtn" title="Toàn màn hình">⛶</button>
            <button class="tool-btn" id="nextBtnTop" title="Trang sau">›</button>
            <button class="tool-btn" id="lastBtn" title="Trang cuối">⏭</button>
        </div>
    </div>

    <div class="book-stage">
        <button class="side-nav prev" id="prevBtn">‹</button>
        <div class="book-shell" id="bookShell">
            <div id="book"></div>
            <div class="loading" id="loading">Đang tải sách...</div>
        </div>
        <button class="side-nav next" id="nextBtn">›</button>
    </div>

    <div class="status-row">
        <div class="page-label" id="pageName">Đang tải...</div>
        <div class="counter-pill" id="pageInfo">Trang 1 / 1</div>
    </div>
    <div class="progress"><span id="progressBar"></span></div>
    <div class="thumb-strip" id="thumbStrip"></div>
</div>

<script>
const pages = __PAGES_JSON__;
const viewer = document.getElementById("viewer");
const bookEl = document.getElementById("book");
const bookShell = document.getElementById("bookShell");
const loading = document.getElementById("loading");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");
const prevBtnTop = document.getElementById("prevBtnTop");
const nextBtnTop = document.getElementById("nextBtnTop");
const firstBtn = document.getElementById("firstBtn");
const lastBtn = document.getElementById("lastBtn");
const soundBtn = document.getElementById("soundBtn");
const zoomBtn = document.getElementById("zoomBtn");
const fullBtn = document.getElementById("fullBtn");
const pageName = document.getElementById("pageName");
const pageInfo = document.getElementById("pageInfo");
const progressBar = document.getElementById("progressBar");
const thumbStrip = document.getElementById("thumbStrip");

let pageFlip = null;
let current = 0;
let soundEnabled = true;
let zoomed = false;
let isFallback = false;

function makePageHTML(page, idx) {
    const coverClass = idx === 0 ? " cover" : "";
    if (page.exists && page.src) {
        return `<div class="page${coverClass}" data-page="${idx}"><img src="${page.src}" alt="${page.name}"></div>`;
    }
    return `<div class="page${coverClass}" data-page="${idx}"><div class="page-placeholder">Không tìm thấy ảnh ${page.file}<br>Hãy đặt ảnh cùng cấp file app.py</div></div>`;
}

function renderPages() {
    bookEl.innerHTML = pages.map(makePageHTML).join("");
    thumbStrip.innerHTML = "";
    pages.forEach((page, idx) => {
        const btn = document.createElement("button");
        btn.className = "thumb";
        btn.title = page.name;
        if (page.exists && page.src) {
            btn.innerHTML = `<img src="${page.src}" alt="${page.name}">`;
        } else {
            btn.classList.add("missing-thumb");
            btn.textContent = idx + 1;
        }
        btn.addEventListener("click", () => {
            if (pageFlip && !isFallback) {
                pageFlip.flip(idx, "top");
            } else {
                fallbackGo(idx);
            }
        });
        thumbStrip.appendChild(btn);
    });
}

function playFlipSound() {
    if (!soundEnabled) return;
    try {
        const AudioContext = window.AudioContext || window.webkitAudioContext;
        const ctx = new AudioContext();
        if (ctx.state === "suspended") ctx.resume();

        const duration = 0.42;
        const bufferSize = Math.floor(ctx.sampleRate * duration);
        const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        const data = buffer.getChannelData(0);

        for (let i = 0; i < bufferSize; i++) {
            const t = i / bufferSize;
            const paper = (Math.random() * 2 - 1) * Math.pow(1 - t, 2.6);
            const brush = Math.sin(t * Math.PI * 58) * Math.pow(1 - t, 4);
            data[i] = (paper * 0.22) + (brush * 0.018);
        }

        const source = ctx.createBufferSource();
        const filter = ctx.createBiquadFilter();
        const gain = ctx.createGain();

        source.buffer = buffer;
        filter.type = "bandpass";
        filter.frequency.setValueAtTime(1800, ctx.currentTime);
        filter.frequency.exponentialRampToValueAtTime(330, ctx.currentTime + duration);

        gain.gain.setValueAtTime(0.001, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.16, ctx.currentTime + 0.05);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

        source.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        source.start();
        source.stop(ctx.currentTime + duration);
    } catch (err) {}
}

function updateUI(index) {
    current = Math.max(0, Math.min(index, pages.length - 1));
    const page = pages[current] || pages[0];

    pageName.textContent = page ? page.name : "";
    pageInfo.textContent = `Trang ${current + 1} / ${pages.length}`;
    progressBar.style.width = `${((current + 1) / pages.length) * 100}%`;

    const atStart = current <= 0;
    const atEnd = current >= pages.length - 1;
    prevBtn.disabled = atStart;
    prevBtnTop.disabled = atStart;
    firstBtn.disabled = atStart;
    nextBtn.disabled = atEnd;
    nextBtnTop.disabled = atEnd;
    lastBtn.disabled = atEnd;

    [...thumbStrip.children].forEach((btn, idx) => {
        btn.classList.toggle("active", idx === current);
        if (idx === current) {
            btn.scrollIntoView({ inline: "center", block: "nearest", behavior: "smooth" });
        }
    });
}

function initPageFlip() {
    renderPages();

    if (!window.St || !window.St.PageFlip) {
        initFallback();
        return;
    }

    const mobile = window.matchMedia("(max-width: 760px)").matches;
    const rect = bookShell.getBoundingClientRect();
    const width = Math.max(320, Math.floor(rect.width / (mobile ? 1 : 2)));
    const height = Math.max(430, Math.floor(rect.height));

    pageFlip = new St.PageFlip(bookEl, {
        width: width,
        height: height,
        size: "stretch",
        minWidth: 280,
        maxWidth: 560,
        minHeight: 380,
        maxHeight: 760,
        drawShadow: true,
        flippingTime: 1450,
        usePortrait: mobile,
        startZIndex: 10,
        autoSize: true,
        maxShadowOpacity: 0.42,
        showCover: true,
        mobileScrollSupport: false,
        swipeDistance: 18,
        clickEventForward: true,
        disableFlipByClick: false
    });

    pageFlip.loadFromHTML(document.querySelectorAll(".page"));
    pageFlip.on("flip", (event) => {
        playFlipSound();
        updateUI(event.data);
    });
    pageFlip.on("changeState", (event) => {
        if (event.data === "flipping") playFlipSound();
    });

    setTimeout(() => {
        loading.style.display = "none";
        updateUI(pageFlip.getCurrentPageIndex());
    }, 350);
}

function initFallback() {
    isFallback = true;
    loading.style.display = "none";
    bookEl.classList.add("fallback-book");
    const style = document.createElement("style");
    style.textContent = `
        #book.fallback-book { display:block; position:relative; width:100%; height:100%; }
        #book.fallback-book .page { display:none; width:100%; height:100%; border-radius:18px; }
        #book.fallback-book .page.active { display:block; animation:fallbackFade .45s ease; }
        @keyframes fallbackFade { from { opacity:.35; transform:scale(.985); } to { opacity:1; transform:scale(1); } }
    `;
    document.head.appendChild(style);
    fallbackGo(0);
}

function fallbackGo(index) {
    current = Math.max(0, Math.min(index, pages.length - 1));
    [...bookEl.querySelectorAll(".page")].forEach((page, idx) => {
        page.classList.toggle("active", idx === current);
    });
    playFlipSound();
    updateUI(current);
}

function flipPrev() {
    if (pageFlip && !isFallback) pageFlip.flipPrev("top");
    else fallbackGo(current - 1);
}
function flipNext() {
    if (pageFlip && !isFallback) pageFlip.flipNext("top");
    else fallbackGo(current + 1);
}

prevBtn.addEventListener("click", flipPrev);
prevBtnTop.addEventListener("click", flipPrev);
nextBtn.addEventListener("click", flipNext);
nextBtnTop.addEventListener("click", flipNext);
firstBtn.addEventListener("click", () => pageFlip && !isFallback ? pageFlip.flip(0, "top") : fallbackGo(0));
lastBtn.addEventListener("click", () => pageFlip && !isFallback ? pageFlip.flip(pages.length - 1, "top") : fallbackGo(pages.length - 1));

soundBtn.addEventListener("click", () => {
    soundEnabled = !soundEnabled;
    soundBtn.textContent = soundEnabled ? "🔊" : "🔇";
});

zoomBtn.addEventListener("click", () => {
    zoomed = !zoomed;
    bookShell.style.transform = zoomed ? "scale(1.12)" : "scale(1)";
    bookShell.style.transition = "transform .25s ease";
    zoomBtn.textContent = zoomed ? "－" : "＋";
});

fullBtn.addEventListener("click", async () => {
    try {
        if (!document.fullscreenElement) {
            await viewer.requestFullscreen();
            viewer.classList.add("fullscreen");
        } else {
            await document.exitFullscreen();
            viewer.classList.remove("fullscreen");
        }
        setTimeout(() => {
            if (pageFlip && !isFallback) pageFlip.update();
        }, 250);
    } catch (err) {
        viewer.classList.toggle("fullscreen");
        setTimeout(() => {
            if (pageFlip && !isFallback) pageFlip.update();
        }, 250);
    }
});

document.addEventListener("fullscreenchange", () => {
    if (!document.fullscreenElement) viewer.classList.remove("fullscreen");
});

document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") flipPrev();
    if (event.key === "ArrowRight") flipNext();
    if (event.key === "Home") pageFlip && !isFallback ? pageFlip.flip(0, "top") : fallbackGo(0);
    if (event.key === "End") pageFlip && !isFallback ? pageFlip.flip(pages.length - 1, "top") : fallbackGo(pages.length - 1);
});

window.addEventListener("resize", () => {
    if (pageFlip && !isFallback) {
        clearTimeout(window.__flipResize);
        window.__flipResize = setTimeout(() => pageFlip.update(), 220);
    }
});

initPageFlip();
</script>
</body>
</html>
""".replace("__PAGES_JSON__", pages_json)

    components.html(html, height=620, scrolling=False)

def render_recipe_index_page():
    """Render a recipe index so the menu item Công thức & Cách làm món ăn has a useful page."""
    html = (
        "<div class='card'>"
        "<h3>🍽️ Công thức & Cách làm món ăn</h3>"
        "<p>Chọn món bên dưới để xem nguyên liệu chi tiết, cách làm minh họa, lưu ý chế biến và giá trị dinh dưỡng.</p>"
        "</div>"
    )

    html += "<section class='product-section'><div class='product-grid'>"

    for index, product in enumerate(PRODUCTS):
        detail_url = page_url("chitietsp", product_index=index)
        html += (
            f"<div class='product-card'>"
            f"<a href='{detail_url}' target='_self' class='product-card-link'>"
            f"{render_product_image(product)}"
            f"<div class='product-info'>"
            f"<h3>{product['name']}</h3>"
            f"<p>Xem công thức và cách làm chi tiết</p>"
            f"</div>"
            f"</a>"
            f"</div>"
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
            f'<a href="{page_url("chitietsp", product_index=index)}" target="_self" class="compact-product-card">'
            f'{render_product_image(product)}'
            f'<h4>{product["name"]}</h4>'
            f'<div class="compact-price">{product["price"]}</div>'
            f'</a>'
            f'<div class="compact-actions">'
            f'<a href="tel:0385437503">MUA NGAY</a>'
            f'<a href="{page_url("chitietsp", product_index=index, add_cart=index)}" target="_self">THÊM GIỎ HÀNG</a>'
            f'</div>'
            f'</div>'
        )
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)



def get_recipe_ingredient_data(product):
    """Return detailed ingredient data for recipe views."""
    name = product.get("name", "sản phẩm")

    ingredient_data = {
        "Bánh Cốm Truyền Thống": {
            "serving": "Cho 10 cái",
            "items": [
                ("Cốm khô", "300 gram", ""),
                ("Đậu xanh", "50 gram", "(đã cà vỏ ngâm mềm)"),
                ("Đường cát", "80 gram", "(có thể tăng giảm tùy khẩu vị)"),
                ("Bột nếp", "3 muỗng canh", ""),
                ("Dầu ăn", "1 muỗng canh", ""),
                ("Lá dứa", "20 gram", "(4 lá)"),
                ("Nước hoa bưởi", "10 ml", ""),
            ],
        },
        "Bánh Xu Xê Cốm": {
            "serving": "Cho 33 - 35 viên bánh",
            "items": [
                ("Bột năng", "200 gr", ""),
                ("Cốm khô", "200 gr", ""),
                ("Dừa non nạo sợi", "200 gr", ""),
                ("Nước cốt dừa", "100 gr", ""),
                ("Đường", "210 gr", ""),
                ("Lá dứa", "14 lá", "(lá nếp)"),
                ("Muối", "1 ít", ""),
                ("Tinh chất lá dứa", "1 ít", "(tùy chọn)"),
                ("Vừng rang", "1 ít", ""),
                ("Dầu ăn", "2 thìa cà phê", ""),
            ],
        },
        "Bánh Chưng Cốm": {
            "serving": "Cho 10 cái",
            "items": [
                ("Gạo nếp", "2 kg", ""),
                ("Cốm dẹp", "1 kg", ""),
                ("Thịt ba chỉ", "800 gr", ""),
                ("Đậu xanh", "800 gr", "(cà vỏ)"),
                ("Dầu ăn", "7 muỗng canh", ""),
                ("Gia vị thông dụng", "1 ít", "(muối/ tiêu/ bột ngọt)"),
            ],
        },
        "Bánh Trung Thu Cốm": {
            "serving": "Cho 7 chiếc bánh 150gr",
            "items": [
                ("Bột mì đa dụng", "300 gr", ""),
                ("Cốm khô", "150 gr", ""),
                ("Dừa tươi bào sợi", "150 gr", ""),
                ("Nước đường làm bánh nướng", "200 gr", ""),
                ("Đường", "60 gr", ""),
                ("Dầu ăn", "45 gr", ""),
                ("Nước dừa tươi", "150 gr", "(có thể thay bằng nước lọc)"),
                ("Nước cốt dừa", "50 gr", ""),
                ("Lòng đỏ trứng gà", "2 quả", ""),
                ("Rượu mai quế lộ", "1 muỗng canh", ""),
                ("Bơ đậu phộng", "1 muỗng cà phê", ""),
                ("Hương cốm", "5 gr", ""),
                ("Nước", "1 muỗng canh", "(hoặc sữa tươi)"),
                ("Dầu mè", "1 muỗng cà phê", ""),
            ],
        },
        "Cốm Xào Dừa": {
            "serving": "Cho 2 người",
            "items": [
                ("Cốm dẹp", "150 gr", ""),
                ("Nước dừa", "200 ml", ""),
                ("Dừa nạo", "25 gr", ""),
                ("Đường", "4 muỗng canh", ""),
            ],
        },
        "Mochi Cốm": {
            "serving": "Cho 8 chiếc bánh",
            "items": [
                ("Cốm tươi", "150 gr", "(hoặc 100 gram cốm khô)"),
                ("Đậu xanh khô", "100 gr", "(loại đã tách vỏ)"),
                ("Nước cốt dừa", "180 gr", "(100gr dùng làm vỏ bánh và 80gr sên nhân)"),
                ("Nước dừa tươi", "120 gr", ""),
                ("Đường vàng", "60 gr", ""),
                ("Dầu ăn", "42 gr", ""),
                ("Tinh chất lá dứa", "1 ít", "(khoảng 2 hoặc 3 giọt)"),
                ("Màu thực phẩm vàng", "1 ít", "(có thể bỏ qua)"),
                ("Muối", "1 ít", ""),
                ("Cơm dừa sấy khô", "1 ít", ""),
            ],
        },
        "Sữa Chua Cốm": {
            "serving": "Cho 50 hũ",
            "items": [
                ("Cốm xanh", "300 gr", "(hạt tròn)"),
                ("Sữa chua không đường", "2 hộp", ""),
                ("Sữa đặc", "380 gr", ""),
                ("Sữa tươi không đường", "1 lít", ""),
                ("Bột kem béo", "300 gr", ""),
                ("Bột năng", "120 gr", ""),
                ("Lá dứa", "3 cái", ""),
                ("Đường", "600 gr", ""),
                ("Muối", "2 gr", ""),
            ],
        },
        "Tôm Tẩm Cốm": {
            "serving": "Cho 2 người",
            "items": [
                ("Tôm", "500 gr", ""),
                ("Cốm dẹp", "200 gr", ""),
                ("Bột chiên giòn", "150 gr", ""),
                ("Trứng gà", "2 quả", ""),
                ("Tỏi băm", "1 muỗng cà phê", ""),
                ("Dầu ăn", "30 ml", ""),
                ("Gia vị thông dụng", "1 ít", "(tiêu/ đường/ hạt nêm/ bột ngọt)"),
            ],
        },
        "Xôi Cốm": {
            "serving": "Cho 1 món xôi cốm",
            "items": [
                ("Cốm tươi", "400g", "(chọn cốm màu xanh nhẹ, hơi ngả vàng, loại mỏng nhưng dẻo và chắc)"),
                ("Đậu xanh", "100g", ""),
                ("Hạt sen", "100g", ""),
                ("Dừa sợi", "120g", ""),
                ("Nước cốt dừa", "vừa đủ", ""),
                ("Lá nếp thơm", "vừa đủ", "(lá dứa)"),
                ("Gia vị", "Muối, đường", ""),
                ("Dụng cụ", "Xửng hấp, lá sen", "(nếu có)"),
            ],
        },
    }

    return ingredient_data.get(
        name,
        {
            "serving": "Cho 4 phần",
            "items": [
                ("Nguyên liệu chính", "vừa đủ", ""),
                ("Gia vị", "vừa đủ", ""),
                ("Nguyên liệu phụ", "tùy sản phẩm", ""),
                ("Bao bì thực phẩm sạch", "vừa đủ", ""),
            ],
        },
    )


def build_ingredients_card(product):
    """Return an HTML ingredients card rendered like a recipe box."""
    name = product.get("name", "sản phẩm")

    ingredient_data = {
        "Bánh Cốm Truyền Thống": {
            "serving": "Cho 10 cái",
            "items": [
                ("Cốm khô", "300 gram", ""),
                ("Đậu xanh", "50 gram", "(đã cà vỏ ngâm mềm)"),
                ("Đường cát", "80 gram", "(có thể tăng giảm tùy khẩu vị)"),
                ("Bột nếp", "3 muỗng canh", ""),
                ("Dầu ăn", "1 muỗng canh", ""),
                ("Lá dứa", "20 gram", "(4 lá)"),
                ("Nước hoa bưởi", "10 ml", ""),
            ],
        },
        "Bánh Xu Xê Cốm": {
            "serving": "Cho 33 - 35 viên bánh",
            "items": [
                ("Bột năng", "200 gr", ""),
                ("Cốm khô", "200 gr", ""),
                ("Dừa non nạo sợi", "200 gr", ""),
                ("Nước cốt dừa", "100 gr", ""),
                ("Đường", "210 gr", ""),
                ("Lá dứa", "14 lá", "(lá nếp)"),
                ("Muối", "1 ít", ""),
                ("Tinh chất lá dứa", "1 ít", "(tùy chọn)"),
                ("Vừng rang", "1 ít", ""),
                ("Dầu ăn", "2 thìa cà phê", ""),
            ],
        },
        "Bánh Chưng Cốm": {
            "serving": "Cho 10 cái",
            "items": [
                ("Gạo nếp", "2 kg", ""),
                ("Cốm dẹp", "1 kg", ""),
                ("Thịt ba chỉ", "800 gr", ""),
                ("Đậu xanh", "800 gr", "(cà vỏ)"),
                ("Dầu ăn", "7 muỗng canh", ""),
                ("Gia vị thông dụng", "1 ít", "(muối/ tiêu/ bột ngọt)"),
            ],
        },
        "Bánh Trung Thu Cốm": {
            "serving": "Cho 7 chiếc bánh 150gr",
            "items": [
                ("Bột mì đa dụng", "300 gr", ""),
                ("Cốm khô", "150 gr", ""),
                ("Dừa tươi bào sợi", "150 gr", ""),
                ("Nước đường làm bánh nướng", "200 gr", ""),
                ("Đường", "60 gr", ""),
                ("Dầu ăn", "45 gr", ""),
                ("Nước dừa tươi", "150 gr", "(có thể thay bằng nước lọc)"),
                ("Nước cốt dừa", "50 gr", ""),
                ("Lòng đỏ trứng gà", "2 quả", ""),
                ("Rượu mai quế lộ", "1 muỗng canh", ""),
                ("Bơ đậu phộng", "1 muỗng cà phê", ""),
                ("Hương cốm", "5 gr", ""),
                ("Nước", "1 muỗng canh", "(hoặc sữa tươi)"),
                ("Dầu mè", "1 muỗng cà phê", ""),
            ],
        },
        "Cốm Mộc": {
            "serving": "Cho 500 gram",
            "items": [
                ("Lúa nếp non", "1 kg", ""),
                ("Lá sen", "vài lá", "(dùng để ủ và gói cốm)"),
                ("Nước sạch", "vừa đủ", ""),
            ],
        },
        "Cốm Xào Dừa": {
            "serving": "Cho 2 người",
            "items": [
                ("Cốm dẹp", "150 gr", ""),
                ("Nước dừa", "200 ml", ""),
                ("Dừa nạo", "25 gr", ""),
                ("Đường", "4 muỗng canh", ""),
            ],
        },
        "Mochi Cốm": {
            "serving": "Cho 8 chiếc bánh",
            "items": [
                ("Cốm tươi", "150 gr", "(hoặc 100 gram cốm khô)"),
                ("Đậu xanh khô", "100 gr", "(loại đã tách vỏ)"),
                ("Nước cốt dừa", "180 gr", "(100gr dùng làm vỏ bánh và 80gr sên nhân)"),
                ("Nước dừa tươi", "120 gr", ""),
                ("Đường vàng", "60 gr", ""),
                ("Dầu ăn", "42 gr", ""),
                ("Tinh chất lá dứa", "1 ít", "(khoảng 2 hoặc 3 giọt)"),
                ("Màu thực phẩm vàng", "1 ít", "(có thể bỏ qua)"),
                ("Muối", "1 ít", ""),
                ("Cơm dừa sấy khô", "1 ít", ""),
            ],
        },
        "Sữa Chua Cốm": {
            "serving": "Cho 50 hũ",
            "items": [
                ("Cốm xanh", "300 gr", "(hạt tròn)"),
                ("Sữa chua không đường", "2 hộp", ""),
                ("Sữa đặc", "380 gr", ""),
                ("Sữa tươi không đường", "1 lít", ""),
                ("Bột kem béo", "300 gr", ""),
                ("Bột năng", "120 gr", ""),
                ("Lá dứa", "3 cái", ""),
                ("Đường", "600 gr", ""),
                ("Muối", "2 gr", ""),
            ],
        },
        "Tôm Tẩm Cốm": {
            "serving": "Cho 2 người",
            "items": [
                ("Tôm", "500 gr", ""),
                ("Cốm dẹp", "200 gr", ""),
                ("Bột chiên giòn", "150 gr", ""),
                ("Trứng gà", "2 quả", ""),
                ("Tỏi băm", "1 muỗng cà phê", ""),
                ("Dầu ăn", "30 ml", ""),
                ("Gia vị thông dụng", "1 ít", "(tiêu/ đường/ hạt nêm/ bột ngọt)"),
            ],
        },
        "Bia Cốm Hà Nội": {
            "serving": "Cho 1 mẻ nhỏ",
            "items": [
                ("Malt", "theo công thức", ""),
                ("Hoa bia", "vừa đủ", ""),
                ("Men bia", "vừa đủ", ""),
                ("Nước", "theo dung tích nấu", ""),
                ("Hương cốm", "vừa đủ", ""),
            ],
        },
        "Xôi Cốm": {
            "serving": "Cho 1 món xôi cốm",
            "items": [
                ("Cốm tươi", "400g", "(chọn cốm màu xanh nhẹ, hơi ngả vàng, loại mỏng nhưng dẻo và chắc)"),
                ("Đậu xanh", "100g", ""),
                ("Hạt sen", "100g", ""),
                ("Dừa sợi", "120g", ""),
                ("Nước cốt dừa", "vừa đủ", ""),
                ("Lá nếp thơm", "vừa đủ", "(lá dứa)"),
                ("Gia vị", "Muối, đường", ""),
                ("Dụng cụ", "Xửng hấp, lá sen", "(nếu có)"),
            ],
        },
    }

    data = ingredient_data.get(
        name,
        {
            "serving": "Cho 4 phần",
            "items": [
                ("Nguyên liệu chính", "vừa đủ", ""),
                ("Gia vị", "vừa đủ", ""),
                ("Nguyên liệu phụ", "tùy sản phẩm", ""),
                ("Bao bì thực phẩm sạch", "vừa đủ", ""),
            ],
        },
    )

    rows = ""
    for item_name, amount, note in data["items"]:
        rows += (
            "<div class='ingredient-row'>"
            f"<div class='ingredient-main'><span class='ingredient-dot'>•</span> "
            f"<span class='ingredient-name'>{escape(item_name)}</span> "
            f"<span class='ingredient-amount'>{escape(amount)}</span></div>"
        )
        if note:
            rows += f"<div class='ingredient-note'>{escape(note)}</div>"
        rows += "</div>"

    return (
        "<div class='ingredient-card'>"
        "<div class='ingredient-head'>"
        f"<h3>Nguyên liệu làm {escape(name)}</h3>"
        f"<div class='ingredient-serving'>👥 {escape(data['serving'])}</div>"
        "</div>"
        f"<div class='ingredient-list'>{rows}</div>"
        "</div>"
    )


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

    # Lưu sản phẩm đã xem vào cả session_state và URL.
    # Quan trọng: mọi link nội bộ đều phải giữ tham số viewed, nếu không Streamlit có thể mất lịch sử khi chuyển trang.
    if "viewed_products" not in st.session_state:
        st.session_state.viewed_products = []

    url_viewed = get_viewed_products_from_url()
    merged_viewed = []
    for i in st.session_state.viewed_products + url_viewed:
        if i not in merged_viewed and 0 <= i < len(PRODUCTS):
            merged_viewed.append(i)

    old_viewed = [i for i in merged_viewed if i != product_index]
    st.session_state.viewed_products = [product_index] + old_viewed
    st.session_state.viewed_products = st.session_state.viewed_products[:8]

    new_viewed_param = ",".join(str(i) for i in st.session_state.viewed_products)
    if params.get("viewed", "") != new_viewed_param:
        st.query_params["page"] = "chitietsp"
        st.query_params["product"] = str(product_index)
        st.query_params["viewed"] = new_viewed_param
        st.rerun()

    product = PRODUCTS[product_index]
    ingredients, process, storage = build_product_details(product)
    story = build_product_story(product)
    notes = build_product_notes(product)
    nutrition = build_product_nutrition(product)

    # Trang chi tiết sản phẩm chỉ hiển thị thông tin mua hàng và giới thiệu.
    # Phần công thức/cách làm được giữ riêng trong menu "Công thức & Cách làm món ăn".

    html = (
        f"<a href='{page_url('sanpham')}' target='_self' class='back-products'>← Quay lại danh sách sản phẩm</a>"
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
        f"<a href='{page_url('chitietsp', product_index=product_index, add_cart=product_index)}' target='_self' class='cart-btn'>+ Giỏ hàng</a>"
        f"</div>"
        f"</div></div>"
        f"<div class='detail-block'><h3>Giới thiệu sản phẩm</h3><p>{story}</p><p>{product.get('desc', '')}</p></div>"
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
    """Render Quy trình & nguồn gốc with clean storytelling content and images inside each process step."""
    img_overview = image_to_data_uri("Com tong quan 3.jpg")
    img_grain = image_to_data_uri("Cau chuyen 1.jpg")
    img_rang = image_to_data_uri("rang com.jpg")
    img_gia = image_to_data_uri("gia com.jpg")
    img_thu_hoach = image_to_data_uri("hat com tuoi.jpg")
    img_sang = image_to_data_uri("sang com.jpg")
    img_sen = image_to_data_uri("Cau chuyen 2.jpg")
    img_com_moc = image_to_data_uri("com moc.jpg")
    img_banh_com = image_to_data_uri("Qua dac san.jpg")
    img_lang_nghe = image_to_data_uri("Huong vi lang nghe.jpg")
    img_mua_lua = image_to_data_uri("Mua lua lam nen hat com.jpg")

    html = f"""
<style>
.qn-page {{
    width:100%;
    margin:0 auto;
    padding:0 0 30px;
    color:#17351f;
}}
.qn-page * {{ box-sizing:border-box; }}
.qn-hero {{
    position:relative;
    overflow:hidden;
    border-radius:30px;
    padding:clamp(20px,4vw,42px);
    background:linear-gradient(135deg,#f6fbef 0%,#fffdf4 48%,#e8f4dc 100%);
    border:1px solid #dcebd3;
    box-shadow:0 12px 32px rgba(23,53,31,.08);
}}
.qn-hero::after {{
    content:"";
    position:absolute;
    right:-80px;
    top:-90px;
    width:240px;
    height:240px;
    border-radius:50%;
    background:rgba(139,195,74,.20);
}}
.qn-hero-grid {{
    position:relative;
    z-index:1;
    display:grid;
    grid-template-columns:minmax(0,1.05fr) minmax(240px,.95fr);
    gap:clamp(18px,4vw,34px);
    align-items:center;
}}
.qn-eyebrow {{
    display:inline-flex;
    align-items:center;
    gap:8px;
    background:#2e7d32;
    color:white;
    padding:9px 15px;
    border-radius:999px;
    font-size:13px;
    font-weight:900;
}}
.qn-hero h2 {{
    margin:16px 0 12px;
    font-size:clamp(32px,7vw,62px);
    line-height:1.02;
    letter-spacing:-1.2px;
    color:#14351d;
}}
.qn-hero p {{
    margin:0;
    color:#425344;
    font-size:clamp(15px,3.3vw,18px);
    line-height:1.72;
}}
.qn-hero-points {{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:10px;
    margin-top:18px;
}}
.qn-hero-points div {{
    background:rgba(255,255,255,.80);
    border:1px solid #dcebd3;
    border-radius:17px;
    padding:12px 13px;
    font-weight:900;
    color:#244128;
    line-height:1.35;
}}
.qn-collage {{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:10px;
}}
.qn-collage img {{
    width:100%;
    height:150px;
    object-fit:cover;
    border-radius:22px;
    box-shadow:0 10px 24px rgba(23,53,31,.13);
}}
.qn-collage img:first-child {{
    grid-column:1 / -1;
    height:230px;
}}
.qn-section {{ margin-top:30px; }}
.qn-section-head {{ margin-bottom:15px; }}
.qn-section h3 {{
    margin:0 0 9px;
    color:#14351d;
    font-size:clamp(25px,5vw,40px);
    line-height:1.12;
}}
.qn-section-head p {{
    margin:0;
    color:#536255;
    font-size:15.5px;
    line-height:1.68;
    max-width:880px;
}}
.qn-story-card {{
    display:grid;
    grid-template-columns:minmax(0,1fr) minmax(220px,360px);
    gap:18px;
    align-items:stretch;
    background:#fffdf4;
    border:1px solid #e4ead7;
    border-radius:26px;
    padding:18px;
}}
.qn-story-text {{ display:grid; gap:12px; }}
.qn-story-text p {{
    margin:0;
    color:#405442;
    font-size:15.5px;
    line-height:1.75;
}}
.qn-feature-grid {{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:10px;
    margin-top:2px;
}}
.qn-feature {{
    background:#f1f8e9;
    border:1px solid #dcebd3;
    border-radius:18px;
    padding:13px;
}}
.qn-feature strong {{
    display:block;
    color:#17351f;
    font-size:16px;
    margin-bottom:5px;
}}
.qn-feature span {{
    color:#536255;
    font-size:14px;
    line-height:1.55;
}}
.qn-story-image {{
    height:260px;
    min-height:260px;
    max-height:260px;
    overflow:hidden;
    border-radius:22px;
}}
.qn-story-image img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:22px;
    display:block;
}}
.qn-material-grid {{
    display:grid;
    grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);
    gap:16px;
}}
.qn-material-photo {{
    background:#f1f8e9;
    border-radius:24px;
    padding:10px;
    border:1px solid #dcebd3;
}}
.qn-material-photo {{
    height:260px;
    min-height:260px;
    max-height:260px;
    overflow:hidden;
    border-radius:18px;
}}
.qn-material-photo img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:18px;
    display:block;
}}
.qn-material-list {{ display:grid; gap:10px; }}
.qn-material-item {{
    background:white;
    border:1px solid #e3ead8;
    border-radius:20px;
    padding:15px;
    box-shadow:0 5px 14px rgba(23,53,31,.05);
}}
.qn-material-item h4 {{
    margin:0 0 6px;
    font-size:18px;
    color:#17351f;
}}
.qn-material-item p {{
    margin:0;
    color:#536255;
    line-height:1.62;
    font-size:14.5px;
}}
.qn-journey {{
    display:grid;
    gap:14px;
}}
.qn-journey-step {{
    display:grid;
    grid-template-columns:minmax(180px,285px) minmax(0,1fr);
    gap:14px;
    align-items:stretch;
    background:#fffdf4;
    border:1px solid #e3ead8;
    border-radius:24px;
    padding:12px;
    box-shadow:0 8px 20px rgba(23,53,31,.06);
}}
.qn-journey-img {{
    position:relative;
    height:260px;
    min-height:260px;
    max-height:260px;
    overflow:hidden;
    border-radius:18px;
}}
.qn-journey-img img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:18px;
    display:block;
}}
.qn-journey-icon {{
    position:absolute;
    left:10px;
    top:10px;
    width:48px;
    height:48px;
    border-radius:16px;
    display:grid;
    place-items:center;
    font-size:25px;
    background:linear-gradient(135deg,#2e7d32,#8bc34a);
    box-shadow:0 10px 18px rgba(46,125,50,.24);
}}
.qn-journey-body {{
    display:flex;
    flex-direction:column;
    justify-content:center;
    padding:8px 6px;
}}
.qn-journey-body h4 {{
    margin:0 0 7px;
    color:#17351f;
    font-size:clamp(19px,4.4vw,25px);
    line-height:1.2;
}}
.qn-journey-body p {{
    margin:0 0 10px;
    color:#536255;
    line-height:1.65;
    font-size:14.8px;
}}
.qn-mini-list {{
    display:flex;
    flex-wrap:wrap;
    gap:7px;
}}
.qn-mini-list span {{
    background:#eef8e7;
    border:1px solid #d6e8cd;
    color:#2d5d32;
    border-radius:999px;
    padding:6px 9px;
    font-size:12.5px;
    font-weight:800;
}}
.qn-quality-grid {{
    display:grid;
    grid-template-columns:repeat(4,minmax(0,1fr));
    gap:12px;
}}
.qn-quality {{
    background:linear-gradient(180deg,#ffffff,#f7fff3);
    border:1px solid #dcebd3;
    border-radius:22px;
    padding:16px;
}}
.qn-quality .qicon {{ font-size:30px; margin-bottom:8px; }}
.qn-quality h4 {{
    margin:0 0 7px;
    color:#17351f;
    font-size:18px;
}}
.qn-quality p {{
    margin:0;
    color:#536255;
    line-height:1.58;
    font-size:14px;
}}
.qn-final-note {{
    margin-top:18px;
    border-radius:24px;
    padding:18px;
    background:linear-gradient(135deg,#17351f,#2e7d32);
    color:white;
}}
.qn-final-note h4 {{
    margin:0 0 8px;
    color:white;
    font-size:22px;
}}
.qn-final-note p {{
    margin:0;
    color:rgba(255,255,255,.92);
    line-height:1.65;
}}
@media (max-width:900px) {{
    .qn-hero-grid,
    .qn-story-card,
    .qn-material-grid {{ grid-template-columns:1fr; }}
    .qn-quality-grid {{ grid-template-columns:repeat(2,minmax(0,1fr)); }}
    .qn-story-image {{
    height:260px;
    min-height:260px;
    max-height:260px;
    overflow:hidden;
    border-radius:22px;
}}
.qn-story-image img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:22px;
    display:block;
}}
}}
@media (max-width:640px) {{
    .qn-page {{ padding-bottom:18px; }}
    .qn-hero {{ border-radius:22px; padding:16px 13px; }}
    .qn-hero-points {{ grid-template-columns:1fr; gap:8px; }}
    .qn-collage {{ gap:8px; }}
    .qn-collage img {{ height:112px; border-radius:16px; }}
    .qn-collage img:first-child {{ height:165px; }}
    .qn-section {{ margin-top:24px; }}
    .qn-story-card {{ padding:12px; border-radius:21px; }}
    .qn-feature-grid {{ grid-template-columns:1fr; }}
    .qn-material-photo {{
    height:260px;
    min-height:260px;
    max-height:260px;
    overflow:hidden;
    border-radius:18px;
}}
.qn-material-photo img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:18px;
    display:block;
}}
    .qn-journey-step {{ grid-template-columns:1fr; padding:10px; border-radius:20px; }}
    .qn-journey-img, .qn-journey-img img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:18px;
    display:block;
}}
    .qn-journey-body {{ padding:4px 2px 2px; }}
    .qn-quality-grid {{ grid-template-columns:1fr; }}
    .qn-quality {{ border-radius:18px; padding:14px; }}
}}
@media (max-width:380px) {{
    .qn-hero h2 {{ font-size:30px; }}
    .qn-journey-img, .qn-journey-img img {{
    width:100%;
    height:100%;
    min-height:100%;
    max-height:100%;
    object-fit:cover;
    border-radius:18px;
    display:block;
}}
}}

/* ONLY LOWER SECTION IMAGES - keep top 3 collage images unchanged */
.qn-story-image,
.qn-material-photo,
.qn-journey-img {{
    height:260px !important;
    min-height:260px !important;
    max-height:260px !important;
    overflow:hidden !important;
}}

.qn-story-image img,
.qn-material-photo img,
.qn-journey-img img {{
    width:100% !important;
    height:100% !important;
    min-height:100% !important;
    max-height:100% !important;
    object-fit:cover !important;
    display:block !important;
}}

@media (max-width:640px) {{
    .qn-story-image,
    .qn-material-photo,
    .qn-journey-img {{
        height:220px !important;
        min-height:220px !important;
        max-height:220px !important;
    }}

    .qn-story-image img,
    .qn-material-photo img,
    .qn-journey-img img {{
        height:100% !important;
        min-height:100% !important;
        max-height:100% !important;
    }}
}}

</style>

<div class="qn-page">
  <section class="qn-hero">
    <div class="qn-hero-grid">
      <div>
        <div class="qn-eyebrow">🍃 Quy trình & nguồn gốc</div>
        <h2>Câu chuyện hạt cốm từ làng nghề đến tay khách hàng</h2>
        <p>Một hành trình liền mạch từ nghề truyền thống, vùng lúa nếp non, các công đoạn chế biến thủ công đến cam kết chất lượng cho từng sản phẩm.</p>
        <div class="qn-hero-points">
          <div>🏮 Hương vị làng nghề</div>
          <div>🌾 Lúa nếp non tuyển chọn</div>
          <div>🔥 Rang, giã, sàng thủ công</div>
          <div>✅ Sạch, rõ nguồn gốc</div>
        </div>
      </div>
      <div class="qn-collage">
        <img src="{img_overview}" alt="Cốm Làng Vòng">
        <img src="{img_grain}" alt="Lúa nếp non">
        <img src="{img_sen}" alt="Mẹt cốm">
      </div>
    </div>
  </section>

  <section class="qn-section">
    <div class="qn-section-head">
      <h3>Hương vị từ làng nghề trăm năm</h3>
      <p>Cốm Làng Vòng là nét đẹp ẩm thực gắn với mùa thu Hà Nội. Giá trị của cốm đến từ đôi tay người thợ, từ cách cảm nhận độ non của lúa, giữ lửa khi rang và nhịp giã vừa đủ để hạt cốm dẻo thơm.</p>
    </div>
    <div class="qn-story-card">
      <div class="qn-story-text">
        <p>Người làm cốm không chỉ làm theo công thức cố định. Mỗi mẻ lúa có độ non, độ ẩm và mùi thơm khác nhau, nên người thợ phải quan sát màu hạt, nghe tiếng rang và điều chỉnh nhịp giã bằng kinh nghiệm.</p>
        <p>Cốm ngon là cốm giữ được màu xanh dịu, mùi thơm nhẹ, vị ngọt thanh và cảm giác mềm dẻo khi thưởng thức. Đó là lý do nghề cốm luôn cần sự tỉ mỉ trong từng công đoạn.</p>
        <div class="qn-feature-grid">
          <div class="qn-feature"><strong>🌿 Hương vị mộc</strong><span>Giữ mùi thơm tự nhiên của lúa nếp non, không làm mất đi nét thanh nhẹ đặc trưng.</span></div>
          <div class="qn-feature"><strong>🥢 Tay nghề thủ công</strong><span>Rang, giã và sàng đều cần sự cảm nhận trực tiếp của người thợ.</span></div>
          <div class="qn-feature"><strong>🎁 Quà Hà Nội</strong><span>Phù hợp làm quà biếu, quà du lịch và món ăn gợi nhớ mùa thu.</span></div>
          <div class="qn-feature"><strong>🏮 Bản sắc làng nghề</strong><span>Lưu giữ câu chuyện văn hóa qua hương cốm, lá sen và những mẹt cốm xanh.</span></div>
        </div>
      </div>
      <div class="qn-story-image">
        <img src="{img_lang_nghe}" alt="Nghề cốm">
      </div>
    </div>
  </section>

  <section class="qn-section">
    <div class="qn-section-head">
      <h3>Những mùa lúa làm nên hạt cốm</h3>
      <p>Nguyên liệu quyết định phần lớn chất lượng cốm. Hạt lúa phải được chọn khi còn non, có độ sữa, mùi thơm nhẹ và màu xanh tự nhiên.</p>
    </div>
    <div class="qn-material-grid">
      <div class="qn-material-photo"><img src="{img_mua_lua}" alt="Lúa nếp non"></div>
      <div class="qn-material-list">
        <article class="qn-material-item"><h4>🌾 Chọn lúa đúng độ non</h4><p>Ưu tiên hạt nếp còn ngậm sữa, vỏ xanh, hạt chắc vừa phải để cốm có độ dẻo và vị ngọt thanh.</p></article>
        <article class="qn-material-item"><h4>⏰ Sơ chế sớm sau thu hoạch</h4><p>Lúa được đưa vào xử lý sớm để hạn chế xuống màu, khô hạt hoặc mất mùi thơm tự nhiên.</p></article>
        <article class="qn-material-item"><h4>🧺 Phân loại kỹ trước khi rang</h4><p>Loại bỏ hạt lép, hạt sâu, tạp chất và phần nguyên liệu không đạt để chất lượng từng mẻ đồng đều hơn.</p></article>
        <article class="qn-material-item"><h4>🍃 Giữ nguyên mùi thơm tự nhiên</h4><p>Nguyên liệu được đặt ở nơi sạch, khô, tránh khói bụi, hóa chất và thực phẩm có mùi mạnh.</p></article>
      </div>
    </div>
  </section>

  <section class="qn-section">
    <div class="qn-section-head">
      <h3>Hành trình giữ trọn hương cốm</h3>
      <p>Mỗi công đoạn đều có vai trò riêng: chọn đúng nguyên liệu, rang vừa lửa, giã đủ nhịp, sàng sạch vỏ và hoàn thiện thành phẩm để giữ được hương cốm non.</p>
    </div>
    <div class="qn-journey">
      <article class="qn-journey-step">
        <div class="qn-journey-img"><img src="{img_thu_hoach}" alt="Thu hoạch và tuyển chọn lúa nếp non"><div class="qn-journey-icon">🌾</div></div>
        <div class="qn-journey-body"><h4>Thu hoạch & tuyển chọn nguyên liệu</h4><p>Lúa nếp non được chọn ở thời điểm hạt còn mềm, thơm nhẹ và có độ sữa. Phần hạt lép, hạt sâu hoặc lẫn tạp chất được loại bỏ trước khi chế biến.</p><div class="qn-mini-list"><span>Hạt còn non</span><span>Màu xanh tự nhiên</span><span>Không lẫn tạp chất</span></div></div>
      </article>
      <article class="qn-journey-step">
        <div class="qn-journey-img"><img src="{img_rang}" alt="Rang cốm"><div class="qn-journey-icon">🔥</div></div>
        <div class="qn-journey-body"><h4>Rang cốm</h4><p>Lúa được rang từng mẻ nhỏ trên chảo nóng. Người thợ đảo đều tay để hạt chín tới, giữ được màu xanh và mùi thơm dịu của lúa non.</p><div class="qn-mini-list"><span>Lửa vừa</span><span>Đảo đều tay</span><span>Giữ mùi thơm</span></div></div>
      </article>
      <article class="qn-journey-step">
        <div class="qn-journey-img"><img src="{img_gia}" alt="Giã cốm"><div class="qn-journey-icon">🥣</div></div>
        <div class="qn-journey-body"><h4>Giã cốm</h4><p>Hạt sau khi rang được giã nhịp nhàng để tách vỏ và làm hạt mềm hơn. Lực giã cần vừa đủ để cốm dẻo mà không bị nát vụn.</p><div class="qn-mini-list"><span>Nhịp giã đều</span><span>Hạt mềm dẻo</span><span>Không làm nát</span></div></div>
      </article>
      <article class="qn-journey-step">
        <div class="qn-journey-img"><img src="{img_sang}" alt="Sàng sảy cốm"><div class="qn-journey-icon">🍃</div></div>
        <div class="qn-journey-body"><h4>Sàng sảy</h4><p>Cốm được sàng nhiều lượt để tách vỏ trấu, hạt vỡ và bụi mịn. Công đoạn này giúp thành phẩm sạch hơn, đều hạt hơn và dễ bảo quản hơn.</p><div class="qn-mini-list"><span>Tách vỏ trấu</span><span>Lọc hạt vỡ</span><span>Đều hạt</span></div></div>
      </article>
      <article class="qn-journey-step">
        <div class="qn-journey-img"><img src="{img_com_moc}" alt="Hoàn thiện cốm thành phẩm"><div class="qn-journey-icon">📦</div></div>
        <div class="qn-journey-body"><h4>Hoàn thiện thành phẩm</h4><p>Cốm sau khi đạt độ sạch và độ dẻo sẽ được cân định lượng, đóng gói và bảo quản phù hợp. Một phần cốm được dùng để phát triển các sản phẩm như bánh cốm, xôi cốm, cốm xào hoặc món quà đặc sản.</p><div class="qn-mini-list"><span>Cân định lượng</span><span>Đóng gói sạch</span><span>Bảo quản đúng cách</span></div></div>
      </article>
      <article class="qn-journey-step">
        <div class="qn-journey-img"><img src="{img_banh_com}" alt="Sản phẩm từ cốm"><div class="qn-journey-icon">🎁</div></div>
        <div class="qn-journey-body"><h4>Từ cốm mộc đến quà đặc sản</h4><p>Hạt cốm được giữ làm cốm mộc hoặc chế biến thành nhiều món quà hiện đại. Dù ở dạng nào, tinh thần chính vẫn là giữ hương vị thanh nhã của Hà Nội.</p><div class="qn-mini-list"><span>Cốm mộc</span><span>Bánh cốm</span><span>Quà Hà Nội</span></div></div>
      </article>
    </div>
  </section>

  <section class="qn-section">
    <div class="qn-section-head">
      <h3>Cam kết chất lượng</h3>
      <p>Những tiêu chí dưới đây giúp khách hàng yên tâm hơn khi lựa chọn sản phẩm từ cốm Làng Vòng.</p>
    </div>
    <div class="qn-quality-grid">
      <article class="qn-quality"><div class="qicon">✅</div><h4>Nguyên liệu tuyển chọn</h4><p>Lúa nếp non được kiểm tra cảm quan, loại bỏ phần không đạt trước khi đưa vào chế biến.</p></article>
      <article class="qn-quality"><div class="qicon">🧼</div><h4>Vệ sinh chế biến</h4><p>Dụng cụ tiếp xúc thực phẩm cần sạch, khô, không gỉ sét và không dùng chung với hóa chất.</p></article>
      <article class="qn-quality"><div class="qicon">🏷️</div><h4>Nhãn và truy xuất</h4><p>Bao bì thể hiện tên sản phẩm, định lượng, ngày sản xuất, hạn sử dụng và thông tin liên hệ.</p></article>
      <article class="qn-quality"><div class="qicon">📦</div><h4>Bảo quản đúng cách</h4><p>Sản phẩm được để nơi khô mát hoặc bảo quản lạnh tùy dòng hàng, tránh nắng và nguồn nhiệt.</p></article>
    </div>
    <div class="qn-final-note">
      <h4>Điều chúng tôi luôn gìn giữ</h4>
      <p>Mỗi sản phẩm từ cốm cần truyền tải được ba giá trị: hương vị dẻo thơm, nguồn gốc rõ ràng và cảm giác trang trọng khi dùng làm quà đặc sản Hà Nội.</p>
    </div>
  </section>
</div>
"""
    st.markdown(html, unsafe_allow_html=True)

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
            f'<p>{product.get("desc", "")}</p>'
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
    if page_data["page_id"] == "congthuc":
        render_recipe_book_page()
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
<h3>🌾 Cốm Làng Vòng Bà Hoản</h3>
<p>📍 Địa chỉ: Số 36, ngõ 63 Xuân Thủy, Cầu Giấy, Hà Nội</p>
<p>📞 <a href="tel:0385437503">0385 437 503</a></p>
<p>💬 <a href="https://zalo.me/0385437503" target="_blank">Chat Zalo</a></p>
<p style="margin-top:15px; font-size:13px; color:#ccc;">© 2026 Cốm Làng Vòng. All rights reserved.</p>
</div>
</div>
""",
    unsafe_allow_html=True,
)

# viewer background updated to soft green

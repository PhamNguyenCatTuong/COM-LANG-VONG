from pathlib import Path

code = r'''# FILE HOÀN CHỈNH - CỐM LÀNG VÒNG
# Responsive mobile + menu + chứng nhận slider

import sqlite3
import streamlit as st

st.set_page_config(
    page_title="CỐM LÀNG VÒNG",
    layout="wide"
)

params = st.query_params
page = params.get("page", "thongtinsp")

st.markdown("""
<style>

*{
    box-sizing:border-box;
}

#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden;}
[data-testid="stToolbar"] {display:none !important;}

html, body{
    margin:0;
    padding:0;
    overflow-x:hidden;
}

img{
    max-width:100%;
    height:auto;
}

.block-container{
    padding-top:0 !important;
    padding-left:16px !important;
    padding-right:16px !important;
    padding-bottom:0 !important;
}

/* TOPBAR */

.topbar{
    position:relative;
    background:white;
    padding:14px;
    border-radius:18px;
    margin:10px;
    z-index:999;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.top-row{
    display:flex;
    justify-content:space-between;
    align-items:center;
}

.logo{
    font-size:clamp(20px,4vw,32px);
    font-weight:800;
    color:#2e7d32;
    white-space:nowrap;
}

.hamburger{
    font-size:28px;
    cursor:pointer;
}

#menu-toggle{
    display:none;
}

.menu{
    display:none;
    flex-direction:column;
    gap:8px;
    margin-top:14px;
}

#menu-toggle:checked ~ .menu{
    display:flex;
}

/* MENU */

.dropdown{
    background:white;
    border-radius:10px;
    overflow:hidden;
}

.dropbtn{
    background:#2e7d32;
    color:white;
    border:none;
    width:100%;
    text-align:left;
    padding:10px 14px;
    font-size:clamp(12px,2.5vw,16px);
    border-radius:10px 10px 0 0;
    cursor:pointer;
    font-weight:600;
}

.dropdown-content{
    display:block;
    background:white;
}

.dropdown-content a{
    display:block;
    padding:8px 14px;
    text-decoration:none;
    color:#333;
    border-bottom:1px solid #f0f0f0;
    font-size:clamp(11px,2.4vw,15px);
}

.dropdown-content a:hover{
    background:#f1f8e9;
}

/* CONTENT */

.content{
    max-width:950px;
    margin:auto;
    padding:18px;
}

.page-title{
    text-align:center;
    font-size:clamp(18px,5vw,34px);
    margin:20px 0 14px 0;
    color:#222;
    white-space:nowrap;
}

.card,
.card2{
    padding:18px;
    border-radius:16px;
    margin-top:16px;
}

.card{
    background:#f1f8e9;
}

.card2{
    background:#e8f5e9;
}

/* BANNER */

.hero-banner{
    width:calc(100vw - 32px);
    margin-left:calc(50% - 50vw + 16px);
    min-height:460px;
    border-radius:24px;
    overflow:hidden;
    position:relative;
    display:flex;
    align-items:center;

    background:
    linear-gradient(
        90deg,
        rgba(0,0,0,0.62) 0%,
        rgba(0,0,0,0.35) 45%,
        rgba(0,0,0,0.05) 100%
    ),
    url("https://images.unsplash.com/photo-1506744038136-46273834b3fb?q=80&w=1600");

    background-size:cover;
    background-position:center;
}

.hero-content{
    width:min(52%,520px);
    padding-left:28px;
    color:white;
}

.hero-small{
    font-size:clamp(11px,2vw,16px);
    margin-bottom:8px;
    letter-spacing:1px;
    text-transform:uppercase;
    font-weight:700;
}

.hero-content h1{
    font-size:clamp(34px,8vw,58px);
    line-height:1.05;
    margin:0 0 12px 0;
}

.hero-content p{
    font-size:clamp(13px,2.5vw,20px);
    line-height:1.4;
    margin-bottom:18px;
}

.hero-actions{
    display:flex;
    gap:10px;
    flex-wrap:wrap;
}

.hero-btn{
    padding:8px 14px;
    border-radius:999px;
    text-decoration:none;
    font-size:clamp(11px,2vw,15px);
    font-weight:700;
}

.hero-btn.order{
    background:#2e7d32;
    color:white;
}

.hero-btn.call{
    background:white;
    color:#2e7d32;
}

/* CHỨNG NHẬN */

.cert-box{
    background:white;
    border-radius:18px;
    padding:12px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

.cert-title{
    text-align:center;
    color:#2e7d32;
    margin-top:10px;
    font-size:22px;
}

.cert-desc{
    text-align:center;
    color:#555;
    font-size:14px;
    line-height:1.5;
}

.arrow-btn{
    width:100%;
}

/* FLOAT */

.floating-contact{
    position:fixed;
    bottom:55px;
    right:14px;
    display:flex;
    flex-direction:column;
    gap:10px;
    z-index:9999;
}

.float-btn{
    width:50px;
    height:50px;
    border-radius:50%;
    display:flex;
    align-items:center;
    justify-content:center;
    text-decoration:none;
    color:white;
    font-size:22px;
}

.call-btn{
    background:#2e7d32;
}

.zalo-btn{
    background:#0084ff;
}

/* FOOTER */

.footer-full{
    width:calc(100vw - 32px);
    margin-left:calc(50% - 50vw + 16px);
    background:black;
    color:white;
    margin-top:40px;
    padding:24px 16px;
}

.footer-content{
    max-width:950px;
    margin:auto;
    text-align:center;
}

.footer-content a{
    color:white;
    text-decoration:none;
}

/* DESKTOP */

@media(min-width:768px){

    .topbar{
        display:flex;
        align-items:center;
        gap:20px;
    }

    .hamburger{
        display:none;
    }

    .menu{
        display:flex !important;
        flex-direction:row;
        flex-wrap:wrap;
        margin-top:0;
    }

    .dropdown{
        position:relative;
    }

    .dropdown-content{
        display:none;
        position:absolute;
        min-width:240px;
        z-index:9999;
        box-shadow:0 4px 12px rgba(0,0,0,0.12);
    }

    .dropdown:hover .dropdown-content{
        display:block;
    }

    .dropbtn{
        width:auto;
        border-radius:10px;
    }
}

/* MOBILE */

@media(max-width:768px){

    .topbar{
        padding:10px;
        margin:6px;
    }

    .hero-banner{
        min-height:360px;
    }

    .hero-content{
        width:52%;
        padding-left:22px;
    }

    .content{
        padding:12px;
    }
}

</style>
''', unsafe_allow_html=True)

st.markdown("""
<div class="topbar">

<input type="checkbox" id="menu-toggle">

<div class="top-row">
<div class="logo">🌾 Cốm Làng Vòng</div>
<label for="menu-toggle" class="hamburger">☰</label>
</div>

<div class="menu">

<div class="dropdown">
<a href="?page=thongtinsp" target="_self">
<button class="dropbtn">Thông tin sản phẩm</button>
</a>

<div class="dropdown-content">
<a href="?page=tensp_masp" target="_self">Tên & mã sản phẩm</a>
<a href="?page=thuonghieu" target="_self">Thương hiệu</a>
</div>
</div>

<div class="dropdown">
<a href="?page=truyxuat" target="_self">
<button class="dropbtn">Truy xuất nguồn gốc</button>
</a>

<div class="dropdown-content">
<a href="?page=nguyenlieu" target="_self">Nguồn nguyên liệu</a>
<a href="?page=khuvuc" target="_self">Khu vực sản xuất</a>
<a href="?page=malo" target="_self">Mã lô hàng</a>
</div>
</div>

<div class="dropdown">
<a href="?page=chatluong" target="_self">
<button class="dropbtn">Chất lượng & chứng nhận</button>
</a>
</div>

<div class="dropdown">
<a href="?page=truyenthong" target="_self">
<button class="dropbtn">Nội dung truyền thông</button>
</a>

<div class="dropdown-content">
<a href="?page=cauchuyen" target="_self">Câu chuyện sản phẩm</a>
<a href="?page=hinhanh" target="_self">Hình ảnh</a>
<a href="?page=video" target="_self">Video giới thiệu</a>
</div>
</div>

<div class="dropdown">
<a href="?page=baobi" target="_self">
<button class="dropbtn">Thông tin bao bì</button>
</a>

<div class="dropdown-content">
<a href="?page=muc_giay" target="_self">Mực & giấy bao bì</a>
<a href="?page=thuhoi" target="_self">Chính sách thu hồi</a>
</div>
</div>

</div>

</div>

<section class="hero-banner">
<div class="hero-content">

<div class="hero-small">
Đặc sản mùa thu Hà Nội
</div>

<h1>Cốm Làng Vòng</h1>

<p>
Hương vị truyền thống của Hà Nội với hạt cốm dẻo thơm.
</p>

<div class="hero-actions">
<a href="#dathang" class="hero-btn order">
Đặt hàng ngay
</a>

<a href="tel:0385437503" class="hero-btn call">
Gọi tư vấn
</a>
</div>

</div>
</section>
""", unsafe_allow_html=True)

st.markdown("<div class='content'>", unsafe_allow_html=True)

PAGE_DATABASE = {

    "thongtinsp":{
        "title":"Thông tin sản phẩm",
        "type":"group",
        "items":["tensp_masp","thuonghieu"]
    },

    "tensp_masp":{
        "title":"Tên & mã sản phẩm",
        "card_class":"card",
        "card_title":"🌾 Thông tin nhận diện sản phẩm",
        "fields":{
            "Tên sản phẩm":"Cốm Làng Vòng",
            "Mã sản phẩm":"COM-LV-001",
            "Loại sản phẩm":"Đặc sản truyền thống"
        },
        "paragraphs":[
            "Thông tin nhận diện giúp khách hàng tra cứu và truy xuất sản phẩm nhanh chóng."
        ]
    },

    "thuonghieu":{
        "title":"Thương hiệu",
        "card_class":"card",
        "card_title":"🌿 Thương hiệu Cốm Làng Vòng",
        "paragraphs":[
            "Cốm Làng Vòng là đặc sản nổi tiếng gắn với mùa thu Hà Nội."
        ]
    },

    "truyxuat":{
        "title":"Truy xuất nguồn gốc",
        "type":"group",
        "items":["nguyenlieu","khuvuc","malo"]
    },

    "nguyenlieu":{
        "title":"Nguồn nguyên liệu",
        "card_class":"card2",
        "card_title":"🌾 Nguồn nguyên liệu",
        "paragraphs":[
            "Sử dụng lúa nếp non tuyển chọn kỹ lưỡng."
        ]
    },

    "khuvuc":{
        "title":"Khu vực sản xuất",
        "card_class":"card2",
        "card_title":"📍 Khu vực sản xuất",
        "paragraphs":[
            "Làng Vòng - Hà Nội"
        ]
    },

    "malo":{
        "title":"Mã lô hàng",
        "card_class":"card2",
        "card_title":"🏷️ Mã lô hàng",
        "fields":{
            "Mã lô":"LV-2026-001"
        }
    },

    "chatluong":{
        "title":"Chất lượng & chứng nhận",
        "type":"custom_cert"
    },

    "truyenthong":{
        "title":"Nội dung truyền thông",
        "type":"group",
        "items":["cauchuyen","hinhanh","video"]
    },

    "cauchuyen":{
        "title":"Câu chuyện sản phẩm",
        "card_class":"card",
        "card_title":"🍃 Câu chuyện sản phẩm",
        "paragraphs":[
            "Cốm Làng Vòng là ký ức mùa thu của người Hà Nội."
        ]
    },

    "hinhanh":{
        "title":"Hình ảnh",
        "type":"images",
        "intro":"Hình ảnh sản phẩm",
        "images":[
            "Com tong quan.jpg"
        ]
    },

    "video":{
        "title":"Video giới thiệu",
        "card_class":"card",
        "card_title":"🎬 Video giới thiệu",
        "paragraphs":[
            "Khu vực video giới thiệu sản phẩm."
        ]
    },

    "baobi":{
        "title":"Thông tin bao bì",
        "type":"group",
        "items":["muc_giay","thuhoi"]
    },

    "muc_giay":{
        "title":"Mực & giấy bao bì",
        "card_class":"card2",
        "card_title":"📦 Mực & giấy bao bì",
        "paragraphs":[
            "Bao bì sử dụng giấy sạch và mực in an toàn."
        ]
    },

    "thuhoi":{
        "title":"Chính sách thu hồi",
        "card_class":"card2",
        "card_title":"♻️ Chính sách thu hồi",
        "paragraphs":[
            "Khuyến khích tái chế và phân loại bao bì."
        ]
    }
}

def create_database():

    conn = sqlite3.connect(":memory:")

    conn.execute("""
    CREATE TABLE pages(
        page_id TEXT PRIMARY KEY,
        title TEXT,
        page_type TEXT,
        card_class TEXT,
        card_title TEXT,
        intro TEXT,
        group_items TEXT
    )
    """)

    conn.execute("""
    CREATE TABLE page_fields(
        page_id TEXT,
        field_name TEXT,
        field_value TEXT,
        sort_order INTEGER
    )
    """)

    conn.execute("""
    CREATE TABLE page_paragraphs(
        page_id TEXT,
        content TEXT,
        sort_order INTEGER
    )
    """)

    conn.execute("""
    CREATE TABLE page_images(
        page_id TEXT,
        image_path TEXT,
        sort_order INTEGER
    )
    """)

    for page_id, data in PAGE_DATABASE.items():

        conn.execute(
            "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?)",
            (
                page_id,
                data.get("title",""),
                data.get("type","content"),
                data.get("card_class","card"),
                data.get("card_title",""),
                data.get("intro",""),
                ",".join(data.get("items",[]))
            )
        )

        for idx, (name, value) in enumerate(data.get("fields",{}).items(), start=1):

            conn.execute(
                "INSERT INTO page_fields VALUES (?, ?, ?, ?)",
                (page_id, name, value, idx)
            )

        for idx, paragraph in enumerate(data.get("paragraphs",[]), start=1):

            conn.execute(
                "INSERT INTO page_paragraphs VALUES (?, ?, ?)",
                (page_id, paragraph, idx)
            )

        for idx, image in enumerate(data.get("images",[]), start=1):

            conn.execute(
                "INSERT INTO page_images VALUES (?, ?, ?)",
                (page_id, image, idx)
            )

    conn.commit()
    return conn

def fetch_page(conn, page_id):

    cur = conn.cursor()

    cur.execute("""
    SELECT
        page_id,
        title,
        page_type,
        card_class,
        card_title,
        intro,
        group_items
    FROM pages
    WHERE page_id = ?
    """, (page_id,))

    row = cur.fetchone()

    if not row:
        return None

    page_data = {
        "page_id":row[0],
        "title":row[1],
        "type":row[2],
        "card_class":row[3],
        "card_title":row[4],
        "intro":row[5],
        "group_items":row[6].split(",") if row[6] else [],
        "fields":[],
        "paragraphs":[],
        "images":[]
    }

    cur.execute("""
    SELECT field_name, field_value
    FROM page_fields
    WHERE page_id = ?
    ORDER BY sort_order
    """, (page_id,))

    page_data["fields"] = cur.fetchall()

    cur.execute("""
    SELECT content
    FROM page_paragraphs
    WHERE page_id = ?
    ORDER BY sort_order
    """, (page_id,))

    page_data["paragraphs"] = [x[0] for x in cur.fetchall()]

    cur.execute("""
    SELECT image_path
    FROM page_images
    WHERE page_id = ?
    ORDER BY sort_order
    """, (page_id,))

    page_data["images"] = [x[0] for x in cur.fetchall()]

    return page_data

def render_page(page_data):

    st.markdown(
        f"<h1 class='page-title'>{page_data['title']}</h1>",
        unsafe_allow_html=True
    )

    if page_data["type"] == "custom_cert":

        certs = [

            {
                "image":"CBSP(1).jpg",
                "title":"Tự công bố sản phẩm",
                "desc":"Giấy xác nhận tự công bố sản phẩm."
            },

            {
                "image":"KQKN(1).jpg",
                "title":"Kiểm nghiệm chất lượng",
                "desc":"Kết quả kiểm nghiệm an toàn thực phẩm."
            },

            {
                "image":"OCOP(1).JPEG",
                "title":"OCOP 4 sao",
                "desc":"Chứng nhận sản phẩm OCOP Hà Nội."
            },

            {
                "image":"HACCP(1).JPEG",
                "title":"HACCP",
                "desc":"Hệ thống kiểm soát an toàn thực phẩm."
            },

            {
                "image":"GMP(1).JPEG",
                "title":"GMP",
                "desc":"Thực hành sản xuất tốt."
            },

            {
                "image":"CNATTP(1).jpg",
                "title":"An toàn thực phẩm",
                "desc":"Cơ sở đủ điều kiện an toàn thực phẩm."
            }
        ]

        if "cert_index" not in st.session_state:
            st.session_state.cert_index = 0

        left, center, right = st.columns([1,6,1])

        with left:

            if st.button("⬅", use_container_width=True):

                st.session_state.cert_index -= 1

                if st.session_state.cert_index < 0:
                    st.session_state.cert_index = len(certs)-1

        with right:

            if st.button("➡", use_container_width=True):

                st.session_state.cert_index += 1

                if st.session_state.cert_index >= len(certs):
                    st.session_state.cert_index = 0

        cert = certs[st.session_state.cert_index]

        with center:

            st.image(cert["image"], use_container_width=True)

            st.markdown(f"""
            <div class="cert-box">
                <div class="cert-title">{cert["title"]}</div>

                <p class="cert-desc">
                    {cert["desc"]}
                </p>

                <p style="text-align:center;color:#888;">
                    {st.session_state.cert_index + 1} / {len(certs)}
                </p>
            </div>
            """, unsafe_allow_html=True)

        return

    if page_data["type"] == "group":

        for child_page_id in page_data["group_items"]:

            child_data = fetch_page(conn, child_page_id)

            if child_data:

                html = f"<div class='{child_data['card_class']}'>"

                html += f"<h3>{child_data['card_title']}</h3>"

                for name, value in child_data["fields"]:
                    html += f"<p><b>{name}:</b> {value}</p>"

                for paragraph in child_data["paragraphs"]:
                    html += f"<p>{paragraph}</p>"

                html += f"""
                <p>
                <a href="?page={child_page_id}" target="_self">
                Xem chi tiết →
                </a>
                </p>
                """

                html += "</div>"

                st.markdown(html, unsafe_allow_html=True)

        return

    if page_data["type"] == "images":

        st.write(page_data["intro"])

        for image_path in page_data["images"]:
            st.image(image_path)

        return

    html = f"<div class='{page_data['card_class']}'>"

    if page_data["card_title"]:
        html += f"<h3>{page_data['card_title']}</h3>"

    for name, value in page_data["fields"]:
        html += f"<p><b>{name}:</b> {value}</p>"

    for paragraph in page_data["paragraphs"]:
        html += f"<p>{paragraph}</p>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)

conn = create_database()

current_page = fetch_page(conn, page)

if current_page:
    render_page(current_page)

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

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="footer-full" id="dathang">

<div class="footer-content">

<h3>🌾 Cốm Làng Vòng</h3>

<p>
📍 44 Trần Thái Tông, Cầu Giấy, Hà Nội
</p>

<p>
📞 <a href="tel:0385437503">0385 437 503</a>
</p>

<p>
💬 <a href="https://zalo.me/0385437503">
Chat Zalo
</a>
</p>

</div>

</div>
""", unsafe_allow_html=True)
'''

path = Path("/mnt/data/com_lang_vong_complete.py")
path.write_text(code, encoding="utf-8")

print("DONE")
print(path)

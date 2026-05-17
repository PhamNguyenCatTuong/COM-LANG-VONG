import sqlite3
import streamlit as st

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="CỐM LÀNG VÒNG",
    layout="wide"
)

# =========================
# LẤY TRANG HIỆN TẠI
# =========================
params = st.query_params
page = params.get("page", "tensp")

# =========================
# CSS GIAO DIỆN WEBSITE
# =========================
st.markdown("""
<style>

/* ẨN THANH STREAMLIT */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}

html, body {
    margin: 0;
    padding: 0;
}

.block-container {
    padding-left: 16px !important;
    padding-right: 16px !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

.topbar {
    position: sticky;
    top: 0;
    background: white;
    padding: 15px;
    border-radius: 15px;
    margin: 10px;
    z-index: 999;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
}

.top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 30px;
    font-weight: bold;
    color: #2e7d32;
    white-space: nowrap;
}

.hamburger {
    font-size: 28px;
    cursor: pointer;
}

#menu-toggle {
    display: none;
}

.menu {
    display: none;
    flex-direction: column;
    gap: 10px;
    margin-top: 15px;
}

#menu-toggle:checked ~ .menu {
    display: flex;
}

.dropdown {
    position: relative;
}

.dropbtn {
    background: #2e7d32;
    color: white;
    border: none;
    padding: 10px 14px;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14px;
    width: 100%;
    text-align: left;
}

.dropdown-content {
    display: none;
    background: white;
    min-width: 230px;
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 10px rgba(0,0,0,0.12);
    z-index: 9999;
}

.dropdown-content a {
    display: block;
    padding: 12px 14px;
    text-decoration: none;
    color: #333;
    border-bottom: 1px solid #eee;
}

.dropdown-content a:hover {
    background: #f1f8e9;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.content {
    max-width: 850px;
    margin: auto;
    padding: 20px;
    line-height: 1.8;
    font-size: 16px;
}

.card {
    background: #f1f8e9;
    padding: 20px;
    border-radius: 14px;
    margin-top: 18px;
}

.card2 {
    background: #e8f5e9;
    padding: 20px;
    border-radius: 14px;
    margin-top: 18px;
}

img {
    max-width: 100%;
    height: auto;
    border-radius: 12px;
}

.floating-contact {
    position: fixed;
    bottom: 50px;
    right: 15px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    z-index: 9999;
}

.float-btn {
    width: 48px;
    height: 48px;
    border-radius: 50%;
    display: flex;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: white;
    font-size: 22px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

.call-btn {
    background: #2e7d32;
}

.zalo-btn {
    background: #0084ff;
}

.footer-full {
    width: calc(100vw - 32px);
    margin-left: calc(50% - 50vw + 16px);
    background: #000;
    color: white;
    padding: 10px 10px;
    margin-top: 40px;
    box-sizing: border-box;
}

.footer-content {
    max-width: 850px;
    margin: auto;
    text-align: center;
}

.footer-content a {
    color: white;
    text-decoration: none;
}


/* =========================
BANNER TRANG CHỦ
========================= */
.hero-banner {
    width: calc(100vw - 32px);
    margin-left: calc(50% - 50vw + 16px);
    min-height: 470px;
    border-radius: 22px;
    overflow: hidden;
    position: relative;
    display: flex;
    align-items: flex-end;
    background:
        linear-gradient(90deg, rgba(0,0,0,0.62) 0%, rgba(0,0,0,0.35) 45%, rgba(0,0,0,0.08) 100%),
        url("https://source.unsplash.com/1800x900/?vietnam,rice,farmer,harvest");
    background-size: cover;
    background-position: center;
    box-sizing: border-box;
    margin-top: 14px;
}

.hero-content {
    max-width: 620px;
    padding: 48px;
    color: white;
}

.hero-small {
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    margin-bottom: 8px;
}

.hero-content h1 {
    font-size: 56px;
    line-height: 1.08;
    margin: 0 0 12px 0;
}

.hero-content p {
    font-size: 20px;
    line-height: 1.45;
    margin: 0 0 22px 0;
}

.hero-actions {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

.hero-btn {
    padding: 12px 20px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
    display: inline-block;
}

.hero-btn.order {
    background: #2e7d32;
    color: white;
}

.hero-btn.call {
    background: white;
    color: #2e7d32;
}

@media (min-width:768px) {
    .topbar {
        display: flex;
        align-items: center;
        gap: 20px;
    }

    .hamburger {
        display: none;
    }

    .menu {
        display: flex !important;
        flex-direction: row;
        flex-wrap: wrap;
        margin-top: 0;
    }

    .dropbtn {
        width: auto;
        text-align: center;
    }

    .dropdown-content {
        position: absolute;
    }
}

@media (max-width:768px) {
    .logo {
        font-size: 25px;
    }

    .dropdown-content {
        position: relative;
        width: 100%;
    }

    .hero-banner {
        min-height: 430px;
        align-items: flex-end;
        background-position: center;
    }

    .hero-content {
        max-width: 78%;
        padding: 0 0 28px 22px;
    }

    .hero-small {
        font-size: 12px;
        letter-spacing: 1px;
        margin-bottom: 4px;
    }

    .hero-content h1 {
        font-size: 30px;
        line-height: 1.05;
        margin-bottom: 6px;
    }

    .hero-content p {
        font-size: 14px;
        line-height: 1.35;
        margin-bottom: 12px;
    }

    .hero-btn {
        padding: 9px 13px;
        font-size: 13px;
    }

}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbar">

<input type="checkbox" id="menu-toggle">

<div class="top-row">
    <div class="logo">🌾 Cốm Làng Vòng</div>
    <label for="menu-toggle" class="hamburger">☰</label>
</div>

<div class="menu">

<div class="dropdown">
    <a href="?page=thongtinsp" target="_self" style="text-decoration:none;">
        <button class="dropbtn">Thông tin sản phẩm</button>
    </a>
    <div class="dropdown-content">
        <a href="?page=tensp" target="_self">Tên sản phẩm</a>
        <a href="?page=masp" target="_self">Mã sản phẩm</a>
        <a href="?page=thuonghieu" target="_self">Thương hiệu</a>
    </div>
</div>

<div class="dropdown">
    <a href="?page=truyxuat" target="_self" style="text-decoration:none;">
        <button class="dropbtn">Truy xuất nguồn gốc</button>
    </a>
    <div class="dropdown-content">
        <a href="?page=nguyenlieu" target="_self">Nguồn nguyên liệu</a>
        <a href="?page=khuvuc" target="_self">Khu vực sản xuất</a>
        <a href="?page=malo" target="_self">Mã lô hàng</a>
    </div>
</div>

<div class="dropdown">
    <a href="?page=chatluong" target="_self" style="text-decoration:none;">
        <button class="dropbtn">Chất lượng & chứng nhận</button>
    </a>
    <div class="dropdown-content">
        <a href="?page=ocop" target="_self">Chứng nhận OCOP</a>
        <a href="?page=kiemdinh" target="_self">Kiểm định chất lượng</a>
    </div>
</div>

<div class="dropdown">
    <a href="?page=truyenthong" target="_self" style="text-decoration:none;">
        <button class="dropbtn">Nội dung truyền thông</button>
    </a>
    <div class="dropdown-content">
        <a href="?page=cauchuyen" target="_self">Câu chuyện sản phẩm</a>
        <a href="?page=hinhanh" target="_self">Hình ảnh</a>
        <a href="?page=video" target="_self">Video giới thiệu</a>
    </div>
</div>

<div class="dropdown">
    <a href="?page=baobi" target="_self" style="text-decoration:none;">
        <button class="dropbtn">Thông tin bao bì</button>
    </a>
    <div class="dropdown-content">
        <a href="?page=muc" target="_self">Mực</a>
        <a href="?page=giay" target="_self">Giấy</a>
        <a href="?page=thuhoi" target="_self">Chính sách thu hồi bao bì</a>
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

# =========================
# CƠ SỞ DỮ LIỆU NỘI DUNG MENU
# =========================
# Cách hoạt động:
# - Mỗi dòng trong PAGE_DATABASE tương ứng với 1 trang con trên menu.
# - Muốn sửa nội dung: chỉnh title, card_title, paragraphs, bullets.
# - Muốn thêm menu mới: thêm dòng vào PAGE_DATABASE và thêm link trên thanh menu phía trên.

PAGE_DATABASE = {
        "thongtinsp": {
        "title": "Thông tin sản phẩm",
        "type": "group",
        "items": ["tensp", "masp", "thuonghieu"]
    },
    "truyxuat": {
        "title": "Truy xuất nguồn gốc",
        "type": "group",
        "items": ["nguyenlieu", "khuvuc", "malo"]
    },
    "chatluong": {
        "title": "Chất lượng & chứng nhận",
        "type": "group",
        "items": ["ocop", "kiemdinh"]
    },
    "truyenthong": {
        "title": "Nội dung truyền thông",
        "type": "group",
        "items": ["cauchuyen", "hinhanh", "video"]
    },
    "baobi": {
        "title": "Thông tin bao bì",
        "type": "group",
        "items": ["muc", "giay", "thuhoi"]
    },

def create_database():
    conn = sqlite3.connect(":memory:")
    conn.execute("""
         CREATE TABLE pages (
            page_id TEXT PRIMARY KEY,
            title TEXT,
            page_type TEXT,
            card_class TEXT,
            card_title TEXT,
            intro TEXT,
            group_items TEXT
        )
    """)
    conn.execute(
        "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            page_id,
            data.get("title", ""),
            data.get("type", "content"),
            data.get("card_class", "card"),
            data.get("card_title", ""),
            data.get("intro", ""),
            ",".join(data.get("items", []))
        )
    )
    conn.execute("""
        CREATE TABLE page_paragraphs (
            page_id TEXT,
            content TEXT,
            sort_order INTEGER
        )
    """)
    conn.execute("""
        CREATE TABLE page_bullets (
            page_id TEXT,
            content TEXT,
            sort_order INTEGER
        )
    """)
    conn.execute("""
        CREATE TABLE page_images (
            page_id TEXT,
            image_path TEXT,
            sort_order INTEGER
        )
    """)

    for page_id, data in PAGE_DATABASE.items():
        conn.execute(
            "INSERT INTO pages VALUES (?, ?, ?, ?, ?, ?)",
            (
                page_id,
                data.get("title", ""),
                data.get("type", "content"),
                data.get("card_class", "card"),
                data.get("card_title", ""),
                data.get("intro", "")
            )
        )
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
        "images": []
        "group_items": row[6].split(",") if row[6] else [],
    }

    cur.execute("SELECT field_name, field_value FROM page_fields WHERE page_id = ? ORDER BY sort_order", (page_id,))
    page_data["fields"] = cur.fetchall()

    cur.execute("SELECT content FROM page_paragraphs WHERE page_id = ? ORDER BY sort_order", (page_id,))
    page_data["paragraphs"] = [item[0] for item in cur.fetchall()]

    cur.execute("SELECT content FROM page_bullets WHERE page_id = ? ORDER BY sort_order", (page_id,))
    page_data["bullets"] = [item[0] for item in cur.fetchall()]

    cur.execute("SELECT image_path FROM page_images WHERE page_id = ? ORDER BY sort_order", (page_id,))
    page_data["images"] = [item[0] for item in cur.fetchall()]

    return page_data


def render_page(page_data):
    st.markdown(f"<h1 style='text-align:center;'>{page_data['title']}</h1>", unsafe_allow_html=True)

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

                if child_data["bullets"]:
                    html += "<ul>"
                    for bullet in child_data["bullets"]:
                        html += f"<li>{bullet}</li>"
                    html += "</ul>"

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
            st.image(image_path, width=700)
        return

    html = f"<div class='{page_data['card_class']}'>"
    if page_data["card_title"]:
        html += f"<h3>{page_data['card_title']}</h3>"

    for name, value in page_data["fields"]:
        html += f"<p><b>{name}:</b> {value}</p>"

    for paragraph in page_data["paragraphs"]:
        html += f"<p>{paragraph}</p>"

    if page_data["bullets"]:
        html += "<ul>"
        for bullet in page_data["bullets"]:
            html += f"<li>{bullet}</li>"
        html += "</ul>"

    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


conn = create_database()
current_page = fetch_page(conn, page)

if current_page:
    render_page(current_page)
else:
    st.markdown("<h1 style='text-align:center;'>Trang không tồn tại</h1>", unsafe_allow_html=True)
    st.write("Vui lòng chọn lại mục trong menu.")

st.markdown("""
<div class="floating-contact">
    <a href="tel:0385437503" class="float-btn call-btn">📞</a>
    <a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">💬</a>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

st.markdown("""
<div class="footer-full" id="dathang">
    <div class="footer-content">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p>📍 Địa chỉ: 44 Trần Thái Tông, Dịch Vọng Hậu, Cầu Giấy, Hà Nội</p>
        <p>📞 <a href="tel:0385437503">0385 437 503</a></p>
        <p>💬 <a href="https://zalo.me/0385437503" target="_blank">Chat Zalo</a></p>
        <p style="margin-top:15px; font-size:13px; color:#ccc;">
            © 2026 Cốm Làng Vòng. All rights reserved.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

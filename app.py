import streamlit as st

# =========================
# CÀI ĐẶT TRANG WEB
# =========================
st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide"
)

# =========================
# LẤY TRANG HIỆN TẠI
# =========================
params = st.query_params
page = params.get("page", "tongquan")

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
    padding: 10px 20px;
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
    <button class="dropbtn">Thông tin sản phẩm</button>
    <div class="dropdown-content">
        <a href="?page=tensp" target="_self">Tên sản phẩm</a>
        <a href="?page=masp" target="_self">Mã sản phẩm</a>
        <a href="?page=thuonghieu" target="_self">Thương hiệu</a>
    </div>
</div>

<div class="dropdown">
    <button class="dropbtn">Truy xuất nguồn gốc</button>
    <div class="dropdown-content">
        <a href="?page=nguyenlieu" target="_self">Nguồn nguyên liệu</a>
        <a href="?page=khuvuc" target="_self">Khu vực sản xuất</a>
        <a href="?page=malo" target="_self">Mã lô hàng</a>
    </div>
</div>

<div class="dropdown">
    <button class="dropbtn">Chất lượng & chứng nhận</button>
    <div class="dropdown-content">
        <a href="?page=ocop" target="_self">Chứng nhận OCOP</a>
        <a href="?page=kiemdinh" target="_self">Kiểm định chất lượng</a>
    </div>
</div>

<div class="dropdown">
    <button class="dropbtn">Nội dung truyền thông</button>
    <div class="dropdown-content">
        <a href="?page=cauchuyen" target="_self">Câu chuyện sản phẩm</a>
        <a href="?page=hinhanh" target="_self">Hình ảnh</a>
        <a href="?page=video" target="_self">Video giới thiệu</a>
    </div>
</div>

<div class="dropdown">
    <button class="dropbtn">Thông tin bao bì</button>
    <div class="dropdown-content">
        <a href="?page=muc" target="_self">Mực</a>
        <a href="?page=giay" target="_self">Giấy</a>
        <a href="?page=thuhhoi" target="_self">Chính sách thu hồi bao bì</a>
    </div>
</div>
</div>

""", unsafe_allow_html=True)

st.markdown("<div class='content'>", unsafe_allow_html=True)

if page == "tongquan":
    st.markdown("<h1 style='text-align:center;'>Tổng quan</h1>", unsafe_allow_html=True)
    st.image("Com tong quan.jpg", width=700)
    st.write("""
    Cốm Làng Vòng là đặc sản truyền thống nổi tiếng của Hà Nội, gắn liền với mùa thu và văn hóa ẩm thực đất kinh kỳ.
    Sản phẩm được làm từ lúa nếp non, có màu xanh dịu, hương thơm nhẹ, vị ngọt thanh và độ dẻo đặc trưng.
    """)

elif page == "tensp":
    st.markdown("<h1 style='text-align:center;'>Tên sản phẩm</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p><b>Tên sản phẩm:</b> Cốm Làng Vòng</p>
        <p><b>Loại sản phẩm:</b> Thực phẩm truyền thống</p>
        <p><b>Đặc điểm:</b> Hạt cốm mỏng, dẻo, thơm nhẹ, màu xanh non tự nhiên.</p>
        <p>Sản phẩm phù hợp để ăn trực tiếp, làm quà biếu hoặc chế biến thành bánh cốm, chả cốm, xôi cốm, chè cốm.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "masp":
    st.markdown("<h1 style='text-align:center;'>Mã sản phẩm</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🏷️ Mã sản phẩm</h3>
        <p><b>Mã sản phẩm:</b> COM-LV-001</p>
        <p><b>Nhóm sản phẩm:</b> Đặc sản Hà Nội</p>
        <p><b>Dòng sản phẩm:</b> Cốm truyền thống</p>
        <p>Mã sản phẩm giúp khách hàng nhận diện và tra cứu thông tin sản phẩm dễ dàng hơn.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "thuonghieu":
    st.markdown("<h1 style='text-align:center;'>Thương hiệu</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🌿 Thương hiệu Cốm Làng Vòng</h3>
        <p>Cốm Làng Vòng là thương hiệu gắn với làng nghề truyền thống tại Hà Nội.</p>
        <p>Sản phẩm đại diện cho nét tinh tế, thanh tao và giá trị văn hóa ẩm thực của Thủ đô.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "nguyenlieu":
    st.markdown("<h1 style='text-align:center;'>Nguồn nguyên liệu</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>🌾 Lúa nếp non chọn lọc</h3>
        <p>Nguyên liệu chính để làm cốm là lúa nếp non, thường được chọn khi hạt còn ngậm sữa.</p>
        <p>Lúa được sàng lọc kỹ, loại bỏ hạt lép trước khi rang và giã để tạo nên hạt cốm dẻo thơm.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "khuvuc":
    st.markdown("<h1 style='text-align:center;'>Khu vực sản xuất</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>📍 Làng Vòng, Cầu Giấy, Hà Nội</h3>
        <p>Sản phẩm gắn với làng Vòng, phường Dịch Vọng Hậu, quận Cầu Giấy, Hà Nội.</p>
        <p>Đây là địa danh nổi tiếng với nghề làm cốm truyền thống lâu đời.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "malo":
    st.markdown("<h1 style='text-align:center;'>Mã lô hàng</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>🏷️ Thông tin lô hàng</h3>
        <p><b>Mã lô mẫu:</b> LV-2026-001</p>
        <p><b>Ngày sản xuất:</b> Cập nhật trên bao bì sản phẩm</p>
        <p><b>Hạn sử dụng:</b> Cập nhật theo từng loại sản phẩm</p>
        <p>Mã lô hàng giúp theo dõi thông tin sản xuất và chất lượng sản phẩm.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "ocop":
    st.markdown("<h1 style='text-align:center;'>Chứng nhận OCOP</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>✅ Định hướng sản phẩm OCOP</h3>
        <p>OCOP là chương trình đánh giá, phân hạng sản phẩm đặc trưng của địa phương.</p>
        <p>Cốm Làng Vòng phù hợp phát triển theo định hướng sản phẩm OCOP nhờ giá trị truyền thống và nguồn gốc rõ ràng.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "kiemdinh":
    st.markdown("<h1 style='text-align:center;'>Kiểm định chất lượng</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🔍 Kiểm soát chất lượng</h3>
        <ul>
            <li>Nguyên liệu có nguồn gốc rõ ràng.</li>
            <li>Quy trình chế biến sạch sẽ.</li>
            <li>Không sử dụng nguyên liệu kém chất lượng.</li>
            <li>Bảo quản nơi khô ráo, thoáng mát.</li>
            <li>Đóng gói cẩn thận, hạn chế tiếp xúc với môi trường bên ngoài.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "cauchuyen":
    st.markdown("<h1 style='text-align:center;'>Câu chuyện sản phẩm</h1>", unsafe_allow_html=True)
    st.write("""
    Cốm Làng Vòng không chỉ là một món ăn mà còn là một phần ký ức của Hà Nội.
    Mỗi hạt cốm là kết quả của quá trình chọn lúa, rang, giã và sàng sảy công phu.
    """)
    st.write("""
    Hương cốm thơm nhẹ, màu xanh non và vị ngọt thanh khiến sản phẩm trở thành thức quà quen thuộc mỗi độ thu về.
    """)

elif page == "hinhanh":
    st.markdown("<h1 style='text-align:center;'>Hình ảnh</h1>", unsafe_allow_html=True)
    st.write("Một số hình ảnh giới thiệu sản phẩm Cốm Làng Vòng:")
    st.image("Com tong quan.jpg", width=700)
    st.image("Com tong quan 1.jpg", width=700)
    st.image("Com tong quan 2.jpg", width=700)

elif page == "video":
    st.markdown("<h1 style='text-align:center;'>Video giới thiệu</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🎬 Video giới thiệu sản phẩm</h3>
        <p>Khu vực này dùng để hiển thị video giới thiệu quy trình làm cốm hoặc câu chuyện làng nghề.</p>
        <p><i>Khi có video, bạn thêm:</i></p>
        <p><b>st.video("link_youtube")</b></p>
    </div>
    """, unsafe_allow_html=True)

elif page == "muc":
    st.markdown("<h1 style='text-align:center;'>Thông tin mực in</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>🖨️ Mực in bao bì</h3>
        <p>Bao bì nên sử dụng mực in rõ nét, bền màu và phù hợp với bao bì thực phẩm.</p>
        <p>Các thông tin quan trọng như tên sản phẩm, hạn sử dụng, mã lô hàng cần được in rõ ràng.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "giay":
    st.markdown("<h1 style='text-align:center;'>Thông tin giấy bao bì</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>📦 Chất liệu bao bì</h3>
        <p>Bao bì cần sạch, chắc chắn và phù hợp với thực phẩm.</p>
        <p>Thiết kế có thể dùng màu xanh cốm, họa tiết lá sen để tăng tính nhận diện thương hiệu.</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "thuhoi":
    st.markdown("<h1 style='text-align:center;'>Chính sách thu hồi bao bì</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>♻️ Chính sách thu hồi bao bì</h3>
        <p>Khách hàng được khuyến khích phân loại và xử lý bao bì sau khi sử dụng.</p>
        <ul>
            <li>Không vứt bao bì ra môi trường.</li>
            <li>Phân loại bao bì giấy, túi, hộp sau khi dùng.</li>
            <li>Ưu tiên sử dụng bao bì thân thiện với môi trường.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

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
<div class="footer-full">
    <div class="footer-content">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p>📍 Địa chỉ: Làng Vòng, Dịch Vọng Hậu, Cầu Giấy, Hà Nội</p>
        <p>📞 <a href="tel:0385437503">0385 437 503</a></p>
        <p>💬 <a href="https://zalo.me/0385437503" target="_blank">Chat Zalo</a></p>
        <p style="margin-top:15px; font-size:13px; color:#ccc;">
            © 2026 Cốm Làng Vòng. All rights reserved.
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

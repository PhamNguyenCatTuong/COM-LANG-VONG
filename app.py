import streamlit as st

st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide"
)

# Lấy tham số trang
params = st.query_params
page = params.get("page","home")

# CSS giao diện
st.markdown("""
<style>

/* ẨN MENU STREAMLIT */
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
[data-testid="stToolbar"] {display: none !important;}

/* ===== RESET ===== */
html, body {
margin: 0;
padding: 0;import streamlit as st

st.set_page_config(
    page_title="Cốm Làng Vòng",
    layout="wide"
)

params = st.query_params
page = params.get("page", "tongquan")

st.markdown("""
<style>

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

</style>
""", unsafe_allow_html=True)

.topbar {
    position: sticky;
    top: 0;
    width: calc(100% - 20px);
    padding: 12px 16px;
    display: flex;
    flex-direction: column;
    box-shadow: 0 2px 10px rgba(0,0,0,0.08);
    z-index: 999;
    border-radius: 15px;
    margin: 10px auto;
    background: white;
}

.top-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
}

.logo {
    font-size: 30px;
    font-weight: 700;
    color: #2e7d32;
    white-space: nowrap;
    line-height: 1.2;
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
    margin-top: 10px;
    gap: 8px;
}

#menu-toggle:checked ~ .menu {
    display: flex;
}

.dropdown {
    position: relative;
    display: block;
}

.dropbtn {
    background: #2e7d32;
    color: white;
    padding: 11px 14px;
    border: none;
    border-radius: 8px;
    font-size: 15px;
    cursor: pointer;
    width: 100%;
    text-align: left;
    font-weight: 600;
}

.dropdown-content {
    display: none;
    background: white;
    border: 1px solid #e5e5e5;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 5px;
}

.dropdown-content a {
    color: #333;
    padding: 12px 14px;
    text-decoration: none;
    display: block;
    border-bottom: 1px solid #eee;
    font-size: 15px;
}

.dropdown-content a:hover {
    background: #f1f8e9;
}

.dropdown:hover .dropdown-content {
    display: block;
}

.content {
    padding: 20px;
    max-width: 850px;
    margin: 40px auto 0 auto;
    font-size: 16px;
    line-height: 1.8;
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
    border-radius: 12px;
    max-width: 100%;
    height: auto;
    box-sizing: border-box;
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
    align-items: center;
    justify-content: center;
    color: white;
    font-size: 22px;
    text-decoration: none;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    animation: pulse 1.5s infinite;
}

.call-btn {background: #2e7d32;}
.zalo-btn {background: #0084ff;}

@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.1);}
    100% {transform: scale(1);}
}

.footer-full {
    width: calc(100vw - 32px);
    margin-left: calc(50% - 50vw + 16px);
    background: #000;
    color: #fff;
    padding: 40px 20px;
    margin-top: 40px;
    box-sizing: border-box;
}

.footer-content {
    max-width: 850px;
    margin: auto;
    text-align: center;
}

.footer-content a {
    color: #fff;
    text-decoration: none;
}

@media (min-width: 768px) {
    .topbar {
        flex-direction: row;
        align-items: center;
        padding: 15px 30px;
    }

    .top-row {
        margin-right: 20px;
    }

    .menu {
        display: flex !important;
        flex-direction: row;
        flex-wrap: wrap;
        margin-top: 0;
        gap: 8px;
    }

    .hamburger {
        display: none;
    }

    .logo {
        font-size: 28px;
    }

    .dropbtn {
        width: auto;
        text-align: center;
        font-size: 14px;
    }

    .dropdown {
        display: inline-block;
    }

    .dropdown-content {
        position: absolute;
        min-width: 240px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.12);
        z-index: 9999;
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
            <a href="?page=tensp">Tên sản phẩm</a>
            <a href="?page=masp">Mã sản phẩm</a>
            <a href="?page=thuonghieu">Thương hiệu</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Truy xuất nguồn gốc</button>
        <div class="dropdown-content">
            <a href="?page=nguyenlieu">Nguồn nguyên liệu</a>
            <a href="?page=khuvuc">Khu vực sản xuất</a>
            <a href="?page=malo">Mã lô hàng</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Chất lượng & chứng nhận</button>
        <div class="dropdown-content">
            <a href="?page=ocop">Chứng nhận OCOP</a>
            <a href="?page=kiemdinh">Kiểm định chất lượng</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Nội dung truyền thông</button>
        <div class="dropdown-content">
            <a href="?page=cauchuyen">Câu chuyện sản phẩm</a>
            <a href="?page=hinhanh">Hình ảnh</a>
            <a href="?page=video">Video giới thiệu</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Thông tin bao bì</button>
        <div class="dropdown-content">
            <a href="?page=muc">Mực</a>
            <a href="?page=giay">Giấy</a>
            <a href="?page=thuhoi">Chính sách thu hồi bao bì</a>
        </div>
    </div>

    <div class="dropdown">
        <button class="dropbtn">Thông tin liên hệ</button>
        <div class="dropdown-content">
            <a href="?page=website">Website</a>
            <a href="?page=hotline">Hotline</a>
            <a href="?page=mxh">Mạng xã hội</a>
        </div>
    </div>

</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='content'>", unsafe_allow_html=True)

if page == "tongquan":
    st.markdown("<h1 style='text-align:center;'>Tổng quan</h1>", unsafe_allow_html=True)
    st.image("Com tong quan.jpg", width=700)
    st.write("""
    Cốm Làng Vòng là một trong những đặc sản nổi tiếng của Hà Nội, gắn liền với mùa thu và văn hóa ẩm thực đất kinh kỳ.
    Sản phẩm được làm từ lúa nếp non, có màu xanh dịu, hương thơm nhẹ, vị ngọt thanh và độ dẻo đặc trưng.
    """)
    st.write("""
    Không chỉ là món ăn truyền thống, cốm còn được dùng làm quà biếu, nguyên liệu chế biến bánh cốm, chả cốm, xôi cốm,
    chè cốm và nhiều món ăn đặc sản khác.
    """)

elif page == "tensp":
    st.markdown("<h1 style='text-align:center;'>Tên sản phẩm</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p><b>Tên sản phẩm:</b> Cốm Làng Vòng</p>
        <p><b>Loại sản phẩm:</b> Thực phẩm truyền thống</p>
        <p><b>Đặc điểm:</b> Hạt cốm mỏng, dẻo, thơm nhẹ, có màu xanh non tự nhiên.</p>
        <p>
        Sản phẩm phù hợp để ăn trực tiếp, làm quà biếu hoặc chế biến thành các món ăn truyền thống như bánh cốm,
        chả cốm, xôi cốm và chè cốm.
        </p>
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
        <p>
        Mã sản phẩm giúp khách hàng nhận diện, tra cứu thông tin và phân biệt sản phẩm với các dòng sản phẩm khác.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "thuonghieu":
    st.markdown("<h1 style='text-align:center;'>Thương hiệu</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🌿 Thương hiệu Cốm Làng Vòng</h3>
        <p>
        Cốm Làng Vòng là thương hiệu gắn liền với làng nghề truyền thống tại Hà Nội.
        Sản phẩm đại diện cho sự tinh tế, thanh tao và nét đẹp trong văn hóa ẩm thực Thủ đô.
        </p>
        <p>
        Thương hiệu hướng đến việc gìn giữ hương vị cốm truyền thống, kết hợp với cách giới thiệu hiện đại,
        giúp khách hàng dễ dàng tìm hiểu nguồn gốc, chất lượng và thông tin sản phẩm.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "nguyenlieu":
    st.markdown("<h1 style='text-align:center;'>Nguồn nguyên liệu</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>🌾 Lúa nếp non chọn lọc</h3>
        <p>
        Nguyên liệu chính để làm cốm là lúa nếp non, thường được chọn khi hạt còn ngậm sữa.
        Đây là thời điểm hạt lúa có độ mềm, dẻo và mùi thơm tự nhiên.
        </p>
        <p>
        Lúa sau khi thu hoạch được tuốt, sàng lọc và loại bỏ hạt lép trước khi đưa vào rang và giã.
        Việc chọn nguyên liệu kỹ giúp cốm giữ được màu xanh đẹp, hương thơm nhẹ và vị ngọt thanh.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "khuvuc":
    st.markdown("<h1 style='text-align:center;'>Khu vực sản xuất</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>📍 Làng Vòng, Cầu Giấy, Hà Nội</h3>
        <p>
        Sản phẩm gắn với khu vực làng Vòng, phường Dịch Vọng Hậu, quận Cầu Giấy, Hà Nội.
        Đây là địa danh nổi tiếng với nghề làm cốm truyền thống.
        </p>
        <p>
        Khu vực sản xuất mang giá trị văn hóa lâu đời, góp phần tạo nên hình ảnh cốm như một thức quà đặc trưng
        của mùa thu Hà Nội.
        </p>
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
        <p>
        Mã lô hàng giúp người bán và khách hàng theo dõi thông tin sản xuất, thời gian đóng gói và chất lượng sản phẩm.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "ocop":
    st.markdown("<h1 style='text-align:center;'>Chứng nhận OCOP</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>✅ Định hướng sản phẩm OCOP</h3>
        <p>
        OCOP là chương trình đánh giá, phân hạng sản phẩm đặc trưng của địa phương.
        Với giá trị truyền thống và nguồn gốc rõ ràng, Cốm Làng Vòng phù hợp để phát triển theo định hướng sản phẩm OCOP.
        </p>
        <p>
        Thông tin chứng nhận cụ thể cần được cập nhật theo hồ sơ thực tế của cơ sở sản xuất.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "kiemdinh":
    st.markdown("<h1 style='text-align:center;'>Kiểm định chất lượng</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🔍 Kiểm soát chất lượng sản phẩm</h3>
        <ul>
            <li>Nguyên liệu có nguồn gốc rõ ràng.</li>
            <li>Quy trình chế biến sạch sẽ, đảm bảo vệ sinh.</li>
            <li>Không sử dụng nguyên liệu kém chất lượng.</li>
            <li>Bảo quản nơi khô ráo, thoáng mát.</li>
            <li>Đóng gói cẩn thận để hạn chế tiếp xúc với môi trường bên ngoài.</li>
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
    Cốm thường được gói trong lá sen để giữ hương thơm tự nhiên và tạo nên nét riêng rất Hà Nội.
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
        <p>
        Khu vực này dùng để hiển thị video giới thiệu về quy trình làm cốm, câu chuyện làng nghề hoặc hướng dẫn sử dụng sản phẩm.
        </p>
        <p><i>Khi có video, bạn thêm lệnh:</i></p>
        <p><b>st.video("link_youtube")</b></p>
    </div>
    """, unsafe_allow_html=True)

elif page == "muc":
    st.markdown("<h1 style='text-align:center;'>Thông tin mực in</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>🖨️ Mực in bao bì</h3>
        <p>
        Bao bì sản phẩm nên sử dụng loại mực in rõ nét, bền màu và phù hợp với bao bì thực phẩm.
        Thông tin trên bao bì cần dễ đọc, không bị lem nhòe trong quá trình vận chuyển.
        </p>
        <p>
        Các nội dung quan trọng như tên sản phẩm, hạn sử dụng, mã lô hàng và thông tin liên hệ cần được in rõ ràng.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "giay":
    st.markdown("<h1 style='text-align:center;'>Thông tin giấy bao bì</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>📦 Chất liệu bao bì</h3>
        <p>
        Bao bì cần đảm bảo sạch, chắc chắn và phù hợp với thực phẩm.
        Với sản phẩm cốm, bao bì nên giúp hạn chế ẩm, giữ hương thơm và bảo vệ sản phẩm trong quá trình vận chuyển.
        </p>
        <p>
        Có thể kết hợp phong cách truyền thống như họa tiết lá sen, màu xanh cốm cùng thiết kế hiện đại.
        </p>
    </div>
    """, unsafe_allow_html=True)

elif page == "thuhoi":
    st.markdown("<h1 style='text-align:center;'>Chính sách thu hồi bao bì</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card2">
        <h3>♻️ Chính sách thu hồi bao bì</h3>
        <p>
        Khách hàng được khuyến khích phân loại và xử lý bao bì sau khi sử dụng.
        Với các đơn hàng số lượng lớn, cơ sở có thể triển khai chương trình thu hồi bao bì để góp phần giảm rác thải.
        </p>
        <ul>
            <li>Không vứt bao bì ra môi trường.</li>
            <li>Phân loại bao bì giấy, túi, hộp sau khi dùng.</li>
            <li>Ưu tiên sử dụng bao bì thân thiện với môi trường.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

elif page == "website":
    st.markdown("<h1 style='text-align:center;'>Website</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>🌐 Website giới thiệu sản phẩm</h3>
        <p>
        Website cung cấp thông tin về sản phẩm, nguồn gốc, chất lượng, bao bì và kênh liên hệ đặt hàng.
        </p>
        <p><b>Địa chỉ website:</b> com-lang-vong.streamlit.app</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "hotline":
    st.markdown("<h1 style='text-align:center;'>Hotline</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card" style="text-align:center;">
        <h3>📞 Hotline đặt hàng</h3>
        <p>Khách hàng có thể liên hệ để được tư vấn sản phẩm, giá bán và phương thức giao hàng.</p>
        <p style="font-size:26px; font-weight:bold; color:#2e7d32;">0385 437 503</p>
        <a href="tel:0385437503" style="
            background:#2e7d32;
            color:white;
            padding:12px 20px;
            border-radius:8px;
            text-decoration:none;
            font-weight:bold;
        ">Gọi ngay</a>
    </div>
    """, unsafe_allow_html=True)

elif page == "mxh":
    st.markdown("<h1 style='text-align:center;'>Mạng xã hội</h1>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <h3>💬 Kết nối với chúng tôi</h3>
        <p>
        Theo dõi các kênh mạng xã hội để cập nhật hình ảnh sản phẩm, chương trình khuyến mãi
        và thông tin đặt hàng mới nhất.
        </p>
        <p>💬 Zalo: 0385 437 503</p>
        <p>📘 Facebook: Cốm Làng Vòng</p>
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

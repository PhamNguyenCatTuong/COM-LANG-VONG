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
padding: 0;
}

/* ===== TOPBAR ===== */
.topbar{
position:sticky;
top:0;
left:0;
width:100%;
padding:10px 15px;
display:flex;
flex-direction:column;
box-shadow:0 2px 8px rgba(0,0,0,0.08);
z-index:999;
}

/* ===== HEADER ===== */
.topbar{
position:sticky;
top:0;
padding:12px 16px;
box-shadow:0 2px 10px rgba(0,0,0,0.08);
z-index:999;
border-radius: 15px;
margin:10px;
}

/* ROW */
.top-row{
display:flex;
justify-content:space-between;
align-items:center;
gap:10px;
width:100%;
overflow:hidden;
}

/* LOGO */
.logo{
font-size:35px;
font-weight:700;
color:#2e7d32;
white-space: nowrap;
overflow: visible;
line-height:1.2;
padding-right:10px;
}

/* ===== FLOAT BUTTON ===== */
.floating-contact{
position:fixed;
bottom:50px;
right:15px;
display:flex;
flex-direction:column;
gap:10px;
z-index:9999;
}

/* NÚT CHUNG */
.float-btn{
width:50px;
height:50px;
border-radius:50%;
display:flex;
align-items:center;
justify-content:center;
color:white;
font-size:22px;
text-decoration:none;
box-shadow:0 4px 10px rgba(0,0,0,0.2);
animation: pulse 1.5s infinite;
}

/* GỌI */
.call-btn{
background:#2e7d32;
}

/* ZALO */
.zalo-btn{
background:#0084ff;
}

/* HIỆU ỨNG NHẤP NHÁY */
@keyframes pulse {
0% {transform: scale(1);}
50% {transform: scale(1.1);}
100% {transform: scale(1);}
}

/* MOBILE chỉnh nhỏ lại */
@media (max-width:768px){
.float-btn{
width:45px;
height:45px;
font-size:20px;
}
}

/* HAMBURGER */
.hamburger{
font-size:25px;
cursor:pointer;
}

/* ẨN CHECKBOX */
#menu-toggle{
display:none;
}

/* ===== DROPDOWN MENU ===== */

.dropdown {
position: relative;
display: inline-block;
}

.dropbtn {
background: #2e7d32;
color: white;
padding: 10px 16px;
border: none;
border-radius: 8px;
font-size: 14px;
cursor: pointer;
margin: 5px;
}

.dropdown-content {
display: none;
position: absolute;
background-color: white;
min-width: 230px;
box-shadow: 0 4px 10px rgba(0,0,0,0.1);
border-radius: 10px;
overflow: hidden;
z-index: 9999;
}

.dropdown-content a {
color: #333;
padding: 12px 16px;
text-decoration: none;
display: block;
border-bottom: 1px solid #eee;
}

.dropdown-content a:hover {
background: #f1f8e9;
}

.dropdown:hover .dropdown-content {
display: block;
}

/* MOBILE */

@media (max-width:768px){

.menu{
display:flex;
flex-direction:column;
gap:10px;
}

.dropdown{
width:100%;
}

.dropbtn{
width:100%;
text-align:left;
}

.dropdown-content{
position: relative;
width:100%;
box-shadow:none;
border:1px solid #eee;
}

}

/* MENU */
.menu{
display:none;
flex-direction:column;
margin-top:10px;
}

.menu a{
padding:10px 0;
border-bottom:1px solid #eee;
text-decoration:none;
color:#333;
font-size:15px;
}

/* Khi check thì mở menu */
#menu-toggle:checked ~ .menu{
display:flex;
}

/* ===== CONTENT ===== */
.content{
margin-top:90px;
padding:20px;
max-width:700px;
margin-left:auto;
margin-right:auto;
font-size:15px;
line-height:1.8;
}

/* IMAGE AUTO SCALE */
img{
border-radius:10px;
max-width:100%;
height:auto;
padding:5px;
box-sizing:border-box;
}

/* ===== DESKTOP ===== */
@media (min-width:768px){

.topbar{
flex-direction:row;
align-items:center;
padding:15px 40px;
}

.menu{
display:flex !important;
flex-direction:row;
margin-top:0;
}

.menu a{
border:none;
margin-left:20px;
padding:0;
}

.hamburger{
display:none;
}

.logo{
font-size:26px;
}

.content{
margin-top:80px;
font-size:16px;
}

}

</style>
""", unsafe_allow_html=True)

# Lấy trang hiện tại
params = st.query_params
page = params.get ("page", "tongquan")

# Thanh tiêu đề + menu
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
        <a href="?page=thuhhoi">Chính sách thu hồi bao bì</a>
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
""", unsafe_allow_html=True)

st.markdown("<div class='content'>", unsafe_allow_html=True)

# Nội dung các menu

elif page == "tensp":

    st.markdown("<h1 style='text-align:center;'>Tên sản phẩm</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px;">
        <h3>🌾 Cốm Làng Vòng</h3>
        <p>
        Cốm Làng Vòng là sản phẩm truyền thống đặc trưng của Hà Nội, được làm từ lúa nếp non.
        Sản phẩm có màu xanh dịu, hạt mỏng dẻo, hương thơm nhẹ và vị ngọt thanh tự nhiên.
        </p>
        <p>
        Cốm thường được dùng để ăn trực tiếp, làm quà biếu hoặc chế biến thành nhiều món ăn như
        bánh cốm, chả cốm, xôi cốm, chè cốm.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "masp":

    st.markdown("<h1 style='text-align:center;'>Mã sản phẩm</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px;">
        <h3>🏷️ Mã sản phẩm</h3>
        <p><b>Mã sản phẩm:</b> COM-LV-001</p>
        <p><b>Nhóm sản phẩm:</b> Thực phẩm truyền thống</p>
        <p><b>Dòng sản phẩm:</b> Đặc sản Hà Nội</p>
        <p>
        Mã sản phẩm giúp khách hàng dễ dàng nhận diện, tra cứu thông tin và phân biệt
        sản phẩm Cốm Làng Vòng với các sản phẩm khác.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "thuonghieu":

    st.markdown("<h1 style='text-align:center;'>Thương hiệu</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px;">
        <h3>🌿 Thương hiệu Cốm Làng Vòng</h3>
        <p>
        Cốm Làng Vòng là thương hiệu gắn liền với làng nghề truyền thống tại Hà Nội.
        Sản phẩm đại diện cho nét tinh tế trong văn hóa ẩm thực đất kinh kỳ.
        </p>
        <p>
        Thương hiệu hướng đến việc gìn giữ hương vị cốm truyền thống, đồng thời giới thiệu
        sản phẩm đến nhiều khách hàng hơn thông qua bao bì, thông tin truy xuất và kênh liên hệ hiện đại.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "nguyenlieu":

    st.markdown("<h1 style='text-align:center;'>Nguồn nguyên liệu</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f5e9; padding:20px; border-radius:12px;">
        <h3>🌾 Lúa nếp non chọn lọc</h3>
        <p>
        Nguyên liệu chính để làm cốm là lúa nếp non, thường được chọn khi hạt lúa còn ngậm sữa.
        Đây là thời điểm hạt có độ mềm, dẻo và mùi thơm đặc trưng.
        </p>
        <p>
        Lúa sau khi thu hoạch được tuốt, sàng lọc và loại bỏ hạt lép trước khi đưa vào rang, giã.
        Việc chọn nguyên liệu kỹ giúp cốm giữ được màu xanh đẹp, vị ngọt nhẹ và hương thơm tự nhiên.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "khuvuc":

    st.markdown("<h1 style='text-align:center;'>Khu vực sản xuất</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f5e9; padding:20px; border-radius:12px;">
        <h3>📍 Làng Vòng, Cầu Giấy, Hà Nội</h3>
        <p>
        Sản phẩm gắn với khu vực làng Vòng, phường Dịch Vọng Hậu, quận Cầu Giấy, Hà Nội.
        Đây là địa danh nổi tiếng với nghề làm cốm truyền thống.
        </p>
        <p>
        Khu vực sản xuất mang giá trị văn hóa lâu đời, góp phần tạo nên hình ảnh cốm như
        một thức quà đặc trưng của mùa thu Hà Nội.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "malo":

    st.markdown("<h1 style='text-align:center;'>Mã lô hàng</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f5e9; padding:20px; border-radius:12px;">
        <h3>🏷️ Thông tin lô hàng</h3>
        <p><b>Mã lô mẫu:</b> LV-2026-001</p>
        <p><b>Ngày sản xuất:</b> Cập nhật trên bao bì sản phẩm</p>
        <p><b>Hạn sử dụng:</b> Cập nhật theo từng loại sản phẩm</p>
        <p>
        Mã lô hàng giúp người bán và khách hàng theo dõi thông tin sản xuất,
        thời gian đóng gói và chất lượng sản phẩm theo từng đợt.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "ocop":

    st.markdown("<h1 style='text-align:center;'>Chứng nhận OCOP</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px;">
        <h3>✅ Định hướng sản phẩm OCOP</h3>
        <p>
        OCOP là chương trình đánh giá, phân hạng sản phẩm đặc trưng của địa phương.
        Với giá trị truyền thống và nguồn gốc rõ ràng, Cốm Làng Vòng phù hợp để phát triển
        theo định hướng sản phẩm OCOP.
        </p>
        <p>
        Thông tin chứng nhận cụ thể cần được cập nhật theo hồ sơ thực tế của cơ sở sản xuất.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "kiemdinh":

    st.markdown("<h1 style='text-align:center;'>Kiểm định chất lượng</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px;">
        <h3>🔍 Kiểm soát chất lượng sản phẩm</h3>
        <p>
        Cốm cần được sản xuất trong điều kiện sạch sẽ, nguyên liệu được chọn lọc kỹ
        và quy trình chế biến đảm bảo vệ sinh an toàn thực phẩm.
        </p>
        <ul>
            <li>Nguyên liệu rõ nguồn gốc</li>
            <li>Không sử dụng nguyên liệu kém chất lượng</li>
            <li>Bảo quản nơi khô ráo, thoáng mát</li>
            <li>Đóng gói sạch, hạn chế tiếp xúc trực tiếp với môi trường bên ngoài</li>
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
    Hương cốm thơm nhẹ, màu xanh non và vị ngọt thanh khiến sản phẩm trở thành thức quà
    quen thuộc mỗi độ thu về. Cốm thường được gói trong lá sen để giữ hương thơm tự nhiên
    và tạo nên nét riêng rất Hà Nội.
    """)


elif page == "hinhanh":

    st.markdown("<h1 style='text-align:center;'>Hình ảnh</h1>", unsafe_allow_html=True)

    st.write("Một số hình ảnh giới thiệu sản phẩm Cốm Làng Vòng:")

    st.image("Com tong quan.jpg", width=450)
    st.image("Com tong quan 1.jpg", width=450)
    st.image("Com tong quan 2.jpg", width=450)


elif page == "video":

    st.markdown("<h1 style='text-align:center;'>Video giới thiệu</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px; text-align:center;">
        <h3>🎬 Video giới thiệu sản phẩm</h3>
        <p>
        Khu vực này dùng để hiển thị video giới thiệu về quy trình làm cốm,
        câu chuyện làng nghề hoặc hướng dẫn sử dụng sản phẩm.
        </p>
        <p><i>Bạn có thể thêm link YouTube bằng lệnh st.video("link_video").</i></p>
    </div>
    """, unsafe_allow_html=True)

    # Ví dụ khi có video:
    # st.video("https://www.youtube.com/watch?v=link_video")


elif page == "muc":

    st.markdown("<h1 style='text-align:center;'>Thông tin mực in</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f5e9; padding:20px; border-radius:12px;">
        <h3>🖨️ Mực in bao bì</h3>
        <p>
        Bao bì sản phẩm nên sử dụng loại mực in rõ nét, bền màu và phù hợp với bao bì thực phẩm.
        Thông tin trên bao bì cần dễ đọc, không bị lem nhòe trong quá trình vận chuyển.
        </p>
        <p>
        Các nội dung quan trọng như tên sản phẩm, hạn sử dụng, mã lô hàng và thông tin liên hệ
        cần được in rõ ràng để khách hàng dễ tra cứu.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "giay":

    st.markdown("<h1 style='text-align:center;'>Thông tin giấy bao bì</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f5e9; padding:20px; border-radius:12px;">
        <h3>📦 Chất liệu bao bì</h3>
        <p>
        Bao bì cần đảm bảo sạch, chắc chắn và phù hợp với thực phẩm.
        Với sản phẩm cốm, bao bì nên giúp hạn chế ẩm, giữ hương thơm và bảo vệ sản phẩm
        trong quá trình vận chuyển.
        </p>
        <p>
        Có thể kết hợp phong cách truyền thống như họa tiết lá sen, màu xanh cốm
        cùng thiết kế hiện đại để tăng tính nhận diện thương hiệu.
        </p>
    </div>
    """, unsafe_allow_html=True)


elif page == "thuhhoi":

    st.markdown("<h1 style='text-align:center;'>Chính sách thu hồi bao bì</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#e8f5e9; padding:20px; border-radius:12px;">
        <h3>♻️ Chính sách thu hồi bao bì</h3>
        <p>
        Khách hàng được khuyến khích phân loại và xử lý bao bì sau khi sử dụng.
        Với các đơn hàng số lượng lớn, cơ sở có thể triển khai chương trình thu hồi bao bì
        để góp phần giảm rác thải và bảo vệ môi trường.
        </p>
        <ul>
            <li>Không vứt bao bì ra môi trường</li>
            <li>Phân loại bao bì giấy, túi, hộp sau khi dùng</li>
            <li>Ưu tiên sử dụng bao bì thân thiện với môi trường</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)


elif page == "website":

    st.markdown("<h1 style='text-align:center;'>Website</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px; text-align:center;">
        <h3>🌐 Website giới thiệu sản phẩm</h3>
        <p>
        Website cung cấp thông tin về sản phẩm, nguồn gốc, chất lượng, bao bì
        và kênh liên hệ đặt hàng.
        </p>
        <p><b>Địa chỉ website:</b> com-lang-vong.streamlit.app</p>
    </div>
    """, unsafe_allow_html=True)


elif page == "hotline":

    st.markdown("<h1 style='text-align:center;'>Hotline</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px; text-align:center;">
        <h3>📞 Hotline đặt hàng</h3>
        <p>Khách hàng có thể liên hệ để được tư vấn sản phẩm, giá bán và phương thức giao hàng.</p>
        <p style="font-size:24px; font-weight:bold; color:#2e7d32;">
            0385 437 503
        </p>
        <a href="tel:0385437503" style="
            background:#2e7d32;
            color:white;
            padding:12px 20px;
            border-radius:8px;
            text-decoration:none;
            font-weight:bold;
        ">
            Gọi ngay
        </a>
    </div>
    """, unsafe_allow_html=True)


elif page == "mxh":

    st.markdown("<h1 style='text-align:center;'>Mạng xã hội</h1>", unsafe_allow_html=True)

    st.markdown("""
    <div style="background:#f1f8e9; padding:20px; border-radius:12px; text-align:center;">
        <h3>💬 Kết nối với chúng tôi</h3>
        <p>
        Theo dõi các kênh mạng xã hội để cập nhật hình ảnh sản phẩm, chương trình khuyến mãi
        và thông tin đặt hàng mới nhất.
        </p>
        <p>💬 Zalo: 0385 437 503</p>
        <p>📘 Facebook: Cốm Làng Vòng</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<style>

/* GIỮ KHOẢNG CÁCH NỘI DUNG TRÊN MOBILE */
.block-container {
    padding-left: 16px !important;
    padding-right: 16px !important;
    padding-top: 0 !important;
    padding-bottom: 0 !important;
}

/* FOOTER FULL MÀN HÌNH */
.footer-full {
    position: relative;
    width: calc(100vw - 32px);
    left: 50%;
    margin-left: calc(-50vw + 16px);

/* NỘI DUNG BÊN TRONG */
.footer-content {
    max-width: 700px;
    margin: auto;
    text-align: center;
}

/* LINK */
.footer-content a {
    color: #fff;
    text-decoration: none;
}

</style>

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

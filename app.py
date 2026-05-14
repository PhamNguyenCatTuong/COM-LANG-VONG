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

if page == "tongquan":

    import streamlit as st
    st.markdown("<h1 style='text-align: center;'>Tổng quan</h1>", unsafe_allow_html=True)
    st.image("Com tong quan.jpg", width=450)
    st.write("""
            Mỗi khi thu về, Hà Nội như dịu lại trong làn gió heo may và sắc vàng nhè nhẹ của nắng cuối mùa. Giữa không gian ấy, hương thơm ngọt lành của lúa non từ những gánh cốm thoảng qua từng con phố khiến lòng người bỗng chậm lại. Nhắc đến mùa thu Hà Nội, người ta không thể không nhắc đến Cốm Làng Vòng – thức quà thanh tao đã trở thành biểu tượng ẩm thực của Thủ đô. Câu ca dao xưa vẫn còn nhắc:
    """)
    st.write("""
            “Cốm Vòng, gạo tám Mễ Trì
    """)
    st.write("""
            Tương Bần, húng Láng còn gì ngon hơn!”
    """)
    st.write("""
            Lời ca ấy không chỉ tôn vinh hương vị mà còn khẳng định vị thế của cốm làng Vòng trong bản đồ ẩm thực đất kinh kỳ.
    """)
    st.image("Com tong quan 1.jpg", width=450)
    st.write("""
             Nguyên liệu làm nên cốm là lúa nếp cái hoa vàng – giống nếp quý nổi tiếng thơm dẻo. Lúa phải được gặt khi hạt vừa ngậm sữa, không quá non để khỏi nát, cũng không quá già để tránh cứng. Chính sự chuẩn xác trong khâu chọn lúa đã quyết định đến chất lượng hạt cốm. Sau khi tuốt lấy thóc, người thợ phải sàng sảy kỹ, đãi sạch hạt lép rồi đem rang trong chảo gang trên lửa đều tay. Đây là công đoạn đòi hỏi kinh nghiệm và sự tinh tế, bởi chỉ cần quá lửa một chút là hạt sẽ gãy, mất đi độ dẻo đặc trưng.
    """)
    st.image("Com tong quan 2.jpg", width=450)
    st.write("""
            Thóc rang xong còn nóng được đem giã bằng chày gỗ. Người thợ phải giã nhiều lần, nhịp nhàng và kiên nhẫn để tách vỏ trấu mà không làm nát hạt. Sau đó cốm được sàng sảy lại nhiều lượt cho đến khi hạt mỏng, dẹt, xanh mướt. Cuối cùng, cốm được gói trong hai lớp lá – bên trong là lá ráy giữ ẩm, bên ngoài là lá sen thơm ngát. Chính lớp lá sen ấy đã góp phần làm nên mùi hương rất riêng của cốm, khiến mỗi gói cốm như gói trọn hương thu Hà Nội.
            Từ một sản phẩm làng nghề, cốm dần trở thành món quà đặc trưng của Thủ đô. Mỗi độ thu sang, người Hà Nội lại mong chờ những mẻ cốm mới. Hình ảnh các bà, các mẹ gánh cốm đi bán đã in sâu vào ký ức bao thế hệ. Cốm không phải để ăn vội vàng, mà để nhâm nhi. Người ta thường dùng năm đầu ngón tay nâng nhẹ một nhúm cốm, nhai chậm rãi để cảm nhận vị ngọt thanh, dẻo thơm hòa cùng hương sữa non. Nhấp thêm một ngụm trà xanh ấm nóng, đặc biệt là trà Thái Nguyên, vị chát dịu của trà quyện với vị ngọt của cốm tạo nên một sự cân bằng tinh tế.
    """)
    st.image("Com tong quan 3.jpg", width=450)
    st.write("""
         Không chỉ thưởng thức trực tiếp, cốm còn được sáng tạo thành nhiều món ăn hấp dẫn như bánh cốm, chả cốm, xôi cốm hạt sen, cốm xào hay đậu chiên cốm. Trong đó, bánh cốm đã trở thành lễ vật quen thuộc trong các dịp cưới hỏi truyền thống ở miền Bắc, góp phần đưa hương cốm làng Vòng lan tỏa rộng khắp cả nước.
    """)
    st.write("""
         Ngày nay, giữa nhịp sống hiện đại và sự phát triển không ngừng của Hà Nội, nghề làm cốm vẫn được gìn giữ như một phần hồn cốt của Thủ đô. Dù có nhiều biến đổi về hình thức kinh doanh hay bao bì sản phẩm, hương vị cốm truyền thống vẫn giữ nguyên nét thanh tao vốn có. Cốm làng Vòng không chỉ là món ăn, mà còn là ký ức, là văn hóa, là biểu tượng của mùa thu Hà Nội – một thức quà giản dị nhưng chứa đựng cả tinh hoa của đất trời và bàn tay cần mẫn của con người.
    """)
    st.markdown("""
<div class="floating-contact">

<a href="tel:0385437503" class="float-btn call-btn">
📞
</a>

<a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">
💬
</a>

</div>
""", unsafe_allow_html=True)

elif page == "sanpham":

    import streamlit as st

    st.markdown("<h1 style='text-align: center;'>Sản phẩm từ cốm</h1>", unsafe_allow_html=True)

    st.write("""
    Cốm không chỉ là món ăn truyền thống mà còn được chế biến thành nhiều sản phẩm hấp dẫn, phù hợp làm quà biếu hoặc thưởng thức hàng ngày.
    """)

    # ===== DANH SÁCH SẢN PHẨM =====
    st.markdown("### 🌾 Các sản phẩm nổi bật")

    st.markdown("""
<div style="padding:15px; border-radius:10px; background:#f1f8e9;">
<b>🌿 Cốm khô</b><br>
Thơm nhẹ, dễ bảo quản, phù hợp ăn trực tiếp hoặc chế biến
</div>

<div style="padding:15px; border-radius:10px; background:#f1f8e9;">
<b>🍰 Bánh cốm</b><br>
Dẻo thơm, nhân đậu xanh ngọt dịu – đặc sản cưới hỏi
</div>

<div style="padding:15px; border-radius:10px; background:#f1f8e9;">
<b>🍖 Chả cốm</b><br>
Kết hợp thịt và cốm – món ăn đậm vị Hà Nội
</div>

<div style="padding:15px; border-radius:10px; background:#f1f8e9;">
<b>🍚 Xôi cốm</b><br>
Mềm dẻo, thơm hương lá sen, ăn sáng cực ngon
</div>
""", unsafe_allow_html=True)
    # ===== ĐIỂM NỔI BẬT =====
    st.markdown("""
    <div style="
        background:#e8f5e9;
        padding:15px;
        border-radius:10px;
        margin-top:20px;
    ">
        ✔ Nguyên liệu nếp non chọn lọc <br>
        ✔ Không chất bảo quản <br>
        ✔ Hương vị truyền thống Hà Nội
    </div>
    """, unsafe_allow_html=True)

    # ===== CTA =====
    st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <a href="tel:0385437503" style="
            background:#2e7d32;
            color:white;
            padding:12px 20px;
            border-radius:8px;
            text-decoration:none;
            font-weight:bold;
        ">
            📞 Đặt hàng ngay
        </a>
    </div>
    """, unsafe_allow_html=True)

    # FLOAT BUTTON
    st.markdown("""
    <div class="floating-contact">

    <a href="tel:0385437503" class="float-btn call-btn">📞</a>

    <a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">💬</a>

    </div>
    """, unsafe_allow_html=True)

elif page == "dinhduong":

    import streamlit as st
    st.markdown("<h1 style='text-align: center;'>Dinh dưỡng</h1>", unsafe_allow_html=True)
    st.write("""
    Cốm khô được làm từ gạo nếp non, không chỉ thơm ngon mà còn cung cấp nhiều giá trị dinh dưỡng tự nhiên cho cơ thể.
    """)

    # ===== BẢNG DINH DƯỠNG =====
    st.markdown("### 📊 Thành phần dinh dưỡng trong 100g cốm khô")

    st.markdown("""
    <table>
        <tr>
            <th>Thành phần</th>
            <th>Hàm lượng</th>
        </tr>
        <tr>
            <td>Năng lượng</td>
            <td>350 – 370 kcal</td>
        </tr>
        <tr>
            <td>Carbohydrate</td>
            <td>75 – 80g</td>
        </tr>
        <tr>
            <td>Protein</td>
            <td>6 – 8g</td>
        </tr>
        <tr>
            <td>Chất béo</td>
            <td>1 – 2g</td>
        </tr>
        <tr>
            <td>Chất xơ</td>
            <td>1 – 2g</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)

    # ===== HIGHLIGHT =====
    st.markdown("""
    <div style="
        background:#e8f5e9;
        padding:15px;
        border-radius:10px;
        margin-top:20px;
    ">
        👉 <b>Điểm nổi bật:</b> Giàu năng lượng – Ít chất béo – Dễ tiêu hóa
    </div>
    """, unsafe_allow_html=True)

    # ===== LỢI ÍCH =====
    st.markdown("### 💪 Lợi ích khi sử dụng cốm")

    st.write("""
    - ⚡ **Bổ sung năng lượng nhanh**: Hàm lượng tinh bột cao giúp cơ thể hoạt động hiệu quả  
    - 🌿 **Tự nhiên, ít chế biến**: Giữ được hương vị và dưỡng chất từ lúa non  
    - 🧠 **Hỗ trợ chuyển hóa**: Chứa vitamin nhóm B tốt cho cơ thể  
    - ❤️ **Dễ tiêu hóa**: Phù hợp ăn nhẹ, không gây nặng bụng  
    """)

    # ===== LƯU Ý =====
    st.markdown("### ⚠️ Lưu ý khi sử dụng")

    st.write("""
    - Nên ăn vừa phải nếu đang giảm cân  
    - Người cần kiểm soát đường huyết nên hạn chế  
    """)

    # ===== CTA =====
    st.markdown("""
    <div style="
        text-align:center;
        margin-top:30px;
    ">
        <a href="?page=sanpham" style="
            background:#2e7d32;
            color:white;
            padding:12px 20px;
            border-radius:8px;
            text-decoration:none;
            font-weight:bold;
        ">
            👉 Xem sản phẩm ngay
        </a>
    </div>
    """, unsafe_allow_html=True)

    # ===== FLOAT BUTTON =====
    st.markdown("""
    <div class="floating-contact">

    <a href="tel:0385437503" class="float-btn call-btn">
    📞
    </a>

    <a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">
    💬
    </a>

    </div>
    """, unsafe_allow_html=True)
    st.image("GANH COM.png", width=450)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "nguongoc":

    import streamlit as st

    st.markdown("<h1 style='text-align: center;'>Nguồn gốc cốm làng Vòng</h1>", unsafe_allow_html=True)

    st.write("""
    Cốm làng Vòng là đặc sản nổi tiếng của Hà Nội, gắn liền với truyền thống hàng trăm năm và được xem là biểu tượng của mùa thu đất Bắc.
    """)

    # ===== CÂU CHUYỆN =====
    st.markdown("### 📜 Câu chuyện hình thành")

    st.write("""
    Theo truyền lại, vào một năm mưa bão lớn, lúa bị ngập khi còn xanh. Người dân đã thu hoạch lúa non, rang lên để chống đói. Không ngờ hạt lúa non lại mang hương vị dẻo thơm đặc biệt. Từ đó, nghề làm cốm ra đời và phát triển cho đến ngày nay.
    """)

    # ===== QUY TRÌNH =====
    st.markdown("### ⚙️ Quy trình làm cốm truyền thống")

    st.write("""
    - 🌾 Gặt lúa nếp non đúng thời điểm  
    - 🔥 Rang thóc bằng chảo gang  
    - 🥣 Giã thủ công nhiều lần  
    - 🍃 Gói trong lá sen giữ hương thơm  
    """)

    # ===== GIÁ TRỊ =====
    st.markdown("""
    <div style="
        background:#f1f8e9;
        padding:15px;
        border-radius:10px;
        margin-top:20px;
    ">
        💚 Cốm không chỉ là món ăn mà còn là:
        <br>• Văn hóa
        <br>• Ký ức tuổi thơ
        <br>• Tinh hoa ẩm thực Hà Nội
    </div>
    """, unsafe_allow_html=True)

    # ===== CTA =====
    st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <a href="?page=sanpham" style="
            background:#2e7d32;
            color:white;
            padding:12px 20px;
            border-radius:8px;
            text-decoration:none;
            font-weight:bold;
        ">
            👉 Xem sản phẩm
        </a>
    </div>
    """, unsafe_allow_html=True)

    # FLOAT BUTTON
    st.markdown("""
    <div class="floating-contact">

    <a href="tel:0385437503" class="float-btn call-btn">📞</a>

    <a href="https://zalo.me/0385437503" target="_blank" class="float-btn zalo-btn">💬</a>

    </div>
    """, unsafe_allow_html=True)
    st.image("GANH COM.png", width=450)
    st.markdown('</div>', unsafe_allow_html=True)

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

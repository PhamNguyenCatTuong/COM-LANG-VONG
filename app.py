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
}

/* LOGO */
.logo{
font-size:35px;
font-weight:700;
color:#2e7d32;
}

/* ===== FLOAT BUTTON ===== */
.floating-contact{
position:fixed;
bottom:20px;
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
padding:12px;
max-width:700px;
margin-left:auto;
margin-right:auto;
font-size:15px;
line-height:1.6;
}

/* IMAGE AUTO SCALE */
img{
border-radius:10px;
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
page = params.get("page","tongquan")

# Thanh tiêu đề + menu
st.markdown("""
<div class="topbar">

<input type="checkbox" id="menu-toggle">

<div class="top-row">
    <div class="logo">🌾 Cốm Làng Vòng</div>
    <label for="menu-toggle" class="hamburger">☰</label>
</div>

<div class="menu">
    <a href="?page=tongquan">Tổng quan</a>
    <a href="?page=sanpham">Sản phẩm</a>
    <a href="?page=dinhduong">Dinh dưỡng</a>
    <a href="?page=nguongoc">Nguồn gốc</a>
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
    st.markdown("<h1 style='text-align: center;'>Sản phẩm</h1>", unsafe_allow_html=True)

    st.write("""
    Các sản phẩm phổ biến từ cốm:

    - Cốm tươi  
    - Bánh cốm  
    - Chả cốm  
    - Xôi cốm
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

elif page == "dinhduong":

    import streamlit as st
    st.markdown("<h1 style='text-align: center;'>Giá trị dinh dưỡng</h1>", unsafe_allow_html=True)

    st.write("""
    Cốm chứa nhiều chất dinh dưỡng từ lúa nếp non:

    - Carbohydrate cung cấp năng lượng
    - Vitamin nhóm B
    - Chất xơ
    - Một số khoáng chất cần thiết
    """)
    st.markdown('<div class="watermark-center">', unsafe_allow_html=True)
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
    st.markdown("<h1 style='text-align: center;'>Nguồn gốc</h1>", unsafe_allow_html=True)

    st.write("""
             Cốm Làng Vòng có nguồn gốc từ làng Vòng xưa (nay thuộc phường Dịch Vọng Hậu, quận Cầu Giấy, Hà Nội). Theo truyền lại, nghề làm cốm đã có từ hàng trăm năm trước. Có giai thoại kể rằng vào một năm mưa bão lớn, lúa ngoài đồng bị ngập khi còn xanh. Để cứu đói, người dân hái lúa non rang lên ăn tạm, không ngờ lại phát hiện hương vị dẻo thơm đặc biệt. Từ sự tình cờ ấy, nghề làm cốm ra đời và dần được hoàn thiện, truyền từ đời này sang đời khác như một báu vật của làng.
             Trải qua thời gian, cốm không chỉ là món ăn mà còn trở thành niềm tự hào của người dân nơi đây. Từ những gánh hàng rong len lỏi khắp phố phường đến các dịp lễ hỏi, cưới xin truyền thống của người Hà Nội, cốm luôn hiện diện như một phần không thể thiếu. 
            
    """)
    st.markdown('<div class="watermark-center">', unsafe_allow_html=True)
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

import streamlit as st
from datetime import datetime

# =====================================================
# st.image("ảnh quán trà sữa.png")
# =====================================================
st.set_page_config(
    page_title="Quán Trà Sữa - Tính Hóa Đơn",
    page_icon="🧋",
    layout="wide"
)

# =====================================================
# HIỂN THỊ ẢNH QUÁN
# =====================================================
try:
    st.image(
        "ảnh quán trà sữa.png",
        use_container_width=True
    )
except:
    st.info("💡 Chưa tìm thấy file ảnh 'ảnh quán trà sữa.png'.")

# =====================================================
# DỮ LIỆU MENU
# =====================================================

MENU = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa khoai môn": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa ô long": 38000,
    "Trà sữa caramel": 38000,
    "Trà sữa trân châu đường đen": 40000
}

TOPPING = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Thạch phô mai": 7000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000
}

SIZE = {
    "M": 0,
    "L": 5000,
    "XL": 10000
}

SUGAR = [
    "100% đường",
    "70% đường",
    "50% đường",
    "30% đường",
    "0% đường"
]

ICE = [
    "100% đá",
    "70% đá",
    "50% đá",
    "30% đá",
    "Không đá"
]

# =====================================================
# SESSION STATE
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

if "paid" not in st.session_state:
    st.session_state.paid = False

if "customer_name" not in st.session_state:
    st.session_state.customer_name = ""

if "invoice_number" not in st.session_state:
    st.session_state.invoice_number = ""

if "payment_method" not in st.session_state:
    st.session_state.payment_method = ""


# =====================================================
# HÀM ĐỊNH DẠNG TIỀN
# =====================================================

def format_money(number):
    return f"{number:,.0f} VNĐ".replace(",", ".")


# =====================================================
# TIÊU ĐỀ
# =====================================================

st.title("🧋 QUÁN TRÀ SỮA")

st.subheader(
    "📋 HỆ THỐNG GỌI MÓN VÀ TÍNH HÓA ĐƠN"
)

st.divider()


# =====================================================
# THÔNG TIN KHÁCH HÀNG
# =====================================================

st.markdown("### 👤 THÔNG TIN KHÁCH HÀNG")

customer_name = st.text_input(
    "Tên khách hàng",
    value=st.session_state.customer_name,
    placeholder="Nhập tên khách hàng..."
)

st.session_state.customer_name = customer_name


# =====================================================
# CHỌN MÓN
# =====================================================

st.markdown("### 🧋 CHỌN MÓN")

col1, col2 = st.columns(2)

with col1:

    drink = st.selectbox(
        "Loại trà sữa",
        list(MENU.keys())
    )

    size = st.selectbox(
        "Size ly",
        list(SIZE.keys())
    )

    quantity = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=50,
        value=1,
        step=1
    )


with col2:

    sugar = st.selectbox(
        "Mức độ đường",
        SUGAR
    )

    ice = st.selectbox(
        "Mức độ đá",
        ICE
    )

    topping = st.selectbox(
        "Topping",
        list(TOPPING.keys())
    )


# =====================================================
# TÍNH TIỀN
# =====================================================

base_price = MENU[drink]

size_price = SIZE[size]

topping_price = TOPPING[topping]

unit_price = (
    base_price
    + size_price
    + topping_price
)

total_item = unit_price * quantity


st.info(
    f"💰 Đơn giá: **{format_money(unit_price)}** "
    f"| Thành tiền: **{format_money(total_item)}**"
)


# =====================================================
# THÊM MÓN
# =====================================================

if st.button(
    "➕ THÊM MÓN VÀO ĐƠN",
    use_container_width=True
):

    item = {
        "drink": drink,
        "size": size,
        "quantity": quantity,
        "sugar": sugar,
        "ice": ice,
        "topping": topping,
        "unit_price": unit_price,
        "total": total_item
    }

    st.session_state.cart.append(item)

    st.success(
        f"✅ Đã thêm {quantity} ly {drink} vào đơn hàng!"
    )


# =====================================================
# ĐƠN HÀNG
# =====================================================

st.divider()

st.markdown("### 🛒 ĐƠN HÀNG HIỆN TẠI")


if len(st.session_state.cart) == 0:

    st.warning(
        "🛒 Chưa có món nào trong đơn hàng."
    )

else:

    grand_total = sum(
        item["total"]
        for item in st.session_state.cart
    )

    # -------------------------------------------------
    # HIỂN THỊ TỪNG MÓN
    # -------------------------------------------------

    for i, item in enumerate(
        st.session_state.cart
    ):

        with st.container(border=True):

            col1, col2, col3 = st.columns(
                [4, 2, 1]
            )

            with col1:

                st.markdown(
                    f"### {i + 1}. {item['drink']}"
                )

                st.write(
                    f"🥤 Size: **{item['size']}**"
                )

                st.write(
                    f"🍬 Đường: **{item['sugar']}**"
                )

                st.write(
                    f"🧊 Đá: **{item['ice']}**"
                )

                st.write(
                    f"🍮 Topping: **{item['topping']}**"
                )


            with col2:

                st.write(
                    f"📦 Số lượng: "
                    f"**{item['quantity']}**"
                )

                st.write(
                    f"💰 Đơn giá: "
                    f"**{format_money(item['unit_price'])}**"
                )

                st.write(
                    f"💵 Thành tiền: "
                    f"**{format_money(item['total'])}**"
                )


            with col3:

                if st.button(
                    "🗑️ Xóa",
                    key=f"delete_{i}"
                ):

                    st.session_state.cart.pop(i)

                    st.rerun()


    # =================================================
    # TỔNG TIỀN
    # =================================================

    st.divider()

    st.markdown(
        f"""
        <div style="
            background-color:#fff0f5;
            padding:20px;
            border-radius:15px;
            text-align:right;
            border:2px solid #ff69b4;
        ">

        <h2>💰 TỔNG THANH TOÁN</h2>

        <h1 style="color:#e91e63;">
            {format_money(grand_total)}
        </h1>

        </div>
        """,
        unsafe_allow_html=True
    )


    # =================================================
    # THANH TOÁN
    # =================================================

    st.write("")

    st.markdown("### 💳 THANH TOÁN")

    payment_method = st.radio(
        "Phương thức thanh toán",
        [
            "💵 Tiền mặt",
            "🏦 Chuyển khoản",
            "📱 Ví điện tử"
        ],
        horizontal=True
    )


    if st.button(
        "💳 THANH TOÁN",
        type="primary",
        use_container_width=True
    ):

        if not customer_name.strip():

            st.error(
                "❌ Vui lòng nhập tên khách hàng!"
            )

        else:

            st.session_state.paid = True

            st.session_state.payment_method = (
                payment_method
            )

            st.session_state.invoice_number = (
                datetime.now().strftime(
                    "%Y%m%d%H%M%S"
                )
            )

            st.success(
                "✅ Thanh toán thành công!"
            )


    # =================================================
    # HÓA ĐƠN
    # =================================================

    if st.session_state.paid:

        st.divider()

        st.markdown(
            "## 🧾 HÓA ĐƠN THANH TOÁN"
        )

        now = datetime.now()

        invoice_number = (
            st.session_state.invoice_number
        )

        # ---------------------------------------------
        # THÔNG TIN HÓA ĐƠN
        # ---------------------------------------------

        st.markdown(
            f"""
            <div style="
                border:2px solid #333;
                padding:25px;
                border-radius:10px;
                background-color:white;
            ">

            <h2 style="text-align:center;">
                🧋 QUÁN TRÀ SỮA
            </h2>

            <p style="text-align:center;">
                <b>HÓA ĐƠN THANH TOÁN</b>
            </p>

            <hr>

            <p>
                <b>Mã hóa đơn:</b>
                {invoice_number}
            </p>

            <p>
                <b>Khách hàng:</b>
                {customer_name}
            </p>

            <p>
                <b>Thời gian:</b>
                {now.strftime("%d/%m/%Y %H:%M:%S")}
            </p>

            <hr>

            </div>
            """,
            unsafe_allow_html=True
        )


        # ---------------------------------------------
        # CHI TIẾT HÓA ĐƠN
        # ---------------------------------------------

        st.markdown(
            "### 📋 Chi tiết hóa đơn"
        )

        for i, item in enumerate(
            st.session_state.cart
        ):

            st.markdown(
                f"""
                **{i + 1}. {item['drink']}**

                🥤 Size: {item['size']}  
                📦 Số lượng: {item['quantity']}  
                🍬 Đường: {item['sugar']}  
                🧊 Đá: {item['ice']}  
                🍮 Topping: {item['topping']}  
                💰 Đơn giá: {format_money(item['unit_price'])}  
                💵 Thành tiền: **{format_money(item['total'])}**
                """
            )

            st.divider()


        # ---------------------------------------------
        # TỔNG HÓA ĐƠN
        # ---------------------------------------------

        st.markdown(
            f"""
            <div style="
                text-align:right;
                padding:20px;
                border-radius:10px;
                background-color:#fff0f5;
            ">

            <h2>
                Tổng tiền:
                <span style="color:#e91e63;">
                    {format_money(grand_total)}
                </span>
            </h2>

            <p>
                Phương thức thanh toán:
                <b>
                    {st.session_state.payment_method}
                </b>
            </p>

            <h3>
                ✅ ĐÃ THANH TOÁN
            </h3>

            <p>
                Cảm ơn quý khách đã sử dụng dịch vụ! ❤️
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


        # =================================================
        # TẠO ĐƠN HÀNG MỚI
        # =================================================

        st.write("")

        if st.button(
            "🔄 TẠO ĐƠN HÀNG MỚI",
            use_container_width=True
        ):

            st.session_state.cart = []

            st.session_state.paid = False

            st.session_state.customer_name = ""

            st.session_state.invoice_number = ""

            st.session_state.payment_method = ""

            st.rerun()

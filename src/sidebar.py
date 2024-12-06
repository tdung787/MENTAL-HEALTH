import os
import streamlit as st

def show_sidebar(username):
    if username:  # Kiểm tra xem người dùng đã đăng nhập hay chưa
        st.sidebar.markdown("### Lịch sử trò chuyện")
        
        # Thư mục chứa các tệp chat history
        cache_dir = "data/cache"
        
        # Lọc các tệp chat history chỉ thuộc về người dùng hiện tại
        chat_files = [f for f in os.listdir(cache_dir) if f.startswith(username) and f.endswith(".json")]
        
        if chat_files:  # Kiểm tra nếu có lịch sử trò chuyện
            for idx, file in enumerate(chat_files):
                # Dạng tệp: username_chatTitle_timestamp.json
                try:
                    parts = file.split("_")
                    chat_title = "_".join(parts[1:-1])  # Lấy phần giữa (bỏ username và timestamp)
                except IndexError:
                    chat_title = "Untitled Chat"
                
                # Thêm key duy nhất cho mỗi nút
                if st.sidebar.button(chat_title.strip(), key=f"chat_{idx}"):
                    st.session_state.selected_chat_file = os.path.join(cache_dir, file)
        else:
            st.sidebar.write("Không có lịch sử trò chuyện nào.")
            
def tutorial():
    st.sidebar.markdown('### 🧠 Ứng dụng AI chăm sóc sức khỏe tâm thần')
    st.sidebar.markdown('Hướng dẫn sử dụng:')
    st.sidebar.markdown('1. 🟢 **Đăng nhập tài khoản để lưu nhật kí sức khỏe mỗi lần sử dụng.**')
    st.sidebar.markdown('2. 💬 **Sử dụng chức năng chat - "Nói chuyện với chuyên gia tâm lý AI" để chia sẻ cảm xúc của bạn.**')
    st.sidebar.markdown('3. 📈 **Khi có đủ dữ liệu hoặc bạn kết thúc cuộc trò chuyện. Chuyên gia AI sẽ chuẩn đoán tình trạng sức khỏe tinh thần của bạn theo DSM5.**')
    st.sidebar.markdown('4. 📊 **Tình trạng sức khỏe tinh thần của bạn sẽ được lưu lại. Bạn có thể sử dụng chức năng user - "Theo dõi thông tin sức khỏe của bạn" để xem thống kê chi tiết về tình trạng sức khỏe tinh thần của mình.**')

def main_tutorial():
    st.markdown('### 🧠 Ứng dụng AI người bạn tâm giao')
    st.markdown('***Hướng dẫn sử dụng:***')
    st.markdown('1. 🟢 **Đăng nhập tài khoản để lưu nhật kí sức khỏe mỗi lần sử dụng.**')
    st.markdown('2. 💬 **Sử dụng chức năng chat - "Nói chuyện với chuyên gia tâm lý AI" để chia sẻ cảm xúc của bạn hoặc khó khăn trong học tập.**')
    st.markdown('3. 💡 **AI có thể giải đáp thắc mắc và hướng dẫn giải chi tiết các bài tập để *giải tỏa áp lực* trong học tập**')
    st.markdown('4. 📈 **Khi bạn muốn kết thúc cuộc trò chuyện hãy nhắn cho chuyên gia đánh giá sức khỏe của bạn. Chuyên gia AI sẽ chuẩn đoán tình trạng sức khỏe tinh thần của bạn.**')
    st.markdown('5. 📊 **Tình trạng sức khỏe tinh thần của bạn sẽ được lưu lại. Bạn có thể sử dụng chức năng user - "Theo dõi thông tin sức khỏe của bạn" để xem thống kê chi tiết về tình trạng sức khỏe tinh thần của mình.**')


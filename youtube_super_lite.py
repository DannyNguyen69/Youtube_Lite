import sys
import webview

def on_closed():
    """Hàm này đảm bảo ứng dụng thoát hoàn toàn khi đóng cửa sổ"""
    sys.exit(0)

if __name__ == "__main__":
    # Tạo cửa sổ trình duyệt với YouTube mobile
    window = webview.create_window(
        title="YouTube Lite",
        url="https://m.youtube.com",
        width=800,
        height=600,
        resizable=True,  # Có thể thay đổi kích thước cửa sổ
        frameless=False,  # Giữ khung cửa sổ
        on_top=False  # Không buộc cửa sổ luôn ở trên cùng
    )
    # Gắn hàm xử lý khi đóng cửa sổ
    window.closed = on_closed
    # Khởi động ứng dụng
    webview.start()
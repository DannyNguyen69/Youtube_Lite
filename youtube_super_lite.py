import sys
import webview

def on_closed():
    sys.exit(0)

if __name__ == "__main__":
    window = webview.create_window(
        title="YouTube Lite",
        url="https://m.youtube.com",
        width=800,
        height=600,
        resizable=True,
        frameless=False,
        on_top=False
    )
    window.closed = on_closed
    webview.start(private_mode=False) 
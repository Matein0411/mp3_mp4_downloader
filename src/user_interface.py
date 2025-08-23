import sys
from mp3_downloader import *
from mp4_downloader import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap, QFont, QIcon

class DownloaderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MP3/MP4 Downloader")
        self.setGeometry(100, 100, 400, 200)
        icon_path = "assets/logo.png"
        
        window_icon = QIcon(icon_path)
        self.setWindowIcon(window_icon)
        self.layout = QVBoxLayout()
        
        self.welcome_label = QLabel("Inter Downloader!")
        self.welcome_label.setFont(QFont('Arial', 16))
        self.welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.image_label = QLabel()
        try:
            pixmap = QPixmap(icon_path)  
            self.image_label.setPixmap(pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio))
            self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        except Exception as e:
            print(f"Could not load image: {e}", file=sys.stderr)    

        self.url_label = QLabel("Enter Video URL:")
        self.url_input = QLineEdit()
        
        self.download_button = QPushButton("See options")
        #self.download_button.clicked.connect(self.show_options)
        
        self.layout.addWidget(self.welcome_label)
        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.url_label)
        self.layout.addWidget(self.url_input)
        self.layout.addWidget(self.download_button)
        
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = DownloaderApp()
    window.show()
    
    sys.exit(app.exec())
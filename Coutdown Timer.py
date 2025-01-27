import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QSpinBox, QWidget, QHBoxLayout
)
from PyQt5.QtCore import QTimer, Qt  # Qt burada eklendi

class CountdownTimer(QMainWindow):  # Sınıf adı düzeltildi
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Countdown Timer")
        self.setGeometry(400, 200, 400, 300)

        # Ana düzen
        self.layout = QVBoxLayout()

        # Geri sayım etiketi
        self.timer_label = QLabel("00:00", self)
        self.timer_label.setStyleSheet("font-size: 64px; color: lightblue; text-align: center;")
        self.timer_label.setAlignment(Qt.AlignCenter)  # Hata burada giderildi
        self.layout.addWidget(self.timer_label)

        # Süre ayarlama bölümü
        self.time_layout = QHBoxLayout()
        self.minute_spinbox = QSpinBox(self)
        self.minute_spinbox.setRange(0, 60)
        self.minute_spinbox.setSuffix(" min")
        self.minute_spinbox.setStyleSheet("font-size: 18px;")
        self.time_layout.addWidget(self.minute_spinbox)

        self.second_spinbox = QSpinBox(self)
        self.second_spinbox.setRange(0, 59)
        self.second_spinbox.setSuffix(" sec")
        self.second_spinbox.setStyleSheet("font-size: 18px;")
        self.time_layout.addWidget(self.second_spinbox)
        self.layout.addLayout(self.time_layout)

        # Düğmeler
        self.button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start", self)
        self.reset_button = QPushButton("Reset", self)
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.reset_button)
        self.layout.addLayout(self.button_layout)

        # Merkezi widget
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)

        # Değişkenler
        self.remaining_time = 0

        # Olay bağlantıları
        self.start_button.clicked.connect(self.start_timer)
        self.reset_button.clicked.connect(self.reset_timer)

    def start_timer(self):
        # Süreyi al ve başlat
        minutes = self.minute_spinbox.value()
        seconds = self.second_spinbox.value()
        self.remaining_time = minutes * 60 + seconds
        if self.remaining_time > 0:
            self.timer.start(1000)
            self.start_button.setEnabled(False)

    def reset_timer(self):
        # Timer'ı sıfırla
        self.timer.stop()
        self.remaining_time = 0
        self.timer_label.setText("00:00")
        self.start_button.setEnabled(True)

    def update_timer(self):
        # Kalan süreyi güncelle ve ekranda göster
        if self.remaining_time > 0:
            minutes, seconds = divmod(self.remaining_time, 60)
            self.timer_label.setText(f"{minutes:02d}:{seconds:02d}")
            self.remaining_time -= 1
        else:
            self.timer.stop()
            self.timer_label.setText("Time is up!")
            self.start_button.setEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = CountdownTimer()  # Sınıf adı düzeltildi
    pencere.show()
    sys.exit(app.exec_())

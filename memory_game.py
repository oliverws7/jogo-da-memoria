import sys
import random
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QGridLayout,
                             QPushButton, QLabel, QVBoxLayout)
from PySide6.QtCore import Qt, QTimer, QSize
from PySide6.QtGui import QFont, QIcon, QResizeEvent

class MemoryGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Memory Game")
        self.setMinimumSize(400, 500)  # Tamanho mínimo para garantir usabilidade
        self.resize(600, 700)  # Tamanho inicial sugerido
        
        # Configuração do widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Área superior com informações e botão novo jogo
        top_layout = QVBoxLayout()
        
        # Botão Novo Jogo
        self.new_game_button = QPushButton("🔄 New Game")
        self.new_game_button.setProperty("class", "new-game-button")
        self.new_game_button.clicked.connect(self.start_new_game)
        self.new_game_button.setFixedHeight(40)
        top_layout.addWidget(self.new_game_button)
        
        # Área de informações
        self.info_label = QLabel("Number of attempts: 0")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setFont(QFont("Arial", 16))
        self.info_label.setStyleSheet("color: #2C3E50; margin: 10px;")
        top_layout.addWidget(self.info_label)
        
        main_layout.addLayout(top_layout)
        
        # Container para o grid
        self.grid_container = QWidget()
        self.grid_layout = QGridLayout(self.grid_container)
        self.grid_layout.setSpacing(10)
        main_layout.addWidget(self.grid_container)
        
        # Variáveis do jogo
        self.buttons = []
        self.first_card = None
        self.can_click = True
        self.attempts = 0
        self.matches = 0
        
        # Emojis para os pares
        self.emojis = ['🎮', '🎲', '🎯', '🎨', '🎭', '🎪', '🎟️', '🎬']
        self.emojis *= 2
        random.shuffle(self.emojis)
        
        # Criar os botões
        self.create_buttons()
        
        # Carregar estilos
        self.load_styles()
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.adjust_button_sizes()
    
    def adjust_button_sizes(self):
        # Calcula o tamanho ideal dos botões baseado no tamanho da janela
        container_width = self.grid_container.width()
        container_height = self.grid_container.height()
        
        # Considera o espaçamento entre os botões
        spacing = self.grid_layout.spacing()
        available_width = container_width - (3 * spacing)
        available_height = container_height - (3 * spacing)
        
        # Calcula o tamanho ideal do botão (menor entre largura e altura disponível)
        button_size = min(available_width // 4, available_height // 4)
        
        # Ajusta o tamanho da fonte proporcionalmente
        font_size = max(int(button_size * 0.4), 12)  # Mínimo de 12pt
        
        # Aplica os novos tamanhos
        for button in self.buttons:
            button.setFixedSize(button_size, button_size)
            font = button.font()
            font.setPointSize(font_size)
            button.setFont(font)
    
    def create_buttons(self):
        for i in range(4):
            for j in range(4):
                button = QPushButton()
                button.setFont(QFont("Arial", 40))
                button.setProperty("class", "card")
                button.clicked.connect(lambda checked, row=i, col=j: self.button_clicked(row, col))
                self.grid_layout.addWidget(button, i, j)
                self.buttons.append(button)
        
        # Ajusta o tamanho inicial dos botões
        QTimer.singleShot(0, self.adjust_button_sizes)
    
    def load_styles(self):
        try:
            with open("game/styles.qss", "r") as f:
                self.setStyleSheet(f.read())
        except:
            # Estilo padrão caso o arquivo não seja encontrado
            self.setStyleSheet("""
                QPushButton.card {
                    background-color: #3498db;
                    border-radius: 10px;
                    border: none;
                }
                QPushButton.card:hover {
                    background-color: #2980b9;
                }
                QPushButton.matched {
                    background-color: #2ecc71;
                }
            """)
    
    def button_clicked(self, row, col):
        if not self.can_click:
            return
            
        button = self.grid_layout.itemAtPosition(row, col).widget()
        index = row * 4 + col
        
        # Não permitir clicar em cartas já reveladas ou combinadas
        if button.text() or button.property("matched"):
            return
            
        # Revelar a carta
        button.setText(self.emojis[index])
        
        # Se for a primeira carta
        if self.first_card is None:
            self.first_card = (button, index)
        # Se for a segunda carta
        else:
            # Garantir que não é a mesma carta
            first_button, first_index = self.first_card
            if button == first_button:
                return
                
            self.attempts += 1
            self.info_label.setText(f"attempts: {self.attempts}")
            
            # Verificar se as cartas combinam
            if self.emojis[index] == self.emojis[first_index]:
                button.setProperty("matched", True)
                first_button.setProperty("matched", True)
                button.setStyleSheet("background-color: #2ecc71; border-radius: 10px;")
                first_button.setStyleSheet("background-color: #2ecc71; border-radius: 10px;")
                self.matches += 1
                
                if self.matches == 8:
                    self.info_label.setText(f"Congratulations! You win after {self.attempts} attempts! ")
            else:
                self.can_click = False
                QTimer.singleShot(1000, lambda: self.hide_cards(button, first_button))
            
            self.first_card = None
    
    def hide_cards(self, button1, button2):
        button1.setText("")
        button2.setText("")
        self.can_click = True
    
    def start_new_game(self):
        # Embaralha os emojis
        random.shuffle(self.emojis)
        
        # Reseta as variáveis do jogo
        self.first_card = None
        self.can_click = True
        self.attempts = 0
        self.matches = 0
        
        # Reseta o texto de informações
        self.info_label.setText("attempts: 0")
        
        # Reseta todos os botões
        for button in self.buttons:
            button.setText("")
            button.setProperty("matched", False)
            button.setStyleSheet("")  # Remove o estilo de matched
            button.setProperty("class", "card")  # Reaplica a classe card
        
        # Recarrega os estilos para garantir aparência correta
        self.load_styles()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = MemoryGame()
    game.show()
    sys.exit(app.exec())
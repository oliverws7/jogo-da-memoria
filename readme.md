🎮 Memory Game em PySide6
Um jogo da memória interativo e responsivo desenvolvido com PySide6 (Qt para Python). Encontre todos os pares de emojis com o menor número de tentativas possível!

✨ Funcionalidades
Interface gráfica moderna com design responsivo

Grade 4x4 com 8 pares de emojis variados

Sistema de pontuação que conta tentativas

Botão "New Game" para reiniciar a qualquer momento

Cartas com efeitos visuais para indicar:

Cartas viradas

Pares encontrados (verde)

Cartas não correspondentes (temporariamente visíveis)

Redimensionamento dinâmico dos botões conforme o tamanho da janela

Estilização personalizável via arquivo QSS

🚀 Instalação
Pré-requisitos
Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

Passo a passo
Clone o repositório (ou baixe os arquivos):

bash
git clone <URL_DO_REPOSITORIO>
cd memory-game-pyside6
Crie e ative um ambiente virtual (recomendado):

bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

bash
pip install PySide6
Execute o jogo:

bash
python memory_game.py
🎯 Como Jogar
Início: O jogo começa com todas as cartas viradas para baixo

Clique em uma carta: Revele o emoji escondido

Encontre pares: Clique em outra carta para tentar formar um par

Resultados:

Par correto: Cartas ficam verdes e permanecem viradas

Par incorreto: Cartas são viradas novamente após 1 segundo

Vitória: Encontre todos os 8 pares para vencer!

Novo jogo: Use o botão "🔄 New Game" para reiniciar

📁 Estrutura do Projeto
text
memory-game-pyside6/
├── memory_game.py          # Código principal do jogo
├── game/
│   └── styles.qss         # Arquivo de estilos (opcional)
├── README.md              # Este arquivo
└── requirements.txt       # Dependências do projeto
🎨 Personalização
Modificar Emojis
Edite a lista self.emojis na linha 56 do memory_game.py:

python
self.emojis = ['🎮', '🎲', '🎯', '🎨', '🎭', '🎪', '🎟️', '🎬']
Alterar Estilos
Estilo embutido: Modifique o dicionário de estilos nas linhas 121-130

Arquivo externo: Crie um arquivo game/styles.qss com suas regras CSS

Exemplo de estilo personalizado:

css
QPushButton.card {
    background-color: #9b59b6;
    border-radius: 20px;
    font-size: 50px;
}

QPushButton.matched {
    background-color: #e74c3c;
}
Mudar Tamanho da Grade
Para alterar para 6x6 (por exemplo):

python
# Altere estas linhas:
for i in range(6):  # Mudar de 4 para 6
    for j in range(6):
        # ...
        index = row * 6 + col  # Mudar de 4 para 6

# Atualize também a verificação de vitória:
if self.matches == 18:  # 6x6 = 36 cartas = 18 pares
🛠️ Solução de Problemas
Erro: "ModuleNotFoundError: No module named 'PySide6'"
bash
pip install PySide6
Erro: Janela fecha imediatamente
Execute pelo terminal para ver mensagens de erro:

bash
python memory_game.py
Problemas com o arquivo de estilos
O jogo funciona mesmo sem o arquivo styles.qss. Se quiser criá-lo:

bash
mkdir game
echo "QPushButton.card { background-color: #3498db; border-radius: 10px; }" > game/styles.qss
Interface não redimensiona corretamente
A função adjust_button_sizes() calcula automaticamente o tamanho ideal. Se houver problemas:

Maximize a janela

Use o botão "New Game"

Ou reinicie o jogo

📋 Requisitos do Sistema
Sistema Operacional: Windows 10+, macOS 10.14+, ou Linux com GUI

Python: Versão 3.8 ou superior

Memória RAM: Mínimo 512MB (recomendado 1GB)

Espaço em disco: Aproximadamente 50MB

🤝 Contribuindo
Contribuições são bem-vindas! Siga estes passos:

Faça um Fork do projeto

Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)

Commit suas mudanças (git commit -m 'Add some AmazingFeature')

Push para a branch (git push origin feature/AmazingFeature)

Abra um Pull Request

📄 Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

🙏 Agradecimentos
PySide6 - Framework Qt para Python

Qt Company - Pelo incrível framework Qt

Emojipedia - Por fornecer os emojis Unicode

📞 Suporte
Encontrou um bug ou tem uma sugestão? Por favor:

Abra uma issue

Descreva o problema ou sugestão

Inclua detalhes como sistema operacional e versão do Python

<div align="center"> Feito com ❤️ e Python
Divirta-se jogando! 🎯

</div>
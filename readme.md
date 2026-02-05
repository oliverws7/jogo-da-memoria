# 🎮 Memory Game (PySide6)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)
![PySide6](https://img.shields.io/badge/PySide6-Qt-green?style=for-the-badge&logo=qt)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

> Um jogo da memória moderno, responsivo e interativo desenvolvido em Python com a biblioteca PySide6 (Qt).

---

## ✨ Funcionalidades

### 🕹️ Gameplay
* **Grade 4x4:** 8 pares de emojis desafiadores.
* **Contador de Tentativas:** Acompanhe seu desempenho em tempo real.
* **Feedback Visual:**
    * 🟩 Cartas verdes para pares encontrados.
    * 🟦 Efeitos de *hover* e clique suaves.
* **Reinício Rápido:** Botão "New Game" para começar uma nova partida instantaneamente.

### ⚙️ Destaques Técnicos
* **Design Responsivo:** O grid e as fontes se ajustam automaticamente ao redimensionar a janela (evento `resizeEvent` customizado).
* **Estilização Externa:** Uso de arquivo `.qss` (Qt Style Sheets) para separação entre lógica e design.
* **Lógica Assíncrona:** Uso de `QTimer` para gerenciar a visualização das cartas sem travar a interface.

---

## 📁 Estrutura do Projeto

Para que o estilo funcione corretamente, o projeto deve seguir esta estrutura:

```text
memory-game/
├── memory_game.py          # Código principal (Logica e GUI)
├── LICENSE                 # Arquivo de licença MIT
├── README.md               # Documentação
└── game/                   # ⚠️ Importante: Pasta para recursos
    └── styles.qss          # Arquivo de estilos CSS/QSS

```

---

## 🚀 Instalação e Execução

### Pré-requisitos

* Python 3.8 ou superior.

### Passo a Passo

1. **Clone o repositório:**
```
git clone [https://github.com/oliverws7/memory-game-pyside6.git](https://github.com/oliverws7/memory-game-pyside6.git)
cd memory-game-pyside6

```


2. **Crie um ambiente virtual (Recomendado):**
```
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate

```


3. **Instale as dependências:**
```
pip install PySide6

```


4. **Configure o Estilo:**
*Certifique-se de que o arquivo `styles.qss` esteja dentro de uma pasta chamada `game` no mesmo diretório do script, caso contrário o jogo carregará o estilo padrão.*
5. **Execute o jogo:**
```
python memory_game.py

```



---

## 🎨 Personalização

O jogo foi construído pensando na flexibilidade. Veja como alterar alguns aspectos:

### Mudar os Emojis

No arquivo `memory_game.py`, localize a lista `self.emojis`:

```python
# Linha ~56
self.emojis = ['🚀', '🌙', '⭐', '👨‍🚀', '👽', '☄️', '📡', '🔭'] 

```

### Alterar Cores e Bordas

Edite o arquivo `game/styles.qss`. O código aceita sintaxe CSS padrão:

```css
/* Exemplo: Cartas redondas e roxas */
QPushButton.card {
    background-color: #8e44ad;
    border-radius: 50%; /* Deixa a carta redonda */
}

```

---

## 🛠️ Solução de Problemas Comuns

| Problema | Solução |
| --- | --- |
| `ModuleNotFoundError: No module named 'PySide6'` | Execute `pip install PySide6` no seu terminal/ambiente virtual. |
| O jogo abre sem cores/estilo | Verifique se a pasta `game` existe e se `styles.qss` está dentro dela. |
| A janela fecha instantaneamente | Execute via terminal (`python memory_game.py`) para ler o log de erro. |

---

## 🤝 Contribuindo

Contribuições são muito bem-vindas!

1. Faça um Fork do projeto.
2. Crie uma Branch para sua Feature (`git checkout -b feature/IncrívelRecurso`).
3. Faça o Commit (`git commit -m 'Adiciona IncrívelRecurso'`).
4. Faça o Push (`git push origin feature/IncrívelRecurso`).
5. Abra um Pull Request.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](https://www.google.com/search?q=LICENSE) para mais detalhes.

Copyright (c) 2026 **Mateus Nunes**

---

<div align="center">

**Feito com 🐍 Python e ❤️**

</div>

```

```

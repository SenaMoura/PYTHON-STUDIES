# 📦 Organizador Automático de Downloads

Um script em Python desenvolvido para organizar pastas de download bagunçadas, movendo os arquivos para subpastas categorizadas com base em suas extensões.

---

## 📌 Visão Geral do Projeto

É comum que a pasta `Downloads` fique acumulada com documentos, imagens, instaladores e arquivos compactados ao longo do tempo. Esta ferramenta automatizada varre a pasta, identifica a extensão de cada arquivo e o move para a pasta correspondente. Qualquer formato de arquivo não reconhecido é movido com segurança para uma pasta chamada `Others`.

---

## ✨ Funcionalidades

- **Detecção Automática de Extensões:** Categoriza arquivos em `Imagens`, `Documentos`, `Executáveis`, `Compactados`, `Áudios/Vídeos`, etc.
- **Gestão de Arquivos Diversos (Pasta `Others`):** Garante que nenhum arquivo fique perdido ou fora de lugar.
- **Criação Dinâmica de Pastas:** Cria as pastas de destino apenas quando necessário.
- **Execução Segura:** Ignora pastas já existentes para evitar mover diretórios acidentalmente.

---

## 🛠️ Estrutura do Projeto


## 📖 Instruções de Uso
1. Pré-requisitos
Certifique-se de ter o Python 3.x instalado na sua máquina.

2. Configuração
Por padrão, o script está configurado para a pasta de Downloads do seu sistema operacional:

Python
DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
Nota: Se você quiser organizar uma pasta diferente, abra o arquivo script.py e substitua ~/Downloads pelo seu caminho personalizado (ex: "C:/Users/SeuUsuario/Desktop/MinhaPasta").

3. Execução
Abra o seu terminal ou o terminal do VS Code no diretório do projeto.

Execute o seguinte comando:

Bash
python script.py
Confira a sua pasta! Todos os arquivos serão agrupados automaticamente em subpastas organizadas.

## 🧰 Tecnologias Utilizadas
Python 3.x

Módulo os: Para navegação e manipulação de caminhos do sistema.

Módulo shutil: Para operações de movimentação de arquivos.

```text
Folder Organizer/
├── script.py          # Script principal de automação
└── README.md          # Documentação do projeto

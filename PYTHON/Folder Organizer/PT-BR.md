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

```text
Folder Organizer/
├── script.py          # Script principal de automação
└── README.md          # Documentação do projeto
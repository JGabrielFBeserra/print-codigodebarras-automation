# Leitor de Código de Barras na Tela - Automação Financeiro

Sistema para ler códigos de barras diretamente da tela do computador e copiar automaticamente para a área de transferência.

## O que faz

Este programa resolve o problema de códigos de barras que aparecem na tela mas não têm o número copiável embaixo ou não mostram o número. Ele:

- Ativa com uma combinação de teclas simples (z+x+c)
- Permite selecionar uma área da tela onde está o código de barras
- Lê automaticamente o código usando visão computacional
- Copia o número para a área de transferência
- Mostra uma mensagem de confirmação
- Remove arquivos temporários automaticamente

## Por que criamos isso

O setor financeiro da empresa dm que atuo lida com muitas faturas digitais que contêm códigos de barras. Muitas vezes:
- O código de barras não vem com o número legível embaixo
- O número não é copiável (está em imagem)
- É difícil digitar manualmente números longos sem errar

**A solução inicial era comprar um leitor físico**, mas sugeri este script que:
- ✅ Funciona direto na tela
- ✅ Não precisa equipamento extra
- ✅ É mais rápido que digitar
- ✅ Elimina erros de digitação
- ✅ E de graça po

## Trajetória do desenvolvimento

### 0. Basicamente cada arquivo é um estudo de uma lib ou funcionalidade.

### 1. Primeiro teste - Detecção de teclas (`1-keyboard-detec.py`)
- Implementei captura de atalhos de teclado
- Testei combinações de teclas para ativação

### 2. Captura de tela (`2-print-screen.py`)
- Adicionei funcionalidade de screenshot automático
- Salvamento de imagens temporárias
- Testando a lib

### 3. Controle de mouse (`3-mouse-click.py`)
- Criei interface para seleção de área
- Sistema de arrastar e selecionar com mouse
- Overlay transparente em tela cheia

### 4. Primeira integração (`4-integrando.py`)
- Combinei as funcionalidades básicas
- Hotkey para ativar seleção de área
- Captura da região selecionada

### 5. Leitor de código de barras (`5-reader-barcode.py`)
- Implementei decodificação com pyzbar
- Identifiquei problemas de performance e dependências

### 6-7. Otimização com threading (`6-testando-thread.py`, `7-integrando-thread.py`)
- Experimentei threading para melhor responsividade
- Pensar em integrar sistema completo multithread
- No final acabei desistindo, mas entendi o conceito

### 8. Sistema final (`project.py`)
- Unificação de todas as funcionalidades
- Interface de usuário polida
- Sistema robusto de mensagens

## O que você precisa instalar antes

### 🚀 Método automatizado (recomendado):
1. **Execute:** `LEITOR_AUTOMATION.bat` (instala Python, bibliotecas e dependências automaticamente)

### ⚙️ Método manual:
1. **Baixe Python 3.11 LTS:** https://www.python.org/downloads/ (marque "Add Python to PATH")
2. **Baixe Visual C++ 2013:** https://www.microsoft.com/en-us/download/details.aspx?id=40784
3. **Instale bibliotecas Python:**
   ```bash
   pip install opencv-python pyzbar pyautogui keyboard pyperclip
   ```
4. **Instale dependência Windows (.whl) dentro de /dependencies:**
   ```bash
   pip install pyzbar-0.1.9-py2.py3-none-win_amd64.whl
   ```

> **Por que o arquivo .whl?** O pyzbar precisa de DLLs específicas do Windows que nem sempre instalam automaticamente. Este arquivo contém as bibliotecas pré-compiladas.

## Como usar (passo a passo)

### 🎯 Método automatizado (.bat):
1. Execute `EXECUTAR_LEITOR.bat`
2. Pressione **z+x+c** quando quiser ler um código
3. Selecione a área do código de barras na tela
4. Clique no botão "Print"
5. O número será copiado automaticamente

### 📱 Criar atalho na área de trabalho:
1. Botão direito no `EXECUTAR_LEITOR.bat` → "Enviar para" → "Área de trabalho"
2. **Para trocar ícone:** Botão direito no atalho → "Propriedades" → "Alterar ícone"
3. Renomear para "LEITOR AUTOMATION"

### 💻 Método manual (cmd):
```bash
python project.py
```

### O que acontece na tela:
- Tela escura transparente aparece
- Você arrasta para selecionar a área
- Retângulo branco pontilhado mostra a seleção
- Botão "Print" aparece para confirmar
- Mensagem popup confirma a cópia
- **ESC** cancela a operação

## Mensagens do sistema

**"Código Copiado: 123456789"** - Sucesso! Número já está na área de transferência

**"Erro: Nenhum código de Barras Encontrado"** - Área selecionada não contém código legível

**"Erro ao abrir imagem"** - Problema na captura da tela

**"Erro: Código de Barras Inválido"** - Código existe mas não conseguiu decodificar

## Configurações

### Mudando a combinação de teclas
No arquivo `project.py`, linha final:
```python
keyboard.add_hotkey('z+x+c', on_click)
```
Troque por qualquer combinação, exemplos:
- `'ctrl+alt+c'` 
- `'f12'`
- `'ctrl+shift+b'`

### Ajustando tempo da mensagem
Na função `mensagem`, linha:
```python
popup.after(1000, popup.destroy)  # 1000 = 1 segundo
```

## Se algo der errado

**"'python' não é reconhecido":**
- Python não está no PATH
- Reinstale marcando "Add to PATH"

**"No module named 'cv2'" ou similar:**
- Instale as dependências: `pip install opencv-python pyzbar pyautogui keyboard pyperclip`

**"Erro ao carregar pyzbar" ou "DLL não encontrada":**
- Instale Visual C++ 2015-2022 Redistributable
- Instale o arquivo .whl da pasta dependencies

**Código não é detectado:**
- Certifique-se que o código está bem visível
- Evite selecionar área muito grande
- Códigos muito pequenos podem não funcionar
- Experimente melhorar contraste da tela

**Programa não responde:**
- Pressione ESC para cancelar
- Feche e reabra o programa


## Links úteis

- **Python:** https://www.python.org/downloads/
- **Visual C++ Redistributable:** https://www.microsoft.com/en-us/download/details.aspx?id=40784
- **Documentação OpenCV:** https://opencv.org/
- **Documentação pyzbar:** https://pypi.org/project/pyzbar/

## Para desenvolvedores

**Bibliotecas utilizadas:**
- `opencv-python` - Processamento de imagens
- `pyzbar` - Decodificação de códigos de barras
- `pyautogui` - Captura de tela e automação
- `keyboard` - Detecção de teclas globais
- `pyperclip` - Manipulação da área de transferência
- `tkinter` - Interface gráfica (já vem com Python)

**Fluxo principal:**
1. `keyboard.add_hotkey()` - Monitora combinação de teclas
2. `on_click()` - Ativa interface de seleção
3. `tkinter.Canvas` - Overlay transparente para seleção
4. `pyautogui.screenshot()` - Captura área selecionada
5. `cv2.imread()` + `pyzbar.decode()` - Processa código
6. `pyperclip.copy()` - Copia resultado

---

**Sistema desenvolvido para otimizar o trabalho do setor financeiro**

## Estrutura do projeto

```
print-faturas-automation/
├── project.py                  # Sistema final integrado
├── LEITOR_AUTOMATION.bat       # Script de instalação de dependências  
├── EXECUTAR_LEITOR.bat         # Script para executar o sistema
├── 1-keyboard-detec.py         # Teste inicial de teclas
├── 2-print-screen.py           # Captura de tela
├── 3-mouse-click.py            # Interface de seleção
├── 4-integrando.py             # Primeira integração
├── 5-reader-barcode.py         # Leitor de códigos
├── 6-testando-thread.py        # Testes de threading
├── 7-integrando-thread.py      # Sistema com threads
├── pyzbar-0.1.9-py2.py3-none-win_amd64.whl  # Dependência Windows
└── README.md
```

## Arquivos .bat incluídos

### `LEITOR_AUTOMATION.bat` - Instalador automático
- Verifica se Python está instalado
- Instala todas as bibliotecas necessárias
- Instala a dependência .whl (procura na pasta atual ou dependencies/)
- Testa se tudo funcionou
- Lembra de baixar Visual C++ 2013

### `EXECUTAR_LEITOR.bat` - Executar sistema
- Interface visual amigável
- Executa o `project.py` automaticamente
- Ideal para criar atalho na área de trabalho

### Como personalizar o atalho:
1. Botão direito no `EXECUTAR_LEITOR.bat` → "Enviar para" → "Área de trabalho"
2. Botão direito no atalho criado → "Propriedades"
3. Aba "Atalho" → "Alterar ícone" → Escolher sua imagem .ico
4. Renomear para "LEITOR AUTOMATION"
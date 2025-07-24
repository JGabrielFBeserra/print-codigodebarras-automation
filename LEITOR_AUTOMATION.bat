@echo off
title LEITOR AUTOMATION - Instalacao de Dependencias
color 0A

echo.
echo  ===============================================
echo  LEITOR AUTOMATION - Instalacao de Dependencias
echo  ===============================================
echo.
echo  Este script instala todas as dependencias
echo  necessarias para o leitor de codigo de barras.
echo.
echo  Requisitos:
echo  - Python 3.11 LTS instalado
echo  - Visual C++ 2013 Redistributable
echo.
pause

echo.
echo [1/3] Verificando Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python nao encontrado!
    echo Baixe Python 3.11 LTS em: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo [2/3] Instalando bibliotecas Python...
pip install opencv-python pyzbar pyautogui keyboard pyperclip

echo.
echo [3/3] Instalando dependencia Windows (pyzbar)...
if exist "pyzbar-0.1.9-py2.py3-none-win_amd64.whl" (
    echo Instalando arquivo .whl local...
    pip install pyzbar-0.1.9-py2.py3-none-win_amd64.whl
) else if exist "dependencies\pyzbar-0.1.9-py2.py3-none-win_amd64.whl" (
    echo Instalando arquivo .whl da pasta dependencies...
    pip install dependencies\pyzbar-0.1.9-py2.py3-none-win_amd64.whl
) else (
    echo ⚠️ Arquivo .whl nao encontrado!
    echo Certifique-se de ter o arquivo pyzbar-0.1.9-py2.py3-none-win_amd64.whl
    echo na pasta atual ou dentro da pasta dependencies
)

echo.
echo [TESTE] Verificando instalacao...
python -c "import cv2, pyzbar, pyautogui, keyboard, pyperclip; print('✅ Todas as bibliotecas instaladas!')"

echo.
echo ===============================================
echo  INSTALACAO CONCLUIDA!
echo ===============================================
echo.
echo Para usar o sistema:
echo 1. Execute: EXECUTAR_LEITOR.bat
echo 2. Pressione z+x+c para ativar
echo 3. Selecione area do codigo de barras
echo 4. Clique em Print
echo.
echo IMPORTANTE - BAIXE ANTES DE USAR:
echo ⚠️ Visual C++ 2013 Redistributable (OBRIGATORIO!):
echo https://www.microsoft.com/en-us/download/details.aspx?id=40784
echo.
echo Se nao instalar o Visual C++, o pyzbar nao vai funcionar!
echo.
echo Crie um atalho na area de trabalho para facilitar!
echo.
pause
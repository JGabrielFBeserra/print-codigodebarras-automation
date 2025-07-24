@echo off
title LEITOR AUTOMATION - Sistema Ativo
color 0A

echo.
echo  ===============================================
echo  LEITOR AUTOMATION - Sistema Ativo
echo  ===============================================
echo.
echo   Sistema iniciado e aguardando comando!
echo.
echo   Deixe esta aba aberta em segundo plano
echo   Ele so vai funcionar quando digitar (z+x+c)
echo   Pressione z+x+c para ativar captura
echo   Para sair do modo de selecao APERTE "ESC"
echo   Selecione area do codigo de barras (tracejado em branco)
echo   Quando selecionar corretamente aperte em "Print"
echo   O sistema mostrara uma mensagem de resposta
echo   Caso tudo ocorra corretamente
echo   O numero sera copiado automaticamente e mostrara mensagem de SUCESSO
echo   E vai copiar o codigo na area de transferencia 
echo   (so falta apertar ctrl + v)
echo.
echo   Para fechar: Ctrl+C ou feche esta janela
echo  ===============================================
echo.

python project.py

echo.
echo 🛑 Sistema encerrado.
pause
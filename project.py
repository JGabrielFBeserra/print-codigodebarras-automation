import tkinter as tk
import pyautogui
import keyboard
import cv2
import os
from pyzbar.pyzbar import decode
import pyperclip
import json



start_x, start_y = None, None
end_x, end_y = None, None
rect_id = None
btn_id = None
codigo = ""

def on_click():
    global root, canvas, start_x, start_y, end_x, end_y, rect_id, btn_id

    def abrir_janela():
        global root, canvas
        
        def mensagem(text, tempo=1500):
            popup = tk.Tk()
            popup.overrideredirect(True)  # remove bordas
            popup.attributes("-topmost", True)
            popup.configure(bg='black')

            label = tk.Label(popup, text=text, bg='black', fg='white', font=("Arial", 14))
            label.pack(ipadx=20, ipady=10)

            # centraliza a janela na tela
            popup.update_idletasks()
            width = popup.winfo_width()
            height = popup.winfo_height()
            screen_width = popup.winfo_screenwidth()
            screen_height = popup.winfo_screenheight()
            x = (screen_width - width) // 2
            y = (screen_height - height) // 2
            popup.geometry(f'+{x}+{y}')

            # fecha depois de 3 segundos
            popup.after(tempo, popup.destroy)

            popup.mainloop()

        def reader_barcode_copy():
            global codigo
            
            barcodes = []
            
            try:
                img = cv2.imread("recorte.png")
                if img is None:
                    mensagem("Erro ao abrir imagem.")
                    return
                
                escalas_testes = [1,2,3,4,5]
                
                
                for escala in escalas_testes:
                    if barcodes:
                        break
                    if escala == 1:
                        test_img = img
                    else:
                        height, width = img.shape[:2] # descubro o tamanho da img [:2] só os dois primeiros valores
                        nova_width = int(width * escala)
                        nova_height = int(height * escala)
                        test_img = cv2.resize(img, (nova_width, nova_height), interpolation=cv2.INTER_CUBIC) # aumenta a imagem e cria pixels novos com mais qualidade

                    # converte para escala cinza
                    gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)
                    
                    # testes para tentar ler a imagem
                    images_to_try = [
                        ("normal", test_img),  # img tratada colorida
                        ("cinza", gray),  # escala de cinza
                        ("binaria", cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]),  # binariza em preto e branco
                        ("desfocada", cv2.GaussianBlur(gray, (3, 3), 0))  # desfoca para suavizar
                    ]         
                    for escala_teste, (nome_tratamento, imagem_tratada) in enumerate(images_to_try):
                        barcodes = decode(imagem_tratada)
                        if barcodes:
                            print(f"✅ Código encontrado no processamento Foi encontrado na escala: {escala}x e na imagem: {nome_tratamento}")
                            
                           
                            break
                
                if not barcodes:
                    mensagem("Erro: Nenhum código de barras encontrado\n💡 Dica: Tente selecionar só o código ou dar zoom na página", 4000)
                    with open("estatisticas_leituras.json", "a", encoding="utf-8") as f:
                        error = {
                            "erro": "nao foi lido nenhum codigo de barras"
                        }
                        json.dump(error, f)
                        f.write("\n")
                        
                    return
                for barcode in barcodes:
                    try:
                        codigo = barcode.data.decode("utf-8")
                        resultado = {
                            "codigo": codigo,
                            "tipo-codigo": barcode.type,
                            "escala": escala,
                            "tipo-imagem": nome_tratamento
                        }
            
                        with open("estatisticas_leituras.json", "a", encoding="utf-8") as f:
                            json.dump(resultado, f)
                            f.write("\n") 
                        
                        print("📦 Código:", codigo)
                        pyperclip.copy(codigo)
                        mensagem(f"Sucesso:✅✅✅ Código Copiado = {codigo}")
                        return  
                    except Exception:
                        mensagem("ERRO PERIGOSO: Nenhum código identificado")
               
            except Exception as e:
                mensagem(f"Erro inesperado: {e}")  
            finally:
                if os.path.exists("recorte.png"):
                    os.remove("recorte.png")

        def print_screen():
            root.destroy()
            x = min(start_x, end_x)
            y = min(start_y, end_y)
            width = abs(end_x - start_x)
            height = abs(end_y - start_y)
            img = pyautogui.screenshot(region=(x, y, width, height))
            img.save("recorte.png")
            reader_barcode_copy()

        def show_action_box(x, y):
            global btn_id
            btn_id = tk.Button(root, text="Print", command=print_screen)
            btn_id.place(x=x + 10, y=y + 10)

        def on_mouse_press(event):
            global start_x, start_y, btn_id
            start_x, start_y = event.x, event.y
            if btn_id:
                try:
                    if btn_id.winfo_exists():
                        btn_id.destroy()
                except tk.TclError:
                    pass  #ja foi destruido
                finally:
                    btn_id = None

        def on_mouse_drag(event):
            global rect_id
            if rect_id:
                canvas.delete(rect_id)
            rect_id = canvas.create_rectangle(
                start_x, start_y, event.x, event.y,
                outline="white", width=2, dash=(4, 2)
            )

        def on_mouse_release(event):
            global end_x, end_y
            end_x, end_y = event.x, event.y
            show_action_box(end_x, end_y)

        
        root = tk.Tk()
        root.attributes("-fullscreen", True)
        root.configure(bg='black')
        root.attributes("-alpha", 0.55)

        canvas = tk.Canvas(root, bg="black")
        canvas.pack(fill="both", expand=True)

        canvas.bind("<ButtonPress-1>", on_mouse_press)
        canvas.bind("<B1-Motion>", on_mouse_drag)
        canvas.bind("<ButtonRelease-1>", on_mouse_release)
        root.bind("<Escape>", lambda e: root.destroy())
        root.mainloop()
        
    abrir_janela()
keyboard.add_hotkey('z+x+c', on_click)
keyboard.wait()

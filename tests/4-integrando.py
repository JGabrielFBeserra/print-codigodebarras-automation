import tkinter as tk
import pyautogui
import keyboard




start_x, start_y = None, None
end_x, end_y = None, None
rect_id = None
btn_id = None

def on_click():
    
    


    def on_mouse_drag(event):
        global rect_id
        
        # deleta o retângulo antigo
        if rect_id:
            canvas.delete(rect_id)
        

        # desenha um novo com base nos pontos iniciais e atuais
        rect_id = canvas.create_rectangle(
            start_x, start_y, event.x, event.y,
            outline="white", width=2, dash=(4, 2)
        )

    def show_action_box(x, y):
        global btn_id
        

        btn_id = tk.Button(root, text="Print", command=print_screen)

        # inserindo o botão no canvas com .place()
        btn_id.place(x=x + 10, y=y + 10)

        
        
    def print_screen():
        root.destroy()
        
        global start_x, start_y, end_x, end_y
        
        x = min(start_x, end_x)
        y = min(start_y, end_y)
        width = abs(end_x - start_x)
        height = abs(end_y - start_y)
        
        img = pyautogui.screenshot(region=(x, y, width, height))
        img.save("recorte.png")
        
        
        
    def on_mouse_press(event):
        global start_x, start_y, btn_id
        start_x, start_y = event.x, event.y
        print(f"🟢 Início da seleção: ({start_x}, {start_y})")
        if btn_id:
            btn_id.destroy()
            btn_id = None
        
    def on_mouse_release(event):
        global end_x, end_y
        end_x, end_y = event.x, event.y
        print(f"🔴 Fim da seleção: ({end_x}, {end_y})")
        print(f"📦 Área selecionada: {start_x},{start_y} → {end_x},{end_y}")
        show_action_box(end_x, end_y)
        




    root = tk.Tk()
    canvas = tk.Canvas()

    root.attributes("-fullscreen", True)
    root.overrideredirect(True)
    root.configure(bg='black')
    root.attributes("-alpha", 0.55)


    canvas = tk.Canvas(root, bg="black")
    canvas.pack(fill="both", expand=True)

    canvas.bind("<ButtonPress-1>", on_mouse_press)
    canvas.bind("<B1-Motion>", on_mouse_drag)
    canvas.bind("<ButtonRelease-1>", on_mouse_release)



    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()   



keyboard.add_hotkey('ctrl+alt+a', on_click)

keyboard.wait()

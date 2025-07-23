import tkinter as tk
import threading
import time


def abrir_sem_thread():
    print(" janela sem thread... (trava tudo)")
    root = tk.Tk()
    root.title("Sem Thread")
    tk.Label(root, text="trava tudo").pack(padx=50, pady=30)
    root.mainloop()
    print("janel sem thread fechada.")


def abrir_com_thread():
    print("abrindo janela COM thread... (não trava)")

    def janela():
        root = tk.Tk()
        root.title("com Thread")
        tk.Label(root, text="essa janela não trava o programa").pack(padx=50, pady=30)
        root.mainloop()
        print("janela COM thread fechada.")

    threading.Thread(target=janela).start()



print("\n janela SEM thread...")
abrir_sem_thread()

print("\n janela COM thread...")
abrir_com_thread()


for i in range(5):
    print(f"programa ainda rodando... {i+1}")
    time.sleep(1)

print("teste")

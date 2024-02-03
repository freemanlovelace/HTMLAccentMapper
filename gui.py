import tkinter as tk
import mapper



root = tk.Tk()
root.geometry('400x100')
root.resizable(False, False)
root.title("HTMLAccentMapper")

radio_var = tk.StringVar()


activated_radio = tk.Radiobutton(root, text="Activate",variable=radio_var, 
                                 value="Activate", command=mapper.start_mapping)

deactivated_radio = tk.Radiobutton(root, text="Deactivate", variable=radio_var, 
                                   value="Deactivate", command=mapper.stop_mapping)


activated_radio.grid(row=0, column=0, padx=10, pady=10)
deactivated_radio.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()

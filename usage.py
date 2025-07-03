import tkinter as tk
from tkinter import ttk
from logic import Logic

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(True, True)
        self.root.minsize(250, 350)
        self.logic = Logic()
        
        # Create the display
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        # Create the main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Create/Update display
        self.create_display(main_frame)
        self.create_buttons(main_frame)
        self.update_display()
    
    def create_display(self, parent):
        '''
        Create the calculator display
        '''
        display_frame = ttk.Frame(parent)
        display_frame.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        display_frame.columnconfigure(0, weight=1)
        display_frame.rowconfigure(0, weight=1)
        
        # Label
        display_label = ttk.Label(
            display_frame, 
            textvariable=self.display_var,
            font=('Arial', 24),
            anchor='e',
            background='white',
            relief='sunken',
            padding=(10, 5)
        )
        display_label.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    def create_buttons(self, parent):
        '''
        Create the calculator buttons
        '''
        buttons = [
            ['C', '+/-', '%', '+'],
            ['7', '8', '9', '-'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '/'],
            ['0', '', '.', '=']
        ]
        
        # Create buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:
                    if text == 'C':
                        btn = ttk.Button(
                            parent,
                            text=text,
                            command=self.clear
                        )
                    elif text == '=':
                        btn = ttk.Button(
                            parent,
                            text=text,
                            command=self.equals
                        )
                    elif text in ['+', '-', '*', '/', '%', '+/-', '.']:
                        btn = ttk.Button(
                            parent,
                            text=text,
                            command=lambda op=text: self.operation(op)
                        )
                    else:
                        btn = ttk.Button(
                            parent,
                            text=text,
                            command=lambda num=text: self.number(num)
                        )
                    
                    btn.grid(row=i+1, column=j, sticky=(tk.W, tk.E, tk.N, tk.S), padx=2, pady=2)
        
        # Configure grid weights for buttons
        for i in range(4):
            parent.columnconfigure(i, weight=1)
        for i in range(6):
            parent.rowconfigure(i, weight=1)
    
    def number(self, num):
        '''
        Handle number button presses
        '''
        self.logic.commence(num)
        self.update_display()
    
    def operation(self, op):
        '''
        Handle operation button presses
        '''
        self.logic.commence(op)
        self.update_display()
    
    def equals(self):
        '''
        Handle equals button press
        '''
        self.logic.commence('=')
        self.update_display()
    
    def clear(self):
        '''
        Clear the calculator
        '''
        self.logic = Logic()
        self.update_display()

    def update_display(self):
        '''
        Update the display with current value
        '''
        self.display_var.set(self.logic.display())

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()

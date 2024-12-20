import tkinter as tk

class PDA:
    def __init__(self):
        self.transitions = {
            'q0': {'a': ('q0', 'A'), 'b': ('q1', 'ϵ')},  # Transitions for q0
            'q1': {'b': ('q1', 'ϵ')},  # Transitions for q1
        }
        self.accepting_state = 'qf'
    
    def simulate(self, input_string):
        stack = ['Z']  # Initialize the stack with the initial symbol 'Z'
        current_state = 'q0'  # Start in the initial state q0
        input_string += '$'  # Append end-of-input marker

        # Flag to ensure at least one 'a' and one 'b' are processed
        seen_a = False
        seen_b = False
        
        for char in input_string:
            if current_state == 'q0':
                if char == 'a':
                    stack.append('A')  # Push 'A' for each 'a'
                    seen_a = True
                elif char == 'b' and stack[-1] == 'A':
                    stack.pop()  # Pop an 'A' for each 'b'
                    current_state = 'q1'
                    seen_b = True
                else:
                    return "REJECTED"  # Invalid transition

            elif current_state == 'q1':
                if char == 'b' and stack[-1] == 'A':
                    stack.pop()  # Pop 'A' for each 'b'
                    seen_b = True
                elif char == '$' and stack[-1] == 'Z':
                    if seen_a and seen_b:
                        current_state = self.accepting_state  # Accept if valid stack and n >= 1
                    else:
                        return "REJECTED"
                else:
                    return "REJECTED"  # Invalid transition
        
        return "ACCEPTED" if current_state == self.accepting_state and stack == ['Z'] else "REJECTED"

class PDAVisualizer:
    def __init__(self, root, pda):
        self.root = root
        self.pda = pda

        # Set window title
        self.root.title("PDA String Validator")

        # Input label
        self.label = tk.Label(root, text="Enter a string:")
        self.label.pack(pady=10)

        # Input entry box
        self.entry = tk.Entry(root, width=20)
        self.entry.pack(pady=5)

        # Button to check input
        self.check_button = tk.Button(root, text="Check", command=self.check_string)
        self.check_button.pack(pady=5)

        # Label for displaying results
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Canvas for drawing the PDA diagram
        self.canvas = tk.Canvas(root, width=600, height=300)
        self.canvas.pack(pady=20)

        self.draw_pda_diagram()

    def check_string(self):
        input_string = self.entry.get()
        result = self.pda.simulate(input_string)
        self.result_label.config(text=f"Result: {result}")

    def draw_pda_diagram(self):
        
        self.canvas.create_oval(100, 100, 200, 200, fill="lightblue", outline="black")
        self.canvas.create_text(150, 150, text="q0", font=("Arial", 14))

        self.canvas.create_oval(250, 100, 350, 200, fill="lightblue", outline="black")
        self.canvas.create_text(300, 150, text="q1", font=("Arial", 14))

        self.canvas.create_oval(400, 100, 500, 200, fill="lightblue", outline="black")
        self.canvas.create_text(450, 150, text="qf", font=("Arial", 14))

       
        self.canvas.create_line(200, 150, 250, 150, arrow=tk.LAST)
        self.canvas.create_text(225, 130, text="a, Z -> A", font=("Arial", 10))

        self.canvas.create_line(350, 150, 400, 150, arrow=tk.LAST)
        self.canvas.create_text(375, 130, text="b, A -> ϵ", font=("Arial", 10))

        
        self.canvas.create_arc(130, 100, 170, 140, start=0, extent=180, style=tk.ARC)
        self.canvas.create_line(150, 70, 150, 100, arrow=tk.LAST)
        self.canvas.create_text(150, 50, text="a, A -> A", font=("Arial", 10))
        self.canvas.create_text(300, 250, text="L = {aⁿbⁿ | n ≥ 1}", font=("Arial", 12), fill="blue")

def main():
    pda = PDA()
    root = tk.Tk()
    visualizer = PDAVisualizer(root, pda)
    root.mainloop()

if __name__ == "__main__":
    main()

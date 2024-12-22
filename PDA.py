import tkinter as tk

class PDA:
    def __init__(self):
        pass

    def dpda_accepts(self, input_string):
        stack = []  
        state = "q0"  
        for char in input_string:
            if state == "q0":
                if char in {'a', 'b'}:
                    stack.append(char)  # Push 'a' or 'b' onto the stack
                elif char == 'c':
                    state = "q1"  
                else:
                    return "REJECTED"  

            elif state == "q1":
                if char in {'a', 'b'}:
                    if not stack or stack[-1] != char:
                        return "REJECTED"  
                    stack.pop()  
                else:
                    return "REJECTED"  

        return "ACCEPTED" if state == "q1" and not stack else "REJECTED"

    def simulate(self, input_string):
        return self.dpda_accepts(input_string)


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

        # Bind mouse click event to display coordinates
        self.canvas.bind("<Button-1>", self.show_coordinates)

        self.draw_pda_diagram()

    def check_string(self):
        input_string = self.entry.get()
        if not input_string:
            self.result_label.config(text="Result: REJECTED (empty input)")
        else:
            result = self.pda.simulate(input_string)
            self.result_label.config(text=f"Result: {result}")

    def draw_pda_diagram(self):
        # Draw states
        self.canvas.create_oval(100, 100, 200, 200, fill="lightblue", outline="black")
        self.canvas.create_text(150, 150, text="q0", font=("Arial", 14))

        self.canvas.create_oval(250, 100, 350, 200, fill="lightblue", outline="black")
        self.canvas.create_text(300, 150, text="q1", font=("Arial", 14))

        self.canvas.create_oval(400, 100, 500, 200, fill="lightblue", outline="black")
        self.canvas.create_oval(395, 95, 505, 205, outline="black")
        self.canvas.create_text(450, 150, text="qf", font=("Arial", 14))

        # Starting arrow to q0
        self.canvas.create_line(50, 150, 100, 150, arrow=tk.LAST)

        # Transition arrows
        self.canvas.create_line(200, 150, 250, 150, arrow=tk.LAST)
        self.canvas.create_text(225, 130, text="(c, b/b)", font=("Arial", 10))
        self.canvas.create_text(225, 165, text="(c, a/a)", font=("Arial", 10))

        self.canvas.create_line(350, 150, 400, 150, arrow=tk.LAST)
        self.canvas.create_text(375, 130, text="(ε, Z/Z)", font=("Arial", 10))

        # Self-loop on q0 for a and b
        self.canvas.create_arc(120, 50, 180, 110, start=-50, extent=290, style=tk.ARC)
        self.canvas.create_line(175, 95, 160, 110, arrow=tk.LAST)
        self.canvas.create_text(150, 40, text="(a, Z/aZ)", font=("Arial", 10))
        self.canvas.create_text(150, 25, text="(a, a/aa)", font=("Arial", 10))
        self.canvas.create_text(150, 15, text="(a, b/ab)", font=("Arial", 10))
        
        self.canvas.create_arc(120, 245, 180, 195, start=130, extent=290, style=tk.ARC)        
        self.canvas.create_line(175, 205, 160, 195, arrow=tk.LAST)
        self.canvas.create_text(150, 255, text="(b, Z/bZ)", font=("Arial", 10))
        self.canvas.create_text(150, 270, text="(b, b/bb)", font=("Arial", 10))
        self.canvas.create_text(150, 285, text="(b, a/ba)", font=("Arial", 10))

        # Self-loop on q1 for a and b
        self.canvas.create_arc(270, 50, 330, 110, start=-50, extent=290, style=tk.ARC)
        self.canvas.create_line(325, 95, 310, 110, arrow=tk.LAST)
        self.canvas.create_text(300, 25, text="(a, a/ε)", font=("Arial", 10))
        self.canvas.create_text(300, 40, text="(b, b/ε)", font=("Arial", 10))

        # Label the language description
        self.canvas.create_text(300, 250, text="L = {W C W^R | W ∈ (a, b)*}", font=("Arial", 12), fill="blue")

    def show_coordinates(self, event):
        print(f"Mouse clicked at: ({event.x},{event.y})")


def main():
    pda = PDA()
    root = tk.Tk()
    visualizer = PDAVisualizer(root, pda)
    root.mainloop()


if __name__ == "__main__":
    main()

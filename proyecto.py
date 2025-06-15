import tkinter as tk

class App:
    def __init__(self, master):
        # Inicializar la ventana principal
        self.master = master
        self.master.geometry("600x700")

        # Configurar la ventana
        self.master.title("Optimizacion ubicacion de Concierto")
        
        # Titulo arriba en el centro
        self.label_input = tk.Label(master, text="Entrada")
        self.label_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

       # abajo  # descripcion lado izquierdo y TextArea para la entrada lado derecho debajo del label
        self.description_label = tk.Label(master, text="Ingrese \nN: tamano del cuadrado \nM: numero de ciudades \nCiudades: ciudad, X, Y:")
        self.description_label.grid(row=1, column=0, padx=10, pady=10)
        self.text_area = tk.Text(master, width=50, height=15)
        self.text_area.grid(row=1, column=1, padx=10, pady=10)
        # Placeholder que desaparece al hacer click en el TextArea
        self.text_area.insert(tk.END, "12\n5\nPalmira 2 3\nCali 10 2\nBuga 11 0\nTulua 0 3\nRioFrio 1 2")
        self.text_area.bind("<FocusIn>", lambda e: self.text_area.delete("1.0", tk.END) if self.text_area.get("1.0", tk.END).strip() == "12\n5\nPalmira 2 3\nCali 10 2\nBuga 11 0\nTulua 0 3\nRioFrio 1 2" else None)
        self.text_area.bind("<FocusOut>", lambda e: self.text_area.insert(tk.END, "12\n5\nPalmira 2 3\nCali 10 2\nBuga 11 0\nTulua 0 3\nRioFrio 1 2") if not self.text_area.get("1.0", tk.END).strip() else None)

        # Botón para resolver el problema
        self.solve_button = tk.Button(master, text="Resolver Problema", command=self.solve_problem)
        self.solve_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Label para mostrar el resultado del código MiniZinc generado texto izquierda y TextArea derecha uno al lado del otro
        self.label_output = tk.Label(master, text="Código MiniZinc generado")
        self.label_output.grid(row=3, column=0, padx=10, pady=10)
        # Area para mostrar el código MiniZinc generado, no se puede escribir en él
        self.output_area = tk.Text(master, width=50, height=15)
        self.output_area.grid(row=3, column=1, padx=10, pady=10)
        self.output_area.config(state=tk.DISABLED)  # Deshabilitar la edición del TextArea
        
        # Botón para copiar el código MiniZinc generado al portapapeles
        self.copy_button = tk.Button(master, text="Copiar Código MiniZinc", command=self.copy_to_clipboard)
        self.copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


    def copy_to_clipboard(self):
        # Habilitar el TextArea para copiar el texto
        self.output_area.config(state=tk.NORMAL)
        self.output_area.focus_set()
        self.output_area.tag_add(tk.SEL, "1.0", tk.END)
        self.master.clipboard_clear()
        self.master.clipboard_append(self.output_area.get("1.0", tk.END))
        self.output_area.tag_remove(tk.SEL, "1.0", tk.END)
        self.output_area.config(state=tk.DISABLED)


    def solve_problem(self):
        # Obtener la entrada del TextArea
        input_text = self.text_area.get("1.0", tk.END).strip().split("\n")
        
        # Procesar la entrada
        N = int(input_text[0])
        M = int(input_text[1])
        cities = [line.split() for line in input_text[2:2 + M]]
        
        # Verificaciones de la entrada
        error = self.verification(N, M, cities)
        
        if error:
            return
        
        minizinc_code = self.generate_minizinc_code(N, M, cities)
        # Mostrar el código MiniZinc generado en el TextArea de salida
        self.output_area.config(state=tk.NORMAL)
        self.output_area.delete("1.0", tk.END)
        self.output_area.insert(tk.END, minizinc_code)
        self.output_area.config(state=tk.DISABLED)
        

    def verification(self, N, M, cities):
        # Comprobar que el número de ciudades es M
        error = False
        if len(cities) != M:
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, "Error: El número de ciudades no coincide con M.")
            self.output_area.config(state=tk.DISABLED)
            error = True
            return error
        
        # Comprobar que las ciudades estén en el formato correcto
        for city in cities:
            if len(city) != 3:
                self.output_area.config(state=tk.NORMAL)
                self.output_area.delete("1.0", tk.END)
                self.output_area.insert(tk.END, "Error: Formato de ciudad incorrecto.")
                self.output_area.config(state=tk.DISABLED)
                error = True
                return error
            try:
                x = int(city[1])
                y = int(city[2])
            except ValueError:
                self.output_area.config(state=tk.NORMAL)
                self.output_area.delete("1.0", tk.END)
                self.output_area.insert(tk.END, "Error: Coordenadas no son enteras.")
                self.output_area.config(state=tk.DISABLED)
                error = True
                return error
            
        # Comprobar que las coordenadas están dentro del rango [0, N]
        for city in cities:
            x = int(city[1])
            y = int(city[2])
            if x < 0 or x > N or y < 0 or y > N:
                self.output_area.config(state=tk.NORMAL)
                self.output_area.delete("1.0", tk.END)
                self.output_area.insert(tk.END, "Error: Coordenadas fuera de rango.")
                self.output_area.config(state=tk.DISABLED)
                error = True
                return error
            
        # Comprobar que las ciudades no están en la misma posición
        city_positions = [(int(city[1]), int(city[2])) for city in cities]
        if len(city_positions) != len(set(city_positions)):
            self.output_area.config(state=tk.NORMAL)
            self.output_area.delete("1.0", tk.END)
            self.output_area.insert(tk.END, "Error: Hay ciudades en la misma posición.")
            self.output_area.config(state=tk.DISABLED)
            error = True
            return error
        
    def generate_minizinc_code(self, N, M, cities):
        # Definimos N y M como enteros
        code = f"int: N = {N};          % Tamaño del Valle del Cauca \n"
        code += f"int: M = {M};         % Número de ciudades\n\n"

        # Definición del array de ciudades
        code += "% Ciudades: (nombre, x, y)\n"

        code += f"array[1..M] of tuple(string, int, int): ciudades = [\n"
        for i, city in enumerate(cities):
            nombre = city[0]
            x = int(city[1])
            y = int(city[2])
            code += f"  (\"{nombre}\", {x}, {y})"
            if i < len(cities) - 1:
                code += ",\n"
        code += "\n];\n\n"

        # Variables del concierto
        code += "% Variables del concierto\n"
        code += "var 0..N: concert_x;       % Coordenada x del concierto\n"
        code += "var 0..N: concert_y;       % Coordenada y del concierto\n\n"

        # Distancias Manhattan
        code += f"array[1..M] of var 0..{(2*(N-1))}: distances;   % Distancias a cada ciudad\n\n" 

        # Restricciónes
        code += "% Restricciones:\n"

        code += "  % Calcular las distancias Manhattan desde el concierto a cada ciudad, no puede superar 2*(N-1)\n"
        code += "constraint\n"
        code += "  forall(i in 1..M)(\n"
        code += "    distances[i] = abs(concert_x - ciudades[i].2) + abs(concert_y - ciudades[i].3)\n"
        code += "  );\n\n"

        code += "  % El concierto no puede estar en la misma posición que ninguna ciudad\n"
        code += "constraint\n"
        code += "  forall(i in 1..M)(\n"
        code += "    concert_x != ciudades[i].2 \\/ concert_y != ciudades[i].3\n"
        code += "  );\n\n"

        code += "  % La diferencia máxima entre distancias es 2 (nadie es favorecido)\n"
        code += "constraint\n"
        code += "  max(distances) - min(distances) <= 2;\n\n"
        
        # Minimizar la distancia máxima
        code += "% Objetivo: Minimizar la distancia máxima \n"
        code += "var int: max_distance = max(distances);\n"
        code += "solve minimize max_distance;\n\n"

        code += "output [\n"
        code += "  \"Concierto en: (\", show(concert_x), \", \", show(concert_y), \")\\n\",\n"
        code += "  \"Distancia máxima a una ciudad: \", show(max_distance), \"\\n\",\n"
        code += "  \"Ciudades y sus distancias:\\n\",\n"
        code += "] ++ [\n"
        code += "   if i > 1 then \"\\n\" else \"\" endif ++\n"
        code += "  \"- \" ++ show(ciudades[i].1) ++ \": \" ++ show(distances[i])\n"
        code += "  | i in 1..M\n"
        code += "];\n"

        return code
            
                         
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
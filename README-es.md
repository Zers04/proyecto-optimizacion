# 🎶 Proyecto de Optimización: ¿Dónde pongo mi concierto?

[![en](https://img.shields.io/badge/lang-en-blue.svg)](https://github.com/Zers04/optimizacion-concierto/blob/main/README.md)
[![es](https://img.shields.io/badge/lang-es-blue.svg)](https://github.com/Zers04/optimizacion-concierto/blob/main/README-es.md)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange)
![MiniZinc](https://img.shields.io/badge/Modelado-MiniZinc-purple)

Este proyecto aborda un **problema de optimización discreta**: determinar la ubicación más justa para realizar un concierto dentro del departamento del **Valle del Cauca**, evitando favorecer a una ciudad sobre otra.  

Se modela el problema en un plano cartesiano **N x N**, donde cada ciudad tiene coordenadas enteras, y la solución debe garantizar una distribución equitativa de las distancias usando la **distancia Manhattan**.

---

## 📖 Descripción del problema

- El concierto **no puede realizarse en la misma ubicación de ninguna ciudad**.
- Se busca una ubicación tal que:
  - La diferencia entre la ciudad más cercana y la más lejana al concierto sea **≤ 2 km**.
  - Se **minimice la distancia máxima (Manhattan)** entre el concierto y cualquier ciudad.

---

## 🧮 Modelo matemático

**Función objetivo**  
Minimizar la distancia máxima entre el concierto y cualquier ciudad:

```
min ( max di ) donde di = |x - xi| + |y - yi|
```

**Restricciones principales**
1. El concierto no puede ubicarse en la misma posición que una ciudad.  
2. La diferencia entre la ciudad más cercana y la más lejana debe ser ≤ 2 km.  
3. Se deben cumplir los límites del plano \(N \times N\).  

---

## 💻 Implementación

El proyecto fue desarrollado en **Python** con los siguientes componentes:

- **Tkinter GUI**: interfaz que permite ingresar datos de entrada (N, número de ciudades y sus coordenadas).  
- **Procesamiento**: validación de entradas y verificación de restricciones.  
- **Generación de código MiniZinc**: el sistema no resuelve directamente, sino que **genera el código de modelo en MiniZinc**, listo para ejecutarse en el IDE correspondiente.  

Ejemplo de entrada esperada en la interfaz:

```
12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
```

## 🚀 Instalación y ejecución

### 1. Clonar repositorio
```bash
git clone https://github.com/Zers04/proyecto-optimizacion.git
cd proyecto-optimizacion
```

Para iniciar el proyecto, ejecuta:

```bash
python main.py
```

## Autores ✒️

* **Juan David Cataño** - [Zers04](https://github.com/Zers04)
* **Valentina Londoño** - [Valtimore](https://github.com/valtimore)

## Licencia 📄

Este proyecto está bajo la Licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
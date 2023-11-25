import turtle
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def dibujar_arbol(self):
        turtle.clear()
        turtle.setup(width=800, height=800)
        turtle.speed(0)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        nivel = self._obtener_nivel(self.raiz)
        espaciado_horizontal = 300  # Espaciado horizontal entre nodos
        espaciado_vertical = 80  # Espaciado vertical inicial
        y = nivel * espaciado_vertical // 2  # Posición inicial en el centro vertical
        self._dibujar_nodo(self.raiz, 0, y, espaciado_horizontal, espaciado_vertical)

    

    def _dibujar_nodo(self, nodo, x, y, espaciado_horizontal, espaciado_vertical):
        if nodo is None:
            return

        # Dibujar nodo
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.write(nodo.dato, align="center", font=("Arial", 12, "normal"))

        # Calcular coordenadas de los hijos
        hijo_izquierdo_x = x - espaciado_horizontal
        hijo_izquierdo_y = y - espaciado_vertical
        hijo_derecho_x = x + espaciado_horizontal
        hijo_derecho_y = y - espaciado_vertical

        # Dibujar conexiones y dibujar hijos
        if nodo.izquierda:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.goto(hijo_izquierdo_x, hijo_izquierdo_y)
            self._dibujar_nodo(nodo.izquierda, hijo_izquierdo_x, hijo_izquierdo_y, espaciado_horizontal / 2, espaciado_vertical * 1.1)  # Ajustar el espaciado

        if nodo.derecha:
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()
            turtle.goto(hijo_derecho_x, hijo_derecho_y)
            self._dibujar_nodo(nodo.derecha, hijo_derecho_x, hijo_derecho_y, espaciado_horizontal / 2, espaciado_vertical * 1.1)  # Ajustar el espaciado

    def _obtener_nivel(self, nodo):
        if nodo is None:
            return 0
        return max(self._obtener_nivel(nodo.izquierda), self._obtener_nivel(nodo.derecha)) + 1
        
            
    def insertar_binario(self, raiz, dato):
        if raiz is None:
            return Nodo(dato)
        else:
            if dato <= raiz.dato:
                raiz.izquierda = self.insertar_binario(raiz.izquierda, dato)
            else:
                raiz.derecha = self.insertar_binario(raiz.derecha, dato)
            return raiz

    def imprimir_preorden(self, raiz):
        if raiz is None:
            return
        print(raiz.dato, end=" ")
        self.imprimir_preorden(raiz.izquierda)
        self.imprimir_preorden(raiz.derecha)

    def imprimir_inorden(self, raiz):
        if raiz is None:
            return
        self.imprimir_inorden(raiz.izquierda)
        print(raiz.dato, end=" ")
        self.imprimir_inorden(raiz.derecha)

    def imprimir_postorden(self, raiz):
        if raiz is None:
            return
        self.imprimir_postorden(raiz.izquierda)
        self.imprimir_postorden(raiz.derecha)
        print(raiz.dato, end=" ")

    def imprimir_nodos(self, raiz):
        if raiz is None:
            return
        cola = [raiz]
        while cola:
            nodo = cola.pop(0)
            print(nodo.dato, end=" ")
            if nodo.izquierda:
                cola.append(nodo.izquierda)
            if nodo.derecha:
                cola.append(nodo.derecha)

    def eliminar(self, raiz, dato):
        if raiz is None:
            return raiz

        if dato < raiz.dato:
            raiz.izquierda = self.eliminar(raiz.izquierda, dato)
        elif dato > raiz.dato:
            raiz.derecha = self.eliminar(raiz.derecha, dato)
        else:
            # Caso 1: Nodo a eliminar es una hoja
            if raiz.izquierda is None and raiz.derecha is None:
                raiz = None
            # Caso 2: Nodo a eliminar tiene un solo hijo
            elif raiz.izquierda is None:
                raiz = raiz.derecha
            elif raiz.derecha is None:
                raiz = raiz.izquierda
            # Caso 3: Nodo a eliminar tiene dos hijos
            else:
                nodo_reemplazo = self.encontrar_minimo(raiz.derecha)
                raiz.dato = nodo_reemplazo.dato
                raiz.derecha = self.eliminar(raiz.derecha, nodo_reemplazo.dato)

        return raiz

    def encontrar_minimo(self, raiz):
        if raiz.izquierda is None:
            return raiz
        return self.encontrar_minimo(raiz.izquierda)

#### Características

    def es_arbol_perfecto(self, raiz):
        def calcular_altura(raiz):
            if raiz is None:
                return 0
            return max(calcular_altura(raiz.izquierda), calcular_altura(raiz.derecha)) + 1

        def es_arbol_perfecto_uti(raiz, altura, nivel):
            if raiz is None:
                return True

            if raiz.izquierda is None and raiz.derecha is None:
                return altura == nivel + 1

            if raiz.izquierda is None or raiz.derecha is None:
                return False

            return (es_arbol_perfecto_uti(raiz.izquierda, altura, nivel + 1) and
                    es_arbol_perfecto_uti(raiz.derecha, altura, nivel + 1))

        altura = calcular_altura(raiz)
        return es_arbol_perfecto_uti(raiz, altura, 0)

    def es_arbol_lleno(self, raiz):
        if raiz is None:
            return True

        if raiz.izquierda is None and raiz.derecha is None:
            return True

        if raiz.izquierda is not None and raiz.derecha is not None:
            return (self.es_arbol_lleno(raiz.izquierda) and self.es_arbol_lleno(raiz.derecha))

        return False

    def obtener_altura(self, raiz):
        if raiz is None:
            return 0
        return max(self.obtener_altura(raiz.izquierda), self.obtener_altura(raiz.derecha)) + 1

    def obtener_peso(self, raiz):
        if raiz is None:
            return 0

        peso = 1
        peso += self.obtener_peso(raiz.izquierda)
        peso += self.obtener_peso(raiz.derecha)

        return peso
    
    def imprimir_nodos_hoja(self, raiz):
        if raiz is None:
            return
        if raiz.izquierda is None and raiz.derecha is None:
            print(raiz.dato, end=" ")
        self.imprimir_nodos_hoja(raiz.izquierda)
        self.imprimir_nodos_hoja(raiz.derecha)
        

    def obtener_nodo_raiz(self):
        return self.raiz


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        return len(self.items) == 0

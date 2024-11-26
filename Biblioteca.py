#juan david vargas 
#manuel borrero 
#keider chavarria
# proyecto final biblioteca :)
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, field

# === Clases del sistema ===

@dataclass
class Usuario:
    id: int
    nombre: str  
    prestamos: List['Prestamo'] = field(default_factory=list)
    MAX_PRESTAMOS = 3

    def puede_prestar(self) -> bool:
        return len(self.prestamos) < self.MAX_PRESTAMOS

@dataclass
class Libro:
    id: int
    titulo: str
    autor: str
    categoria: str
    disponible: bool = True

@dataclass
class Prestamo:
    id: int
    usuario: Usuario
    libro: Libro
    fecha_prestamo: datetime
    fecha_devolucion: Optional[datetime] = None

class Biblioteca:
    def __init__(self):
        self.usuarios: Dict[int, Usuario] = {}
        self.libros: Dict[int, Libro] = {}
        self.prestamos: Dict[int, Prestamo] = {}
        self.siguiente_id_prestamo = 1

    def agregar_libro(self, id: int, titulo: str, autor: str, categoria: str) -> Libro:
        if id in self.libros:
            raise ValueError("Ya existe un libro con este ID")
        libro = Libro(id, titulo, autor, categoria)
        self.libros[id] = libro
        return libro

    def eliminar_libro(self, id: int) -> None:
        if id not in self.libros:
            raise ValueError("Libro no encontrado")
        if not self.libros[id].disponible:
            raise ValueError("No se puede eliminar un libro prestado")
        del self.libros[id]

    def buscar_libros(self, criterio: str, valor: str) -> List[Libro]:
        resultados = []
        for libro in self.libros.values():
            if criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def registrar_usuario(self, id: int, nombre: str) -> Usuario:
        if id in self.usuarios:
            raise ValueError("Ya existe un usuario con este ID")
        usuario = Usuario(id, nombre)
        self.usuarios[id] = usuario
        return usuario

    def prestar_libro(self, usuario_id: int, libro_id: int) -> Prestamo:
        if usuario_id not in self.usuarios:
            raise ValueError("Usuario no encontrado")
        if libro_id not in self.libros:
            raise ValueError("Libro no encontrado")
        
        usuario = self.usuarios[usuario_id]
        libro = self.libros[libro_id]
        
        if not libro.disponible:
            raise ValueError("Libro no disponible")
        if not usuario.puede_prestar():
            raise ValueError(f"El usuario ha alcanzado el límite de {Usuario.MAX_PRESTAMOS} libros")
        
        prestamo = Prestamo(
            id=self.siguiente_id_prestamo,
            usuario=usuario,
            libro=libro,
            fecha_prestamo=datetime.now()
        )
        
        self.siguiente_id_prestamo += 1
        libro.disponible = False
        usuario.prestamos.append(prestamo)
        self.prestamos[prestamo.id] = prestamo
        return prestamo

    def devolver_libro(self, prestamo_id: int) -> None:
        if prestamo_id not in self.prestamos:
            raise ValueError("Préstamo no encontrado")
        
        prestamo = self.prestamos[prestamo_id]
        if prestamo.fecha_devolucion is not None:
            raise ValueError("Este libro ya fue devuelto")
        
        prestamo.fecha_devolucion = datetime.now()
        prestamo.libro.disponible = True
        prestamo.usuario.prestamos.remove(prestamo)

    def reporte_libros_solicitados(self) -> Dict[str, int]:
        conteo_prestamos = {}
        for prestamo in self.prestamos.values():
            titulo = prestamo.libro.titulo
            conteo_prestamos[titulo] = conteo_prestamos.get(titulo, 0) + 1
        return dict(sorted(conteo_prestamos.items(), key=lambda x: x[1], reverse=True))

    def reporte_usuarios_activos(self) -> Dict[str, int]:
        usuarios_activos = {}
        for usuario in self.usuarios.values():
            prestamos_activos = len([p for p in usuario.prestamos if p.fecha_devolucion is None])
            if prestamos_activos > 0:
                usuarios_activos[usuario.nombre] = prestamos_activos
        return usuarios_activos

# === Interfaz gráfica con Tkinter ===

# Contraseña del administrador
ADMIN_PASSWORD = "Wasabi"  # Contraseña para acceder a la administración

class InterfazBiblioteca:
    def __init__(self, root):
        self.root = root
        self.root.title("Biblioteca")
        self.biblioteca = Biblioteca()  # Instanciamos la clase Biblioteca

        # Frame principal
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Botones de navegación
        self.btn_buscar = tk.Button(frame, text="Buscar libro", command=self.buscar_libros)
        self.btn_buscar.pack(pady=5)
        self.btn_registrar = tk.Button(frame, text="Registrar usuario", command=self.registrar_usuario)
        self.btn_registrar.pack(pady=5)
        self.btn_prestar = tk.Button(frame, text="Prestar libro", command=self.prestar_libro)
        self.btn_prestar.pack(pady=5)
        self.btn_devolver = tk.Button(frame, text="Devolver libro", command=self.devolver_libro)
        self.btn_devolver.pack(pady=5)
        self.btn_admin = tk.Button(frame, text="Administrar inventario", command=self.admin_login)
        self.btn_admin.pack(pady=5)

    # Función para verificar la contraseña de administrador
    def verificar_contraseña_admin(self):
        password = simpledialog.askstring("Contraseña", "Ingrese la contraseña de administrador:", show="*")
        if password == ADMIN_PASSWORD:
            return True
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")
            return False

    def admin_login(self):
        """Función para administrar inventario, requiere autenticación de administrador."""
        if not self.verificar_contraseña_admin():
            return  # Si la contraseña es incorrecta, salimos de la función
        
        # Si la contraseña es correcta, accedemos a las opciones de administración
        subopcion = simpledialog.askstring("Administración", "¿Qué acción desea realizar?\n1. Agregar libro\n2. Eliminar libro")
        if subopcion == "1":
            self.agregar_libro()
        elif subopcion == "2":
            self.eliminar_libro()
        else:
            messagebox.showerror("Error", "Opción no válida.")
    
    def agregar_libro(self):
        id_libro = simpledialog.askinteger("Agregar libro", "Ingrese el ID del libro:")
        titulo = simpledialog.askstring("Agregar libro", "Ingrese el título del libro:")
        autor = simpledialog.askstring("Agregar libro", "Ingrese el autor del libro:")
        categoria = simpledialog.askstring("Agregar libro", "Ingrese la categoría del libro:")
        
        try:
            libro = self.biblioteca.agregar_libro(id_libro, titulo, autor, categoria)
            messagebox.showinfo("Éxito", f"Libro agregado: {libro.id} - {libro.titulo}")
        except ValueError as e:
            messagebox.showerror("Error", f"Error al agregar libro: {e}")

    def eliminar_libro(self):
        id_libro = simpledialog.askinteger("Eliminar libro", "Ingrese el ID del libro a eliminar:")
        
        try:
            self.biblioteca.eliminar_libro(id_libro)
            messagebox.showinfo("Éxito", "Libro eliminado correctamente.")
        except ValueError as e:
            messagebox.showerror("Error", f"Error al eliminar libro: {e}")

    # Funciones adicionales de búsqueda, registro de usuario, préstamo y devolución...
    def buscar_libros(self):
        pass

    def registrar_usuario(self):
        pass

    def prestar_libro(self):
        pass

    def devolver_libro(self):
        pass


# Crear la ventana principal de Tkinter
root = tk.Tk()
interfaz = InterfazBiblioteca(root)
root.mainloop()




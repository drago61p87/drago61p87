#juan david vargas 
#manuel borrero
#keider chavarria 
import unittest
from datetime import datetime
from Biblioteca import Biblioteca, Usuario, Libro, Prestamo

class TestBiblioteca(unittest.TestCase):

    def setUp(self):
        
        self.biblioteca = Biblioteca()

        
        self.usuario_1 = self.biblioteca.registrar_usuario(1, "Juan Perez")
        self.usuario_2 = self.biblioteca.registrar_usuario(2, "Ana Gomez")

        
        self.libro_1 = self.biblioteca.agregar_libro(1, "Python para Todos", "Juan Pérez", "Tecnología")
        self.libro_2 = self.biblioteca.agregar_libro(2, "Aprendiendo Java", "Ana Gómez", "Tecnología")

    def test_registrar_usuario(self):
        """ Verifica que un usuario pueda ser registrado correctamente """
        usuario = self.biblioteca.registrar_usuario(3, "Carlos Díaz")
        self.assertEqual(usuario.nombre, "Carlos Díaz")
        self.assertIn(usuario.id, self.biblioteca.usuarios)
    
    def test_prestar_libro(self):
        """ Verifica que un libro pueda ser prestado correctamente a un usuario """
        prestamo = self.biblioteca.prestar_libro(1, 1)  
        self.assertIsNotNone(prestamo)
        self.assertFalse(self.libro_1.disponible)
        self.assertIn(prestamo, self.usuario_1.prestamos)
    
    def test_no_puede_prestar_libro_sin_disponibilidad(self):
        """ Verifica que no se pueda prestar un libro si no está disponible """
        
        self.biblioteca.prestar_libro(1, 1)
        with self.assertRaises(ValueError) as context:
            self.biblioteca.prestar_libro(2, 1)  
        self.assertEqual(str(context.exception), "Libro no disponible")
    
    def test_devolver_libro(self):
        """ Verifica que un libro pueda ser devuelto correctamente """
        prestamo = self.biblioteca.prestar_libro(1, 1)
        self.biblioteca.devolver_libro(prestamo.id)
        self.assertTrue(self.libro_1.disponible)
        self.assertIsNotNone(prestamo.fecha_devolucion)
    
    def test_no_devolver_libro_ya_devuelto(self):
        """ Verifica que no se pueda devolver un libro que ya fue devuelto """
        prestamo = self.biblioteca.prestar_libro(1, 1)
        self.biblioteca.devolver_libro(prestamo.id)
        with self.assertRaises(ValueError) as context:
            self.biblioteca.devolver_libro(prestamo.id)  
        self.assertEqual(str(context.exception), "Este libro ya fue devuelto")
    
    def test_reporte_libros_solicitados(self):
        """ Verifica que el reporte de libros solicitados funcione correctamente """
        self.biblioteca.prestar_libro(1, 1)  
        self.biblioteca.prestar_libro(2, 1)  
        reporte = self.biblioteca.reporte_libros_solicitados()
        self.assertIn("Python para Todos", reporte)
        self.assertEqual(reporte["Python para Todos"], 2)
    
    def test_reporte_usuarios_activos(self):
        """ Verifica que el reporte de usuarios activos funcione correctamente """
        self.biblioteca.prestar_libro(1, 1)  
        reporte = self.biblioteca.reporte_usuarios_activos()
        self.assertIn("Juan Perez", reporte)
        self.assertEqual(reporte["Juan Perez"], 1)

    def test_limite_prestamos_usuario(self):
        """ Verifica que un usuario no pueda tomar más de 3 libros prestados """
        self.biblioteca.prestar_libro(1, 1)  
        self.biblioteca.prestar_libro(1, 2)  
        with self.assertRaises(ValueError) as context:
            self.biblioteca.prestar_libro(1, 3)  
        self.assertEqual(str(context.exception), "El usuario ha alcanzado el límite de 3 libros")
    
    def test_agregar_libro(self):
        """ Verifica que un libro pueda ser agregado correctamente """
        libro = self.biblioteca.agregar_libro(3, "Curso de C++", "Carlos Ruiz", "Tecnología")
        self.assertEqual(libro.titulo, "Curso de C++")
        self.assertIn(libro.id, self.biblioteca.libros)

    def test_eliminar_libro(self):
        """ Verifica que un libro pueda ser eliminado correctamente """
        self.biblioteca.eliminar_libro(2)
        self.assertNotIn(2, self.biblioteca.libros)

    def test_eliminar_libro_prestado(self):
        """ Verifica que no se pueda eliminar un libro prestado """
        self.biblioteca.prestar_libro(1, 1)  
        with self.assertRaises(ValueError) as context:
            self.biblioteca.eliminar_libro(1)  
        self.assertEqual(str(context.exception), "No se puede eliminar un libro prestado")
    
if __name__ == '__main__':
    unittest.main()

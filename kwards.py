import unittest
def buscar_datos(*args, **kwargs):
  for arg in args:
        for key, value in kwargs.items():
            for k, v in value.items():
                if arg == v:
                    return True
        return False

database = {
    "persona1": {"primer_nombre": "Rene","segundo_nombre": "Geronimo","primer_apellido": "Favaloro","segundo_apellido": ""},
    "persona2": {"primer_nombre": "Robert","segundo_nombre": "John","primer_apellido": "Downey","segundo_apellido": "Jr"},
    "persona3": {"primer_nombre": "Valentin","segundo_nombre": "","primer_apellido": "Barzola","segundo_apellido": "Vilela"},
    "persona4": {"primer_nombre": "Marcos","segundo_nombre": "","primer_apellido": "Galperin","segundo_apellido": ""}


}

resultado= buscar_datos("Rene", "Geronimo", "Favaloro", **database)
resultado=buscar_datos("Robert", "Downey", "John", "Jr", **database)
resultado=buscar_datos("Valentin", "Barzola", "Vilela", **database)
resultado=buscar_datos("Marcos", "Galperin", **database)



class test_busqueda(unittest.TestCase):
    
    def test_0(self):
        resultado = buscar_datos("Valentin", "Barzola", "Vilela", **database)
        self.assertEqual(resultado, True)
    def test_1(self):
        resultado = buscar_datos("Marcos", "Galperin", **database)
        self.assertEqual(resultado, True)
    def test_2(self):
        resultado = buscar_datos("Robert", "Downey", "John", "Jr", **database)
        self.assertEqual(resultado, True)
    def test_3(self):
        resultado = buscar_datos("Rene", "Geronimo", "Favaloro", **database)
        self.assertEqual(resultado, True)
    def test_4(self):
        resultado = buscar_datos("michael", "jackson", **database)
        self.assertEqual(resultado, False)


unittest.main()
import unittest
from Examen2 import MiClase


class TestMiClase(unittest.TestCase):

    def setUp(self):
        self.obj = MiClase(
            Valencia=5,
            Tempo=120,
            Tonos=12,
            listaCanciones=["Canción 1", "Canción 2", "Canción 3"],
            listaBailabilidad=[0.8, 0.9, 0.7]
        )

    # ---------- ObtieneValencia ----------

    def test_obtiene_valencia_numero_mixto(self):
        self.assertEqual(self.obj.ObtieneValencia(1234567), 4)

    def test_obtiene_valencia_valor_no_numerico_lanza_value_error(self):
        with self.assertRaises(ValueError):
            self.obj.ObtieneValencia("12a3")

    def test_obtiene_valencia_valor_cero(self):
        self.assertEqual(self.obj.ObtieneValencia(0), 0)

    def test_obtiene_valencia_numero_sin_par_puro(self):
        self.assertEqual(self.obj.ObtieneValencia(2468), 0)
    
    # ---------- DivisibleTempo ----------

    def test_divisible_tempo_numero_compuesto(self):
        self.assertEqual(self.obj.DivisibleTempo(12), [1, 2, 3, 4, 6, 12])

    def test_divisible_tempo_tipo_invalido_lanza_type_error(self):
        with self.assertRaises(TypeError):
            self.obj.DivisibleTempo("abc")

    def test_divisible_tempo_entrada_cero(self):
        self.assertEqual(self.obj.DivisibleTempo(0), [])

    def test_divisible_tempo_entrada_vacia_lanza_type_error(self):
        with self.assertRaises(TypeError):
            self.obj.DivisibleTempo(None)

    # ---------- ObtieneMasBailable ----------

    def test_obtiene_mas_bailable_lista_normal(self):
        self.assertEqual(
            self.obj.ObtieneMasBailable([0.8, 0.9, 0.7]),
            0.9
        )

    def test_obtiene_mas_bailable_lista_vacia_devuelve_none(self):
        self.assertIsNone(self.obj.ObtieneMasBailable([]))

    def test_obtiene_mas_bailable_valores_no_numericos_lanza_type_error(self):
        with self.assertRaises(TypeError):
            self.obj.ObtieneMasBailable([0.8, "a", 0.7])    

    def test_obtiene_mas_bailable_todos_iguales(self):
        self.assertEqual(
            self.obj.ObtieneMasBailable([0.8, 0.8, 0.8]),
            0.8
        )

    # ---------- VerificaListaCanciones ----------

    def test_verifica_lista_canciones_todas_validas(self):
        self.assertTrue(
            self.obj.VerificaListaCanciones(
                ["Canción 1", "Canción 2", "Canción 3"]
            )
        )

    def test_verifica_lista_canciones_con_none(self):
        self.assertFalse(
            self.obj.VerificaListaCanciones(
                ["Canción 1", None, "Canción 3"]
            )
        )

    def test_verifica_que_sea_lista(self):
        self.assertIsInstance(
            self.obj.listaCanciones,
            list
        )

    def test_verifica_lista_vacia(self):
        self.assertTrue(
            self.obj.VerificaListaCanciones([])
    )

if __name__ == "__main__":
    unittest.main()

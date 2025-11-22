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

    # ---------- DivisibleTempo ----------

    def test_divisible_tempo_numero_compuesto(self):
        self.assertEqual(self.obj.DivisibleTempo(12), [1, 2, 3, 4, 6, 12])

    def test_divisible_tempo_tipo_invalido_lanza_type_error(self):
        with self.assertRaises(TypeError):
            self.obj.DivisibleTempo("abc")

    # ---------- ObtieneMasBailable ----------

    def test_obtiene_mas_bailable_lista_normal(self):
        self.assertEqual(
            self.obj.ObtieneMasBailable([0.8, 0.9, 0.7]),
            0.9
        )

    def test_obtiene_mas_bailable_lista_vacia_devuelve_none(self):
        self.assertIsNone(self.obj.ObtieneMasBailable([]))

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


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest import TestCase
from periodos import *
from datetime import date

# Para rodar os testes: python test.py

class TestPeriodosRetriever(TestCase):

    def test_get_um_periodo_quadrienio_federal(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2004, 7, 1)
        data_final = date(2006, 7, 1)
        periodos = periodos_retriever.get_periodos(FEDERAL, QUADRIENIO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(2003, 1, 1), date(2006, 12, 31))])

    def test_get_outro_periodo_quadrienio_federal(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2000, 7, 1)
        data_final = date(2001, 7, 1)
        periodos = periodos_retriever.get_periodos(FEDERAL, QUADRIENIO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(1999, 1, 1), date(2002, 12, 31))])

    def test_get_um_periodo_quadrienio_estadual(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2000, 7, 1)
        data_final = date(2001, 7, 1)
        periodos = periodos_retriever.get_periodos(ESTADUAL, QUADRIENIO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(1999, 1, 1), date(2002, 12, 31))])

    def test_get_um_periodo_quadrienio_municipal(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2002, 7, 1)
        data_final = date(2003, 7, 1)
        periodos = periodos_retriever.get_periodos(MUNICIPAL, QUADRIENIO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(2001, 1, 1), date(2004, 12, 31))])

    def test_get_um_periodo_bienio_federal(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2004, 7, 1)
        data_final = date(2004, 11, 1)
        periodos = periodos_retriever.get_periodos(FEDERAL, BIENIO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(2003, 1, 1), date(2004, 12, 31))])

    def test_get_outro_periodo_bienio_federal(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2005, 7, 1)
        data_final = date(2005, 11, 1)
        periodos = periodos_retriever.get_periodos(FEDERAL, BIENIO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(2005, 1, 1), date(2006, 12, 31))])

    def test_get_um_periodo_ano_federal(self):
        periodos_retriever = PeriodosRetriever()
        data_inicial = date(2004, 7, 1)
        data_final = date(2004, 11, 1)
        periodos = periodos_retriever.get_periodos(FEDERAL, ANO, data_inicial, data_final)
        self.assertEqual(periodos, [(date(2004, 1, 1), date(2004, 12, 31))])

if __name__ == '__main__':
    unittest.main()

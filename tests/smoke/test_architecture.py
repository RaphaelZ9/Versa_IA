"""
Smoke Test da Arquitetura Versa AI

Objetivo:
Verificar rapidamente se todos os componentes principais da arquitetura
podem ser importados e instanciados sem erros.

Este teste NÃO valida regras de negócio.
Ele apenas garante que a arquitetura permanece íntegra.

Autor: Versa AI
"""

import unittest


class TestArchitecture(unittest.TestCase):

    def test_kernel(self):
        from app.core.kernel import VersaKernel

        kernel = VersaKernel()

        self.assertIsNotNone(kernel)

    def test_versa_ai(self):
        from app.versa_ai import VersaAI

        ai = VersaAI()

        self.assertIsNotNone(ai)


if __name__ == "__main__":
    unittest.main()
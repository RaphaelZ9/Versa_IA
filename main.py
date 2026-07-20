from app.versa_ai import VersaAI
from app.core.config import Config


def banner():

    print("\n" + "═" * 60)
    print(f"🤖 {Config.APP_NAME}")
    print(f"Versão : {Config.VERSION}")
    print("Status  : 🟢 Online")
    print("═" * 60)
    print("Digite 'limpar' para limpar a tela.")
    print("Digite 'sair' para encerrar.")
    print()


def main():

    ia = VersaAI()

    ia.initialize()

    banner()

    while True:

        mensagem = input("Você: ").strip()

        if not mensagem:
            continue

        comando = mensagem.lower()

        if comando == "sair":
            break

        if comando == "limpar":
            print("\n" * 50)
            banner()
            continue

        try:
            resposta = ia.chat(mensagem)
            print("\nVersa:")
            print(resposta.content)
            print()

        except Exception as erro:
            print("\nVersa: Ocorreu um erro ao processar sua solicitação.")
            print(f"Detalhes: {erro}\n")

    ia.shutdown()

    print("\nAté logo! 👋\n")


if __name__ == "__main__":
    main()
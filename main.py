import time


# ==============================
# CORES DO TERMINAL
# ==============================

VERMELHO = "\033[31m"
AMARELO = "\033[33m"
VERDE = "\033[32m"
RESET = "\033[0m"


# ==============================
# FUNÇÕES AUXILIARES
# ==============================

def contagem(segundos):
    """Realiza uma contagem regressiva no terminal."""
    for i in range(segundos, 0, -1):
        print(f"⏱️  Mudança em: {i}s")
        time.sleep(1)


def exibir_sinal(icone, cor, titulo, mensagem):
    """Exibe o estado atual de um sinal."""
    print(f"\n{icone} {titulo}")
    print(f"{cor}{mensagem}{RESET}")


def sinal_rua(nome, cor, estado, mensagem):
    """Exibe o estado de uma rua."""
    print(f"\n🚗 {nome}: {estado}")
    print(f"{cor}{nome}: {mensagem}{RESET}")


def sinal_pedestres(cor, estado, mensagem):
    """Exibe o estado do sinal de pedestres."""
    print(f"\n🚶 Pedestres: {estado}")
    print(f"{cor}Pedestres: {mensagem}{RESET}")


# ==============================
# CICLO DO SEMÁFORO
# ==============================

def ciclo_semaforo():
    """Executa um ciclo completo da simulação."""

    # ------------------------------
    # FASE 1 - RUA A VERDE
    # ------------------------------

    sinal_rua(
        "Rua A",
        VERDE,
        "🟢 VERDE",
        "Sinal aberto. Continue!"
    )

    sinal_rua(
        "Rua B",
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado! Pare."
    )

    sinal_pedestres(
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado. Aguarde!"
    )

    contagem(5)

    # ------------------------------
    # FASE 2 - RUA A AMARELO
    # ------------------------------

    sinal_rua(
        "Rua A",
        AMARELO,
        "🟡 AMARELO",
        "Atenção! O sinal vai fechar!"
    )

    sinal_rua(
        "Rua B",
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado! Pare."
    )

    sinal_pedestres(
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado. Aguarde!"
    )

    contagem(5)

    # ------------------------------
    # FASE 3 - PEDESTRES VERDE
    # ------------------------------

    sinal_rua(
        "Rua A",
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado! Pare."
    )

    sinal_rua(
        "Rua B",
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado! Pare."
    )

    sinal_pedestres(
        VERDE,
        "🟢 VERDE",
        "O sinal está aberto. Atravesse!"
    )

    contagem(5)

    # ------------------------------
    # FASE 4 - RUA B VERDE
    # ------------------------------

    sinal_rua(
        "Rua A",
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado! Pare."
    )

    sinal_rua(
        "Rua B",
        VERDE,
        "🟢 VERDE",
        "Sinal aberto. Continue!"
    )

    sinal_pedestres(
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado. Aguarde!"
    )

    contagem(5)

    # ------------------------------
    # FASE 5 - RUA B AMARELO
    # ------------------------------

    sinal_rua(
        "Rua A",
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado! Pare."
    )

    sinal_rua(
        "Rua B",
        AMARELO,
        "🟡 AMARELO",
        "Atenção! O sinal vai fechar!"
    )

    sinal_pedestres(
        VERMELHO,
        "🔴 VERMELHO",
        "O sinal está fechado. Aguarde!"
    )

    contagem(5)


# ==============================
# PROGRAMA PRINCIPAL
# ==============================

def main():
    """Inicia a simulação do semáforo."""

    print("=" * 45)
    print("🚦 SIMULADOR DE SEMÁFORO")
    print("=" * 45)

    while True:

        ciclo_semaforo()

        resposta = input(
            "\nDeseja continuar a simulação? (s/n): "
        ).lower()

        if resposta != "s":
            print("\n🛑 Simulação encerrada.")
            print("Obrigado por utilizar o simulador! 🚦")
            break


if __name__ == "__main__":
    main()
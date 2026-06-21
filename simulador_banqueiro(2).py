"""
Simulador do Algoritmo do Banqueiro
Disciplina: Sistemas Operacionais
"""

def separador(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)


def exibir_estado(alocacao, necessidade, disponivel, processos, recursos):
    """Exibe as matrizes do estado atual do sistema."""
    print(f"\n  {'Processo':<12}", end="")
    print(f"{'Alocacao':<{len(recursos)*6}}  ", end="")
    print(f"{'Necessidade':<{len(recursos)*6}}  ", end="")
    print(f"Disponivel")

    header_rec = "  " + " ".join(f"{r:<5}" for r in recursos)
    print(f"\n  {'':12}", end="")
    print("  ".join(f"{r:<5}" for r in recursos), end="  ")
    print("  ", end="")
    print("  ".join(f"{r:<5}" for r in recursos), end="  ")
    print("  ".join(f"{r:<5}" for r in recursos))
    print(f"  {'-'*70}")

    for i, p in enumerate(processos):
        aloc_str = "  ".join(f"{alocacao[i][j]:<5}" for j in range(len(recursos)))
        nec_str  = "  ".join(f"{necessidade[i][j]:<5}" for j in range(len(recursos)))
        if i == 0:
            disp_str = "  ".join(f"{disponivel[j]:<5}" for j in range(len(recursos)))
        else:
            disp_str = ""
        print(f"  {p:<12}{aloc_str}  {nec_str}  {disp_str}")


def verificar_seguro(alocacao, necessidade, disponivel, processos, recursos):
    """Algoritmo de verificação de estado seguro. Retorna (seguro, sequencia)."""
    n = len(processos)
    r = len(recursos)

    work      = disponivel[:]
    finish    = [False] * n
    sequencia = []

    while len(sequencia) < n:
        progresso = False
        for i in range(n):
            if not finish[i]:
                # verifica se necessidade[i] <= work
                if all(necessidade[i][j] <= work[j] for j in range(r)):
                    # simula liberação dos recursos
                    for j in range(r):
                        work[j] += alocacao[i][j]
                    finish[i]  = True
                    sequencia.append(processos[i])
                    progresso  = True
        if not progresso:
            break

    seguro = all(finish)
    return seguro, sequencia


#  ENTRADA
def ler_entrada():
    separador("SIMULADOR DO ALGORITMO DO BANQUEIRO")
    print("\n  Pressione ENTER para usar o exemplo padrão ou digite seus valores.\n")

    # Número de processos e recursos
    entrada = input("  Número de processos [padrão: 5]: ").strip()
    n = int(entrada) if entrada else 5

    entrada = input("  Número de tipos de recursos [padrão: 3]: ").strip()
    r = int(entrada) if entrada else 3

    processos = [f"P{i}" for i in range(n)]
    recursos  = [chr(65 + i) for i in range(r)]  # A, B, C...

    print(f"\n  Processos : {processos}")
    print(f"  Recursos  : {recursos}")

    # Recursos disponíveis
    print(f"\n  Digite o vetor de recursos DISPONÍVEIS ({r} valores separados por espaço)")
    while True:
        entrada = input(f"  [padrao: 3 3 2]: ").strip()
        if not entrada:
            disponivel = [3, 3, 2]
            break
        vals = list(map(int, entrada.split()))
        if len(vals) != r:
            print(f"  AVISO: esperado {r} valores, recebido {len(vals)}. Tente novamente.")
            continue
        disponivel = vals
        break

    # Matriz de alocacao
    print(f"\n  Digite a matriz de ALOCACAO ({n} linhas, {r} valores cada):")
    import random; random.seed(42); alocacao_padrao = [[random.randint(0,3) for _ in range(r)] for _ in range(n)]
    alocacao = []
    for i in range(n):
        while True:
            entrada = input(f"  {processos[i]} [padrao: {' '.join(map(str, alocacao_padrao[i]))}]: ").strip()
            if not entrada:
                alocacao.append(alocacao_padrao[i][:r])
                break
            vals = list(map(int, entrada.split()))
            if len(vals) != r:
                print(f"  AVISO: esperado {r} valores, recebido {len(vals)}. Tente novamente.")
                continue
            alocacao.append(vals)
            break

    # Matriz de necessidade maxima
    print(f"\n  Digite a matriz de NECESSIDADE MAXIMA ({n} linhas, {r} valores cada):")
    nec_padrao = [[alocacao_padrao[i][j] + random.randint(0,4) for j in range(r)] for i in range(n)]
    necessidade = []
    for i in range(n):
        while True:
            entrada = input(f"  {processos[i]} [padrao: {' '.join(map(str, nec_padrao[i]))}]: ").strip()
            if not entrada:
                necessidade.append(nec_padrao[i][:r])
                break
            vals = list(map(int, entrada.split()))
            if len(vals) != r:
                print(f"  AVISO: esperado {r} valores, recebido {len(vals)}. Tente novamente.")
                continue
            necessidade.append(vals)
            break
    return processos, recursos, disponivel, alocacao, necessidade


# MAIN
def main():
    processos, recursos, disponivel, alocacao, necessidade = ler_entrada()

    # Estado inicial
    separador("ESTADO INICIAL DO SISTEMA")
    exibir_estado(alocacao, necessidade, disponivel, processos, recursos)

    # Verificação inicial
    seguro, sequencia = verificar_seguro(alocacao, necessidade, disponivel, processos, recursos)

    separador("VERIFICAÇÃO DE ESTADO SEGURO")
    if seguro:
        print(f"\n  Estado: SEGURO ✓")
        print(f"  Sequência segura: {' → '.join(sequencia)}")
    else:
        print(f"\n  Estado: INSEGURO ✗")
        print(f"  Não existe sequência segura com os recursos disponíveis.")
        return

    # Loop de requisições
    while True:
        separador("NOVA REQUISIÇÃO DE RECURSOS")
        print(f"\n  Processos disponíveis: {processos}")
        print(f"  Digite 'sair' para encerrar.\n")

        proc_input = input("  Processo solicitante: ").strip().upper()
        if proc_input.lower() == "sair":
            print("\n  Simulação encerrada.\n")
            break

        if proc_input not in processos:
            print(f"\n  Processo '{proc_input}' não encontrado.")
            continue

        pi = processos.index(proc_input)

        entrada = input(f"  Recursos solicitados por {proc_input} ({len(recursos)} valores): ").strip()
        try:
            requisicao = list(map(int, entrada.split()))
        except ValueError:
            print("\n  Entrada inválida.")
            continue

        print(f"\n  Requisição de {proc_input}: {requisicao}")

        # Passo 1: requisição <= necessidade?
        if any(requisicao[j] > necessidade[pi][j] for j in range(len(recursos))):
            print("\n  NEGADA ✗ — processo solicitou mais do que sua necessidade máxima declarada.")
            continue

        # Passo 2: requisição <= disponível?
        if any(requisicao[j] > disponivel[j] for j in range(len(recursos))):
            print("\n  NEGADA ✗ — recursos insuficientes no momento. Processo deve aguardar.")
            continue

        # Passo 3: simula a concessão
        for j in range(len(recursos)):
            disponivel[j]      -= requisicao[j]
            alocacao[pi][j]    += requisicao[j]
            necessidade[pi][j] -= requisicao[j]

        # Verifica se o novo estado é seguro
        seguro, sequencia = verificar_seguro(alocacao, necessidade, disponivel, processos, recursos)

        if seguro:
            print(f"\n  CONCEDIDA ✓ — estado permanece SEGURO.")
            print(f"  Sequência segura: {' → '.join(sequencia)}")
            separador("ESTADO ATUALIZADO")
            exibir_estado(alocacao, necessidade, disponivel, processos, recursos)
        else:
            # Reverte a concessão
            for j in range(len(recursos)):
                disponivel[j]      += requisicao[j]
                alocacao[pi][j]    -= requisicao[j]
                necessidade[pi][j] += requisicao[j]
            print(f"\n  NEGADA ✗ — concessão levaria a estado INSEGURO. Recursos não alocados.")


if __name__ == "__main__":
    main()

"""
Simulador de Escalonamento de Braço de Disco
Algoritmos: FCFS, SSTF, SCAN (Elevador)
Disciplina: Sistemas Operacionais
"""

def separador(titulo):
    print("\n" + "=" * 55)
    print(f"  {titulo}")
    print("=" * 55)


def mostrar_movimento(ordem, posicao_inicial):
    """Exibe o passo a passo dos movimentos do braço."""
    posicao = posicao_inicial
    total = 0
    print(f"\n  Posição inicial: {posicao}")
    print(f"  {'Passo':<6} {'De':<8} {'Para':<8} {'Deslocamento'}")
    print(f"  {'-'*40}")
    for i, destino in enumerate(ordem, 1):
        deslocamento = abs(destino - posicao)
        total += deslocamento
        print(f"  {i:<6} {posicao:<8} {destino:<8} {deslocamento}")
        posicao = destino
    print(f"  {'-'*40}")
    print(f"  Total de cilindros percorridos: {total}")
    return total


# ─── FCFS ────────────────────────────────────────────────
def fcfs(posicao_inicial, requisicoes):
    """First Come, First Served: atende na ordem de chegada."""
    separador("FCFS — First Come, First Served")
    print(f"\n  Fila de requisições: {requisicoes}")
    print("\n  Lógica: atende cada requisição na ordem em que chegou.")
    total = mostrar_movimento(requisicoes, posicao_inicial)
    return total


# ─── SSTF ────────────────────────────────────────────────
def sstf(posicao_inicial, requisicoes):
    """Shortest Seek Time First: sempre vai para o cilindro mais próximo."""
    separador("SSTF — Shortest Seek Time First")
    print(f"\n  Fila de requisições: {requisicoes}")
    print("\n  Lógica: a cada passo, escolhe o cilindro mais próximo da posição atual.")

    pendentes = requisicoes.copy()
    posicao = posicao_inicial
    ordem = []

    while pendentes:
        mais_proximo = min(pendentes, key=lambda x: abs(x - posicao))
        ordem.append(mais_proximo)
        pendentes.remove(mais_proximo)
        posicao = mais_proximo

    total = mostrar_movimento(ordem, posicao_inicial)
    print(f"\n  Ordem de atendimento: {ordem}")
    return total


# ─── SCAN ────────────────────────────────────────────────
def scan(posicao_inicial, requisicoes, direcao="crescente", max_cilindro=199):
    """
    SCAN (Elevador): o braço se move em uma direção atendendo requisições;
    ao chegar no fim, inverte o sentido.
    direcao: 'crescente' (sobe) ou 'decrescente' (desce)
    """
    separador("SCAN — Algoritmo do Elevador")
    print(f"\n  Fila de requisições : {requisicoes}")
    print(f"  Direção inicial     : {direcao}")
    print(f"  Cilindro máximo     : {max_cilindro}")
    print("\n  Lógica: o braço percorre numa direção atendendo tudo que encontra;")
    print("  ao chegar no extremo, inverte e varre no sentido contrário.")

    pendentes = sorted(requisicoes)
    menores = [c for c in pendentes if c < posicao_inicial]
    maiores = [c for c in pendentes if c >= posicao_inicial]
    ordem = []

    if direcao == "crescente":
        ordem += maiores          # sobe atendendo os maiores
        ordem += menores[::-1]    # desce atendendo os menores (de volta)
    else:
        ordem += menores[::-1]    # desce atendendo os menores
        ordem += maiores          # sobe atendendo os maiores

    total = mostrar_movimento(ordem, posicao_inicial)
    print(f"\n  Ordem de atendimento: {ordem}")
    return total


# ─── COMPARATIVO ─────────────────────────────────────────
def comparativo(resultados):
    separador("COMPARATIVO FINAL")
    print(f"\n  {'Algoritmo':<10} {'Cilindros Percorridos':<25} {'Eficiência'}")
    print(f"  {'-'*50}")
    minimo = min(resultados.values())
    for alg, total in resultados.items():
        destaque = " ← MAIS EFICIENTE" if total == minimo else ""
        print(f"  {alg:<10} {total:<25} {destaque}")


# ─── ENTRADA DO USUÁRIO ──────────────────────────────────
def ler_entrada():
    print("\n" + "=" * 55)
    print("  SIMULADOR DE ESCALONAMENTO DE BRAÇO DE DISCO")
    print("=" * 55)
    print("\n  Pressione ENTER para usar o exemplo padrão")
    print("  ou digite seus próprios valores.\n")

    entrada = input("  Posição inicial do braço [padrão: 53]: ").strip()
    posicao_inicial = int(entrada) if entrada else 53

    entrada = input("  Fila de requisições [padrão: 98 183 37 122 14 124 65 67]: ").strip()
    if entrada:
        requisicoes = list(map(int, entrada.split()))
    else:
        requisicoes = [98, 183, 37, 122, 14, 124, 65, 67]

    entrada = input("  Cilindro máximo do disco [padrão: 199]: ").strip()
    max_cilindro = int(entrada) if entrada else 199

    entrada = input("  Direção inicial do SCAN (crescente/decrescente) [padrão: crescente]: ").strip().lower()
    if "decr" in entrada or entrada in ("d", "dec", "decrescente"):
        direcao = "decrescente"
    else:
        direcao = "crescente"

    # Validação: remover requisições fora do intervalo do disco
    invalidas = [c for c in requisicoes if c < 0 or c > max_cilindro]
    if invalidas:
        print(f"\n  AVISO: As seguintes requisições estão fora do disco (0–{max_cilindro}) e serão ignoradas: {invalidas}")
        requisicoes = [c for c in requisicoes if 0 <= c <= max_cilindro]
        print(f"  Requisições válidas: {requisicoes}")

    return posicao_inicial, requisicoes, max_cilindro, direcao


# ─── MAIN ─────────────────────────────────────────────────
def main():
    posicao_inicial, requisicoes, max_cilindro, direcao = ler_entrada()

    resultados = {}
    resultados["FCFS"] = fcfs(posicao_inicial, requisicoes)
    resultados["SSTF"] = sstf(posicao_inicial, requisicoes)
    resultados["SCAN"] = scan(posicao_inicial, requisicoes, direcao, max_cilindro)

    comparativo(resultados)
    print("\n")


if __name__ == "__main__":
    main()

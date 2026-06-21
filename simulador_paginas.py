"""
Simulador de Substituição de Páginas
Algoritmos: FIFO e LRU
Disciplina: Sistemas Operacionais
"""

def separador(titulo):
    print("\n" + "=" * 55)
    print(f"  {titulo}")
    print("=" * 55)


# FIFO
def fifo(referencias, num_frames):
    """First In, First Out: substitui a página que entrou há mais tempo."""
    separador("FIFO — First In, First Out")
    print(f"\n  Sequência de referências : {referencias}")
    print(f"  Número de frames         : {num_frames}")
    print("\n  Lógica: a página que está há mais tempo na memória é substituída primeiro.")

    frames    = []   # páginas na memória (fila)
    faults    = 0
    print(f"\n  {'Ref':<6} {'Frames':<30} {'Fault?'}")
    print(f"  {'-'*44}")

    for ref in referencias:
        fault = False
        if ref not in frames:
            fault  = True
            faults += 1
            if len(frames) < num_frames:
                frames.append(ref)
            else:
                frames.pop(0)        # remove o mais antigo (primeiro da fila)
                frames.append(ref)

        frames_str = str(frames).ljust(28)
        print(f"  {ref:<6} {frames_str}  {'PAGE FAULT' if fault else '-'}")

    print(f"\n  Total de page faults: {faults}")
    return faults


#  LRU
def lru(referencias, num_frames):
    """Least Recently Used: substitui a página usada há mais tempo."""
    separador("LRU — Least Recently Used")
    print(f"\n  Sequência de referências : {referencias}")
    print(f"  Número de frames         : {num_frames}")
    print("\n  Lógica: a página que não é usada há mais tempo é a próxima a sair.")

    frames = []   # páginas na memória
    faults = 0
    print(f"\n  {'Ref':<6} {'Frames':<30} {'Fault?'}")
    print(f"  {'-'*44}")

    for ref in referencias:
        fault = False
        if ref not in frames:
            fault  = True
            faults += 1
            if len(frames) < num_frames:
                frames.append(ref)
            else:
                frames.pop(0)        # remove o menos recentemente usado (primeiro)
                frames.append(ref)
        else:
            # move para o final (marca como recentemente usado)
            frames.remove(ref)
            frames.append(ref)

        frames_str = str(frames).ljust(28)
        print(f"  {ref:<6} {frames_str}  {'PAGE FAULT' if fault else '-'}")

    print(f"\n  Total de page faults: {faults}")
    return faults


#  COMPARATIVO
def comparativo(resultados):
    separador("COMPARATIVO FINAL")
    print(f"\n  {'Algoritmo':<10} {'Page Faults':<20} {'Eficiência'}")
    print(f"  {'-'*45}")
    minimo = min(resultados.values())
    for alg, faults in resultados.items():
        destaque = " ← MENOS PAGE FAULTS" if faults == minimo else ""
        print(f"  {alg:<10} {faults:<20} {destaque}")


# ENTRADA DO USUÁRIO
def ler_entrada():
    print("\n" + "=" * 55)
    print("  SIMULADOR DE SUBSTITUIÇÃO DE PÁGINAS")
    print("=" * 55)
    print("\n  Pressione ENTER para usar o exemplo padrão")
    print("  ou digite seus próprios valores.\n")

    entrada = input("  Sequência de referências [padrão: 1 2 3 4 1 2 5 1 2 3 4 5]: ").strip()
    if entrada:
        referencias = list(map(int, entrada.split()))
    else:
        referencias = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

    entrada = input("  Número de frames da RAM [padrão: 3]: ").strip()
    num_frames = int(entrada) if entrada else 3

    return referencias, num_frames


#  MAIN
def main():
    referencias, num_frames = ler_entrada()

    resultados = {}
    resultados["FIFO"] = fifo(referencias, num_frames)
    resultados["LRU"]  = lru(referencias, num_frames)

    comparativo(resultados)
    print("\n")


if __name__ == "__main__":
    main()

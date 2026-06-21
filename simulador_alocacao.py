"""
Simulador de Alocação de Blocos no Disco
Algoritmos: Contígua, Encadeada e Indexada (i-nodes)
Disciplina: Sistemas Operacionais
"""

def separador(titulo):
    print("\n" + "=" * 60)
    print(f"  {titulo}")
    print("=" * 60)


def exibir_mapa(disco, num_blocos):
    """Exibe o mapa visual do disco."""
    print("\n  Mapa do disco:")
    print("  ", end="")
    for i in range(num_blocos):
        bloco = disco[i] if disco[i] else " "
        print(f"[{bloco:^3}]", end="")
        if (i + 1) % 10 == 0:
            print("\n  ", end="")
    print()


def blocos_livres(disco):
    return [i for i, b in enumerate(disco) if b is None]


# ─── CONTÍGUA ────────────────────────────────────────────
def alocacao_contigua(arquivos, num_blocos):
    """Aloca blocos contíguos para cada arquivo."""
    separador("ALOCAÇÃO CONTÍGUA")
    print("\n  Lógica: cada arquivo ocupa um bloco contínuo de posições no disco.")
    print("  Vantagem: acesso direto rápido.")
    print("  Desvantagem: fragmentação externa e dificuldade de crescimento.\n")

    disco = [None] * num_blocos
    tabela = {}  # nome -> (inicio, tamanho)

    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for idx, (nome, tamanho) in enumerate(arquivos):
        letra = letras[idx % len(letras)]
        # busca sequência contígua livre
        inicio = None
        for i in range(num_blocos - tamanho + 1):
            if all(disco[i + j] is None for j in range(tamanho)):
                inicio = i
                break

        if inicio is None:
            print(f"  ERRO: sem espaço contíguo para '{nome}' ({tamanho} blocos).")
            continue

        for j in range(tamanho):
            disco[inicio + j] = letra

        tabela[nome] = (inicio, tamanho)
        print(f"  '{nome}': blocos {inicio} a {inicio + tamanho - 1} ({tamanho} blocos)")

    exibir_mapa(disco, num_blocos)

    print(f"\n  {'Arquivo':<12} {'Início':<10} {'Tamanho':<10} {'Blocos'}")
    print(f"  {'-'*45}")
    for nome, (inicio, tam) in tabela.items():
        blocos = list(range(inicio, inicio + tam))
        print(f"  {nome:<12} {inicio:<10} {tam:<10} {blocos}")

    livres = blocos_livres(disco)
    print(f"\n  Blocos livres ({len(livres)}): {livres}")
    return disco


# ─── ENCADEADA ───────────────────────────────────────────
def alocacao_encadeada(arquivos, num_blocos):
    """Cada bloco aponta para o próximo (lista encadeada)."""
    separador("ALOCAÇÃO ENCADEADA")
    print("\n  Lógica: cada bloco contém um ponteiro para o próximo bloco do arquivo.")
    print("  Vantagem: sem fragmentação externa, usa blocos espalhados.")
    print("  Desvantagem: acesso sequencial lento, overhead de ponteiros.\n")

    disco  = [None] * num_blocos
    cadeia = {}  # bloco -> próximo bloco (-1 = fim)
    tabela = {}  # nome -> (inicio, lista de blocos)

    livres_atuais = list(range(num_blocos))

    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for fi, (nome, tamanho) in enumerate(arquivos):
        letra = letras[fi % len(letras)]
        if len(livres_atuais) < tamanho:
            print(f"  ERRO: sem blocos livres para '{nome}' ({tamanho} blocos).")
            continue

        blocos_arq = livres_atuais[:tamanho]
        livres_atuais = livres_atuais[tamanho:]

        for idx, bloco in enumerate(blocos_arq):
            disco[bloco] = letra
            cadeia[bloco] = blocos_arq[idx + 1] if idx + 1 < tamanho else -1

        tabela[nome] = (blocos_arq[0], blocos_arq)
        print(f"  '{nome}': início={blocos_arq[0]}, blocos={blocos_arq}")

    exibir_mapa(disco, num_blocos)

    print(f"\n  {'Arquivo':<12} {'Início':<10} {'Blocos (cadeia)'}")
    print(f"  {'-'*50}")
    for nome, (inicio, blocos) in tabela.items():
        cadeia_str = " → ".join(str(b) for b in blocos) + " → FIM"
        print(f"  {nome:<12} {inicio:<10} {cadeia_str}")

    livres = blocos_livres(disco)
    print(f"\n  Blocos livres ({len(livres)}): {livres}")
    return disco


# ─── INDEXADA ────────────────────────────────────────────
def alocacao_indexada(arquivos, num_blocos):
    """Cada arquivo tem um bloco índice (i-node) com a lista de blocos."""
    separador("ALOCAÇÃO INDEXADA (i-nodes)")
    print("\n  Lógica: um bloco especial (i-node) armazena os endereços de todos os blocos do arquivo.")
    print("  Vantagem: acesso direto sem fragmentação externa.")
    print("  Desvantagem: overhead do bloco índice por arquivo.\n")

    disco  = [None] * num_blocos
    tabela = {}  # nome -> (bloco_indice, blocos_dados)

    livres_atuais = list(range(num_blocos))

    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for fi, (nome, tamanho) in enumerate(arquivos):
        letra = letras[fi % len(letras)]
        # precisa de tamanho + 1 blocos (1 para o i-node)
        if len(livres_atuais) < tamanho + 1:
            print(f"  ERRO: sem blocos livres para '{nome}' ({tamanho + 1} blocos necessários).")
            continue

        bloco_indice  = livres_atuais[0]
        blocos_dados  = livres_atuais[1:tamanho + 1]
        livres_atuais = livres_atuais[tamanho + 1:]

        disco[bloco_indice] = "I"   # I = i-node
        for b in blocos_dados:
            disco[b] = letra

        tabela[nome] = (bloco_indice, blocos_dados)
        print(f"  '{nome}': i-node={bloco_indice}, dados={blocos_dados}")

    exibir_mapa(disco, num_blocos)

    print(f"\n  {'Arquivo':<12} {'i-node':<10} {'Blocos de dados'}")
    print(f"  {'-'*45}")
    for nome, (inode, dados) in tabela.items():
        print(f"  {nome:<12} {inode:<10} {dados}")

    livres = blocos_livres(disco)
    print(f"\n  Blocos livres ({len(livres)}): {livres}")
    print(f"\n  Legenda: [I] = bloco índice (i-node)")
    return disco


# ─── ENTRADA ─────────────────────────────────────────────
def ler_entrada():
    separador("SIMULADOR DE ALOCAÇÃO DE BLOCOS NO DISCO")
    print("\n  Pressione ENTER para usar o exemplo padrão ou digite seus valores.\n")

    entrada = input("  Número de blocos no disco [padrão: 20]: ").strip()
    num_blocos = int(entrada) if entrada else 20

    print(f"\n  Agora informe os arquivos (nome e tamanho em blocos).")
    print(f"  Digite 'fim' quando terminar.\n")

    arquivos_padrao = [("Arquivo_A", 3), ("Arquivo_B", 4), ("Arquivo_C", 2), ("Arquivo_D", 5)]
    usar_padrao = input("  Usar arquivos padrão? (A=3, B=4, C=2, D=5 blocos) [S/n]: ").strip().lower()

    if usar_padrao in ("", "s", "sim"):
        arquivos = arquivos_padrao
        print(f"  Arquivos: {arquivos}")
    else:
        arquivos = []
        while True:
            nome = input("  Nome do arquivo (ou 'fim'): ").strip()
            if nome.lower() == "fim":
                break
            tam  = input(f"  Tamanho de '{nome}' em blocos: ").strip()
            arquivos.append((nome, int(tam)))

    return num_blocos, arquivos


# ─── MAIN ─────────────────────────────────────────────────
def main():
    num_blocos, arquivos = ler_entrada()

    separador("RESUMO DA ENTRADA")
    print(f"\n  Disco: {num_blocos} blocos")
    print(f"  Arquivos:")
    total = 0
    for nome, tam in arquivos:
        print(f"    - {nome}: {tam} blocos")
        total += tam
    print(f"  Total de blocos necessários: {total}")
    print(f"  Blocos livres após alocação estimada: {num_blocos - total}")

    alocacao_contigua(list(arquivos), num_blocos)
    alocacao_encadeada(list(arquivos), num_blocos)
    alocacao_indexada(list(arquivos), num_blocos)

    separador("COMPARATIVO FINAL")
    print(f"""
  {'Estratégia':<20} {'Vantagem':<35} {'Desvantagem'}
  {'-'*80}
  {'Contígua':<20} {'Acesso direto rápido':<35} {'Fragmentação externa'}
  {'Encadeada':<20} {'Sem fragmentação externa':<35} {'Acesso sequencial lento'}
  {'Indexada':<20} {'Acesso direto + flexível':<35} {'Overhead do i-node'}
    """)


if __name__ == "__main__":
    main()

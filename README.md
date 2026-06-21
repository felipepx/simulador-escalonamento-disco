[README(1).md](https://github.com/user-attachments/files/29182946/README.1.md)
#  Simuladores Didáticos de Sistemas Operacionais

Simuladores desenvolvidos em Python 3 para a disciplina de **Sistemas Operacionais**.  
Cada simulador demonstra, passo a passo no terminal, a lógica de um algoritmo clássico de S.O.

**Universidade Federal do Oeste do Pará — UFOPA**  
Bacharelado em Sistemas de Informação — Trabalho em Grupo 2

---

##  Integrantes

- Felipe Brito da Paixão
- Kaio Junio Farias Pereira
- Sebastiao Castilho Sanches Neto
- Kleydson de Jesus Fernandes
- João Pedro Magalhães Carvalho

---

##  Simuladores

| Arquivo | Tema | Algoritmos |
|---------|------|-----------|
| `simulador_paginas.py` | Substituição de Páginas | FIFO, LRU |
| `simulador_banqueiro.py` | Algoritmo do Banqueiro | Verificação de estado seguro |
| `simulador_disco.py` | Escalonamento de Disco | FCFS, SSTF, SCAN |
| `simulador_alocacao.py` | Alocação de Blocos no Disco | Contígua, Encadeada, Indexada |

---

##  Como Executar

**Requisitos:** Python 3.x (sem bibliotecas externas)

```bash
python simulador_paginas.py
python simulador_banqueiro.py
python simulador_disco.py
python simulador_alocacao.py
```

Cada simulador é interativo: pressione **ENTER** para usar os valores padrão ou digite os seus próprios.

---

##  Descrição dos Simuladores

### 01 — Substituição de Páginas (`simulador_paginas.py`)
Simula o comportamento da memória virtual quando todos os frames estão ocupados.

**Entrada:** sequência de referências a páginas e número de frames da RAM  
**Saída:** estado da memória a cada acesso, total de page faults e comparativo

| Algoritmo | Descrição |
|-----------|-----------|
| FIFO | Substitui a página que está na memória há mais tempo |
| LRU | Substitui a página usada há mais tempo (menos recente) |

---

### 02 — Algoritmo do Banqueiro (`simulador_banqueiro.py`)
Previne deadlocks verificando se o estado do sistema permanece seguro antes de conceder recursos.

**Entrada:** matriz de alocação, matriz de necessidade máxima, vetor de disponível  
**Saída:** estado seguro/inseguro, sequência segura, concessão ou negação de cada requisição

---

### 03 — Escalonamento de Disco (`simulador_disco.py`)
Compara estratégias de atendimento de requisições de leitura/escrita no disco rígido.

**Entrada:** posição inicial do braço, fila de cilindros, cilindro máximo, direção do SCAN  
**Saída:** passo a passo de cada algoritmo, total de cilindros percorridos e comparativo

| Algoritmo | Descrição |
|-----------|-----------|
| FCFS | Atende na ordem de chegada, sem otimização |
| SSTF | Sempre escolhe a requisição mais próxima |
| SCAN | Varre em uma direção e inverte ao chegar ao extremo |

---

### 04 — Alocação de Blocos (`simulador_alocacao.py`)
Demonstra como sistemas de arquivos organizam os dados no disco.

**Entrada:** número de blocos do disco, arquivos e seus tamanhos  
**Saída:** mapa visual do disco `[A][A][B][B][ ][ ]...` e tabela de alocação

| Estratégia | Descrição |
|-----------|-----------|
| Contígua | Blocos sequenciais — acesso rápido, fragmentação externa |
| Encadeada | Cada bloco aponta para o próximo — sem fragmentação, acesso lento |
| Indexada | i-node centraliza os endereços — acesso direto e flexível |

---

##  Funcionalidades Comuns

- Entrada interativa com valores padrão prontos para teste
- Validação de entradas com avisos claros ao usuário
- Exibição passo a passo de cada algoritmo
- Comparativo final destacando o resultado mais eficiente

---

##  Disciplina

**Sistemas Operacionais** — Bacharelado em Sistemas de Informação  
Universidade Federal do Oeste do Pará — UFOPA  
Trabalho em Grupo 2 — Simuladores Didáticos de S.O.

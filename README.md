[README.md](https://github.com/user-attachments/files/28976994/README.md)
#  Simulador de Escalonamento de Braço de Disco

Simulador didático desenvolvido em Python 3 para a disciplina de **Sistemas Operacionais**.  
Demonstra e compara três algoritmos clássicos de escalonamento de disco, passo a passo no terminal.

---

##  Algoritmos Implementados

| Algoritmo | Descrição |
|-----------|-----------|
| **FCFS** (First Come, First Served) | Atende as requisições na ordem exata de chegada, sem otimização |
| **SSTF** (Shortest Seek Time First) | A cada passo, escolhe o cilindro mais próximo da posição atual |
| **SCAN** (Elevador) | O braço percorre uma direção atendendo tudo; ao chegar ao extremo, inverte |

---

##  Como Executar

**Requisitos:** Python 3.x (sem bibliotecas externas)

```bash
python simulador_disco.py
```

O programa solicitará os seguintes dados (pressione **ENTER** para usar os valores padrão):

```
Posição inicial do braço [padrão: 53]:
Fila de requisições [padrão: 98 183 37 122 14 124 65 67]:
Cilindro máximo do disco [padrão: 199]:
Direção inicial do SCAN (crescente/decrescente) [padrão: crescente]:
```

---

##  Exemplo de Saída

```
=======================================================
  SIMULADOR DE ESCALONAMENTO DE BRAÇO DE DISCO
=======================================================

  Posição inicial do braço [padrão: 53]: 90
  Fila de requisições [padrão: ...]: 
  Cilindro máximo do disco [padrão: 199]: 
  Direção inicial do SCAN (crescente/decrescente) [padrão: crescente]: 

=======================================================
  COMPARATIVO FINAL
=======================================================

  Algoritmo  Cilindros Percorridos     Eficiência
  --------------------------------------------------
  FCFS       603
  SSTF       313
  SCAN       245                        ← MAIS EFICIENTE
```

---

##  Estrutura do Projeto

```
 simulador-disco/
├── simulador_disco.py   # Código principal
├── README.md            # Este arquivo
└── relatorio.docx       # Relatório técnico (entrega)
```

---

## ⚙️ Funcionalidades

- Entrada interativa com valores padrão prontos para teste
- Validação automática de requisições fora do intervalo do disco
- Direção do SCAN flexível (aceita variações de digitação)
- Exibição do passo a passo de cada algoritmo
- Comparativo final destacando o algoritmo mais eficiente

---

##  Disciplina

**Sistemas Operacionais** — Bacharelado em Sistemas de Informação  
Universidade Federal do Oeste do Pará — UFOPA  
Simuladores Didáticos

---

##  Integrantes

- FELIPE BRITO DA PAIXÃO
- KAIO JUNIO FARIAS PEREIRA
- SEBASTIAO CASTILHO SANCHES NETO
- KLEYDSON DE JESUS FERNANDES
- JOÃO PEDRO MAGALHÃES CARVALHO

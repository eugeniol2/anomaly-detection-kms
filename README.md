# anomaly-detection-kms

Pipeline experimental de um TCC de Sistemas de Informação (UFRPE). Compara um baseline
de regras contra modelos supervisionados na detecção de anomalias em metadados de
auditoria de um KMS experimental.

O modelo de ataque é credencial legítima de administrador comprometida: o atacante age
sob a credencial de um administrador real, o que elimina detecção por controle de acesso
e deixa o comportamento como único sinal.

Não há log real de KMS disponível. Os dados são gerados pelo próprio pipeline, e a
documentação do gerador é parte do trabalho.

## Estrutura

```
src/
  shared/          auxiliares comuns a M1..M10
    rng.py         fluxos de aleatoriedade derivados da semente
    tables.py      escrita de CSV e embaralhamento de linhas
    layout.py      onde cada arquivo mora dentro de data/
    experiment.py  a grade: sementes 1 a 30, sigma de 0,0 a 1,0
  population/      M1, um arquivo por conceito
    __main__.py    linha de comando e fluxo principal
    specification.py  parametros do repositorio de chaves
    scopes.py      escopos, compartilhados por operadores e chaves
    profiles.py    perfis comportamentais da populacao
    operators.py   construcao de operators.csv
    keys.py        construcao de keys.csv
data/              saida CSV de todos os modulos (nao versionada)
tests/             verificacao de determinismo e de formato
```

A pasta `data/` espelha a dependencia dos modulos: o que depende so da semente fica
no nivel da semente, o que depende tambem de sigma fica um nivel abaixo.

```
data/
  runs.csv                        indice das 330 execucoes
  metrics.csv                     agregado final (M10)
  seed-01/
    operators.csv  keys.csv       M1, dependem so da semente
    requests.csv                  M2, trafego legitimo
    sigma-0.0/
      requests.csv                M3, legitimo + ataque
      outcomes.csv  log.csv       M4, M5
      windows.csv                 M6
      train.csv  holdout.csv      M7
      predictions_rules.csv       M8
      predictions_ml.csv          M9
    sigma-0.1/ ... sigma-1.0/
  seed-02/ ... seed-30/
  calibration/                    preparacoes, fora das 330
```

Cada modulo M1..M10 e um pacote sob `src/`, com o fluxo principal em `__main__.py`
e um arquivo por conceito. A fronteira entre modulos continua sendo o arquivo CSV,
nao a chamada de funcao.

## Módulos

Cada módulo lê arquivo e escreve arquivo. A fronteira entre módulos é o arquivo, não a
chamada de função: cada um roda isolado e a saída é inspecionável antes do próximo.

| | Módulo | Entrada | Saída |
|---|---|---|---|
| M1 | `population` | seed | `operators.csv`, `keys.csv` |
| M2 | `traffic` | seed, tabelas | `requests.csv` |
| M3 | `attack` | seed, sigma, tabelas | `requests.csv` (+), `compromised_sessions.csv` |
| M4 | `kms` | `requests.csv`, `keys.csv` | `outcomes.csv` |
| M5 | `audit_logger` | requests, outcomes, label | `log.csv` |
| M6 | `dataset` | `log.csv` | `windows.csv` |
| M7 | `partition` | `windows.csv` | `train.csv`, `holdout.csv` |
| M8 | `baseline` | train/holdout, limiares | `predictions_rules.csv` |
| M9 | `models` | train/holdout | `predictions_ml.csv` |
| M10 | `evaluation` | predictions | `metrics.csv` |

Nomes de código e de arquivo em inglês; o texto da monografia é em português e traz uma
tabela de correspondência entre os dois.

## Ambiente

Python 3.11.

```
py -3.11 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

`requirements.txt` fixa as dependências diretas. `requirements-lock.txt` tem o
congelamento completo, para recriar o ambiente exatamente.

## Execução

Cada módulo roda sozinho pela linha de comando e recebe a semente como parâmetro
explícito:

```
python -m src.population --seed 42
```

## Testes

```
python -m pytest
```

Cobrem determinismo e as invariantes de que os modulos seguintes dependem:
toda chave tem proprietario que detem seu escopo, todo escopo tem detentor,
identificadores de chave nunca sequenciais. As invariantes rodam nas 30
sementes da grade, nao numa so.

O `test_reference_output_has_not_changed` e detector de mudanca, nao teste de
correcao: falha sempre que o gerador mudar, inclusive de proposito. Quando
falhar, confirme se a mudanca era intencional, registre a decisao e atualize o
valor de referencia.

## Reprodutibilidade

Semente mais código determinam a saída inteira. É por isso que `data/` não é versionada:
apagar a pasta e reexecutar reproduz os CSVs byte a byte, e é assim que o determinismo é
conferido.

Fluxos de aleatoriedade são separados por subsistema — população e chaves, tráfego
legítimo, campanha de ataque — todos derivados da mesma semente. A grade experimental é
de 11 condições de sigma (0,0 a 1,0) por 30 réplicas, totalizando 330 execuções.

## Estado

Em construção. Nenhum módulo implementado ainda. A ordem de implementação começa por
M1, M2, M4 e M5, sem atacante, para fechar o circuito e validar os formatos antes de
qualquer coisa depender deles.

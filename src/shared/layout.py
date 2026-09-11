"""Onde cada arquivo do pipeline mora dentro de `data/`.

A hierarquia espelha a dependencia. O que depende so da semente fica no nivel da
semente; o que depende tambem de sigma fica um nivel abaixo. Assim a pasta de
uma semente contem, visivelmente, uma unica populacao e as 11 varreduras que a
usam.

    data/
      runs.csv                        indice das 330 execucoes (D-012)
      metrics.csv                     agregado final (M10)
      seed-01/
        operators.csv                 M1, depende so da semente
        keys.csv                      M1
        requests.csv                  M2, trafego legitimo
        sigma-0.0/
          requests.csv                M3, legitimo + ataque
          compromised_sessions.csv    M3
          outcomes.csv                M4
          log.csv                     M5
          windows.csv                 M6
          train.csv, holdout.csv      M7
          predictions_rules.csv       M8
          predictions_ml.csv          M9
        sigma-0.1/ ... sigma-1.0/
      seed-02/ ... seed-30/
      calibration/                    preparacoes com sementes reservadas (D-031, D-032)

O M2 escreve `requests.csv` no nivel da semente e o M3 escreve outro
`requests.csv` no nivel da varredura, ja com as requisicoes do atacante. Sao
arquivos distintos, cada um com um unico modulo que o escreve: nenhum modulo
sobrescreve a saida de outro.
"""

from __future__ import annotations

from pathlib import Path

DEFAULT_ROOT = Path("data")

RUNS_INDEX = "runs.csv"
"""Indice das execucoes: sigma, seed, compromised_admin (D-012)."""

METRICS = "metrics.csv"
"""Saida do M10, agregando as 330 execucoes."""


def seed_directory(root: Path, seed: int) -> Path:
    """Onde ficam as saidas que dependem so da semente."""
    return root / f"seed-{seed:02d}"


def run_directory(root: Path, seed: int, sigma: float) -> Path:
    """Onde ficam as saidas que dependem da semente e de sigma.

    Um decimal em sigma basta para os 11 valores da grade, e mantem a ordem
    alfabetica igual a ordem numerica: sigma-0.0 ate sigma-1.0.
    """
    return seed_directory(root, seed) / f"sigma-{sigma:.1f}"


def calibration_directory(root: Path) -> Path:
    """Onde ficam as preparacoes, que usam sementes reservadas e ficam fora das 330."""
    return root / "calibration"

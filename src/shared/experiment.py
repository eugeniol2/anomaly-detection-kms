"""A grade experimental: quais sementes e quais condicoes de furtividade.

Fixada antes da primeira execucao (D-004, D-039). Uma execucao e identificada
pelo par (semente, sigma); a semente sozinha identifica uma varredura inteira.

Nenhum modulo importa isto ainda. O orquestrador das 330 execucoes vai, e este
e o unico lugar onde os valores da grade sao escritos.
"""

from __future__ import annotations

SEEDS = tuple(range(1, 31))
"""As 30 replicas (D-039). Cada semente varre as 11 condicoes de sigma."""

SIGMAS = tuple(step / 10 for step in range(11))
"""Furtividade do atacante, de 0,0 a 1,0 em passo de 0,1 (D-004)."""

TOTAL_RUNS = len(SEEDS) * len(SIGMAS)
"""330 execucoes."""

"""Escopos: o agrupamento logico a que cada chave pertence.

Cada operador detem um subconjunto dos escopos existentes, e esse subconjunto
delimita as chaves sobre as quais ele pode exercer a recuperacao de material.
Conceito compartilhado entre `operators` e `keys`, por isso mora separado dos dois.
"""

from __future__ import annotations


def scope_pool(quantity: int) -> list[str]:
    """Nomes dos escopos existentes no repositorio."""
    return [f"scope_{number:02d}" for number in range(1, quantity + 1)]

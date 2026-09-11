"""Parametros do repositorio de chaves e seus valores de referencia.

Contrato entre a linha de comando, que os recebe, e a construcao das chaves,
que os consome.
"""

from __future__ import annotations

from dataclasses import dataclass

DEFAULT_KEYS = 300
"""Tamanho do repositorio (D-035, Tabela 1 da proposta)."""

DEFAULT_SCOPES = 12
"""Escopos existentes (D-035)."""

DEFAULT_DISABLED_RATE = 0.05
"""Fracao de chaves que nasce desabilitada (D-038)."""

DEFAULT_SCOPE_FLOOR = 3
"""Piso de chaves por escopo, para que nenhum fique vazio (D-037)."""

DEFAULT_CONCENTRATION = 2.0
"""Concentracao da Dirichlet (D-037). Abaixo de 1 concentra demais; acima de 3 uniformiza."""


@dataclass(frozen=True)
class KeyRepositorySpecification:
    """Como o repositorio de chaves deve ser construido."""

    total_keys: int = DEFAULT_KEYS
    scope_count: int = DEFAULT_SCOPES
    disabled_rate: float = DEFAULT_DISABLED_RATE
    scope_floor: int = DEFAULT_SCOPE_FLOOR
    concentration: float = DEFAULT_CONCENTRATION

"""Parametros do repositorio de chaves e seus valores de referencia.

Contrato entre a linha de comando, que os recebe, e a construcao das chaves,
que os consome.
"""

from __future__ import annotations

from dataclasses import dataclass

DEFAULT_KEYS = 300
"""Tamanho do repositorio de chaves.

Fixado junto com a populacao de 44 operadores. Cada operador alcanca apenas as
chaves compreendidas em seus escopos, e o repositorio precisa ser grande o
bastante para que a enumeracao conduzida pelo atacante encontre chaves fora do
alcance da credencial e produza negacoes por politica (D-035).
"""

DEFAULT_SCOPES = 12
"""Escopos existentes no repositorio.

Escopo e o agrupamento logico a que cada chave pertence, correspondente a
aplicacao ou ao ambiente que a utiliza. Doze permite atribuir 1, 2 e 4 escopos
aos tres perfis mantendo sobreposicao parcial entre operadores, sem que nenhum
alcance o repositorio inteiro (D-035).
"""

DEFAULT_DISABLED_RATE = 0.05
"""Fracao de chaves que nasce desabilitada.

Precisa existir chave desabilitada ja no inicio do periodo de aquecimento para
que o desfecho "erro por chave desabilitada" ocorra em trafego legitimo. Se
surgisse apenas de operacoes DisableKey durante a simulacao, seria raro demais
no periodo avaliado e viraria marcador do atacante (D-038).
"""

DEFAULT_SCOPE_FLOOR = 3
"""Piso de chaves por escopo.

A reparticao entre escopos e deliberadamente desigual, e sem piso um escopo
pequeno poderia ficar vazio, deixando seus detentores sem nada a acessar
(D-037).
"""

DEFAULT_CONCENTRATION = 2.0
"""Concentracao da Dirichlet que reparte as chaves entre escopos.

Abaixo de 1 concentra demais: em varredura sobre 30 sementes, 0,7 produziu ate
128 chaves num unico escopo, quase metade do repositorio. Acima de 3 uniformiza,
e escopos de tamanho parecido fariam o total de chaves distintas acessadas
variar pouco entre operadores legitimos. Em 2,0 os escopos vao de cerca de 8 a
53 chaves (D-037).
"""


@dataclass(frozen=True)
class KeyRepositorySpecification:
    """Como o repositorio de chaves deve ser construido."""

    total_keys: int = DEFAULT_KEYS
    scope_count: int = DEFAULT_SCOPES
    disabled_rate: float = DEFAULT_DISABLED_RATE
    scope_floor: int = DEFAULT_SCOPE_FLOOR
    concentration: float = DEFAULT_CONCENTRATION

"""A grade experimental: quais sementes e quais condicoes de furtividade.

Uma execucao e identificada pelo par (semente, sigma); a semente sozinha
identifica uma varredura inteira de sigma. Dentro de uma varredura, a populacao,
as chaves, o administrador comprometido e o calendario de sessoes legitimas sao
os mesmos nas 11 condicoes: so o comportamento do atacante muda. E esse
pareamento que permite atribuir a sigma a diferenca observada.

A grade foi fixada antes da primeira execucao e antes de qualquer resultado ter
sido observado, o que e o que sustenta o enquadramento confirmatorio do trabalho
(D-004, D-039).

Nenhum modulo importa isto ainda. O orquestrador das 330 execucoes vai, e este e
o unico lugar onde os valores da grade sao escritos.
"""

from __future__ import annotations

SEEDS = tuple(range(1, 31))
"""As 30 replicas. Cada semente varre as 11 condicoes de sigma.

Lista consecutiva de proposito: e publicavel de forma verificavel e nao permite
suspeita de garimpo de sementes favoraveis. A objecao usual contra sementes
sequenciais nao se aplica aqui, porque os fluxos nao usam a semente como estado
interno: saem de `SeedSequence.spawn`, cuja mistura com efeito avalanche faz
sementes vizinhas produzirem estados iniciais sem correlacao (D-039).
"""

SIGMAS = tuple(step / 10 for step in range(11))
"""Furtividade do atacante, de 0,0 a 1,0 em passo de 0,1.

Em 0,0 o atacante e ostensivo em todas as cinco dimensoes comportamentais: taxa
de requisicoes elevada, varredura ampla de chaves, horario atipico, origem de
rede nao habitual e falhas de autorizacao frequentes. Em 1,0 cada dimensao se
aproxima estatisticamente do operador que ele personifica. O objetivo da
campanha e invariante em toda a faixa; o que sigma regula e o compromisso entre
velocidade e discricao (D-004).
"""

TOTAL_RUNS = len(SEEDS) * len(SIGMAS)
"""330 execucoes."""

# Citizen Assist AI

## Sobre o projeto

O Citizen Assist AI é um protótipo educacional desenvolvido
para a Global Solution 2026.2.

Seu objetivo é facilitar o acesso a orientações sobre
documentação, serviços públicos e direitos do consumidor.

O assistente não representa órgãos públicos e não
substitui a consulta às fontes oficiais.

## Funcionalidades

- Base de conhecimento JSON com 15 orientações.
- Busca por palavras-chave e pontuação de relevância.
- Prioridade para perguntas cadastradas exatamente.
- Identificação de perguntas ambíguas.
- Navegação entre três temas relacionados.
- Dois modelos de apresentação das respostas.
- Tratamento de entradas inválidas.
- Apresentação de fontes e datas de verificação.

## Tecnologias utilizadas

- Python
- JSON
- Pandas (análise dos testes)
- Google Colab
- GitHub

## Estrutura do projeto

```text
Citizen-Assist-AI/
├── src/
│   └── sistema.py
├── data/
│   └── base_conhecimento.json
├── tests/
│   └── resultados_testes.csv
├── docs/
│   └── uso_ia.md
└── README.md
```

## Como executar

1. Instale o Python 3.
2. Baixe ou clone o repositório.
3. Abra um terminal na pasta do projeto.
4. Execute:

```bash
python src/sistema.py
```

O sistema carregará automaticamente a base JSON.

## Algoritmos e estruturas de dados

O projeto utiliza listas e dicionários para organizar
as orientações, conjuntos para comparar palavras e
um grafo simples para relacionar os temas.

A busca utiliza uma pontuação baseada na correspondência
entre palavras da consulta e palavras cadastradas.

## Resultados dos testes

Foram realizados 12 testes automatizados.

- Acertos: 12
- Erros: 0
- Taxa de acerto: 100%
- Tempo médio observado: 0,5282 ms

Os resultados correspondem ao conjunto de testes utilizado
e não garantem precisão em perguntas não avaliadas.

Os resultados estão disponíveis em:
`tests/resultados_testes.csv`

## Limitações

- O sistema não utiliza um modelo de linguagem generativo.
- A busca depende das palavras presentes na base.
- Perguntas reformuladas podem não ser reconhecidas.
- A base possui apenas 15 orientações.
- Informações oficiais podem mudar ao longo do tempo.

## Melhorias futuras

- Ampliar a base de conhecimento.
- Melhorar o reconhecimento de perguntas semelhantes.
- Automatizar a atualização e verificação das fontes.
- Desenvolver uma interface gráfica.

## Aviso

Este projeto é exclusivamente educacional.
Confirme procedimentos e informações nos canais oficiais.

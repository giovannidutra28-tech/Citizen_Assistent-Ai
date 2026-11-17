# Citizen Assist AI

## Identificação do projeto

**Autor:** Giovanni Dutra Dias  
**RM:** 572671  
**Instituição:** FIAP  
**Projeto:** Global Solution 2026.2  
**Modalidade:** Desenvolvimento individual

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


## Organização da base de conhecimento

A base de conhecimento possui 15 registros
armazenados em formato JSON.

Os registros estão organizados em três temas:

1. Documentação
2. Serviços públicos
3. Direitos do consumidor

Cada registro contém informações como pergunta,
orientação, fonte oficial e data de verificação.

## Estratégia de busca

O sistema utiliza algoritmos implementados em Python
para localizar orientações relevantes.

A estratégia inclui:

- Normalização do texto das perguntas.
- Comparação entre palavras da consulta e da base.
- Priorização de correspondências exatas.
- Pontuação de relevância.
- Identificação de resultados ambíguos.
- Tratamento de perguntas não reconhecidas.

A busca utiliza listas, dicionários e conjuntos.

## Regras de resposta

O Citizen Assist AI possui dois modelos:

**Modelo 1 - Simples:**
Apresenta uma orientação resumida e sua fonte.

**Modelo 2 - Estruturado:**
Apresenta a pergunta identificada, orientação,
fonte, data de verificação, aviso e assuntos
relacionados.

O sistema utiliza respostas cadastradas na base,
sem gerar novas orientações por meio de um modelo
de linguagem externo.

Quando não encontra informações confiáveis,
informa a limitação ao usuário.

## Exemplos de consultas

**Pergunta:** O que é CPF?

**Resposta:** O CPF é um cadastro de pessoas físicas
administrado pela Receita Federal.

**Fonte:**
https://www.gov.br/receitafederal/pt-br/assuntos/meu-cpf

**Consulta ambígua:** CPF

O sistema pode apresentar diferentes orientações
relacionadas ao CPF para o usuário escolher.

**Consulta fora da base:** Como plantar uma árvore?

O sistema informa que não encontrou uma orientação
confiável e sugere reformular a pergunta.

## Privacidade e acessibilidade

O sistema utiliza uma interface textual com menus
numerados e mensagens de orientação.

Não solicita CPF, senhas ou outros dados pessoais
para realizar consultas.

As respostas apresentam fontes e avisos sobre
a necessidade de confirmação em canais oficiais.

O projeto é educacional e não representa
órgãos públicos.


## Avaliação de desempenho e usabilidade

### Plano de testes

Foram realizados 12 testes automatizados para avaliar
a recuperação das orientações cadastradas.

Também foram realizados testes de integração envolvendo:

- Busca de perguntas.
- Navegação entre temas.
- Alternância entre os modelos de resposta.

### Indicadores obtidos

| Indicador | Resultado |
|---|---|
| Total de testes | 12 |
| Acertos | 12 |
| Erros | 0 |
| Taxa de acerto | 100% |
| Tempo médio | 0,5282 ms |

### Interpretação dos resultados

O sistema acertou as 12 consultas do conjunto de testes.

Durante o desenvolvimento, foi identificada uma
ambiguidade na consulta sobre CPF. Após a revisão
dos critérios de busca e avaliação, os testes
foram executados novamente.

O tempo médio observado foi baixo no ambiente
utilizado, mas pode variar conforme o computador.

Os resultados não garantem precisão para perguntas
que não foram incluídas na avaliação.

### Avaliação de usabilidade

Foram verificadas as seguintes funcionalidades:

- Navegação por menus numerados.
- Consulta aos três temas cadastrados.
- Retorno ao menu principal.
- Apresentação das fontes das orientações.
- Alternância entre dois modelos de resposta.
- Tratamento de opções inválidas.

Os testes funcionais confirmaram a execução
dos fluxos avaliados.

Não foi realizado um estudo formal de usabilidade
com participantes externos. Portanto, não há
uma medida quantitativa de satisfação ou
facilidade de uso.

### Limitações observadas

- A busca depende das informações cadastradas.
- Algumas perguntas podem gerar ambiguidades.
- A base possui somente 15 registros.
- O sistema não interpreta qualquer pergunta livre.
- As informações oficiais exigem atualização periódica.


## Problema e público beneficiado

O acesso a informações sobre documentos, serviços
públicos e direitos do consumidor pode ser difícil
para cidadãos que não sabem onde encontrar
orientações oficiais.

O Citizen Assist AI busca facilitar essa consulta,
organizando informações em uma interface textual.

O público beneficiado inclui cidadãos que precisam
de orientações iniciais sobre:

- Documentação pessoal.
- Serviços públicos.
- Direitos do consumidor.

O sistema não substitui o atendimento dos órgãos
responsáveis.

## Conclusão

O desenvolvimento do Citizen Assist AI permitiu
aplicar conhecimentos de programação Python,
manipulação de arquivos JSON, estruturas de dados,
algoritmos de busca e testes automatizados.

A solução demonstrou capacidade de recuperar
orientações cadastradas, identificar ambiguidades
e apresentar fontes de referência.

Nos 12 testes automatizados realizados, o sistema
obteve 100% de acerto no conjunto avaliado.

Apesar dos resultados positivos, o protótipo
apresenta limitações relacionadas ao tamanho
da base e ao reconhecimento de perguntas
não previstas.

Como evolução futura, recomenda-se ampliar a
base de conhecimento, aperfeiçoar a busca e
desenvolver uma interface mais acessível.

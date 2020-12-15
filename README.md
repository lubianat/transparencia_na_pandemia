# Transparência na Pandemia

Esse repositório contém as análises e entregas do Grupo 8 da disciplina
[MAC434/6967 - Laboratório Avançado de Ciência de Dados(2020)](https://edisciplinas.usp.br/course/view.php?id=81141). A proposta da disciplina envolveu a comunicação com um cliente que veio com uma base de dados pronta e uma proposta de trabalho definida.

No caso do cliente adereçado a este grupo, a [Open Knowledge Brasil](https://www.ok.org.br/), uma organização de terceiro setor que coordena uma série de projetos, sendo um deles o [querido diário](https://queridodiario.ok.org.br/). O querido diário é um projeto com o objetivo de raspar os diários oficiais publicados pelos municípios
brasileiros em virtude de conseguir efetuar algum tipo de análise com o objetivo de acompanhar as ações governamentais.


## Descrição do problema e da solução que foi desenvolvida

Como compras e contratações publicas estão sujeitas a uma diversidade de formas de corrupção o governo desenvolveu um mecanismo para evitar e dificultar que ações maliciosas tomem efeito, que são as licitações. Entretanto, em crises, o município pode fazer uma compra na modalidade “dispensa de licitação”, onde o político decide de quem comprar o valor é combinado diretamente com a empresa.

Em 2020 o mundo passou a enfrentar a pandemia causada pelo novo corona vírus, alterando a forma que muitas pessoas vivem para manter a segurança de todos. Na maioria dos países a quantidade de casos cresceu rápido, exigindo um dinamismo por parte de entidades de saúde e dos gestores públicos para que a situação não fugisse totalmente do controle. Aqui no Brasil não foi diferente; alguns municípios passaram por momentos difíceis, e são nesses casos onde contratações e compras são feitas na modalidade dispensa de licitação.

Portanto, existiu um período no início da pandemia onde prefeituras puderam efetuar acordos do tipo dispensa de licitação, modalidade onde se percebe um aumento de atos ilícitos, desta forma, aumentando o interesse do público em verificar as ações do governo. Isto posto, o objetivo deste trabalho é investigar as informações contidas nos diários oficiais durante tempos de pandemia em busca de pistas que indiquem algum ato ilícito.

## Descrição dos dados

Foi coletado os arquivos pdf de 306 municípios brasileiros, obtidos pelo projeto querido diário, durante o período de 01 de fevereiro de 2020 até o dia 15 de junho de 2020.  Os arquivos foram convertidos de PDF para txt e, então, uma busca por palavras-chave foi executada para tentar separa-los por assunto, já que o interesse das análises desenvolvidas aqui são em assuntos relacionados com a pandemia. As palavras escolhidas foram:

- Emergencial
- Estado de Emergência de Saúde Pública
- Dispensa de licitação
- Equipamentos de Proteção Individual
- EPI
- Ventiladores pulmonares
- Ventilador pulmonar
- Demanda Emergencial Covid-19
- Teste rápido
- RT-PCR
- Hospital de Campanha

Como o mesmo documento pode ser resultado de mais de um destes termos, dos 2108 arquivos recebidos, apenas 1011 são distintos. 

Dado que as prefeituras (em sua maioria) disponibilizam os dados apenas em formato pdf, um tipo de dado não estruturado, não existe padrão entre as prefeituras então cada uma faz de uma forma. Alguns documentos possuem o layout disposto em colunas, sendo observados de 2 até 4, outros possuem tabelas e imagens no documento. Todos estes arquivos pdf foram convertidos para txt usando uma ferramenta chamada “magic” para que fosse possível efetuar análises textuais.

Mais detalhes quantitativos relacionado com os arquivos obtidos, podem ser vistos [neste notebook](https://github.com/lubianat/transparencia_na_pandemia/blob/master/entregas/entrega1/entrega_1.ipynb)


## Quais coisas foram tentadas e não deram certo

Por conta da diversidade do formato que as informações se encontram, foi feito uma série de tentativas de estruturação de dados para conseguir extrair informações relevantes referentescom às “dispensas de licitação”. O primeiro passo para executar esta análise foi por meio da linearização dos documentos, por um pacote independente desenvolvido pelos integrantes do grupo, o [GazettesProcessor](https://github.com/GabrielTrettel/GazettesProcessor). Com os diários linearizados a ideia era desenvolver uma forma de agrupar os dados, que pode ser visto  [no notebook](https://github.com/lubianat/transparencia_na_pandemia/blob/master/misc/src/tiago_teste_rapido_linearizado.ipynb) e também [neste outro](https://github.com/lubianat/transparencia_na_pandemia/blob/master/misc/src/tiago_teste_rapido-Copy1.ipynb).

Em todos os casos, os documentos apresentam muitas informações distintas, e, por isso, nenhum dos modelos conseguiu obter um resultado satisfatório.


## Quais coisas deram certo e quais os resultados obtidos

## Como rodar o software

 

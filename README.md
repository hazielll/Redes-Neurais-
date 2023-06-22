**Este ReadMe será utilizado como diário de bordo para a disciplina de Algoritmos Genéticos e Redes Neurais**

# Algoritmos Genéticos

São algoritmos que utilizam o princípio da evolução Darwiniano como analogia para o seu funcionamento. Graças a isso, a ideia desse tipo de algoritmo é mais palpável e fácil de entender. Seu principal uso é fornecer uma maneira de realizar buscas paralelas. Além disso, o próprio algoritmo se adapta ao seu propósito e "escolhe" os mais aptos a realizarem determinada tarefa.

## Componentes do Algoritmo Genético

Os parâmetros/componentes utilizados, assim como os próprios algoritmos, tem nomenclaturas derivadas da teoria da evolução. Dentre esses termos, temos:

Genótipos e genes - compões os individuos, os quais costumam ser uma string binária dos valores dos genes, dados por 0 e 1.

População - é um conjunto - ou o total - dos nossos indivíduos 

Fitness - é a função responsabilizada pela adaptação dos nossos indivíduos

Seleção - por outro lado, esta é a função responsabilizada pela seleção dos indivíduos que puderam se adaptar, ou não

Crossover - esta é a função responsabilizada pelo cruzamento entre os indivíduos a fim de gerar mais deles - além da troca genética. podemos controlar a quantidade de genes provenientes dos pais dos indivíduos

Mutação - mutações serão alterações aleatórias no gene, as quais poderão ser benéficas ou não para os indivíduos.

## EXP GA

*Experimentos e seus objetivos*

A pasta "Exp GA" será responsável por armazenar os "experimentos avaliativos" que deverão ser resolvidos para fixarmos e aplicarmos os conhecimentos obtidos durante as aulas e nosso aprendizado de algoritmos genéticos e os seus fundamentos. 

## Experimentos I - Algoritmos Genéticos

*A01 - Busca aleatória*

O experimento constitiu em solucionar o problema da caixa binária através de tentativa e errro. O problema de caixa binária consiste em n espaços que podem assumir os valores 0 ou 1, e queremos encontrar o valor máximo da caixa. Isto é, queremos que todos os espaços sejam preenchidos pelo valor 1. Para isso, começamos definindo o espaço de busca, ou seja, os n espaços a serem utilizados. Após foi sorteado um candidato aleatório, o qual analisamos por meio da função fitness.

*A02 - Busca em grade*

O esxperimento consistiu em solucionar o mesmo problema da caixa binária. No entanto, dessa vez combinamos os genes dos nossos indivíduos até encontrar um bom candidato com o passar das gerações dos algoritmos. Com os parametros iniciais definidos, partimos para a função fitness que irá selecionar os melhores indivíduos.

*A03 - O algoritmo genético propriamente dito*

O experimento consistiu em juntar os conceitos aprendidos e otimizá-los para resolver o problema da caixa binária considerando 4 caixas. Para isso, foi utilizado o arquivo funcoes.py, a fim de facilitar a importação das funções criadas anteriormente. 

*A04 - O uso do algoritmo genético em caixas não binárias*

O experimento consistiu em utilizar os conceitos aprendidos em um problema de caixas não binárias, as quais podem receber um número inteiro em um determinado intervalo. Assim, o princípio é o mesmo, no entanto, a dificuldade da resolução do problema seguiu um caminho diferente.

*A05 - O uso do algoritmo genético para descobrir uma senha alfabética*

O experimento consistiu em utilizar os conceitos aprendidos em um novo problema: descobrir uma senha alfabética por tentativa e erro do algoritmo, em conjunto à implementação de mutações, as quais ocorrem ao receber o feedback da fitness - isto é, semelhança entre a string gerada pelo algoritmo e a string da senha - do nosso objetivo. 

*A06 - O uso do algoritmo genético no problema do caixeiro viajante*

O experimento consistiu em revisitar o problema do caixeiro viajante abordado durante o primeiro semestre, mas agora com as ferramentas e conceitos aprendidos, sua resolução foi otimizada, especialmente devido à maior flexibilidade com dados dos algoritmos genéticos, o que facilita que haja uma rápida convergência para o objetivo do problema.  

*A07 - O uso do algoritmo genético e a aplicação de restrições*

O experimento consistiu em, novamente, revisitar um problema já abordado no primeiro semestre. Da mesma forma que com o problema do caixeiro viajante, alcançar uma boa aproximação do nosso objetivo se tornou um processo menos trabalhoso - computacionalmente. 

*A08, A09, A10, A11 - O módulo DEAP*

Este conjunto de experimentos teve como objetivo realizar um aprofundamento no módulo `DEAP`, o qual é utilizado para "facilitar" o processo de criação de algoritmos genéticos, com diversas ferramentas - e até mesmo uma caixa de ferramentas - para não ser necessário criar funções específicas para cada um dos problemas envolvendo algorítmos genéticos a serem tratados. Junto a isso, foram mostrados diversos exemplos da utilização do módulo `DEAP` na resolução de determinados problemas, sendo eles o problema das caixas não-binárias e o problema "descubra a senha".

# Redes Neurais

Redes neurais são estruturas computacionais inspiradas no funcionamento do cérebro humano, em que múltiplos nós, conhecidos como neurônios, estão interconectados para processar informações. Assim como os algoritmos evolutivos, as redes neurais adaptam-se e aprendem a partir dos dados de entrada, ajustando seus parâmetros para melhorar o desempenho em uma tarefa específica, os exemplos mais comuns consistem em identificar padrões complexos, realizar classificações e até mesmo previsões. As redes neurais são capazes de realizar essas tarefas de forma mais eficiente e rápida, tornando-se uma ferramenta poderosa para resolver problemas em áreas como visão computacional, processamento de linguagem natural e reconhecimento de voz, o que fomenta sua gama de aplicações em campos como medicina, finanças, automação industrial e muito mais. 

## Experimentos II - Redes Neurais

*R01 - Os conceitos por trás das Redes Neurais*

Este experimento consistiu em uma abordagem conceitual sobre os conceitos fundamentais dentro da área das Redes Neurais. Na parte computacional, pouco foi feito dessa vez, visto que o assunto abordado, a `back propagation`, é, a princípio, a minimização de erros de dados de determinados output por meio da utilização de derivadas e derivadas parciais. 

*R02 - Aprofundamento nos objetos `classes`*

Este experimento consistiu em um breve aprofundamento no conceito de objetos de classe no Python e sua relação com redes neurais. As classes em Python fornecem uma estrutura organizada para criar objetos que encapsulam dados e comportamentos relacionados. Ao aplicar esse conceito ao contexto de redes neurais, podemos criar classes que representam diferentes componentes, como camadas, neurônios e otimizadores, tornando o processo de construção e treinamento de redes neurais mais modular e reutilizável. A utilização de objetos de classe permite uma abordagem mais intuitiva e orientada a objetos no desenvolvimento de redes neurais, facilitando a compreensão, manutenção e expansão dos modelos. 

*R03 - A construção automatizada de um grafo*

Este experimento consistiu na construção de grafos no Python utilizando a biblioteca Graphviz. Os grafos são estruturas visuais poderosas que nos permitem representar as conexões e relacionamentos entre os elementos de um sistema. Ao aplicar essa abordagem aos princípios das redes neurais, podemos visualizar de forma clara e intuitiva a arquitetura (extensa) e as conexões das camadas e neurônios de uma rede neural. A construção de grafos por meio da biblioteca Graphviz nos permite automatizar a criação e análise visual dessas redes, proporcionando uma boa abordagem sobre seu comportamento e desempenho. O que nos permite entender e aprimorar nossos modelos de redes neurais, explorando sua estrutura. 

*R04 - Computando gradientes*

Este experimento consistiu em explorar a teoria por trás dos gradientes locais em redes neurais. Os gradientes locais desempenham um papel fundamental na medição da sensibilidade de um nó em relação ao seu valor de entrada. Ao aplicar o algoritmo de backpropagation, esses gradientes são calculados e utilizados para ajustar os pesos das conexões da rede, permitindo que ela aprenda e se adapte aos dados de entrada. Esse processo iterativo continua até que a rede neural atinja a convergência desejada. Ao longo desta aula, exploraremos detalhes sobre esse conceito e descobriremos como ele pode impulsionar nosso processo de treinamento e melhorar significativamente os resultados obtidos. 

*R05 - Conclusão da classe `Valor`*

Este experimento consistiu em revisitar os conceitos fundamentais explorados até o momento, com ênfase na classe `Valor` usada para calcular os gradientes locais. A implementação do código e a discussão sobre a relevância dos gradientes locais ressaltam a importância da diferenciação automática nas redes neurais. É fundamental ter um conhecimento sólido desses conceitos para evitar erros e obter resultados precisos.

*R06 - As Redes Neurais Artificiais propriamente ditas*

Este experimento consistiu na criação de uma rede neural artificial (RNA) com um único neurônio, explorando as três camadas essenciais que a compõem. As três camadas fundamentais são a camada de entrada (input layer), a camada oculta (hidden layer) e a camada de saída (output layer). Cada camada desempenha um papel crucial no processamento das informações e na tomada de decisões da rede neural. Durante o experimento, discutimos em detalhes a função de cada camada e como elas se interconectam para formar o fluxo de informação na rede. Ao compreender a importância e a função dessas camadas, estamos mais preparados para projetar e construir redes neurais mais complexas e eficientes. 

*R07 - A finalização da RNA e introdução a mais alguns conceitos*

Este experimento consistiu na finalização da rede neural que construímos anteriormente, explorando aspectos cruciais como funções de ativação, funções de perda, desempenho e ajuste de parâmetros. Durante a jornada, discutimos diferentes funções de ativação, como a função sigmoide e ReLU, as quais desempenham um papel fundamental na introdução de não-linearidade e na capacidade da rede neural de aprender e generalizar padrões complexos. Além disso, exploramos as funções de perda, como o erro quadrático médio, que mede a diferença entre as saídas previstas e os valores reais, auxiliando no ajuste dos pesos da rede. A análise do desempenho da rede, por meio de métricas como a acurácia e o erro, nos fornece insights valiosos sobre o quão bem nosso modelo está aprendendo e fazendo previsões.

*R08 - O pytorch e sua utilização*

Este experimento consistiu na reelaboração da rede neural anterior utilizando a biblioteca PyTorch, explorando seus recursos e benefícios. O PyTorch é uma poderosa ferramenta de aprendizado de máquina que nos permite construir redes neurais de forma eficiente e simplificada. Durante o experimento, nos aprofundamos no conceito de tensores, que são estruturas de dados fundamentais no PyTorch, permitindo-nos representar e manipular os dados de entrada e os parâmetros da rede de maneira eficaz. Além disso, exploramos as funções de perda já prontas fornecidas pelo PyTorch como o erro quadrático médio, facilitando o cálculo da diferença entre as saídas previstas e os valores reais. Introduzimos também o otimizador Adam, uma poderosa técnica de otimização estocástica já implementada no PyTorch, que ajusta automaticamente os pesos da rede com base nos gradientes calculados. Com a utilização do PyTorch, podemos aprimorar nossa rede neural com maior facilidade, aproveitando os recursos prontos e otimizados disponíveis na biblioteca. 

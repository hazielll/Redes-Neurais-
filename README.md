*Este ReadMe será utilizado como diário de bordo para Algoritmos Genéticos*

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

## Experimentos

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

O experimento dessa aula consistiu em revisitar o problema do caixeiro viajante, o qual já havia sido explorado - de maneira rasa - na disciplina de algoritmos do primeiro semestre. Agora, com as novas ferramentas e conceitos aprendidos nas aulas de algoritmos genéticos, podemos utilizar uma nova - e melhor - abordagem para encontrar uma solução aproximada para esse problema. Relembrando, o problema do caixeiro viajante consiste em encontrar o caminho mais curto que um vendedor viajante pode percorrer para visitar um conjunto de cidades exatamente uma vez e retornar à cidade de origem. 

*A06 - Aplicando restrições no problema da mochila*

O experimento dessa aula consistiu em revisitar o problema do mochileiro, o qual também já havia sido explorado na disciplina de algoritmos do primeiro semestre. Junto a isso, foi apresentado o conceito de restrições e "punições" ao lidar com algoritmos genéticos.

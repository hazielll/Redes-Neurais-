import random

def caixa():
    '''Gera um gene valido para o problema das caixas binárias
    
    Argumentos:
    
    Retornar: Um valor zero ou um.
    '''
    
    lista = [0,1]
    gene = random.choice(lista)
    return gene
    #pass # Enquanto a função não foi completada, colocamos pass para a função não fazer nada.

def individuo(n):
    '''Gera um individuo para o problema das caixasa binárias.
    
    Argumentos:
    n: número de genes do indivíduo
    
    Retornar: Uma lista com n genes. Cada gene é um valor zero ou um
    '''
    individuo = []
    for i in range(n):
        gene = caixa()
        individuo.append(gene)
    return individuo
    #pass
    
def populacao_cb(tamanho,n):
    '''Criamos uma população no problema das caixas binárias.
    
    Args:
        tamanho: número da população
        n: número de genes do individuo 
        
    Return: Queremos que a função retorne uma lista onde cada item é um indivíduo
    '''
    populacao = []
    for _ in range(tamanho): # utilizamos o _ ao invés de n para mostrar que a variável que estamos iterando não será utilizada
        populacao.append(individuo(n))
        return populacao
    

def funcao_objetivo(individuo):
    '''Computa a função objetivo no problema das caixas binárias
    
    Argumentos: 
    individuo: lista contendo os genes das caixas binarias 
    
    Retornar: Um valor representando a soma dos genes do individuo
    '''
    return sum(individuo)

def selecao_roleta_max(populacao,fitness):
    ''' Roleta onde cada posição será um indivíduo específico. A possibilidade de cada posição depende do quão bom
    é um indivíduo. Obs.: Apenas funciona para problemas de maximização 
    
    Arg: pop = lista com todos os individuos da população
    fitness = lista com o valor da função objetivo dos indivíduos da população
    
    Retornar: população dos indivíduos selecionados
    '''
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len*(populacao))
    return populacao_selecionada

def funcao_objetivo_pop_cb():
    ''' Calcula a funcao objetivo para todos os membros de uma populacao
    
    Args: pop
    
    Retornar: lista de valores representando a fitness de cada individuo da população.
    '''
    fitness = []
    for individuo in populacao:
        fobj = objetivo(individuo)
        fitness.append(fobj)
    return fitness

def cruzamento_ponto_simples(pai,mae):
    '''Operador de cruzamento de ponto simples.
    
    Args: pai = lista de um individuo
    mae = lista de um outro individuo
    
    Retornar: duas listas, cada uma representa um filho com elementos dos pais.
    '''
    ponto_de_corte = random.randint(1, len(pai)-1) #utilizamos 1 para a randomização não selecionar o elemento 0 da lista. por outro lado, utilizamos o len(pai)-1 para não contar o último elemento da lista
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    
    return filho1,filho2
    
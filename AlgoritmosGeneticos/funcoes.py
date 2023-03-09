def funcao_objetivo(individuo):
    '''Computa a função objetivo no problema das caixas binárias
    
    Argumentos: 
    individuo: lista contendo os genes das caixas binarias 
    
    Retornar: Um valor representando a soma dos genes do individuo
    '''
    return sum(individuo)
 

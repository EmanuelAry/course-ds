def removeRecursivo(pilha):
    if(pilha.size > 0):
        pilha[-1].remove()
        removeRecursivo(pilha)
    else:
        return
    
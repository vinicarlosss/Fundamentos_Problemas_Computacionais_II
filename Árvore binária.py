class No:
    def __init__(self,data, left, right):
        self.data = data
        self.left = left
        self.right = right

class three:
    def __init__(self):
        self.root = No(None, None, None)
        self.root = None

    def inserir(self, v):
        new = No(v, None, None) #Cria-se um novo nó
        if self.root == None: #se não tiver raiz o novo nó vai ser a raiz
            self.root = new
        else: #se a raiz já tiver um valor então...
            atual = self.root
            if atual.data == v:
                print("Número repetido")
            else:
                while True:
                    anterior = atual
                    if v <= atual.data: #ir para a esquerda
                        atual = atual.left
                        if atual == None: #se o valor a esquerda estiver vazio
                            anterior.left = new
                            return
                        elif atual.data ==v:
                            print("Número repetido")
                        #fim da condição de ir para a esquerda
                    else: #ir para a direita
                        atual = atual.right

                        if atual == None:
                            anterior.right = new
                            return
                        elif atual.data == v:
                            print("Número repetido")
                    #fim da condição de ir a direita
    def inOrderWalk(self,x):
        if x is not None:
            self.inOrderWalk(x.left)
            print(x.data)
            self.inOrderWalk(x.right)



minhaArvore = three()

for i in range(10):
    minhaArvore.inserir(int(input("digite um novo valor:")))

minhaArvore.inOrderWalk(minhaArvore.root)



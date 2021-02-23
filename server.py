import Pyro4
import queue

q = queue.Queue()

@Pyro4.expose
class Queue:
    def push(self, valor):
        q.put(valor)
        print("valor inserido na fila: ", valor)
        return "{0} foi inserido com sucesso!\n" .format(valor)
    
    def size(self):
        print(q.qsize())
        return "tamanho da fila: {0}\n" .format(q.qsize())
    
    def pop(self):
        if(q.empty()):
            print("fila encontra-se vazia")
            return "fila vazia\n"
        else:
            item = q.get()
            print(item ," foi removido da fila")
            return "{0} removido com sucesso!\n" .format(item)

daemon = Pyro4.Daemon()
uri = daemon.register(Queue)

ns = Pyro4.locateNS()
ns.register('obj', uri)

print(uri)

daemon.requestLoop()
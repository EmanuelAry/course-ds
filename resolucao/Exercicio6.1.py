L = new Array
P = new Pilha
F = new Fila

P.push(1)                 # L = [] | F=[] | P = [1]
P.push(2)                 # L = [] | F=[] | P = [1,2]
F.enqueue(3)              # L = [] | F=[3] | P = [1,2]
F.enqueue(4)              # L = [] | F=[3,4] | P = [1,2]
F.enqueue(5)              # L = [] | F=[3,4,5] | P = [1,2]
L.insert(0,6)             # L = [6] | F=[3,4,5] | P = [1,2]
L.insert(0,7)             # L = [7,6] | F=[3,4,5] | P = [1,2]
L.insert(1,8)             # L = [7,8,6] | F=[3,4,5] | P = [1,2]
P.push(9)                 # L = [7,8,6] | F=[3,4,5] | P = [1,2,9]
L.insert(1, P.top())      # L = [7,9,8,6] | F=[3,4,5] | P = [1,2,9]
L.insert(2, F.dequeue())  # L = [7,9,3,8,6] | F=[4,5] | P = [1,2,9]
L.insert(0, P.pop())      # L = [9,7,9,3,8,6] | F=[4,5] | P = [1,2]
P.push(F.dequeue())       # L = [9,7,9,3,8,6] | F=[5] | P = [1,2,4]
P.push(L.get(3))          # L = [9,7,9,3,8,6] | F=[5] | P = [1,2,4,3]
F.enqueue(L.remove(2))    # L = [9,7,3,8,6] | F=[5,9] | P = [1,2,4,3]
L.set(2, F.first())       # L = [9,7,5,8,6] | F=[5,9] | P = [1,2,4,3]

# L = [9,5,3] | F=[5] | 
# A class to define nodes 
class tree:
    def __init__(self , letter = "" , num = 0):
        self.letter : str = letter
        self.num : int = num
        self.left : tree = None
        self.right : tree = None
    
# All members are an object , so we sort the list (array) by the 'num' property
def sortByProperty(a : list) -> None:
    size = len(a)
    for i in range(size):
        for j in range(size-i-1):
            if( a[j].num > a[j+1].num ):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    
def make_tree( a : list) -> None :
    sum = a[0].num + a[1].num

    newtree = tree(num=sum)
    newtree.left = a[0]
    newtree.right = a[1]

    a.remove(a[1])
    a.remove(a[0])
    a.append(newtree)

    sortByProperty(a)

# Travel to all nodes to determine the code of each character
def travel(code : dict , root: tree , x : str= "") -> None:
    
    if root.left != None:
        x += "0"
        travel(code , root.left , x)
        x = x[:-1]
    if root.right != None:
        x += "1"
        travel(code , root.right , x)
        x = x[:-1]
    
    if root.left == None and root.right == None:
        code[root.letter] = x

 

#read file // change the directory //
file = open(file="t1.txt" , mode="r+")
line = file.readline()
file.close()

# A dict to store the input alphabet and letters count
alphabet = {}
for i in line:
    if i in alphabet.keys():
        alphabet[i] += 1
    else:
        alphabet[i] = 1

a = []
for i in alphabet.keys():
    a.append(tree(letter=i , num=alphabet[i]))

sortByProperty(a)

while len(a) > 1:
    make_tree(a)

root = a[0]
code = {}
travel(code ,root)
print("alphabet : " , alphabet)
print("code table : " ,  code)

text = ""
for i in line:
    text += code[i]

print("the coded text : " , text)

file = open(file="f2.txt" , mode="w" , encoding="utf8")
file.write(text)
file.close()



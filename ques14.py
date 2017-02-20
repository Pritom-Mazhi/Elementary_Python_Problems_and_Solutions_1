class node :
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):
    current = root
    s=[]
    done = False

    while(not done):
        if current is not None:
            s.append(current)
            current=current.left
        else :
            if(len(s)>0):
                current=s.pop()
                print(current.data)
                current = current.right
            else:
                done = True

root = node(1)
root.left = node(2)
root.right = node(3)
root.left.left = node(4)
root.left.right = node(5)
inOrder(root)

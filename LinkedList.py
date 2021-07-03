class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.nextval = None

class Test:
    def createLinkedList(self):
        x = Node(1);
        print(x.dataval);
        y = Node(2);
        print(y.dataval);
        k = x;
        print('======================')
        x.nextval = y;
        print(x.dataval, x.nextval.dataval);
        x = x.nextval.nextval;
        print(x.dataval)
        print(x.nextval)
        x.nextval = Node(3);
        print(x.dataval)
        print(x.nextval)
        print(x.nextval.dataval)
        x = x.nextval
        print(x.dataval)
        print(x.nextval)
        print(k.dataval)
        print(k.nextval.dataval)



ts = Test();
ts.createLinkedList();
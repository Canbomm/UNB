edge1,edge2,edge3 = map(int,input().split())

while edge1 != 0 and edge2 != 0 and edge3 != 0:
    cubo = int((edge1*edge2*edge3)**(1/3))
    print(cubo)
    edge1,edge2,edge3 = map(int,input().split())

lista = []
vocales= "a,e,i,o,u,A,E,I,O,U"
consonantes="b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,X,Y,Z"
acum=0
while True:
    word = input("Ingrese una palabra, o presione Enter para finalizar:  ") 
    if word == "":
        break
    lista.append(word)
    print(lista)
    x=len(word)
print(len(lista))
acum = acum + vocales + consonantes
word= word+acum
print("La palabra con mas caracteres tiene: ", word )

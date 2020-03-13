
matriz_principal = [["-","-","-"],["-","-","-"],["-","-","-"]]
def imprimir():
	print()
	print ("|| C1: ",matriz_principal[0][0],"||","C4: ",matriz_principal[1][0],"||","C7: ",matriz_principal[2][0],"||")
	print()
	print ("|| C2: ",matriz_principal[0][1],"||","C5: ",matriz_principal[1][1],"||","C8: ",matriz_principal[2][1],"||")
	print()
	print ("|| C3: ",matriz_principal[0][2],"||","C6: ",matriz_principal[1][2],"||","C9: ",matriz_principal[2][2],"||")
	print()
def eleccion():
	
	if (cas==1 and coso=="X"):
		matriz_principal[0][0]="X"
	if (cas==1 and coso=="O"):
		matriz_principal[0][0]="O"
	if (cas==2 and coso=="X"):
		matriz_principal[0][1]="X"
	if (cas==2 and coso=="O"):
		matriz_principal[0][1]="O"
	if (cas==3 and coso=="X"):
		matriz_principal[0][2]="X"
	if (cas==3 and coso=="O"):
		matriz_principal[0][2]="O"
	if (cas==4 and coso=="X"):
		matriz_principal[1][0]="X"
	if (cas==4 and coso=="O"):
		matriz_principal[1][0]="O"
	if (cas==5 and coso=="X"):
		matriz_principal[1][1]="X"
	if (cas==5 and coso=="O"):
		matriz_principal[1][1]="O"
	if (cas==6 and coso=="X"):
		matriz_principal[1][2]="X"
	if (cas==6 and coso=="O"):
		matriz_principal[1][2]="O"
	if (cas==7 and coso=="X"):
		matriz_principal[2][0]="X"
	if (cas==7 and coso=="O"):
		matriz_principal[2][0]="O"
	if (cas==8 and coso=="X"):
		matriz_principal[2][1]="X"
	if (cas==8 and coso=="O"):
		matriz_principal[2][1]="O"
	if (cas==9 and coso=="X"):
		matriz_principal[2][2]="X"
	if (cas==9 and coso=="O"):
		matriz_principal[2][2]="O"
def comprobar():
	if (matriz_principal[0][0]=="X" and matriz_principal[1][0]=="X" and matriz_principal[2][0]=="X"):
		return False
	if (matriz_principal[0][1]=="X" and matriz_principal[1][1]=="X" and matriz_principal[2][1]=="X"):
		return False
	if (matriz_principal[0][2]=="X" and matriz_principal[1][2]=="X" and matriz_principal[2][2]=="X"):
		return False
	if (matriz_principal[0][0]=="X" and matriz_principal[0][1]=="X" and matriz_principal[0][2]=="X"):
		return False
	if (matriz_principal[1][0]=="X" and matriz_principal[1][1]=="X" and matriz_principal[1][2]=="X"):
		return False
	if (matriz_principal[2][0]=="X" and matriz_principal[2][1]=="X" and matriz_principal[2][2]=="X"):
		return False
	if (matriz_principal[0][0]=="X" and matriz_principal[1][1]=="X" and matriz_principal[2][2]=="X"):
		return False
	if (matriz_principal[0][2]=="X" and matriz_principal[1][1]=="X" and matriz_principal[2][0]=="X"):
		return False
		
	if (matriz_principal[0][0]=="O" and matriz_principal[1][0]=="O" and matriz_principal[2][0]=="O"):
		return False
	if (matriz_principal[0][1]=="O" and matriz_principal[1][1]=="O" and matriz_principal[2][1]=="O"):
		return False
	if (matriz_principal[0][2]=="O" and matriz_principal[1][2]=="O" and matriz_principal[2][2]=="O"):
		return False
	if (matriz_principal[0][0]=="O" and matriz_principal[0][1]=="O" and matriz_principal[0][2]=="O"):
		return False
	if (matriz_principal[1][0]=="O" and matriz_principal[1][1]=="O" and matriz_principal[1][2]=="O"):
		return False
	if (matriz_principal[2][0]=="O" and matriz_principal[2][1]=="O" and matriz_principal[2][2]=="O"):
		return False
	if (matriz_principal[0][0]=="O" and matriz_principal[1][1]=="O" and matriz_principal[2][2]=="O"):
		return False
	if (matriz_principal[0][2]=="O" and matriz_principal[1][1]=="O" and matriz_principal[2][0]=="O"):
		return False
	return True
imprimir()
cas=0
gan=""
coso=""
a=True
while (a==True):
	a=comprobar()
	if (a==True):
		cas=int(input("Seleccione una casilla (1 al 9): "))
		print()
		coso=input("Seleccione X o O (Mayúsculas): ")
		eleccion()
		imprimir()
if (gan=="X"):
	print("Felicitaciones, las X ganaron")
if (gan=="O"):
	print("Felicitaciones, las O ganaron")

	



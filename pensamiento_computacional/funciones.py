'''
def suma ( a, b):
    total = a + b 
    return  total 
    
suma(3, 3)
    print(f' la suma es {total}')

 '''
def nombre_completo(nombre, apellido, inverso=False):
    if inverso:
         return f' {apellido}, {nombre}'
    else :
        return f' {nombre}, {apellido} '

nombre_completo('Eduardo', 'Carrasco')  
    print(nombre_completo)
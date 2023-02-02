alias=[
    "foo",
    "bar",
    "baz",
    "qux",
    "quux",
    "fred",
    "xyz"
]

def val_init(string):
    return string[0:1] != 'b'

def upper_fin(string):
    long_cadena=len(string)
    return string[0:long_cadena-1]+(string[long_cadena-1:long_cadena].upper())

def interval_bar(string):
    long_cadena=int(len(string)/2)
    return string[0:long_cadena]+"-"+(string[long_cadena:long_cadena*2])

#recusividad directa
def interar(array,i):
    if(i==0):
        array=list(array)
    if(len(array)!=i):
        if(val_init(array[i])):
            if(len(array[i])%2==0):
                array[i]=interval_bar(array[i])
            else:
                array[i]=upper_fin(array[i])
        else:
            array.pop(i)
            i=i-1
        interar(array, i+1)
    return array

print("Salida recusividad")    
print(interar(alias,0))
print(alias)

#recusividad cruzada
def logic_itera(array,i,ban):
    if(val_init(array[i])):
        if(len(array[i])%2==0):
            array[i]=interval_bar(array[i])
        else:
            array[i]=upper_fin(array[i])
    else:
        array.pop(i)
        i=i-1
    if(ban==2):
        itera_cruzada_two(array,i+1)
    else:
        itera_cruzada_one(array,i+1)

def itera_cruzada_one(array,i):
    if(len(array)!=i):
        logic_itera(array,i,2)

def itera_cruzada_two(array,i):
    if(len(array)!=i):
        logic_itera(array,i,1)

def itera_cruzada_init(array):
    new_array=list(array)
    itera_cruzada_one(new_array,0)
    return new_array

print("Salida recusividad cruzada") 
print(itera_cruzada_init(alias))
print(alias)

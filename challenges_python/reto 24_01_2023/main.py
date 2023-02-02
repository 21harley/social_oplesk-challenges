
abc='abcdefghijklmnñopqrstuvwxyz'

def codigo_cesar(cadena=str,type_c=str):

    return  "".join(
        list(
            map(
                lambda c: abc[
                    abc.find(c) + (3 if (type_c=='C') else -3)
                    ], cadena
            )
        )
    )

if __name__=="__main__":
   print(codigo_cesar(1,1))



function codigo_cesar(cadena,type_c,despl=3){
    if(typeof type_c != 'string' || 
       typeof cadena != 'string' ||
      (type_c != 'C' && type_c != 'D') ||
       typeof despl != 'number'){
        return "Error al ingresar datos"
    }
    let abc='abcdefghijklmnñopqrstuvwxyz';
    let new_cadena="";
    let sumador=type_c=='C' ? despl : -despl
    let leng_abc=abc.length;
    for(let i=0;i<cadena.length;i++){
        if(abc.indexOf(cadena[i].toLowerCase())!=-1){
            let valor=abc.indexOf(cadena[i].toLowerCase()) + sumador;
            let aux_1=valor<0?(leng_abc+sumador):((valor>leng_abc)?(sumador+leng_abc):(valor))
            new_cadena+=abc[aux_1]
        }else{
            new_cadena+=cadena[i]
        }
    }
    return new_cadena;
}
console.log(codigo_cesar("admi?n",'C','3'));
console.log(codigo_cesar("dgolp",'D',3));
/*
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
*/

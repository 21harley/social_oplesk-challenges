const mutaciones={ 
    'a':'@', 
    'e':'3', 
    'i':'1', 
    'o':'0', 
    'u':'v' 
} 

const str = ['foo','bar','baz','qux','echo','fred','thud','carter','luis','oso','perro','car','arepa']; 

function Mutacion(str){ 
    let newString=[]; 

    for(let i=0;i<str.length;i++){ 
       let letraInit=mutaciones[str[i][0]]; 
       let letraFinal=mutaciones[str[i][str[i].length-1]]; 

       let nuevaPalabra=''; 
       for(let j=0;j<str[i].length;j++){ 
        nuevaPalabra+=mutaciones[str[i][j]]?mutaciones[str[i][j]]:str[i][j];
       } 
       newString[i]=nuevaPalabra; 
       
       if(letraInit!=undefined && letraFinal!=undefined){ 
          nuevaPalabra="";
          for(let j=0;j<newString[i].length;j++){
             nuevaPalabra+=newString[i][j].toUpperCase();
          }

       }else if(letraFinal==undefined && str[i].length<=3){ 

          nuevaPalabra=newString[i].slice(0,newString[i].length-1)+newString[i][str[i].length-1].toUpperCase();

       }else if(letraInit==undefined && letraFinal!=undefined){ 

          nuevaPalabra=newString[i]; 
          nuevaPalabra=nuevaPalabra[0].toUpperCase()+newString[i].substr(1); 

       }else if(letraInit==undefined && letraFinal==undefined){ 
         nuevaPalabra="";
         for(let j=0;j<newString[i].length;j++){ 
            nuevaPalabra+=(!mutaciones[str[i][j]])?'+':newString[i][j];
          } 

       }
       newString[i]=nuevaPalabra; 
    } 

    return newString;  
} 
 
console.log(Mutacion(str));
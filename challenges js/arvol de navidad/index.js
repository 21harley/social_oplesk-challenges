
function arbol_navidad(niveles){
    if(niveles<=6) return "nivel inferior al requerido por favor ingresar un nivel superior a o igual a 7"
    let estrellas=1;
    let espacios=((niveles-3)*2-1)*2;
    for(let i=0;i<niveles+1;i++){
        let linea="";
        let total_estrellas=0;
      for(let j=0;j<espacios*2;j++){
        if(niveles-2<=i){
            for(let k=0;k<(espacios-3-(niveles));k++){
                linea+=" ";
            }
            for(let k=0;k<3;k++){
                linea+="*";
            }
            break;
        }else{
            if(espacios-(parseInt((estrellas+1)/2))<=j+niveles+1){
                linea+="*";
                total_estrellas++;
                if(estrellas==total_estrellas) break;
            }else{
                linea+=" ";
            }
        }
      }
      console.log(linea);
      if(niveles-2>=i) estrellas+=2;
    }
}
console.log(arbol_navidad(33));

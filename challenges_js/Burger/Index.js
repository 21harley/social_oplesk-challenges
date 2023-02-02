function header(){
    console.log('*'.repeat(5)+' Menu Nueva Esparta '+'*'.repeat(5))
}
const cliente={
    name:'',
    money:0,
    tp:'',
    cart:[],
}
const almacen={
    name:'Nueva Esparta',
    cast:0,
    items:[
        {
            name:'Burger Normal',
            cost:3,
            unitPro:10
        },
        {
            name:'Burger Especial',
            cost:5,
            unitPro:10
        },
        {
            name:'Burger Super Especial',
            cost:10,
            unitPro:10
        },
        {
            name:'Refresco Pequeno',
            cost:1,
            unitPro:10
        },
        {
            name:'Refresco Grande',
            cost:3,
            unitPro:10
        }
    ]
}

function mostrarStok(){
    console.clear()
    header()
    almacen.items.forEach((el,index)=>{
        console.log('Nombre:'+el.name,'Costo:'+el.cost,'Codigo:'+(index+1))
    })
}
function mostrarStokAll(){
    console.clear()
    header()
    almacen.items.forEach((el,index)=>{
        console.log('Nombre:'+el.name,'Costo:'+el.cost,'Unidades Producto:'+el.unitPro)
    })
}

function mostrarUser(){
    console.clear()
    header()
    console.log('Nombre Cliente:'+cliente.name,'Dinero del Cliente:'+cliente.money,'Medio de pago:'+cliente.tp)
}

function Terminal(collback){
    let rl = readline.createInterface(
        process.stdin, process.stdout);
    collback()
    rl.question("Precione enter para continuar", (input1) => {
      rl.close()
      init_terminal()
    })
}

function menu(){
    header()
    console.log("1-Cargar  Cliente")
    console.log("2-Cargar  Pedido")
    console.log("3-Recibo  Cliente")
    console.log("4-Mostrar Stock")
    console.log("5-Mostrar  Datos Cliente")
    console.log("6-salir")
}
var readline = require('readline');

function cargar_cliente(){
    let rl = readline.createInterface(
        process.stdin, process.stdout);
    console.clear()
    header()
    console.log("Proceso de carga de datos:")
    rl.question("Ingrese nombre:", (name) => {
        rl.question("Ingrese dinero:", (money) => {
            rl.question("Ingrese tipo pago:", (tp) => {
               cliente.name=name;
               cliente.money=parseInt(money)
               cliente.tp=tp
               rl.close()
               init_terminal()
            })
        })
    })
}
function pedido(){
    console.clear()
    let rl = readline.createInterface(
        process.stdin, process.stdout);
    mostrarStok()
    rl.question("Ingrese codigo:", (input1) => {
        rl.question('Ingrese la cantidad:', (input2) => {
          rl.question('Esta seguro en comprar?(y/n):',(input3)=>{
            let list_error=[]
            if(input3.includes('y')&&input3.length==1){
                let num=parseInt(input1)
                let cant=parseInt(input2)
                if(typeof num == 'number' && typeof cant == 'number'){
                    if(num>0 && num-1<almacen.items.length){
                        almacen.items.forEach((el,index)=>{
                           if(num-1==index){
                            let ban_cant=(el.unitPro>=cant)?1:0;
                            let ban_money=(cliente.money>=el.cost*cant)?1:0;
        
                            if(ban_cant===1&&ban_money===1){
                                let aux=Object.assign({},el)
                                aux.unitPro=cant
                                el.unitPro-=cant
                                cliente.cart.push(aux)
                                cliente.money=cliente.money-(aux.cost*cant)
                                almacen.cast=almacen.cast+(aux.cost*aux.unitPro)
                                
                            }else{
                                list_error.push('3')
                            }
                            
                            if(ban_cant==0) console.log('Ingreso un numero superior a la cantidad existen')
                            if(ban_money==0) console.log('El cliente no cuenta con los fondos necesarios para la compra')
                           }
                        })
                    }
                }else{
                    console.log("Error al ingresar datos")
                    list_error.push('2')
                }
            }else{
                list_error.push('1')
            }
          
          rl.close()
          
          
          Terminal(()=>{
            if(list_error.length>0){
                console.log("Error",list_error)
            }else{
                console.log("Compra exitosa")
            }
          })
          
          //init_terminal()
          
          })
        })
    })
}

function reciso_cliente(){
    console.clear()
    header()
    cliente.cart.forEach((el,index)=>{
        console.log('Nombre:'+el.name,'Costo:'+el.cost,'Codigo:'+(index+1))
    })

}

function creacte_terminal(mensaje){
    let rl = readline.createInterface(
        process.stdin, process.stdout);
    rl.question(mensaje, (input) => {
        console.log(input)
        rl.close()
        switch(parseInt(input)){
            case 1:
                cargar_cliente()
            break;
            case 2:
                pedido()
            break;
            case 3:
                Terminal(reciso_cliente)
            break;
            case 4:
                Terminal(mostrarStokAll)
            break;
            case 5:
                Terminal(mostrarUser)
            break;
            case 6:
                return 0;

            default:
                menu()
                creacte_terminal(mensaje)
        }
    })
}
function init_terminal(){
    console.clear()
    menu()
    creacte_terminal("@>") 
}

init_terminal()

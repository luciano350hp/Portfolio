class Calculadora {
	constructor(a,b) {
		this.a = a
		this.b = b
	}
	division (){
		let div = 0;
		if (this.b === 0){
			console.log("Error División por Cero \n")
		}
		div = [this.a/this.b, this.a%this.b]
		return div
	}
	multiplicacion(){
		let mult = 0;
		return this.a * this.b
	}
	resta(){
		let resta = 0; 
		return this.a - this.b;
	}
	suma(){
		let suma = 0;
		return this.a + this.b;
	}

	*factorial (numero) {
		let fact = 1
		if (numero < 0){
			fact = 0
		}
		if (numero === 1){
			fact = 1
		}
		for (let i=1; i <= numero; i++){
			fact =  fact * i
			yield (fact)
		}
	}

}

c = new Calculadora (20,15)
const [resultado, resto] = c.division()
console.log("La multiplicación es: ",c.multiplicacion());
console.log("La suma es: ",c.suma());
console.log("La resta es: ",c.resta());
console.log("El resultado de la división es: ",resultado, "Con resto: ",resto, '\n')

console.log("Factorial")
let fact = c.factorial(5)
let estado = fact.next()
let iterador = 1
while (!estado.done){
	console.log("Factorial de",iterador,"----->",estado.value)
	iterador ++;
	estado = fact.next()
}




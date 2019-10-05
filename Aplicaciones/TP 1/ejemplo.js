function dosomething() {
	console.log('Hola Mundo')
}

dosomething()

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
	*ejemplo(input) {
		var doubleThat = 2 * (yield (input / 2))
		var another = yield (doubleThat)
		return (input * doubleThat * another)
	}
	*factorial (number, acc = 1) {
		yield acc
		if (number > 1) 
		yield *factorial(number - 1, acc * number);
		}

}



c = new Calculadora (20,15)
const [resultado, resto] = c.division()
console.log("La multiplicación es: ",c.multiplicacion());
console.log("La suma es: ",c.suma());
console.log("La resta es: ",c.resta());
console.log("El resultado de la división es: ",resultado, "Con resto: ",resto)







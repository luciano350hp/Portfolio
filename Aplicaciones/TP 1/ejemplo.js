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
}

c = new Calculadora (20,15)
const [resultado, resto] = c.division()
console.log(resultado,resto)
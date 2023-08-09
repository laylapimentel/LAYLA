// AULA 1 - DIA 03/07/23
//                         JAVASCRIPT

//  operador (&&) = and
// exemplo 1 de codigo em aula:
var idade = 25;
var possuiCNH = true;
if (idade >= 18 && possuiCNH) {
    console.log("Pode dirigir!");
}

//  operador (||) = or
// exemplo 2 de codigo em aula:
var temCarro = true;
var temMoto = false;
if (temCarro || temMoto) {
    console.log("Tem um veiculo.");
}

//  Operador Not(!)  - negação
// exemplo 3 de codigo:
var temcarro = false;
if (!temCarro) {
    console.log("Não tem um carro.")
}

//  Tipos de variaveis: var, let, const:
// VAR = podendo ser uma variavel global.
// LET = só tem validade dentro do bloco em que está declarada.
// CONST = escopo de bloco, porém devem ser inicializadas no momento da declaração e não podem ter seu valor alterado.

// Pratica 2 - Crie um programa que some dois numeros e mostre-os na tela:
var soma = 1 + 2;
console.log(soma);

//  Comando if
// necessario abrir e fechar colchetes
//exeplo:
if (6 == 3) {
    console.log("A condição é atendida")
} else {
    console.log("A condição não é atendida")
}

// Pratica 3 - Crie um programa que cheque se o usuario é maior de idade sem a entrada do teclado:
var idade = 22;
if (idade >= 18) {
    console.log("É maior de idade");
} else {
    console.log("É menor de idade")
}


//            CONTINUAÇÃO DA AULA ANTERIOR - 04/07/23 

// Exemplo de codigo com elif versão javascript
var idade = 30;
if (idade < 30) {
    console.log ("Você é maior de idade.");
} else if (idade >= 18 && idade <= 65) {    //no lugar de elif é usado *else if*
    console.log("Você é adulto.");
} else {
    console.log("Você é idoso.");
}

// Pratica 4 - Crie um programa que cheque se o numero é positivo, negativo, ou zero. Sem emtrada do teclado:
var num = 10;
if (num > 0) {
    console.log("O número é positivo");
} else if (num == 0) {
    console.log("O numero é zero");
} else {
    console.log("O número é negativo")
}

// Pratica 5 - Faça um programa que verifique se o usuario pode votar ou não:
var idade = 17;
if (idade >= 16 && idade == 18) {
    console.log("Você pode votar opicionalmente!");
} else if (idade >= 18) {
    console.log("Você é obrigado a votar");
} else {
    console.log("Não pode votar")
}

//  FOR:
// for (inicialização; condição; expressão final)
// no fro a variavel fica dentro  ex: for (var i = 1; i <= 5; i++)

// Pratica 6 - Calcular a soma dos numeros de 1 a 10:
var soma = 0;
for (var i = 1; i <= 10; i++) {
    soma += i;
}
console.log("A soma dos numeros de 1 a 10 é: " + soma)

//  WHILE:
// while (condição)
// exemplo:
var contador = 0 
while (contador < 5) {
    console.log("contador: " + contador);
    contador++;
}

//  SWITCH
// exemplo:
var diaDaSemana = 7;
var mensagem;
switch (diaDaSemana) {
    case 1:
        mensagem = "Hoje é Segunda-feira"
        break;
    case 2:
        mensagem = "Hoje é Terça-feira"
    ...
}
console.log(mensagem);

//  LISTAS EM JAVASCRIPT
// exemplo 
let lista = [1, 2, 3,];
// acessando o primeiro elemento da lista
console.log(lista[0])

// adicionando elemento 4 ao final da lista
lista.push(4);    
console.log(lista)

// adicionar o 1 no inicio da lista
lista.unshift(1); 

// adicionando mais de um numero
lista.unshift(0, 1);     // adicionar o 1 e 0 no inicio da lista

// para substituir o numero na lista
lista.splice(2, 1, 3)

// removendo o ultimo elemento da lista
lista.pop()

// tamannho da lilsta 
let lista = [1, 2, 3, 4, 5]
for (let i = 0; i < lista.length; i++) {
    console.log(lista[i]);
}

// checando se o elemento esta na lista
let lista = [1, 2, 3, 4]
console.log(lista.includes(3))  // resultado = True


//  DECLARAÇÃO DE FUNÇÃO 
// exemplos
function soma (a, b) {
    return a + b;
}
function multiplicacao (a, b) {
    return a * b;
}
console.log(multiplicacao(2, 10))



//            CONTINUAÇÃO DA AULA ANTERIOR - 05/07/23 

// função para verificar se o numero é par ou impar
function isPar (numero) {
    return numero % 2 === 0;
}
console.log(isPar(4));     // resultado: true
console.log(isPar(7));     // resultado: false

//  DECLARAÇÃO DE UM OBJETO 
class Animal {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }
    emitirSom() {
        console.log("Oanimal emite um som");
    }
    apresentar() {
        console.log("Nome: $(this.nome)");
        console.log("Idade: $(this.idade)");
    }
}

// chamando a classe
let animal1 = new Animal("Leão", 5);
animal1.emitirSom()  // o animal emite som
animal1.apresentar();
// resultado: nome= leao idade = 5

//  criando a classe Pessoa 
class Pessoa {
    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade
    }
    apresentar() {
        console.log("Olá meu nome é $(this.nome) e tenho $(this.idade) anos.");
    }
}

// PRATICA 
class Pessoa {
    constructor(nome, idade, profissao) {
        this.nome = nome;
        this.idade = idade;
        this.profissao = profissao;
    }
    apresentar() {
        console.log("Olá meu nome é " + this.nome + " e tenho " + this.idade + " anos" )
    }
    job() {
        console.log("Está é minha profissão: " + this.profissao)
    }
}
let pessoa1 = new Pessoa ("Layla", 22, "Oceanografa"); {
    pessoa1.apresentar();
    pessoa1.job();
}

//  COMANDO ALERT

// DOM em javascript

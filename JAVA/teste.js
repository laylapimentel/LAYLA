


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
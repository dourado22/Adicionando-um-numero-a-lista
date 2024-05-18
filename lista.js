const prompt = require('prompt-sync')();

let lista = [1, 3, 5, 7, -2, -8];
console.log(lista);
console.log();

let newlista = [];

while (true) {
    let num = parseInt(prompt('Digite um número: '));
    if (!lista.includes(num)) {
        newlista.push(num);
    } else {
        console.log('ERRO! Número já existe, adicione outro número.');
    }

    let resp = '';
    while (!['S', 'N'].includes(resp)) {
        resp = prompt('Quer continuar? [S/N]: ').trim().toUpperCase();
    }
    if (resp === 'N') {
        break;
    }
}

console.log(`Os números ${newlista} foram adicionados com Sucesso à lista!`);

let combinedList = newlista.concat(lista);
combinedList.sort((a, b) => a - b);
console.log(`A nova lista é composta por esses números ${combinedList}`);

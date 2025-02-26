let listaDeCoisas = [];

// Função para adicionar um item à lista
function adicionarItem() {
    const itemInput = document.getElementById('item');
    const item = itemInput.value.trim();
    const resultado = document.getElementById('resultado');
    
    if (item === '') {
        // Se o item estiver vazio, não faz nada
        return;
    }

    if (listaDeCoisas.includes(item)) {
        // Se o item já estiver na lista, remove-o
        listaDeCoisas = listaDeCoisas.filter(i => i !== item);
        resultado.textContent = `Item "${item}" removido da lista!`;
        itemInput.value = "";
    } else {
        // Se o item não estiver na lista, adiciona-o
        listaDeCoisas.push(item);
        resultado.textContent = `Item "${item}" adicionado à lista!`;
        itemInput.value = "";
    }

    // Remove itens vazios da lista
    listaDeCoisas = listaDeCoisas.filter(item => item !== '');

    atualizarLista();
}

// Adicionar função para remover um item da lista por um botão, sem a necessidade de digitar o item novamente
function removerdaLista() {
    listaDeCoisas = listaDeCoisas.filter(i => i !== item);
    resultado.textContent = `Item "${item}" removido da lista!`;
    
    atualizarLista();
}

// Função para atualizar a lista exibida na tela
function atualizarLista() {
    const lista = document.getElementById('lista');
    lista.innerHTML = '';
    
    listaDeCoisas.forEach(item => {
        const li = document.createElement('li');
        li.textContent = item;
        lista.appendChild(li);
    });
}

// Função para sortear um item da lista
function sortear() {
    if (listaDeCoisas.length === 0) {
        alert('Adicione itens antes de sortear!');
        return;
    }

    const resultado = document.getElementById('resultado');
    resultado.textContent = 'Sorteando...';

    // Efeito de "sorteando"
    setTimeout(() => {
        const indice = Math.floor(Math.random() * listaDeCoisas.length);
        resultado.textContent = `Item sorteado: ${listaDeCoisas[indice]}`;
    }, 500);
}

// Adiciona event listener para a tecla Enter no campo de input
document.getElementById('item').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        adicionarItem();
    }
});

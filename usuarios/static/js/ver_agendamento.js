// Função JavaScript para ordenar a lista de agendamentos por data e hora em ordem inversa
document.addEventListener('DOMContentLoaded', function() {
    const list = document.getElementById('agendamentos-list');
    const items = Array.from(list.getElementsByTagName('li'));

    items.sort((a, b) => {
        const dateA = new Date(a.textContent.split(' - ')[1].replace(' às ', ' '));
        const dateB = new Date(b.textContent.split(' - ')[1].replace(' às ', ' '));
        return dateB - dateA;
    });

    items.forEach(item => list.appendChild(item));
});



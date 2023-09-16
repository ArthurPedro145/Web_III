document.getElementById('cadastro-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const senha = document.getElementById('senha').value;
    const confirmSenha = document.getElementById('confirm-senha').value;

    if (senha !== confirmSenha) {
        alert('As senhas não coincidem. Tente novamente.');
        return;
    }

    // Aqui você pode enviar os dados do formulário para o servidor (Python).
});


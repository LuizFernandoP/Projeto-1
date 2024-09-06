document.getElementById('recoveryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('usuario').value;
    const email = document.getElementById('email').value;
    const codigo = document.getElementById('codigo').value;
    const novaSenha = document.getElementById('password').value;

    if (novaSenha.length < 6) {
        alert("A nova senha deve ter pelo menos 6 caracteres.");
    } else {
        const formData = new URLSearchParams();
        formData.append('name', name);
        formData.append('email', email);
        formData.append('codigo', codigo);
        formData.append('new_password', novaSenha);

        fetch('http://127.0.0.1:5000/api/alterar_senha', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: formData.toString()
        })
        .then(response => {
            console.log('Resposta do servidor:', response);
            if (!response.ok) {
                throw new Error('Erro ao alterar a senha.');
            }
            return response.json();
        })
        .then(data => {
            alert('Senha alterada com sucesso!');
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Ocorreu um erro ao tentar alterar a senha.');
        });
    }
});

document.getElementById('recoveryForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const confirmEmail = document.getElementById('confirmEmail').value;

    if (email !== confirmEmail) {
        alert("Os e-mails não coincidem. Por favor, verifique.");
    } else {
        alert("Formulário enviado com sucesso!");
        //lógica p enviar os dados ao servidor
    }
});
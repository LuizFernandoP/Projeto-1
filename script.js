const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});

let login = document.getElementById('login');
let password = document.getElementById('password');

// Função para fazer login
function loginUser(email, password) {
	fetch('http://localhost:5000/api/login', { // Substitua pela URL da sua API
		method: 'POST',
		headers: {
			'Content-Type': 'application/x-www-form-urlencoded',
		},
		body: new URLSearchParams({
			'email': email,
			'password': password
		})
	})
		.then(response => response.json())
		.then(data => {
			if (data.message === 'Login bem-sucedido') {
				window.location.href = 'servico.html'; 
			} else {
				alert('Erro ao fazer login: ' + data.message);
			}
		})
		.catch(error => {
			console.error('Erro:', error);
			alert('Erro ao conectar-se com o servidor.');
		});
}

// Captura do evento de submissão do formulário de login
document.getElementById('signInForm').addEventListener('submit', function (event) {
	event.preventDefault(); // Evita o envio padrão do formulário

	let email = document.getElementById('signInEmail').value;
	let password = document.getElementById('signInPassword').value;

	// Chama a função de login com os valores capturados
	loginUser(email, password);
});
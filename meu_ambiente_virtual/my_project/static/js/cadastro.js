function validarSenha() {
            var password = document.getElementById("senha").value;

            // verificar o tamanho minimo da senha
            if (password.length < 8) {
                alert("A senha deve ter pelo menos 8 caracteres");
                return false;
            }

            // verificar senha 
            var uppercaseRegex = /[A-Z]/; //Regex é como uma máscara
            var numberRegex = /[0-9]/;
            //uma letra maiúscula e um número
            if (!uppercaseRegex.test(password) || !numberRegex.test(password)) {
                alert("A senha deve conter pelo menos uma letra e um numero");
                return false; // não passou na validação, retorna false
            }
            return true; // o formulário será enviado para a rota /autenticar
        }

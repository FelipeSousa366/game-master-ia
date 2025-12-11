document.addEventListener("DOMContentLoaded", function () {
    const characterCreation = document.getElementById("character-creation");
    const gameInterface = document.getElementById("game-interface");
    const chatHistory = document.getElementById("chat-history");
    const loadingIndicator = document.getElementById("loading");
    const userInput = document.getElementById("user-input");

    function startGame() {
        const nome = document.getElementById("nome").value;
        const classe = document.getElementById("classe").value;
        const origem = document.getElementById("origem").value;
        const aparencia = document.getElementById("aparencia").value;
        const contexto = document.getElementById("contexto").value;
        const mensagem = ""

        if (!nome || !classe || !origem) {
            alert("Preencha todos os campos obrigatórios!");
            return;
        }

        characterCreation.classList.add("hidden");
        gameInterface.classList.remove("hidden");
        //chatHistory.innerHTML = `<p><strong>Mestre:</strong> Bem-vindo, ${nome}! Você é um(a) ${classe} de ${origem}. Vamos começar sua jornada!</p>`;

        fetch("/start_game", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ mensagem, contexto, nome, classe, origem })
        })
        .then(response => response.json())
        .then(data => {
            chatHistory.innerHTML += `<p><strong>Mestre:</strong> ${data.resposta}</p>`;
            chatHistory.scrollTop = chatHistory.scrollHeight;
        })
        .catch(error => {
            console.error("Erro ao enviar mensagem:", error);
            chatHistory.innerHTML += `<p><strong>Mestre:</strong> Ocorreu um erro ao processar sua ação.</p>`;
        })
        .finally(() => {
            loadingIndicator.style.display = "none";
        });
    }

    function sendMessage() {
        const mensagem = userInput.value.trim();
        if (mensagem === "") return;

        chatHistory.innerHTML += `<p><strong>Você:</strong> ${mensagem}</p>`;
        userInput.value = "";
        loadingIndicator.style.display = "block";
        
        const nome = document.getElementById("nome").value;
        const classe = document.getElementById("classe").value;
        const origem = document.getElementById("origem").value;
        const contexto = document.getElementById("contexto").value;

        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ mensagem, contexto, nome, classe, origem })
        })
        .then(response => response.json())
        .then(data => {
            chatHistory.innerHTML += `<p><strong>Mestre:</strong> ${data.resposta}</p>`;
            chatHistory.scrollTop = chatHistory.scrollHeight;
        })
        .catch(error => {
            console.error("Erro ao enviar mensagem:", error);
            chatHistory.innerHTML += `<p><strong>Mestre:</strong> Ocorreu um erro ao processar sua ação.</p>`;
        })
        .finally(() => {
            loadingIndicator.style.display = "none";
        });
    }

    window.startGame = startGame;
    window.sendMessage = sendMessage;
});

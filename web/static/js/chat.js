const textarea = document.getElementById("message");
const sendButton = document.getElementById("sendButton");
const chat = document.getElementById("chat");
const homeScreen = document.getElementById("homeScreen");
const newChatButton = document.querySelector(".new-chat");

/* ===========================================
   Auto Resize
=========================================== */

textarea.addEventListener("input", () => {

    textarea.style.height = "auto";
    textarea.style.height = textarea.scrollHeight + "px";

});

/* ===========================================
   Enter envia
=========================================== */

textarea.addEventListener("keydown", (e) => {

    if (e.key === "Enter" && !e.shiftKey) {

        e.preventDefault();

        sendMessage();

    }

});

sendButton.addEventListener("click", sendMessage);

newChatButton.addEventListener("click", newConversation);

/* ===========================================
   Mensagem
=========================================== */

async function sendMessage() {

    const text = textarea.value.trim();

    if (!text)
        return;

    addMessage("user", text);

    hideHome();

    textarea.value = "";
    textarea.style.height = "58px";

    const thinking = addThinking();

    try {

        /*
            Aqui entraremos no FastAPI.

            const response = await fetch("/chat", {...});
        */

        await sleep(1200);

        thinking.remove();

        addMessage(
            "assistant",
            "Integração com o VersaKernel em andamento..."
        );

    }
    catch (err) {

        thinking.remove();

        addMessage(
            "assistant",
            "Erro ao conectar com a Versa IA."
        );

    }

}

/* ===========================================
   Usuário / IA
=========================================== */

function addMessage(type, text) {

    const div = document.createElement("div");

    div.className = "message " + type;

    div.innerHTML = `
        <div class="bubble">
            ${text}
        </div>
    `;

    chat.appendChild(div);

    scrollBottom();

}

/* ===========================================
   Pensando...
=========================================== */

function addThinking() {

    const div = document.createElement("div");

    div.className = "message assistant thinking";

    div.innerHTML = `
        <div class="bubble">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    chat.appendChild(div);

    scrollBottom();

    return div;

}

/* ===========================================
   Scroll
=========================================== */

function scrollBottom() {

    chat.scrollTop = chat.scrollHeight;

}

/* ===========================================
   Delay
=========================================== */

function sleep(ms){

    return new Promise(resolve => setTimeout(resolve, ms));

}

function hideHome(){

    if(homeScreen){

        homeScreen.style.display = "none";

    }

}

function showHome(){

    if(homeScreen){

        homeScreen.style.display = "flex";

    }

}

function clearConversation(){

    chat.innerHTML = "";

}

function newConversation(){

    clearConversation();

    showHome();

    textarea.value = "";

    textarea.style.height = "58px";

    textarea.focus();

}
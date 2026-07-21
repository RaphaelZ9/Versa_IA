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

        await sleep(800);

        thinking.remove();

        thinking.remove();

        await typeAssistantMessage(
            "Integração com o VersaKernel em andamento..."
        );

    }
    catch (err) {

        thinking.remove();

        thinking.remove();

        await typeAssistantMessage(
            "Erro ao conectar com a Versa IA."
        );

    }

}

/* ===========================================
   Usuário / IA
=========================================== */

function addMessage(type, text) {

    const message = document.createElement("div");

    message.className = `message ${type}`;

    const title = type === "user"
        ? "👤 Você"
        : "⚡ Versa IA";

    message.innerHTML = `

        <div class="bubble">

            <div class="message-header">

                <span class="author">

                    ${title}

                </span>

                <span class="time">

                    ${getCurrentTime()}

                </span>

            </div>

            <div class="message-content">

                ${text}

            </div>

        </div>

    `;

    chat.appendChild(message);

    scrollBottom();

}

async function typeAssistantMessage(text){

    const message = document.createElement("div");

    message.className = "message assistant";

    message.innerHTML = `
        <div class="bubble">

            <div class="message-header">

                <span class="author">

                    ⚡ Versa IA

                </span>

                <span class="time">

                    ${getCurrentTime()}

                </span>

            </div>

            <div class="message-content"></div>

        </div>
    `;

    chat.appendChild(message);

    const content = message.querySelector(".message-content");

    scrollBottom();

    for(let i = 0; i < text.length; i++){

        content.textContent += text[i];

        scrollBottom();

        await sleep(12);

    }

}
/* ===========================================
   Pensando...
=========================================== */

function addThinking(){

    const div = document.createElement("div");

    div.className = "message assistant thinking";

    div.innerHTML = `

        <div class="bubble">

            <div class="message-header">

                <span class="author">

                    ⚡ Versa IA

                </span>

            </div>

            <div class="message-content">

                <span></span>

                <span></span>

                <span></span>

            </div>

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

function getCurrentTime(){

    const now = new Date();

    return now.toLocaleTimeString("pt-BR",{

        hour:"2-digit",

        minute:"2-digit"

    });

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
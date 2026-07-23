/******************************************************************************
 * Versa IA - Chat MVP
 ******************************************************************************/

const form = document.getElementById("chatForm");
const input = document.getElementById("promptInput");

const hero = document.getElementById("hero");
const chat = document.getElementById("chat");
const chatContainer = document.getElementById("chatContainer");

/******************************************************************************
 * Templates
 ******************************************************************************/

const userTemplate = document.getElementById("userMessageTemplate");
const assistantTemplate = document.getElementById("assistantMessageTemplate");
const thinkingTemplate = document.getElementById("thinkingTemplate");

let thinkingNode = null;

const sendButton = document.getElementById("sendButton");

/******************************************************************************
 * Inicialização
 ******************************************************************************/

hideThinking();

input.focus();

/******************************************************************************
 * Eventos
 ******************************************************************************/

form.addEventListener("submit", function (e) {
  e.preventDefault();

  sendMessage();
});

input.addEventListener("keydown", function (e) {
  if (e.key === "Enter" && !e.shiftKey) {
    e.preventDefault();

    sendMessage();
  }
});

/******************************************************************************
 * Envio
 ******************************************************************************/

async function sendMessage() {
  const message = input.value.trim();

  if (message === "") return;

  showChat();

  addMessage("user", message);

  input.value = "";

  showThinking();

  disableInput();

  try {
    const response = await fetch("/chat", {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message: message,
      }),
    });

    if (!response.ok) throw new Error("Erro ao acessar a API.");

    const json = await response.json();

    hideThinking();

    addMessage("assistant", json.response);
  } catch (error) {
    hideThinking();

    addMessage("assistant", "Erro: " + error.message);
  }

  enableInput();
}

/******************************************************************************
 * Interface
 ******************************************************************************/

function showChat() {
  hero.style.display = "fade-out";

  chat.style.display = "block";
}

function showThinking() {
  if (thinkingNode) return;

  thinkingNode = thinkingTemplate.content.cloneNode(true);

  chatContainer.appendChild(thinkingNode);

  scrollBottom();
}

function hideThinking() {
  const node = chatContainer.querySelector(".thinking-message");

  if (node) node.remove();

  thinkingNode = null;
}

function disableInput() {
  input.disabled = true;

  sendButton.disabled = true;
}

function enableInput() {
  input.disabled = false;

  sendButton.disabled = false;

  input.focus();
}

function scrollBottom() {
  window.scrollTo({
    top: document.body.scrollHeight,

    behavior: "smooth",
  });
}

/******************************************************************************
 * Mensagens
 ******************************************************************************/

function addMessage(role, text) {
  const template = role === "user" ? userTemplate : assistantTemplate;

  const fragment = template.content.cloneNode(true);

  const bubble = fragment.querySelector(".message-bubble");

  if (!bubble) {
    console.error("Template inválido:", template.id);
    return;
  }

  bubble.textContent = text;

  chatContainer.appendChild(fragment);

  scrollBottom();
}

/******************************************************************************
 * Utilidades
 ******************************************************************************/

function escapeHtml(text) {
  return text

    .replace(/&/g, "&amp;")

    .replace(/</g, "&lt;")

    .replace(/>/g, "&gt;");
}

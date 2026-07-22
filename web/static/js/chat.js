/*
===============================================================================
Versa IA
Chat Controller

Versão : 2.0
Autor   : Versa Energia

Descrição
-------------------------------------------------------------------------------
Frontend responsável por:

• Comunicação com a API
• Renderização das mensagens
• Streaming
• Markdown
• Highlight.js
• Upload de arquivos
• Histórico
• Controle da interface

===============================================================================
*/


/* =============================================================================
   API
============================================================================= */

class VersaAPI {

    constructor(baseUrl = "") {

        this.baseUrl = baseUrl;

    }

    async chat(message, signal = null) {

        const response = await fetch(

            `${this.baseUrl}/chat`,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    message

                }),

                signal

            }

        );

        if (!response.ok) {

            throw new Error(

                "Erro ao consultar a IA."

            );

        }

        return await response.json();

    }

}


/* =============================================================================
   CHAT
============================================================================= */

class VersaChat {

    constructor() {

        /* Estado */

        this.api = new VersaAPI();

        this.abortController = null;

        this.isWaiting = false;

        this.attachments = [];

        /* Inicialização */

        this.cacheDOM();

        this.bindEvents();

        this.initialize();

    }

    /* =========================================================================
       CACHE DOM
    ========================================================================= */

    cacheDOM() {

        /* Layout */

        this.hero =
            document.getElementById("hero");

        this.chat =
            document.getElementById("chat");

        this.chatContainer =
            document.getElementById("chatContainer");

        this.thinking =
            document.getElementById("thinking");

        /* Composer */

        this.chatForm =
            document.getElementById("chatForm");

        this.promptInput =
            document.getElementById("promptInput");

        this.sendButton =
            document.getElementById("sendButton");

        this.stopButton =
            document.getElementById("stopButton");

        this.attachButton =
            document.getElementById("attachButton");

        this.fileInput =
            document.getElementById("fileInput");

        this.attachmentList =
            document.getElementById("attachmentList");

        /* Sidebar */

        this.btnNewChat =
            document.getElementById("btnNewChat");

        this.sidebarNewChat =
            document.getElementById("newChatButton");

        /* Templates */

        this.userTemplate =
            document.getElementById("userMessageTemplate");

        this.assistantTemplate =
            document.getElementById("assistantMessageTemplate");

    }

    /* =========================================================================
       INITIALIZE
    ========================================================================= */

    initialize() {

        this.hideThinking();

        this.chat.classList.add("hidden");

        this.hero.classList.remove("hidden");

        this.autoResize();

        this.promptInput.focus();

    }

    /* =========================================================================
       EVENTS
    ========================================================================= */

    bindEvents() {

        this.chatForm.addEventListener(

            "submit",

            (e) => {

                e.preventDefault();

                this.send();

            }

        );

        this.promptInput.addEventListener(

            "keydown",

            (e) => {

                if (

                    e.key === "Enter"

                    &&

                    !e.shiftKey

                ) {

                    e.preventDefault();

                    this.send();

                }

            }

        );

        this.promptInput.addEventListener(

            "input",

            () => this.autoResize()

        );

        this.btnNewChat?.addEventListener(

            "click",

            () => this.newChat()

        );

        this.sidebarNewChat?.addEventListener(

            "click",

            () => this.newChat()

        );

        this.stopButton?.addEventListener(

            "click",

            () => this.abort()

        );

    }

    /* =========================================================================
       NEW CHAT
    ========================================================================= */

    newChat() {

        this.chatContainer.innerHTML = "";

        this.promptInput.value = "";

        this.attachments = [];

        this.autoResize();

        this.hideThinking();

        this.hero.classList.remove(

            "hidden"

        );

        this.chat.classList.add(

            "hidden"

        );

        this.promptInput.focus();

    }

    /* =========================================================================
       START CHAT
    ========================================================================= */

    startConversation() {

        this.hero.classList.add(

            "hidden"

        );

        this.chat.classList.remove(

            "hidden"

        );

    }

    /* =========================================================================
       AUTO RESIZE
    ========================================================================= */

    autoResize() {

        this.promptInput.style.height =

            "auto";

        this.promptInput.style.height =

            this.promptInput.scrollHeight + "px";

    }
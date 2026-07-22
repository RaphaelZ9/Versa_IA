class ModelSelector {

    constructor() {

        this.models = [];

        this.selectedModel = null;

        this.trigger = document.getElementById("modelSelectorTrigger");
        this.dropdown = document.getElementById("modelDropdown");

        this.name = document.getElementById("currentModelName");
        this.provider = document.getElementById("currentModelProvider");

        this.initialize();

    }

    async initialize() {

        await this.loadModels();

        this.registerEvents();

    }

    async loadModels() {

        // Temporário (sexta trocamos pela API)

        this.models = [

            {
                id: "qwen3:8b",
                name: "Qwen 3 8B",
                provider: "Local • Ollama",
                description: "Modelo recomendado",
                active: true
            },

            {
                id: "deepseek-r1:latest",
                name: "DeepSeek R1",
                provider: "Local • Ollama",
                description: "Excelente para raciocínio"
            },

            {
                id: "llama3.3:latest",
                name: "Llama 3.3",
                provider: "Meta",
                description: "Modelo geral"
            },

            {
                id: "gemma3:latest",
                name: "Gemma 3",
                provider: "Google",
                description: "Rápido e leve"
            }

        ];

        this.selectedModel = this.models[0];

        this.render();

    }

    render() {

        this.dropdown.innerHTML = "";

        this.models.forEach(model => {

            const item = document.createElement("div");

            item.className = "model-item";

            if (this.selectedModel.id === model.id) {

                item.classList.add("active");

            }

            item.innerHTML = `

                <div class="model-item-left">

                    <div class="model-status"></div>

                    <div>

                        <div class="model-item-name">

                            ${model.name}

                        </div>

                        <div class="model-item-description">

                            ${model.description}

                        </div>

                        <div class="model-item-provider">

                            ${model.provider}

                        </div>

                    </div>

                </div>

                ${this.selectedModel.id===model.id ?
                    '<div class="model-check">✓</div>'
                    : ""
                }

            `;

            item.onclick = () => this.select(model);

            this.dropdown.appendChild(item);

        });

    }

    select(model) {

        this.selectedModel = model;

        this.name.textContent = model.name;

        this.provider.textContent = model.provider;

        localStorage.setItem(
            "versa-model",
            model.id
        );

        this.render();

        this.close();

    }

    registerEvents() {

        this.trigger.addEventListener("click", () => {

            this.dropdown.classList.toggle("show");

            this.trigger.classList.toggle("open");

        });

        document.addEventListener("click", e => {

            if (!e.target.closest(".model-selector")) {

                this.close();

            }

        });

    }

    close() {

        this.dropdown.classList.remove("show");

        this.trigger.classList.remove("open");

    }

}

window.addEventListener("DOMContentLoaded", () => {

    window.modelSelector = new ModelSelector();

});
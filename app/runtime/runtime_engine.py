from app.ai.model_manager import ModelManager
from app.context.context_manager import ContextManager
from app.conversation.conversation_manager import ConversationManager
from app.knowledge.search.search_manager import SearchManager
from app.intent.intent_manager import IntentManager
from app.capabilities.capability_manager import CapabilityManager
from app.capabilities.capability_type import CapabilityType
from app.core.logger import get_logger


class ChatPipeline:

    def __init__(self):

        self.logger = get_logger("ChatPipeline")

        self.model_manager = ModelManager()

        self.conversation_manager = ConversationManager()

        self.context_manager = ContextManager()

        self.search_manager = SearchManager()

        self.intent_manager = IntentManager()

        self.capability_manager = CapabilityManager()

    def initialize(self):

        self.logger.info("Chat Pipeline iniciado.")

        self.model_manager.initialize()

    def execute(self, message: str):

        self.logger.debug(f"Mensagem: {message}")

        intent = self.intent_manager.detect(message)

        self.logger.info(f"Intent detectada: {intent.name}")

        capabilities = self.capability_manager.plan(
            message,
            intent
        )

        self.logger.info(
            "Capabilities: %s",
            [capability.name for capability in capabilities]
        )

        self.conversation_manager.add_user_message(message)


        search_result = None

        if CapabilityType.SEARCH in capabilities:

            self.logger.info("Executando SearchManager...")

            search_result = self.search_manager.search(message)

        else:

            self.logger.info("Pesquisa não necessária.")


        self.context_manager.set_conversation(
            self.conversation_manager.get_conversation()
        )

        if search_result:

            self.context_manager.set_search_result(
                search_result
            )

        context = self.context_manager.get_context()

        response = self.model_manager.chat(context)


        self.conversation_manager.add_assistant_message(
            response.content
        )

        return response

    def shutdown(self):

        self.model_manager.shutdown()

        self.logger.info("Chat Pipeline finalizado.")
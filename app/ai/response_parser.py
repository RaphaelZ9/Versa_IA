from app.domain.entities.ai_response import AIResponse


class ResponseParser:

    def parse(self, response: str) -> AIResponse:

        return AIResponse(
            content=response.strip()
        )
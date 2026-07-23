from time import perf_counter
import traceback

from fastapi import APIRouter, HTTPException, status

from app.api.models.chat_models import (
    ChatRequest,
    ChatResponse,
)

from app.services.chat_service import chat_service


router = APIRouter(
    tags=["Chat"]
)


@router.on_event("startup")
def startup() -> None:
    """
    Inicializa a Versa IA quando a API sobe.
    """
    chat_service.initialize()


@router.on_event("shutdown")
def shutdown() -> None:
    """
    Finaliza a Versa IA quando a API é encerrada.
    """
    chat_service.shutdown()


@router.post(
    "/chat",
    response_model=ChatResponse,
    status_code=status.HTTP_200_OK,
)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Endpoint principal do chat.
    """

    started = perf_counter()

    try:

        result = chat_service.chat(request.message)

        elapsed = int((perf_counter() - started) * 1000)

        return ChatResponse(
            success=True,
            response=result["response"],
            conversation_id=request.conversation_id,
            elapsed_ms=elapsed,
            error=None,
        )

    except Exception as exc:

        print("\n" + "=" * 80)
        print("ERRO NO ENDPOINT /chat")
        traceback.print_exc()
        print("=" * 80 + "\n")

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(exc),
        )
import httpx
from dotenv import load_dotenv

load_dotenv()


class AIClient:
    def __init__(self, api_key: str, model: str, base_url: str) -> None:
        self.api_key = api_key
        self.model = model
        self.base_url = base_url

        self.client = httpx.AsyncClient(timeout=30.0)

    async def send_prompt(self, prompt: str):
        body = self._build_request_body(prompt)
        try:
            response = await self.client.post(
                url=f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}",
                json=body,
            )
            response.raise_for_status()
            response_json = response.json()
            reply = self._extract_response(response_json)
            return reply
        except Exception as e:
            import traceback

            traceback.print_exc()
            return str(e)

    def _create_headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        return headers

    def _build_request_body(self, prompt: str) -> dict:
        return {"contents": [{"parts": [{"text": prompt}]}]}

    def _extract_response(self, response_json: dict) -> str:
        return response_json["candidates"][0]["content"]["parts"][0]["text"]

    def _handle_errors(self):
        pass

    async def close(self):
        await self.client.aclose()

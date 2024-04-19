from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
@app.get("/")
async def get():
    with open('index.html', 'r') as file:
        return HTMLResponse(file.read())
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


if __name__ == '__main__':
    uvicorn.run(app)
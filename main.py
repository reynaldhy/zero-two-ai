from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="ZERO TWO AI")

class Request(BaseModel):
    prompt: str

@app.get("/", response_class=HTMLResponse)
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<title>ZERO TWO AI</title>
<script src='https://cdn.tailwindcss.com'></script>
</head>
<body class='bg-black text-white flex flex-col items-center justify-center h-screen px-4'>
<h1 class='text-5xl text-red-600 font-bold'>ZERO TWO AI</h1>
<p class='text-gray-400 mb-4 text-center'>Cyber Security & OSINT</p>

<textarea id='q' class='bg-gray-900 p-3 w-full max-w-sm h-24 rounded border border-gray-700'
 placeholder='What can I secure today?'></textarea>

<button onclick='go()'
 class='bg-red-600 px-6 py-2 mt-3 rounded'>Analyze</button>

<pre id='o'
 class='bg-gray-900 p-3 w-full max-w-sm mt-4 rounded text-sm whitespace-pre-wrap'></pre>

<script>
async function go(){
 const r = await fetch('/analyze',{
  method:'POST',
  headers:{'Content-Type':'application/json'},
  body:JSON.stringify({prompt:q.value})
 });
 const d = await r.json();
 o.textContent = d.result;
}
</script>
</body>
</html>
"""

@app.post("/analyze")
def analyze(req: Request):
    text = req.prompt.lower()
    if "osint" in text:
        return {"result":"🛰️ ZERO TWO AI — OSINT MODE\\nExposure Level: MEDIUM"}
    return {"result":"🔐 ZERO TWO AI — SECURITY MODE\\nRisk Level: MEDIUM"}

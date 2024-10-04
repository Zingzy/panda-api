from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (
    JSONResponse,
    FileResponse,
    StreamingResponse,
    RedirectResponse,
)
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from cachetools import TTLCache
import random
from io import BytesIO
import os
import json
import uvicorn


app = FastAPI(title="Panda API", description="An API for pandas", version="0.0.1")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Enable CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("facts.txt", "r") as f:
    panda_facts = f.readlines()

panda_facts = [i.strip() for i in panda_facts]

panda_pics = os.listdir("images")
with open("images.json", "r") as f:
    pics_json = json.loads(f.read())

panda_gifs = os.listdir("gifs")
with open("gifs.json", "r") as f:
    gifs_json = json.loads(f.read())


def create_cache():
    return TTLCache(maxsize=100, ttl=3600)


cache = Depends(create_cache)


@app.get("/")
async def read_root(request: Request):
    base_url = str(request.base_url)
    base_url_no_http = base_url[base_url.find("//")+2:-1]
    return templates.TemplateResponse("index.html", {"request": request, "base_url": request.base_url, "base_url_no_http": base_url_no_http})


@app.get("/fact", tags=["facts"])
def get_random_fact():
    return JSONResponse(content={"fact": random.choice(panda_facts)})


@app.get("/pic", tags=["pics"])
def get_random_pic(request: Request):
    return JSONResponse(
        content={"url": f"{request.base_url}i/{random.choice(panda_pics)}"}
    )


@app.get("/gif", tags=["gifs"])
def get_random_gif(request: Request):
    return JSONResponse(
        content={"url": f"{request.base_url}g/{random.choice(panda_gifs)}"}
    )


@app.get("/raw_pic", tags=["pics"])
async def get_random_pic_raw():
    random_pic = random.choice(panda_pics)
    return RedirectResponse(url=pics_json[random_pic])


@app.get("/raw_gif", tags=["gifs"])
async def get_random_gif_raw():
    random_gif = random.choice(panda_gifs)
    return RedirectResponse(url=gifs_json[random_gif])


@app.get("/all", tags=["facts", "pics", "gifs"])
def get_random_fact_and_pic(request: Request):
    return JSONResponse(
        content={
            "fact": random.choice(panda_facts),
            "pic": f"{request.base_url}i/{random.choice(panda_pics)}",
            "gif": f"{request.base_url}g/{random.choice(panda_gifs)}",
        }
    )


@app.get("/all-facts", tags=["facts"])
def get_all_facts():
    return JSONResponse(content={"facts": panda_facts})


@app.get("/all-pics", tags=["pics"])
def get_all_pics(request: Request):
    pics = [f"{request.base_url}i/{i}" for i in panda_pics]
    return JSONResponse(content={"pics": pics})


@app.get("/all-gifs", tags=["gifs"])
def get_all_gifs(request: Request):
    gifs = [f"{request.base_url}g/{i}" for i in panda_gifs]
    return JSONResponse(content={"gifs": gifs})


@app.get("/i/{file_name}", tags=["pics"])
async def get_image(file_name: str, cache: TTLCache = Depends(create_cache)):
    file_path = f"images/{file_name}"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    cached_response = cache.get(file_name)
    if cached_response:
        return cached_response

    return RedirectResponse(url=pics_json[file_name])


@app.get("/g/{file_name}", tags=["gifs"])
async def get_gif(file_name: str, cache: TTLCache = Depends(create_cache)):
    file_path = f"gifs/{file_name}"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    cached_response = cache.get(file_name)
    if cached_response:
        return cached_response

    return RedirectResponse(url=gifs_json[file_name])


@app.get("/health", tags=["health"])
def health():
    return JSONResponse(content={"status": "ok"})


@app.get("/stats", tags=["stats"])
def get_stats():
    num_images = len(panda_pics)
    num_quotes = len(panda_facts)
    num_gifs = len(panda_gifs)

    return JSONResponse(
        content={
            "num_images": num_images,
            "num_gifs": num_gifs,
            "num_quotes": num_quotes,
        }
    )

@app.get("/sitemap.xml", tags=["sitemap"])
def sitemap(cache: TTLCache = Depends(create_cache)):
    return FileResponse(r"static/sitemap.xml")

@app.get("/robots.txt", tags=["robots"])
def robots(cache: TTLCache = Depends(create_cache)):
    return FileResponse(r"static/robots.txt")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

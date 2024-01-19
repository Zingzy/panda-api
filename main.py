from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse, StreamingResponse, RedirectResponse
from cachetools import TTLCache
import random
from io import BytesIO
import os
import uvicorn

app = FastAPI(title="Panda API", description="An API for pandas", version="0.0.1")

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

panda_gifs = os.listdir("gifs")


def create_cache():
    return TTLCache(maxsize=100, ttl=3600)


cache = Depends(create_cache)


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
    random_pic_path = f"images/{random.choice(panda_pics)}"
    with open(random_pic_path, "rb") as file:
        contents = file.read()
    return StreamingResponse(BytesIO(contents), media_type="image/jpeg")


@app.get("/raw_gif", tags=["gifs"])
async def get_random_gif_raw():
    random_gif_path = f"gifs/{random.choice(panda_gifs)}"
    with open(random_gif_path, "rb") as file:
        contents = file.read()
    return StreamingResponse(BytesIO(contents), media_type="image/gif")


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

    response = FileResponse(file_path, media_type="image/jpeg")
    cache[file_name] = response
    return response


@app.get("/g/{file_name}", tags=["gifs"])
async def get_gif(file_name: str, cache: TTLCache = Depends(create_cache)):
    file_path = f"gifs/{file_name}"
    if not os.path.isfile(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    cached_response = cache.get(file_name)
    if cached_response:
        return cached_response

    response = FileResponse(file_path, media_type="image/gif")
    cache[file_name] = response
    return response


@app.get('/health', tags=["health"])
def health():
    return JSONResponse(content={"status": "ok"})


@app.get("/stats", tags=["stats"])
def get_stats():
    num_images = len(panda_pics)
    num_quotes = len(panda_facts)
    num_gifs = len(panda_gifs)

    return JSONResponse(content={"num_images": num_images, "num_gifs": num_gifs, "num_quotes": num_quotes})


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
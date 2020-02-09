import random

from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from foods import foods

templates = Jinja2Templates(directory="templates")


def slugify(string):
    return string.lower().replace(" ", "-")


def get_context_data(request, food, attribution_username, attribution_name):
    return {
        "food": food.title(),
        "attribution_username": attribution_username,
        "attribution_name": attribution_name,
        "title": "Things my mum doesn't eat",
        "description": "Things my mum doesn't eat",
        "request": request,
    }


def home(request):
    food, attribution_username, attribution_name = random.choice(foods)

    return templates.TemplateResponse(
        "food.html",
        get_context_data(request, food, attribution_username, attribution_name),
    )


routes = [
    Route("/", home),
    Mount("/static", StaticFiles(directory="static")),
]

app = Starlette(routes=routes)

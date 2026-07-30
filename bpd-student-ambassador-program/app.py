"""
This is a simple app setup script created with `render-engine init`
"""

from render_engine import (
    Site,
    Page,
    Collection,
    Blog
)
from render_engine_markdown import MarkdownPageParser

app = Site()
app.output_path = "output"

app.site_vars.update(
{
    "SITE_TITLE":"BPD Student Ambassador Program",
    "SITE_URL":"https://students.blackpythondevs.com",
    "NAVIGATION":[
        {
            "name": "Join",
            "url": "/",
        },
        {
            "name": "About",
            "url": "/",
        },
        {
            "name": "Cohort",
            "url": "/",
        },
        {
            "name": "What is BPD ?",
            "url": "/"
        }
    ]
})

@app.page
class Index(Page):
    template = "index.html"

@app.collection
class Pages(Collection):
    content_path = "content/pages" # path to content files
    routes = ["./"] # route to collection page
    template = "page.html"

@app.collection
class Blog(Blog):
    content_path = "content/blog" # path to content files
    routes = ["blog"] # route to collection page
    pageParser = MarkdownPageParser
    template = "page.html"

if __name__ == "__main__":
    app.render()

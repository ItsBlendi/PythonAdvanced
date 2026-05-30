from django.templatetags.i18n import language
from fastapi import FastAPI
from scipy.stats import describe

from model import Developer, Projects

app = FastAPI()

@app.post("/developrs/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", "developer": devloper}


@app.post("/projects/")
def create_project(project: Projects):
    return {"message": "Projects created successfully", "project": project}


@app.get("/projects/")
def get_projects():
    sample_project = Projects(
        title = "Sample Project",
        description = "This is a sample project",
        language = ["HTML", "CSS", "JAVASCRIPT"]
        lead_developer = Developer(name= "John Doe", experience=5)
    )

    return {"projects": [sample_project]}






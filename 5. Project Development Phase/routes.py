from fastapi import APIRouter, Form

router = APIRouter()


@router.post("/generate-workout")
def generate_workout(
    name: str = Form(...),
    age: int = Form(...),
    weight: float = Form(...)
):
    return {
        "name": name,
        "age": age,
        "weight": weight,
        "message": "Workout plan generated successfully!"
    }
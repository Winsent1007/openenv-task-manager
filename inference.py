from fastapi import FastAPI

app = FastAPI()

db = {"tasks": []}
step_count = 0
max_steps = 10


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/reset")
def reset():
    global db, step_count
    db = {"tasks": []}
    step_count = 0
    return {
        "observation": db,
        "reward": 0,
        "done": False
    }


@app.post("/step")
def step(action: dict):
    global db, step_count

    step_count += 1
    reward = 0

    if action["cmd"] == "add":
        db["tasks"].append({
            "id": len(db["tasks"]),
            "text": action["task"],
            "status": "pending"
        })
        reward = 1

    elif action["cmd"] == "done":
        idx = action["id"]
        if 0 <= idx < len(db["tasks"]):
            db["tasks"][idx]["status"] = "completed"
            reward = 5

    done = step_count >= max_steps

    return {
        "observation": db,
        "reward": reward,
        "done": done
    }

import requests

BASE_URL = "http://127.0.0.1:8000"


def reset():
    return requests.post(f"{BASE_URL}/reset").json()


def step(action):
    return requests.post(f"{BASE_URL}/step", json=action).json()


if __name__ == "__main__":
    task_name = "task-manager"

    # 🔹 START
    print(f"[START] task={task_name}", flush=True)

    obs = reset()

    total_reward = 0
    steps = 0

    # Add tasks
    actions = [
        {"cmd": "add", "task": "Study"},
        {"cmd": "add", "task": "Workout"},
        {"cmd": "done", "id": 0},
        {"cmd": "done", "id": 1},
    ]

    for action in actions:
        result = step(action)

        reward = result.get("reward", 0)
        total_reward += reward
        steps += 1

        # 🔹 STEP
        print(f"[STEP] step={steps} reward={reward}", flush=True)

        if result.get("done"):
            break

    score = total_reward / max(steps, 1)

    # 🔹 END
    print(f"[END] task={task_name} score={score} steps={steps}", flush=True)
    

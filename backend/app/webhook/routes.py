from flask import Blueprint, json, request, jsonify
from datetime import datetime
from app.extensions import get_database
import uuid

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')
db = get_database()
actions_collection = db["gitaction"]

@webhook.route('/receiver', methods=["POST"]) 
def receiver():
    payload = request.json
    # print('message',payload)
    event_type = request.headers.get("X-GitHub-Event")  
    request_id = str(uuid.uuid4())
    author = payload.get("pusher", {}).get("name") if event_type == "push" else payload.get("sender", {}).get("login")
    timestamp = datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")
    from_branch = None
    to_branch = None

    if event_type == "push":
        from_branch = payload["ref"].split("/")[-1]
        action = "PUSH"

    elif event_type == "pull_request":
        action = payload.get("action")
        print('action perform=',action)
        if action == "closed" and payload["pull_request"].get("merged"):
            from_branch = payload["pull_request"]["head"]["ref"]
            to_branch = payload["pull_request"]["base"]["ref"]
            action="MERGE"
        else:
            from_branch = payload["pull_request"]["head"]["ref"]
            to_branch = payload["pull_request"]["base"]["ref"]
            action = "PULL_REQUEST"

    event_data = {
        "request_id": request_id,
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }

    actions_collection.insert_one(event_data)
    return jsonify({"status": "Event recorded successfully", "request_id": request_id})

@webhook.route("/gitaction", methods=["GET"])
def get_action():
    actions = list(actions_collection.find({}, {"_id": 0}))
    return jsonify({"events": actions})
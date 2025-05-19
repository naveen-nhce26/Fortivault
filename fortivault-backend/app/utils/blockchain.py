blockchain_log = []

def log_blockchain_action(action: str, user: str):
    blockchain_log.append({"action": action, "user": user})

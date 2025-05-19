def analyze_file_risk(file_content: str) -> str:
    if "virus" in file_content.lower():
        return "High"
    elif "sensitive" in file_content.lower():
        return "Medium"
    return "Low"

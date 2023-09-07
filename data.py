from datetime import datetime

def get_current_day():
    # Get the current day as a string (e.g., "Monday")
    return datetime.now().strftime("%A")

def get_utc_time():
    # Get the current UTC time in ISO 8601 format
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

data = {
    "slack_name": "Franca Mgbogu",
    "current_day": get_current_day(),  
    "utc_time": get_utc_time(),        
    "track": "backend",
    "github_file_url": "https://github.com/franciedigital/HNG/blob/master/main.py",
    "github_repo_url": "https://github.com/franciedigital/HNG",
    "status_code": 200
}
import requests
from typing import Optional, Dict, Any

def Get(url: str, headers: Optional[Dict[str, str]] = None, params: Optional[Dict[str, Any]] = None) -> dict:
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        try:
            data = response.json()
        except ValueError:
            data = response.text
        return {"status": response.status_code, "data": data, "error": None}
    except requests.exceptions.RequestException as e:
        return {"status": None, "data": None, "error": str(e)}
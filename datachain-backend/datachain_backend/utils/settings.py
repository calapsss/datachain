from typing import Dict, Optional, Tuple, Union
from dotenv import dotenv_values


def openai_settings_from_dot_env() -> Tuple[str, Optional[str]]:
    """
    Reads OpenAI API key and Org ID from .env file.

    Returns:
        Tuple[str, Optional[str]]: OpenAI API key and Org ID
    """
    
    config = dotenv_values(".env")
    api_key = config.get("OPENAI_API_KEY")
    
    assert api_key, "OPENAI_API_KEY not found in .env file"

    #Org ID is optional
    return api_key


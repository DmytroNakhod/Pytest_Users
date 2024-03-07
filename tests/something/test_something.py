import requests
from config import BASE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post
from src.baseclasses.response import Response
from src.schemas.user import User

response = requests.get(BASE_URL)


# print(response.__getstate__())
# print(response.url)

def test_another():
    assert 1 == 1

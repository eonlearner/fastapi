from pydantic import BaseModel
from models import CategoryType, TimezoneType, LangType
from typing import Optional, List


# TO support creation and update APIs
class CreateAndUpdateUser(BaseModel):
    firstname: str
    lastname: str
    email: str
    eid: int
    dept: str
    adhr: str
    image: bytes
    username: str
    password: str
    categorytype: CategoryType
    bio: str
    timezonetype: TimezoneType
    langtype: LangType


# TO support list and get APIs
class User(CreateAndUpdateUser):
    id: int

    class Config:
        orm_mode = True


# To support list users API
class PaginatedUserInfo(BaseModel):
    limit: int
    offset: int
    data: List[User]


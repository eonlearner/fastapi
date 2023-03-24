from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum, Boolean
from database import Base 
import enum


class CategoryType(str, enum.Enum):
    Superadmin = "Superadmin"
    Admin = "Admin"
    Instructor = "Instructor"
    Learner = "Learner"

class TimezoneType(str, enum.Enum):
    IST = "India Standard Time (IST)"
    NST = "New Zealand Standard Time (NST)"
    GMT = "Greenwich Mean Time (GMT)"
    AST = "Alaska Standard Time (AST)"
    ECT = "European Central Time (ECT)"
    Arabic = "Egypt Standard Time (Arabic)"

class LangType(str, enum.Enum):
    English = "English"
    Hindi = "Hindi"
    Marathi = "Marathi"

class UserInfo(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, nullable=False)
    eid = Column(Integer)
    dept = Column(String)
    adhr = Column(String)
    image = Column(String)
    username = Column(String)
    password = Column(String)
    categorytype = Column(Enum(CategoryType))
    bio = Column(String)
    timezonetype = Column(Enum(TimezoneType), nullable= False)
    langtype = Column(Enum(LangType), nullable= False)


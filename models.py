from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Enum
from database import Base
import enum



class CategoryType(str, enum.Enum):
    Superadmin = "Superadmin"
    Admin = "Admin"
    Instructor = "Instructor"
    Learner = "Learner"

class TimezoneType(str, enum.Enum):
    ist = "India Standard Time (IST)"
    nst = "New Zealand Standard Time (NST)"
    gmt = "Greenwich Mean Time (GMT)"
    ast = "Alaska Standard Time (AST)"
    ect = "European Central Time (ECT)"
    arabic = "Egypt Standard Time (Arabic)"

class LangType(str, enum.Enum):
    english = "English"
    hindi = "Hindi"
    marathi = "Marathi"

class UserInfo(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String)
    eid = Column(Integer)
    dept = Column(String)
    adhr = Column(Integer)
    image = Column(String)
    username = Column(String)
    password = Column(String)
    categorytype = Column(Enum(CategoryType))
    bio = Column(String)
    timezonetype = Column(Enum(TimezoneType))
    langtype = Column(Enum(LangType))

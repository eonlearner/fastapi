from typing import List
from sqlalchemy.orm import Session
from exceptions import UserInfoInfoAlreadyExistError, UserInfoNotFoundError
from models import UserInfo
from schemas import CreateAndUpdateUser


# Function to get list of user info
def get_all_users(session: Session) -> List[UserInfo]:
    return session.query(UserInfo).all()


# Function to  get info of a particular user
def get_user_info_by_id(session: Session, _id: int) -> UserInfo:
    user_info = session.query(UserInfo).get(_id)

    if user_info is None:
        raise UserInfoNotFoundError

    return user_info


# Function to add a new user info to the database
def create_user(session: Session, user_info: CreateAndUpdateUser) -> UserInfo:
    user_details = session.query(UserInfo).filter(UserInfo.firstname == user_info.firstname).first()
    if user_details is not None:
        raise UserInfoInfoAlreadyExistError

    new_user_info = UserInfo(**user_info.dict())
    session.add(new_user_info)
    session.commit()
    session.refresh(new_user_info)
    return new_user_info


# Function to update details of the user
def update_user_info(session: Session, _id: int, info_update: CreateAndUpdateUser) -> UserInfo:
    user_info = get_user_info_by_id(session, _id)

    if user_info is None:
        raise UserInfoNotFoundError

    user_info.firstname = info_update.firstname
    user_info.lastname = info_update.lastname
    user_info.email = info_update.email
    user_info.eid = info_update.eid
    user_info.dept = info_update.dept
    user_info.adhr = info_update.adhr
    user_info.image = info_update.image
    user_info.username = info_update.username
    user_info.password = info_update.password
    user_info.categorytype = info_update.categorytype
    user_info.bio = info_update.bio
    user_info.timezonetype = info_update.timezonetype
    user_info.langtype = info_update.langtype

    session.commit()
    session.refresh(user_info)

    return user_info


# Function to delete a user info from the db
def delete_user_info(session: Session, _id: int):
    user_info = get_user_info_by_id(session, _id)

    if user_info is None:
        raise UserInfoNotFoundError

    session.delete(user_info)
    session.commit()

    return

import uuid

from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """
    Описание структуры пользователя.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias = True)

    id: str
    email: EmailStr
    last_name: str = Field(alias = "lastName")
    first_name: str = Field(alias = "firstName")
    middle_name: str = Field(alias = "middleName")
    phone_number: str = Field(alias = "phoneNumber")

class CreateUserRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание пользователя.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias = True)

    email: EmailStr
    last_name: str = Field(alias = "lastName")
    first_name: str = Field(alias = "firstName")
    middle_name: str = Field(alias = "middleName")
    phone_number: str = Field(alias = "phoneNumber")

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
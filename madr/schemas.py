from pydantic import BaseModel, EmailStr, ConfigDict


# ############################ schema token##################################

class Token(BaseModel):
    access_token: str
    token_type: str

# ############################# schema usuario###############################


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Message(BaseModel):
    message: str

# ##################### schema romancista####################################


class RomancistaSchema(BaseModel):
    nome: str


class RomancistaPublic(RomancistaSchema):
    id: int


class RomancistaPublicList(BaseModel):
    romancistas: list[RomancistaPublic]

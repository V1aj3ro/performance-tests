from pydantic import BaseModel, EmailStr


class Address(BaseModel):
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    address: Address

user = User(
    id=1,
    name="Alice",
    email="alice@example.com",
    address= Address(
        city = "Moscow",
        zip_code = "10001",
    )
)

print(user.address.city)
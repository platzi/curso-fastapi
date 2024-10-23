from pydantic import BaseModel
from sqlmodel import SQLModel


class CustomerBase(SQLModel):
    name: str
    description: str | None
    email: str
    age: int


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase, table=True):
    id: int | None = None


class Transaction(BaseModel):
    id: int
    ammount: int
    description: str


class Invoice(BaseModel):
    id: int
    customer: Customer
    transactions: list[Transaction]
    total: int

    @property
    def ammount_total(self):
        return sum(transaction.ammount for transaction in self.transactions)

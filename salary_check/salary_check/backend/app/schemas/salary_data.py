from pydantic import BaseModel


class SalaryDataBaseModel(BaseModel):
    sell_currency: str
    buy_currency: str
    bank_sell: float
    bank_buy: float


class SalaryDataCreateModel(SalaryDataBaseModel):
    pass


class SalaryDataUpdateModel(SalaryDataBaseModel):
    pass


class SalaryDataModel(SalaryDataBaseModel):
    id: int

    class Config:
        orm_mode = True
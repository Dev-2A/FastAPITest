# Pydantic 모델을 사용하여 응답 데이터에서 필요한 필드만 선택하거나, 필요 없는 필드를 제외하여 클라이언트에게 반환할 정보를 조절
from pydantic import BaseModel

class ItemBase(BaseModel):
    name: str
    description: str
    price: int
    
class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    
    class Config:
        orm_mode = True
# Pydantic ���� ����Ͽ� ���� �����Ϳ��� �ʿ��� �ʵ常 �����ϰų�, �ʿ� ���� �ʵ带 �����Ͽ� Ŭ���̾�Ʈ���� ��ȯ�� ������ ����
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
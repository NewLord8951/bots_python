from sqlalchemy.orm import Session
from . import models

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_user(self, email: str, username: str, hashed_password: str):
        user = models.User(
            email=email,
            username=username,
            hashed_password=hashed_password
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def get_user_by_email(self, email: str):
        return self.db.query(models.User).filter(models.User.email == email).first()
    
    def get_user_by_username(self, username: str):
        return self.db.query(models.User).filter(models.User.username == username).first()

class ProductRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_product(self, name: str, description: str, price: float, stock_quantity: int = 0):
        product = models.Product(
            name=name,
            description=description,
            price=price,
            stock_quantity=stock_quantity
        )
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product
    
    def get_product(self, product_id: int):
        return self.db.query(models.Product).filter(models.Product.id == product_id).first()
    
    def update_stock(self, product_id: int, new_quantity: int):
        product = self.get_product(product_id)
        if product:
            product.stock_quantity = new_quantity
            self.db.commit()
            return product
        return None

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def create_order(self, user_id: int, total_amount: float):
        order = models.Order(
            user_id=user_id,
            total_amount=total_amount,
            status="pending"
        )
        self.db.add(order)
        self.db.commit()
        self.db.refresh(order)
        return order
    
    def get_order(self, order_id: int):
        return self.db.query(models.Order).filter(models.Order.id == order_id).first()
    
    def update_order_status(self, order_id: int, status: str):
        order = self.get_order(order_id)
        if order:
            order.status = status
            self.db.commit()
            return order
        return None
 

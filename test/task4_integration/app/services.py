import hashlib
from .repositories import UserRepository, ProductRepository, OrderRepository

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def register_user(self, email: str, username: str, password: str):
        # Проверка существования пользователя
        if self.user_repository.get_user_by_email(email):
            raise ValueError("Пользователь с таким email уже существует")
        
        if self.user_repository.get_user_by_username(username):
            raise ValueError("Пользователь с таким именем уже существует")
        
        # Хеширование пароля
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        # Создание пользователя
        return self.user_repository.create_user(email, username, hashed_password)
    
    def authenticate_user(self, username: str, password: str):
        user = self.user_repository.get_user_by_username(username)
        if user and user.hashed_password == hashlib.sha256(password.encode()).hexdigest():
            return user
        return None

class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository
    
    def add_product(self, name: str, description: str, price: float, stock_quantity: int):
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        
        if stock_quantity < 0:
            raise ValueError("Количество не может быть отрицательным")
        
        return self.product_repository.create_product(name, description, price, stock_quantity)
    
    def get_product_with_stock_check(self, product_id: int):
        product = self.product_repository.get_product(product_id)
        if not product:
            raise ValueError("Продукт не найден")
        
        return {
            "id": product.id,
            "name": product.name,
            "description": product.description,
            "price": product.price,
            "stock_quantity": product.stock_quantity,
            "in_stock": product.stock_quantity > 0
        }

class OrderService:
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository):
        self.order_repository = order_repository
        self.product_repository = product_repository
    
    def create_order(self, user_id: int, product_id: int, quantity: int):
        # Проверка наличия товара
        product = self.product_repository.get_product(product_id)
        if not product:
            raise ValueError("Товар не найден")
        
        if product.stock_quantity < quantity:
            raise ValueError("Недостаточно товара на складе")
        
        # Расчет суммы
        total_amount = product.price * quantity
        
        # Создание заказа
        order = self.order_repository.create_order(user_id, total_amount)
        
        # Обновление количества товара
        new_quantity = product.stock_quantity - quantity
        self.product_repository.update_stock(product_id, new_quantity)
        
        return order

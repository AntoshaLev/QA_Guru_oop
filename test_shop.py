import pytest

from models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(product.quantity - 1)

    def test_product_buy_all(self, product):
        # Проверка buy
        product.buy(product.quantity)
        assert product.quantity == 0


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_cart_empty(self, product, cart):
        # Проверка что корзина пуста
        assert len(cart.products) == 0

    def test_add_cart_product(self, product, cart):
        # Проверка на добавление товара в корзину
        cart.add_product(product)
        assert product in cart.products

    def test_cart_product(self, product, cart):
        # Проверка на количество добавленного товара в корзине
        cart.add_product(product, buy_count=8)
        assert cart.products.get(product) == 8

    def test_remove_full_cart_product(self, product, cart):
        # Проверка на очистку корзины при remove_count = None
        cart.add_product(product)
        assert product in cart.products
        cart.remove_product(product)
        assert product not in cart.products

    def test_remove_some_cart_product(self, product, cart):
        # Проверка на удаление из корзины remove_count продукта
        cart.add_product(product, buy_count=4)
        assert product in cart.products
        cart.remove_product(product, 3)
        assert cart.products.get(product) == 1

    def test_remove_count_cart_product(self, product, cart):
        # Проверка на удаление продукта из корзины, если remove_count больше количества товара
        cart.add_product(product, buy_count=4)
        assert product in cart.products
        cart.remove_product(product, 5)
        assert product not in cart.products

    def test_clear_cart(self, product, cart):
        # Проверка на очистку корзины
        cart.add_product(product, buy_count=4)
        assert product in cart.products
        cart.remove_product(product, 4)
        assert len(cart.products) == 0

    def test_get_total_price(self, product, cart):
        # Проверка на получение стоимости корзины
        cart.add_product(product, buy_count=6)
        assert cart.products.get(product) == 6
        assert cart.get_total_price(product) == 600

    def test_buy_product_in_cart(self, product, cart):
        # Проверка на покупку quantity продуктов в корзине
        cart.add_product(product, buy_count=10)
        assert cart.products.get(product) == 10
        cart.buy(quantity=5)
        assert cart.products.get(product) == 5

    def test_buy_product_in_cart_than_available(self, product, cart):
        # Проверка на покупку большего quantity чем возможно
        cart.add_product(product, buy_count=1)
        with pytest.raises(ValueError):
            cart.buy(quantity=2)

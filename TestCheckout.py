import pytest
from Checkout import Checkout
# Documentacion de pytest https://docs.pytest.org/en/latest/reference.html

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("a", 1)
    checkout.addItemPrice("b", 2)
    return checkout

def test_CanCalculateTotal(checkout):
    checkout.addItem("a")
    assert checkout.calculateTotal() == 1

def test_GetCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("a")
    checkout.addItem("b")
    assert checkout.calculateTotal() == 3

def test_CanAddDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)

def test_CanApplayDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2

def test_ExeptionWithBadItem(checkout):
    with pytest.raises(Exception):
        checkout.addDiscount("c")
# Ignorar Test
@pytest.mark.skip("Marcador pytest.mark.skipif declarar para que se omite una prueba")
def test_CanApplayDiscountRule(checkout):
    checkout.addDiscount("a", 3, 2)
    checkout.addItem("a")
    checkout.addItem("a")
    assert checkout.calculateTotal() == 2
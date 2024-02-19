"""
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
"""

from collections import namedtuple
from decimal import Decimal

Order = namedtuple("Order", "id, items")
Item = namedtuple("Item", "type, description, amount, quantity")

MAX_ITEM_AMOUNT = 100000
MAX_TOTAL = 1e6
MIN_QUANTITY, MAX_QUANTITY = 0, 100


def validorder(order: Order):
    payments, expenses = Decimal("0"), Decimal("0")

    for item in order.items:
        item_amount = Decimal(str(item.amount))
        if item.type == "payment":
            if -MAX_ITEM_AMOUNT <= item.amount <= MAX_ITEM_AMOUNT:
                payments += item_amount
        elif item.type == "product":
            if all(
                [
                    isinstance(item.quantity, int),
                    MIN_QUANTITY < item.quantity <= MAX_QUANTITY,
                    MIN_QUANTITY < item.amount <= MAX_ITEM_AMOUNT,
                ]
            ):
                expenses += item_amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type

    if any([expenses > MAX_TOTAL, abs(payments) > MAX_TOTAL]):
        return "Total amount payable for an order exceeded"

    if payments != expenses:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (
            order.id,
            payments - expenses,
        )
    else:
        return "Order ID: %s - Full payment received!" % order.id

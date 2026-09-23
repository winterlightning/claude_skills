"""A rounded payment card with a two-line stripe and two lower marks.

HRECT_L extrema (4,8)-(44,40). The stripe rails attach at shared wall nodes;
two lower account marks repeat with matching length. Lucide credit-card
provides the broad rounded enclosure and full-width stripe construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "599cb766-f08d-4099-8edc-1de4d82672b2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/credit card_599cb766-f08d-4099-8edc-1de4d82672b2.svg"
AUTHOR = "gpt-6"


class BankPaymentCreditCard(Solo48):
    icon_id = "bank-payment-credit-card"
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/payment"
    aliases = ("credit card", "bank card")
    keywords = ("payment", "stripe", "account", "debit")

    def build(self) -> None:
        p=[(8,8),(40,8),(44,12),(44,16),(44,24),(44,36),(40,40),(8,40),(4,36),(4,24),(4,16),(4,12),(8,8)]
        parts=[]
        for i,(a,b) in enumerate(zip(p,p[1:])):
            n=f"frame-{i}"
            if i in (1,5,7,11):self.add_arc(n,a,b,radius_x=4,radius_y=4,sweep=True)
            else:self.add_line(n,a,b)
            parts.append(n)
        self.add_contour("card",*parts,closed=True)
        for name,y in (("stripe-upper",16),("stripe-lower",24)):
            self.add_line(name,(4,y),(44,y))
            self.relate("connect",name,"card")

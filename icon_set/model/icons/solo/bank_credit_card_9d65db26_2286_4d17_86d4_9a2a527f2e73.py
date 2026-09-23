"""A rounded credit card with a stripe and lower-right chip.

SQUARE extrema (6,6)-(42,42). The chip is an eight-unit rounded rectangle;
the second source stripe is omitted to give it clear space. Lucide credit-card
provides the card envelope and attached stripe.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "9d65db26-2286-4d17-86d4-9a2a527f2e73"
SOURCE_PATH = "pictographic-primitives/_uncategorized_13/credit_9d65db26-2286-4d17-86d4-9a2a527f2e73.svg"
AUTHOR = "gpt-6"


class BankCreditCard(Solo48):
    icon_id = "bank-credit-card"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "finance/payment"
    aliases = ("credit card with chip", "payment card")
    keywords = ("bank", "chip", "stripe", "debit")

    def build(self) -> None:
        p=[(10,6),(38,6),(42,10),(42,16),(42,38),(38,42),(10,42),(6,38),(6,16),(6,10),(10,6)]
        parts=[]
        for i,(a,b) in enumerate(zip(p,p[1:])):
            n=f"card-{i}"
            if i in (1,4,6,9):self.add_arc(n,a,b,radius_x=4,radius_y=4,sweep=True)
            else:self.add_line(n,a,b)
            parts.append(n)
        self.add_contour("card",*parts,closed=True)
        self.add_line("stripe",(6,16),(42,16))
        self.relate("connect","stripe","card")
        q=[(27,25),(31,25),(33,27),(33,31),(31,33),(27,33),(25,31),(25,27),(27,25)]
        chip=[]
        for i,(a,b) in enumerate(zip(q,q[1:])):
            n=f"chip-{i}"
            if i%2:self.add_arc(n,a,b,radius_x=2,radius_y=2,sweep=True)
            else:self.add_line(n,a,b)
            chip.append(n)
        self.add_contour("chip",*chip,closed=True)

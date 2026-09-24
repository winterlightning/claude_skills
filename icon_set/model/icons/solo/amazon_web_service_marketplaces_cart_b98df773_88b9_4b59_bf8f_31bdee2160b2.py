"""Marketplace cart carrying a three-cube cluster."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "b98df773-88b9-4b59-bf8f-31bdee2160b2"
SOURCE_PATH = "icon_set/work/todo-references/amazon web service marketplaces cart_b98df773-88b9-4b59-bf8f-31bdee2160b2.svg"
AUTHOR = "gpt-6"


class AmazonMarketplaceCart(Solo48):
    icon_id = "amazon-web-service-marketplaces-cart"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "commerce/cart"
    aliases = ("aws-marketplace-cart",)
    keywords = ("amazon", "aws", "marketplace", "cart", "cubes")

    def build(self) -> None:
        # Basket with a three-cell honeycomb and paired wheels.
        self.add_polyline("basket", (6, 8), (10, 28), (13, 31), (35, 31), (38, 28), (42, 8))
        self.add_line("handle", (42, 8), (44, 8))
        for name, cx, cy in (("top", 24, 10), ("left", 17, 20), ("right", 31, 20)):
            self.add_polyline(name, (cx, cy-5), (cx+5, cy-2), (cx+5, cy+3), (cx, cy+6), (cx-5, cy+3), (cx-5, cy-2), closed=True)
        for name, cx in (("left-wheel", 15), ("right-wheel", 33)):
            self.add_arc(f"{name}-a", (cx-3, 40), (cx+3, 40), radius_x=3)
            self.add_arc(f"{name}-b", (cx+3, 40), (cx-3, 40), radius_x=3)
            self.add_contour(name, f"{name}-a", f"{name}-b", closed=True)

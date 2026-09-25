from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "fe4ed243-598f-461a-b0a7-5906eb6431a4"
SOURCE_PATH = "icon_set/work/todo-references/shop sign 1_fe4ed243-598f-461a-b0a7-5906eb6431a4.svg"
AUTHOR = "gpt-6"

class ShopSign(Solo48):
    """A blank rounded shop sign suspended by a triangular hanger."""
    icon_id = "shop-sign-1"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("container", "other", "primitives-generate")
    aliases = ("hanging sign",)
    keywords = ("shop", "sign", "blank")

    def build(self):
        # Symbol plan: rounded board and symmetric hanger share two top nodes.
        # SQUARE extremes: x6,42; y6,42. Shared axis24 and corner radius4.
        axis, radius = 24, 4
        left, right = axis-18, axis+18
        a,b=(axis-10,18),(axis+10,18)
        for n, (u,v) in enumerate(zip([(10,18),a,b],[a,b,(38,18)]),1):
            self.add_line(f"top-{n}",u,v)
        self.add_arc("tr",(38,18),(right,22),radius_x=radius)
        self.add_line("right",(right,22),(right,38))
        self.add_arc("br",(right,38),(38,42),radius_x=radius)
        self.add_line("bottom",(38,42),(10,42))
        self.add_arc("bl",(10,42),(left,38),radius_x=radius)
        self.add_line("left",(left,38),(left,22))
        self.add_arc("tl",(left,22),(10,18),radius_x=radius)
        self.add_contour("board","top-1","top-2","top-3","tr","right","br","bottom","bl","left","tl",closed=True)
        self.add_polyline("hanger",a,(axis,6),b)
        self.relate("connect","hanger","board")

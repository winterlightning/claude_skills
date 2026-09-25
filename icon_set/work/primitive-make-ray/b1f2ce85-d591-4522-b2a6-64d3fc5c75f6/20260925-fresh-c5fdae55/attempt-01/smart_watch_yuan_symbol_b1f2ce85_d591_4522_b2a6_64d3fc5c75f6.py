"""A round face smartwatch with a yuan mark.

Plan: a six arc circular face, paired rear strap runs, and a centered yuan
glyph. Strap and face share four explicit attachment nodes. Lucide watch
informed the circle and band construction; the currency glyph follows source.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "b1f2ce85-d591-4522-b2a6-64d3fc5c75f6"
SOURCE_PATH = 'pictographic-primitives/combination/smart watch circle yuan sign_b1f2ce85-d591-4522-b2a6-64d3fc5c75f6.svg'
AUTHOR = "gpt-6"


class SmartWatchYuanSymbol(Solo48):
    icon_id = "smart-watch-yuan-symbol"
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ("yuan smartwatch", "watch payment")
    keywords = ("watch", "smartwatch", "yuan", "currency", "payment")

    def build(self) -> None:
        # Face and symmetric straps have deeper negative spaces above and below the dial.
        curves=[((10,24),(10,19),(12,16),(16,14)),((16,14),(20,11),(28,11),(32,14)),((32,14),(36,16),(38,19),(38,24)),((38,24),(38,29),(36,32),(32,34)),((32,34),(28,37),(20,37),(16,34)),((16,34),(12,32),(10,29),(10,24))]
        for j,(a,c1,c2,b) in enumerate(curves):self.add_bezier(f'face-{j}',a,(c1,c2,b))
        self.add_contour('face',*(f'face-{j}' for j in range(6)),closed=True)
        for name,y,end in [('upper-band',14,4),('lower-band',34,44)]:
            self.add_polyline(name,(16,y),(16,end),(32,end),(32,y));self.relate('connect','face',name)
        self.add_polyline('yuan-forks',(20,22),(24,26),(28,22))
        self.add_polyline('yuan-bar',(20,26),(24,26),(28,26))
        self.add_line('yuan-stem',(24,26),(24,28));self.relate('connect','yuan-forks','yuan-bar','yuan-stem')


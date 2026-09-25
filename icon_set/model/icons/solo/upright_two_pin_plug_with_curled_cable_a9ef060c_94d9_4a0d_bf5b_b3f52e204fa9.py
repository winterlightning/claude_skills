"""Two upright pins over a rounded plug and right curling cable.
SQUARE reaches (6,6)-(42,42). Plug owns its symmetrical pins; cable is
intentionally asymmetric. Source supplies curl, Lucide plug supplies rounded
U construction. No ornamental detail. All attachments split at shared nodes.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = "a9ef060c-94d9-4a0d-bf5b-b3f52e204fa9"
SOURCE_PATH = "pictographic-primitives/_uncategorized_15/disconnected_a9ef060c-94d9-4a0d-bf5b-b3f52e204fa9.svg"
AUTHOR = "gpt-6"
class Drawing(Solo48):
    icon_id = "upright-two-pin-plug-with-curled-cable"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ("Electric Power Plug",)
    keywords = ("plug", "electric", "cable", "power", "pins", "connector", "cord")
    def build(self):
        points=[(6,16),(12,16),(24,16),(30,16),(30,22)]
        members=[]
        for i,(a,b) in enumerate(zip(points,points[1:])):
            n=f"body-{i}"; self.add_line(n,a,b); members.append(n)
        self.add_arc("body-turn-right",(30,22),(22,30),radius_x=8)
        self.add_line("body-base-right",(22,30),(18,30))
        self.add_line("body-base-left",(18,30),(14,30))
        self.add_arc("body-turn-left",(14,30),(6,22),radius_x=8)
        self.add_line("body-left",(6,22),(6,16))
        self.add_contour("body",*members,"body-turn-right","body-base-right","body-base-left","body-turn-left","body-left",closed=True)
        for side,x in (("left",12),("right",24)):
            self.add_line("pin-"+side,(x,6),(x,16))
            self.relate("connect","body","pin-"+side)
        self.add_arc("cable-curl",(18,30),(42,30),radius_x=12,sweep=False)
        self.add_line("cable-end",(42,30),(42,24))
        self.add_contour("cable","cable-curl","cable-end")
        self.relate("connect","body","cable")

"""Overheated Head; rebuilt from the supplied visual reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f36b3f14-7240-5664-b800-5adf46ca8c52'
SOURCE_PATH = 'pictographic-primitives/smileys/head sick_f36b3f14-7240-5664-b800-5adf46ca8c52.svg'
AUTHOR = 'gpt-6'


class OverheatedHead(Solo48):
    icon_id = 'overheated-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('overheated', 'heat', 'sick', 'head', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE: heat waves own the open head's upper sides; omit shoulders.
        self.add_arc("heat-left",(10,6),(10,14),radius_x=4,sweep=False)
        self.add_line("temple-left",(10,14),(8,22))
        self.add_arc("jaw",(8,22),(40,22),radius_x=16,radius_y=20,sweep=False)
        self.add_line("temple-right",(40,22),(38,14))
        self.add_arc("heat-right",(38,14),(38,6),radius_x=4,sweep=False)
        self.add_contour("head","heat-left","temple-left","jaw","temple-right","heat-right")
        self.add_arc("heat-center-top",(24,6),(24,10),radius_x=2)
        self.add_arc("heat-center-low",(24,10),(24,14),radius_x=2,sweep=False)
        self.add_contour("heat-center","heat-center-top","heat-center-low")
        for side,x in (("left",18),("right",30)):
            self.add_polyline(f"eye-{side}-a",(x-1,23),(x,24),(x+1,25))
            self.add_polyline(f"eye-{side}-b",(x-1,25),(x,24),(x+1,23))
            for a in (1,2):
                for b in (1,2): self.relate("connect",f"eye-{side}-a-{a}",f"eye-{side}-b-{b}")
        self.add_arc("frown",(22,33),(26,33),radius_x=4)

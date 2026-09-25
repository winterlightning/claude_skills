"""Cowboy Head. Rebuilt from the supplied visual reference on SOLO48.
Lucide construction: face-angry / face-slightly-frowning circular face and sparse expression;
glasses uses paired circular lenses. Shared axis and paired geometry preserve expression.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd88e970d-e37e-43ae-879d-7721d56f8261'
SOURCE_PATH = 'pictographic-primitives/smileys/cowboy_d88e970d-e37e-43ae-879d-7721d56f8261.svg'
AUTHOR = 'gpt-6'


class CowboyHead(Solo48):
    icon_id = 'cowboy-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('cowboy', 'hat', 'western', 'head', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE ink (4,4)-(44,44); brim nodes own crown and round jaw.
        self.add_polyline("crown",(12,18),(17,6),(24,9),(31,6),(36,18))
        self.add_arc("brim-left",(6,13),(11,18),radius_x=5,sweep=False)
        self.add_line("brim-a",(11,18),(12,18))
        self.add_line("brim-b",(12,18),(36,18))
        self.add_line("brim-c",(36,18),(37,18))
        self.add_arc("brim-right",(37,18),(42,13),radius_x=5,sweep=False)
        self.add_contour("brim","brim-left","brim-a","brim-b","brim-c","brim-right")
        self.add_arc("jaw",(36,18),(12,18),radius_x=15,large_arc=True)
        for a in ("brim-a","brim-b"):
            self.relate("connect",a,"crown-1")
            self.relate("connect",a,"jaw")
        for a in ("brim-b","brim-c"):
            self.relate("connect",a,"crown-4")
            self.relate("connect",a,"jaw")
        self.relate("connect","jaw","crown-1")
        self.relate("connect","jaw","crown-4")

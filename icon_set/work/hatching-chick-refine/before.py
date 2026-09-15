"""Chick joined to the shell at both crack valleys, with an integrated beak. Lucide bird informs the head; Lucide egg informs the lower bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20c9a90e-2b2b-5596-bf5f-720461c74888'
SOURCE_PATH = 'pictographic-primitives/animals/chicken hatch_20c9a90e-2b2b-5596-bf5f-720461c74888.svg'
AUTHOR = 'gpt-6'


class HatchingChick(Solo48):
    icon_id = 'hatching-chick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('chick', 'egg', 'hatch', 'shell', 'birth', 'easter', 'bird', 'new')

    def build(self) -> None:
        # VRECT_XL visible (6,6)-(42,42); centerlines (6,6)-(42,42).
        self.add_line('back',(6,32),(6,18))
        self.add_arc('head',(6,18),(30,18),radius_x=12)
        self.add_line('bill-top',(30,18),(42,22))
        self.add_line('bill-bottom',(42,22),(33,27))
        self.add_contour('chick', 'back', 'head', 'bill-top', 'bill-bottom')
        self.add_polyline('crack',(6,32),(15,27),(24,32),(33,27),(42,32))
        self.add_arc('shell',(42,32),(6,32),radius_x=18,radius_y=10)
        self.relate('connect', 'shell', 'crack')
        self.relate('connect', 'chick', 'crack')

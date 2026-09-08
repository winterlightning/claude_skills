"""Chick joined to the shell at both crack valleys, with an integrated beak. Lucide bird informs the head; Lucide egg informs the lower bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '20c9a90e-2b2b-5596-bf5f-720461c74888'
SOURCE_PATH = 'pictographic-primitives/animals/chicken hatch_20c9a90e-2b2b-5596-bf5f-720461c74888.svg'
AUTHOR = 'gpt-6'


class HatchingChick(Solo48):
    icon_id = 'hatching-chick'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('chick', 'egg', 'hatch', 'shell', 'birth', 'easter', 'bird', 'new')

    def build(self) -> None:
        # VRECT_XL visible (3,0)-(45,48); centerlines (5,2)-(43,46).
        self.add_line('back', (13,32), (13,14))
        self.add_arc('head', (13,14), (35,14), radius_x=11, radius_y=12)
        self.add_line('bill-top', (35,14), (43,19))
        self.add_line('bill-bottom', (43,19), (35,24))
        self.add_line('breast', (35,24), (35,32))
        self.add_contour('chick', 'back', 'head', 'bill-top', 'bill-bottom', 'breast')
        self.add_polyline('crack', (5,26), (13,32), (24,26), (35,32), (43,26))
        self.add_arc('shell', (43,26), (5,26), radius_x=19, radius_y=20)
        self.relate('connect', 'shell', 'crack')
        self.relate('connect', 'chick', 'crack')

'Frozen face: smooth circular crown, clear eyes and mouth, and deliberate ice points.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ef715132-dcbb-446d-bc2d-8f47ae0978bf'
SOURCE_PATH = 'icons-json/smileys/cold face frozen_ef715132-dcbb-446d-bc2d-8f47ae0978bf.json'
AUTHOR = 'gpt-6'

class ColdFaceFrozen(Solo48):
    icon_id = 'cold-face-frozen'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'smileys'
    aliases = ()
    keywords = ('cold', 'face', 'frozen', 'smileys')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_arc('face-top', (6, 24), (42, 24), radius_x=18, radius_y=18, large_arc=False, sweep=True)
        self.add_line('ice-1', (42, 24), (42, 34))
        self.add_line('ice-2', (42, 34), (36, 42))
        self.add_line('ice-3', (36, 42), (30, 36))
        self.add_line('ice-4', (30, 36), (24, 42))
        self.add_line('ice-5', (24, 42), (18, 36))
        self.add_line('ice-6', (18, 36), (12, 42))
        self.add_line('ice-7', (12, 42), (6, 34))
        self.add_line('ice-8', (6, 34), (6, 24))
        self.add_line('mouth', (16, 27), (32, 27))
        self.add_line('eye-20', (20, 16), (20, 16))
        self.add_line('eye-28', (28, 16), (28, 16))
        self.add_contour('ice', *('ice-1', 'ice-2', 'ice-3', 'ice-4', 'ice-5', 'ice-6', 'ice-7', 'ice-8'), closed=False)
        self.relate('connect', *('face-top', 'ice'))

"""Closed knight helm on a heater shield. Extremes (5,2)-(43,46). Lucide shield contour; nasal detail omitted to open the face."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '008c3781-679c-536b-8b56-abc407bd1ac1'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/armor shield_008c3781-679c-536b-8b56-abc407bd1ac1.svg'

class KnightHelmOnShield(Solo48):
    icon_id = 'knight-helm-on-shield'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('shield', 'helmet', 'knight', 'armour', 'medieval', 'heraldry', 'crest', 'defence')

    def build(self) -> None:
        self.add_line('shield-top-1', (5, 22), (5, 7))
        self.add_line('shield-top-2', (5, 7), (24, 2))
        self.add_line('shield-top-3', (24, 2), (43, 7))
        self.add_line('shield-top-4', (43, 7), (43, 22))
        self.add_arc('shield-right', (43,22), (24,46), radius_x=25)
        self.add_arc('shield-left', (24,46), (5,22), radius_x=25)
        self.add_contour('shield', 'shield-top-1','shield-top-2','shield-top-3','shield-top-4','shield-right','shield-left', closed=True)
        self.add_arc('dome', (14,23), (34,23), radius_x=10, sweep=True)
        self.add_line('jaw-1', (34, 23), (34, 30))
        self.add_line('jaw-2', (34, 30), (24, 36))
        self.add_line('jaw-3', (24, 36), (14, 30))
        self.add_line('jaw-4', (14, 30), (14, 23))
        self.add_contour('helm','dome','jaw-1','jaw-2','jaw-3','jaw-4',closed=True)
        self.add_line('visor',(14,23),(34,23))
        self.relate('connect','helm','visor')

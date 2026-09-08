"""Armoured head and shoulders. Extremes (2,2)-(46,46). Lucide shirt shoulder organization, symmetric helmet and pauldrons; rivets omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0afdc66e-6ae9-5874-a6cb-bad5b9bb6ece'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/armor_0afdc66e-6ae9-5874-a6cb-bad5b9bb6ece.svg'
AUTHOR = 'astra-chatgpt'

class KnightArmorTorso(Solo48):
    icon_id = 'knight-armor-torso'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('armour', 'knight', 'helmet', 'medieval', 'plate', 'warrior', 'chivalry', 'soldier')

    def build(self) -> None:
        self.add_line('spike',(24,2),(24,8))
        self.add_arc('helm-left',(13,19),(24,8),radius_x=11)
        self.add_arc('helm-right',(24,8),(35,19),radius_x=11)
        self.add_line('jaw-1', (35, 19), (35, 25))
        self.add_line('jaw-2', (35, 25), (24, 31))
        self.add_line('jaw-3', (24, 31), (13, 25))
        self.add_line('jaw-4', (13, 25), (13, 19))
        self.add_contour('helm','helm-left','helm-right','jaw-1','jaw-2','jaw-3','jaw-4',closed=True)
        self.relate('connect','spike','helm')
        self.add_polyline('visor',(20,18),(24,19),(28,18))
        self.add_arc('left-shoulder',(2,46),(12,36),radius_x=10)
        self.add_line('breastplate-1', (12, 36), (24, 41))
        self.add_line('breastplate-2', (24, 41), (36, 36))
        self.add_arc('right-shoulder',(36,36),(46,46),radius_x=10)
        self.add_contour('torso','left-shoulder','breastplate-1','breastplate-2','right-shoulder')
        self.add_polyline('left-pauldron',(2,46),(12,46),(12,36))
        self.add_polyline('right-pauldron',(36,36),(36,46),(46,46))
        self.relate('connect','torso','left-pauldron')
        self.relate('connect','torso','right-pauldron')

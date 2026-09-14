'Knight armor torso.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0afdc66e-6ae9-5874-a6cb-bad5b9bb6ece'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/armor_0afdc66e-6ae9-5874-a6cb-bad5b9bb6ece.svg'
AUTHOR = 'gpt-6'

class KnightArmorTorso(Solo48):
    icon_id = 'knight-armor-torso'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('armour', 'knight', 'helmet', 'medieval', 'plate', 'warrior', 'chivalry', 'soldier')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_6 = (24, 6)
        p_24_10 = (24, 10)
        p_14_20 = (14, 20)
        p_34_20 = (34, 20)
        p_34_25 = (34, 25)
        p_24_29 = (24, 29)
        p_14_25 = (14, 25)
        p_6_42 = (6, 42)
        p_14_34 = (14, 34)
        p_24_38 = (24, 38)
        p_34_34 = (34, 34)
        p_42_42 = (42, 42)
        p_14_42 = (14, 42)
        p_34_42 = (34, 42)
        p_24_19 = (24, 19)
        self.add_line('spike', p_24_6, p_24_10)
        self.add_arc('helm-left', p_14_20, p_24_10, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('helm-right', p_24_10, p_34_20, radius_x=10, radius_y=10, sweep=True, large_arc=False)
        self.add_line('jaw-1', p_34_20, p_34_25)
        self.add_line('jaw-2', p_34_25, p_24_29)
        self.add_line('jaw-3', p_24_29, p_14_25)
        self.add_line('jaw-4', p_14_25, p_14_20)
        self.add_arc('left-shoulder', p_6_42, p_14_34, radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('breastplate-1', p_14_34, p_24_38)
        self.add_line('breastplate-2', p_24_38, p_34_34)
        self.add_arc('right-shoulder', p_34_34, p_42_42, radius_x=8, radius_y=8, sweep=True, large_arc=False)
        self.add_line('left-pauldron-1', p_6_42, p_14_42)
        self.add_line('left-pauldron-2', p_14_42, p_14_34)
        self.add_line('right-pauldron-1', p_34_34, p_34_42)
        self.add_line('right-pauldron-2', p_34_42, p_42_42)
        self.add_line('visor', p_24_19, p_24_19)
        self.add_contour('helm', 'helm-left', 'helm-right', 'jaw-1', 'jaw-2', 'jaw-3', 'jaw-4', closed=True)
        self.add_contour('torso', 'left-shoulder', 'breastplate-1', 'breastplate-2', 'right-shoulder', closed=False)
        self.add_contour('left-pauldron', 'left-pauldron-1', 'left-pauldron-2', closed=False)
        self.add_contour('right-pauldron', 'right-pauldron-1', 'right-pauldron-2', closed=False)
        self.relate('connect', 'spike', 'helm')
        self.relate('connect', 'torso', 'left-pauldron')
        self.relate('connect', 'torso', 'right-pauldron')

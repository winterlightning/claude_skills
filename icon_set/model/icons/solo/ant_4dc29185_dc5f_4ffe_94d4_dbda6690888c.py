"""Ant with the middle left and right leg lines removed as requested. VRECT_L (8,4)-(40,44). Lucide bug informs mirrored attachments; retained parent antennae, head and abdomen."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4dc29185-dc5f-4ffe-94d4-dbda6690888c'
SOURCE_PATH = 'pictographic-primitives/animals/insect ant_4dc29185-dc5f-4ffe-94d4-dbda6690888c.svg'
AUTHOR = 'gpt-6'

class Ant(Solo48):
    icon_id = 'ant'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('ant', 'insect', 'worker', 'bug', 'colony', 'antennae', 'legs', 'nature')

    def build(self) -> None:
        self.add_arc('head-left', (24, 9), (18, 14), radius_x=6, radius_y=5, sweep=False)
        self.add_arc('head-bottom-left', (18, 14), (24, 20), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('head-bottom-right', (24, 20), (30, 14), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('head-right', (30, 14), (24, 9), radius_x=6, radius_y=5, sweep=False)
        self.add_contour('head', 'head-left', 'head-bottom-left', 'head-bottom-right', 'head-right', closed=True)
        self.add_line('waist-top', (24, 20), (24, 24))
        self.add_line('waist-mid', (24, 24), (24, 26))
        self.add_line('waist-low', (24, 26), (24, 28))
        self.add_contour('waist', 'waist-top', 'waist-mid', 'waist-low', closed=False)
        self.relate('connect', 'head', 'waist')
        self.add_arc('abd-top-left', (24, 28), (16, 36), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('abd-low-left', (16, 36), (24, 44), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('abd-low-right', (24, 44), (32, 36), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('abd-top-right', (32, 36), (24, 28), radius_x=8, radius_y=8, sweep=False)
        self.add_contour('abdomen', 'abd-top-left', 'abd-low-left', 'abd-low-right', 'abd-top-right', closed=True)
        self.relate('connect', 'waist', 'abdomen')
        self.add_polyline('antenna-left', (18, 14), (14, 8), (8, 4), closed=False)
        self.relate('connect', 'head', 'antenna-left')
        self.add_arc('leg-low-left', (24, 28), (8, 44), radius_x=19, radius_y=18, sweep=False)
        self.relate('connect', 'waist', 'leg-low-left')
        self.relate('connect', 'abdomen', 'leg-low-left')
        self.add_polyline('antenna-right', (30, 14), (34, 8), (40, 4), closed=False)
        self.relate('connect', 'head', 'antenna-right')
        self.add_arc('leg-low-right', (24, 28), (40, 44), radius_x=19, radius_y=18, sweep=True)
        self.relate('connect', 'waist', 'leg-low-right')
        self.relate('connect', 'abdomen', 'leg-low-right')
        self.relate('connect', 'leg-low-left', 'leg-low-right')

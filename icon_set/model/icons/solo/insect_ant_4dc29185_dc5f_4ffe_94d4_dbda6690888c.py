"""Worker ant; centerline extremes (5,2)-(43,46). Mirrored on x=24; six legs and two antennae retained. Lucide bug informs repeated leg attachments; waist reduced to one stroke."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4dc29185-dc5f-4ffe-94d4-dbda6690888c'
SOURCE_PATH = 'pictographic-primitives/animals/insect ant_4dc29185-dc5f-4ffe-94d4-dbda6690888c.svg'
AUTHOR = 'gpt-6'


class Ant(Solo48):
    icon_id = 'ant'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('ant', 'insect', 'worker', 'bug', 'colony', 'antennae', 'legs', 'nature')

    def build(self) -> None:
        # Worker ant; centerline extremes (5,2)-(43,46). Mirrored on x=24; six legs and two antennae retained. Lucide bug informs repeated leg attachments; waist reduced to one stroke.
        self.add_arc('head-left', (24, 9), (18, 14), radius_x=6, radius_y=5, sweep=False)
        self.add_arc('head-bottom-left', (18, 14), (24, 20), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('head-bottom-right', (24, 20), (30, 14), radius_x=6, radius_y=6, sweep=False)
        self.add_arc('head-right', (30, 14), (24, 9), radius_x=6, radius_y=5, sweep=False)
        self.add_contour('head', 'head-left', 'head-bottom-left', 'head-bottom-right', 'head-right', closed=True)
        self.add_line('waist-top', (24, 20), (24, 24))
        self.add_line('waist-mid', (24, 24), (24, 26))
        self.add_line('waist-low', (24, 26), (24, 28))
        self.add_contour('waist', 'waist-top', 'waist-mid', 'waist-low', closed=False)
        self.relate("connect", 'head', 'waist')
        self.add_arc('abd-top-left', (24, 28), (16, 36), radius_x=8, radius_y=8, sweep=False)
        self.add_arc('abd-low-left', (16, 36), (24, 46), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('abd-low-right', (24, 46), (32, 36), radius_x=14, radius_y=14, sweep=False)
        self.add_arc('abd-top-right', (32, 36), (24, 28), radius_x=8, radius_y=8, sweep=False)
        self.add_contour('abdomen', 'abd-top-left', 'abd-low-left', 'abd-low-right', 'abd-top-right', closed=True)
        self.relate("connect", 'waist', 'abdomen')
        self.add_polyline('antenna-left', (18, 14), (14, 8), (7, 2), closed=False)
        self.relate("connect", 'head', 'antenna-left')
        self.add_arc('leg-top-left', (24, 24), (5, 14), radius_x=19, radius_y=10, sweep=True)
        self.relate("connect", 'waist', 'leg-top-left')
        self.add_line('leg-mid-left', (24, 26), (5, 30))
        self.relate("connect", 'waist', 'leg-mid-left')
        self.add_arc('leg-low-left', (24, 28), (5, 46), radius_x=19, radius_y=18, sweep=False)
        self.relate("connect", 'waist', 'leg-low-left')
        self.relate("connect", 'abdomen', 'leg-low-left')
        self.add_polyline('antenna-right', (30, 14), (34, 8), (41, 2), closed=False)
        self.relate("connect", 'head', 'antenna-right')
        self.add_arc('leg-top-right', (24, 24), (43, 14), radius_x=19, radius_y=10, sweep=False)
        self.relate("connect", 'waist', 'leg-top-right')
        self.add_line('leg-mid-right', (24, 26), (43, 30))
        self.relate("connect", 'waist', 'leg-mid-right')
        self.add_arc('leg-low-right', (24, 28), (43, 46), radius_x=19, radius_y=18, sweep=True)
        self.relate("connect", 'waist', 'leg-low-right')
        self.relate("connect", 'abdomen', 'leg-low-right')
        self.relate("connect", 'leg-top-left', 'leg-top-right')
        self.relate("connect", 'leg-mid-left', 'leg-mid-right')
        self.relate("connect", 'leg-low-left', 'leg-low-right')

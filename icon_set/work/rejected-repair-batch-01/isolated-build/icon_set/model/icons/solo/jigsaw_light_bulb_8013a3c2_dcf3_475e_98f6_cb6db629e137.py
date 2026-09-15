'Puzzle bulb: clean puzzle recess and a deep base, keeping the missing-piece cue.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8013a3c2-dcf3-475e-98f6-cb6db629e137'
SOURCE_PATH = 'pictographic-primitives/work/workflow coaching puzzle lightbulb_8013a3c2-dcf3-475e-98f6-cb6db629e137.svg'
AUTHOR = 'gpt-6'


class JigsawLightBulb(Solo48):
    icon_id = 'jigsaw-light-bulb'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/work"
    aliases = ()
    keywords = ('bulb', 'puzzle', 'jigsaw', 'idea', 'solution', 'creativity')

    def build(self):
        # Puzzle bulb: clean puzzle recess and a deep base, keeping the missing-piece cue.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        a('left-crown',(8,20),(24,4),16)
        l('notch',(24,4),(24,13))
        a('puzzle',(24,13),(24,23),5,sweep=False)
        l('puzzle-edge',(24,23),(40,23))
        a('right-shoulder',(40,23),(32,31),8)
        l('base-right',(32,31),(32,44))
        l('base-bottom',(32,44),(16,44))
        l('base-left',(16,44),(16,31))
        a('left-shoulder',(16,31),(8,20),8,11)
        self.add_contour('bulb','left-crown','notch','puzzle','puzzle-edge','right-shoulder','base-right','base-bottom','base-left','left-shoulder',closed=True)
        l('base-seam',(16,35),(32,35))
        link('connect','bulb','base-seam')
        a('loose-piece',(33,4),(40,11),7)

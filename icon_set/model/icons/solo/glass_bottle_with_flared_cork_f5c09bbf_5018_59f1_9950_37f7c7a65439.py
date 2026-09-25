"""Glass Bottle with Cork Stopper.

Symbol plan: Mirror bottle about x=24; joined flared stopper and shoulder contour. Visible (6,2)-(42,46). A single wave records liquid; omit duplicate inset vessel wall.
Construction references: Lucide wine: liquid cross-section and coherent vessel contour.
Original reference: SOURCE_PATH below; preserved subject, re-authored geometry.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5c09bbf-5018-59f1-9950-37f7c7a65439'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/piracy liquor_f5c09bbf-5018-59f1-9950-37f7c7a65439.svg'
AUTHOR = 'gpt-6'


class GlassBottleWithFlaredCork(Solo48):
    icon_id = 'glass-bottle-with-flared-cork'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('glass', 'bottle', 'with', 'flared', 'cork')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        axis = 24
        left, right = 8, 40
        path('bottle', (16,4), [(32,4),(30,12),(30,16),((34,20),4,4,False),((40,26),6,6,True),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,26),((14,20),6,6,True),((18,16),4,4,False),(18,12),(16,4)], True)
        self.add_line('cork-seam',(18,12),(30,12))
        self.relate('connect','bottle','cork-seam')
        path('liquid',(17,32), [((24,32),4,4,True),((31,32),4,4,False)])

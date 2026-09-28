"""Masked Burglar Carrying Sack.

Symbol plan: Masked head at (32,12), r8, and shoulders y28; exact detached ink gap4. Large left sack joins the simplified shoulder-height grasp. Visible (6,2)-(42,46). Omit eye holes, mask knot and fingers.
Construction references: human_ref/user.svg: circular head and broad shoulders; full_body_ref.png: simplified arm gesture. Lucide hand-grab: reduction to grip gesture.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c3f09802-af83-53a2-a17a-f40b11199de9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/crime man thief_c3f09802-af83-53a2-a17a-f40b11199de9.svg'
AUTHOR = 'gpt-6'


class MaskedBurglarCarryingSack(Solo48):
    icon_id = 'masked-burglar-carrying-sack'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('masked', 'burglar', 'carrying', 'sack')

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
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        path('head',(24,12), [((40,12),8,8,True),((24,12),8,8,True)],True)
        self.add_line('mask',(24,12),(40,12))
        self.relate('connect','mask','head')
        path('shoulder',(32,28),[((40,36),8,8,True),(40,44)])
        self.add_line('arm',(32,28),(24,28))
        self.add_bezier('sack-shoulder',(24,28),((16,28),(8,30),(8,36)))
        self.add_arc('sack-bottom',(8,36),(24,36),radius_x=8,sweep=False)
        self.add_line('sack-neck',(24,36),(24,28))
        self.add_contour('sack','sack-shoulder','sack-bottom','sack-neck',closed=True)
        self.relate('connect','arm','sack')
        self.relate('connect','shoulder','arm')

"""Person Taking an Oath.

Symbol plan: Circular head above upright torso, right oath arm raised, left arm curls inward. Head bottom22, torso30: exact detached ink gap4. Visible (4,4)-(44,44). Omit fingers.
Construction references: human_ref/user.svg and full_body_ref.png: circular head, exact gap and round-ended gesture strokes.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94ab68c9-a988-41a5-b1f9-c945b34ca7ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/oath 1_94ab68c9-a988-41a5-b1f9-c945b34ca7ba.svg'
AUTHOR = 'gpt-6'


class PersonWithRaisedOathHand(Solo48):
    icon_id = 'person-with-raised-oath-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    aliases = ()
    keywords = ('person', 'with', 'raised', 'oath', 'hand')

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

        path('head',(14,14), [((30,14),8,8,True),((14,14),8,8,True)],True)
        self.add_line('torso',(22,30),(22,42))
        path('arm-left',(22,30),[(12,30),((6,36),6,6,False),((12,42),6,6,False),(14,42)])
        self.add_line('raised-shoulder',(22,30),(34,30))
        path('arm-raised',(34,30),[((42,22),8,8,False),(42,14)])
        for a,b in [('torso','arm-left'),('torso','raised-shoulder'),('arm-left','raised-shoulder'),('raised-shoulder','arm-raised')]:self.relate('connect',a,b)
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

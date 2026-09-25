'Acoustic Guitar.\nPlan: Upright neck opens directly into a waisted body, symmetric on x24. Sound hole centered.\nConstruction reference: Lucide guitar: connected neck/body silhouette with reduced musical detail.\nReduction: Strings, bridge and pegs omitted to preserve the sound hole and body waist.\nKeyshape: VRECT_M; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39f10ef4-8250-4acb-b0ce-eaee10f3b757'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/guitars_39f10ef4-8250-4acb-b0ce-eaee10f3b757.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-acoustic-guitar'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('upright', 'acoustic', 'guitar')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def ellipse(name, x, y, rx, ry):
            path(name, (x-rx,y), [((x+rx,y),rx,ry,True), ((x-rx,y),rx,ry,True)], True)

        def circle(name, x, y, radius):
            ellipse(name,x,y,radius,radius)

        def box(name, left, top, right, bottom, radius=4):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('outline',(20,4),[(28,4),(28,19),((36,27),8,8,True),((34,32),7,7,True),((38,38),7,7,True),((32,44),6,6,True),(16,44),((10,38),6,6,True),((14,32),7,7,True),((12,27),7,7,True),((20,19),8,8,True),(20,4)],True)
        circle('sound-hole',24,31,2)

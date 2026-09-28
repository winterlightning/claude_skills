'Town Hall Building.\nPlan: Flat-roof civic building with three window marks and a central doorway.\nConstruction reference: Lucide landmark: distinct roof and repeated facade details.\nReduction: Three window outlines reduced to filled marks; roof overhang reduced.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f52caa33-4341-4e17-9be8-7a993360640f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/hall_f52caa33-4341-4e17-9be8-7a993360640f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'flat-roof-civic-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('flat', 'roof', 'civic', 'building')

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

        path('walls',(6,14),[(6,42),(18,42),(30,42),(42,42),(42,14)])
        path('roof',(6,6),[(42,6),(42,14),(6,14),(6,6)],True);self.relate('connect','walls','roof')
        for x in (14,24,34):self.add_dot(f'window-{x}',(x,22))
        self.add_polyline('door',(18,42),(18,30),(30,30),(30,42));self.relate('connect','door','walls')

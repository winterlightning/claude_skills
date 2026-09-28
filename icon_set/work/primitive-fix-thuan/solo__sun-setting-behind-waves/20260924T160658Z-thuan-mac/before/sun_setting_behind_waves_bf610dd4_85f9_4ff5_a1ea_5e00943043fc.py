'Sunset Over Ocean Waves.\nPlan: Semicircular sun on the first of three shallow parallel water waves.\nConstruction reference: Lucide sunrise and waves: shallow water arcs and a half-disc sun.\nReduction: All three wave lines retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bf610dd4-85f9-4ff5-a1ea-5e00943043fc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fen_bf610dd4-85f9-4ff5-a1ea-5e00943043fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sun-setting-behind-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sun', 'setting', 'behind', 'waves')

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

        path('sun',(14,19),[((24,8),10,11,True),((34,19),10,11,True)])
        for j,y in enumerate((19,29,39)):
         path(f'water-{j}',(4,y),[((24,y),10,1,False),((44,y),10,1,True)])
        self.relate('connect','sun','water-0')

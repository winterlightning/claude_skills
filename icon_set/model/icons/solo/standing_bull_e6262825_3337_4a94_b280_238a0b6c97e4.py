'Horned Bull Farm Animal.\nPlan: Standing right-facing bull; broad body, two readable legs, forward muzzle and rising horns.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Far-side legs merged with the near-side pair; small muzzle details omitted.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e6262825-3337-4a94-b280-238a0b6c97e4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/livestock bull body_e6262825-3337-4a94-b280-238a0b6c97e4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-bull'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('standing', 'bull')

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

        path('body',(4,40),[(4,22),((14,12),10,10,True),(30,12),((38,16),8,8,True),(44,24),(36,24),((30,32),8,8,True),(30,40),(22,40),(22,30),(12,30),(12,40)])
        path('horn-left',(30,12),[((28,8),4,4,True)])
        path('horn-right',(38,16),[((40,8),6,6,False)])
        self.relate('connect','horn-left','body');self.relate('connect','horn-right','body')

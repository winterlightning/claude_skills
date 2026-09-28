'Two People Figures.\nPlan: Two upright round-headed figures with open long body outlines.\nConstruction reference: human_ref/user.svg and full_body_ref.png: outlined heads, shared shoulder radius, open lower bodies.\nReduction: Tiny hip notches omitted; two separate full-height figures retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '0b9cd48a-e936-49e5-8102-fd8d2a559571'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-standing-figures-with-round-heads/20260927T173930Z-thuan-mac-1/reference/escort_0b9cd48a-e936-49e5-8102-fd8d2a559571.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-standing-figures-with-round-heads'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('two', 'standing', 'figures', 'with', 'round', 'heads')

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

        for x in (14,34):
         circle(f'head-{x}',x,8,4)
         path(f'body-{x}',(x-6,44),[(x-6,24),((x-2,20),4,4,True),(x+2,20),((x+6,24),4,4,True),(x+6,44)])

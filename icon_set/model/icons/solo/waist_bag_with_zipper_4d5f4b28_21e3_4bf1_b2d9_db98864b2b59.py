'Zippered Travel Waist Bag.\nPlan: Broad strap loop visible above rounded waist pouch with zipper seam. Bounds4,8..44,40.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit back strap edge hidden behind pouch and tiny zipper pull.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4d5f4b28-21e3-4bf1-b2d9-db98864b2b59'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/fanny pack_4d5f4b28-21e3-4bf1-b2d9-db98864b2b59.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waist-bag-with-zipper'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('waist', 'bag', 'with', 'zipper')

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

        path('strap',(8,24),[((4,16),4,8,True),((24,8),20,8,True),((44,16),20,8,True),((40,24),4,8,True)])
        box('pouch',8,20,40,40,4);self.relate('connect','strap','pouch')
        self.add_line('zipper',(8,29),(40,29));self.relate('connect','pouch','zipper')

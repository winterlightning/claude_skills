'Two Jelly Beans.\nPlan: Three separate rounded jellybeans in a triangular cluster; lower bean retains an inward waist. Bounds6..42. No texture.\nReference: Lucide bean: soft lobed silhouettes; no surface marks.\nKeyshape fitted to exact SOLO48 envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b77c114b-59af-4e4c-a204-66ae35589deb'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_23/jellybeans_b77c114b-59af-4e4c-a204-66ae35589deb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-jellybeans'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'jellybeans')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
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

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        path('left-bean',(6,12),[((22,12),8,6,True),((6,12),8,6,True)],True)
        path('right-bean',(30,18),[((42,18),6,8,True),((30,18),6,8,True)],True)
        path('lower-bean',(12,30),[(17,32),(22,30),((28,36),6,6,True),((22,42),6,6,True),(12,42),((6,36),6,6,True),((12,30),6,6,True)],True)

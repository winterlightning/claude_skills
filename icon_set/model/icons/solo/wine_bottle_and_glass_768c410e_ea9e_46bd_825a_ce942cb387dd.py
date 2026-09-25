'Wine Bottle and Glass.\nPlan: Bottle left and stemmed glass right; narrow neck and rounded shoulder. Bounds6..42.\nConstruction reference: Lucide wine original and atomic-debug: rounded cup on central stem and flat foot.\nReduction: Keep the defining silhouette and essential parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '768c410e-ea9e-46bd-825a-ce942cb387dd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/winery_768c410e-ea9e-46bd-825a-ce942cb387dd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'wine-bottle-and-glass'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('wine', 'bottle', 'and', 'glass')

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

        path('bottle',(10,6),[(18,6),(18,16),((22,24),10,10,False),(22,42),(6,42),(6,24),((10,16),10,10,False),(10,6)],True)
        path('glass',(32,22),[(42,22),(42,28),((32,28),5,6,True),(32,22)],True)
        self.add_line('stem',(37,34),(37,42));self.add_line('foot',(32,42),(42,42));self.relate('connect','glass','stem');self.relate('connect','stem','foot')

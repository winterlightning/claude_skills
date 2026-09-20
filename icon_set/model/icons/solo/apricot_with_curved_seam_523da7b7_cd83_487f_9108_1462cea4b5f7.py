'Apricot Fruit with Leaf.\nPlan: Round apricot with a restrained curved seam and a short upper-right stem.\nConstruction reference: Lucide apple: coherent fruit contour.\nReduction: Leaf reduced to its stem after the leaf attachment crowded the fruit; apricot seam retained.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '523da7b7-cd83-487f-9108-1462cea4b5f7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/fruit apricot_523da7b7-cd83-487f-9108-1462cea4b5f7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apricot-with-curved-seam'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('apricot', 'with', 'curved', 'seam')

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

        ellipse('fruit',24,29,16,15)
        path('seam',(24,14),[((24,44),40,40,False)])
        self.relate('connect','seam','fruit')
        self.add_line('stem',(24,14),(32,4));self.relate('connect','stem','fruit');self.relate('connect','stem','seam')

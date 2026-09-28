'Hand Washing with Water.\nPlan: Upturned left hand below three broken water streams.\nConstruction reference: Lucide hand-helping: open palm with raised thumb.\nReduction: Individual fingers merged into one broad palm silhouette.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a34cf5c7-6f9d-4929-bade-fa576555a44e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_25/locker room wash hands 1_a34cf5c7-6f9d-4929-bade-fa576555a44e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hand-under-running-water'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hand', 'under', 'running', 'water')

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

        path('hand',(6,34),[(18,34),(26,28),((32,34),4,4,True),(36,34),((42,38),6,4,True),((36,42),6,4,True),(6,42)])
        for j,x in enumerate((16,28,40)):
         self.add_line(f'water-{j}',(x,6),(x,8))
         self.add_dot(f'drop-{j}',(x,17))

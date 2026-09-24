'Angel Heart with Halo.\nPlan: Heart between two mirrored wings beneath a floating oval halo. Halo and lobes have 9u minimum axial separation.\nConstruction reference: Lucide heart: equal lobe radii; source halo and wing relationship retained.\nReduction: Wings reduced to one broad feather on each side.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5eceeb50-90bb-44d1-b139-73fdd09edb8b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/love it angel_5eceeb50-90bb-44d1-b139-73fdd09edb8b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angel-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('angel', 'heart')

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

        ellipse('halo',24,10,8,4)
        path('heart',(24,28),[((14,28),5,5,False),((24,42),15,15,False),((34,28),15,15,False),((24,28),5,5,False)],True)
        path('left-wing',(14,28),[((6,28),4,4,False),(6,42),(12,36)])
        path('right-wing',(34,28),[((42,28),4,4,True),(42,42),(36,36)])
        self.relate('connect','heart','left-wing');self.relate('connect','heart','right-wing')

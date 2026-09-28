'Academic Graduation Cap with Tassel.\nPlan: Diamond board, rounded headband, left cord. Shared board nodes own attachments.\nConstruction reference: Lucide graduation-cap: diamond top, curved band, one hanging cord.\nReduction: Tassel reduced to one bold cord; tuft outline removed.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5372370f-380a-4e85-8b88-7380c5c97ff0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/graduation cap_5372370f-380a-4e85-8b88-7380c5c97ff0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'graduation-cap-with-hanging-tassel'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('graduation', 'cap', 'with', 'hanging', 'tassel')

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

        self.add_polyline('board',(4,18),(24,8),(44,18),(24,28),closed=True)
        path('band',(14,23),[(14,30),((34,30),10,10,False),(34,23)])
        self.relate('connect','board','band')
        self.add_line('tassel',(4,18),(4,38));self.relate('connect','board','tassel')

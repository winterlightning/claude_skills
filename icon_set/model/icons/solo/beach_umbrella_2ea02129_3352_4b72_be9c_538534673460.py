'Beach Umbrella on Sand.\nPlan: Broad semicircular canopy and central pole meet a gently curved sand line.\nConstruction reference: Lucide umbrella: semicircular canopy and central shaft.\nReduction: Wavy sand flattened to one ground stroke; canopy scallops retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ea02129-3352-4b72-be9c-538534673460'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/umbrella beach_2ea02129-3352-4b72-be9c-538534673460.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'beach-umbrella'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('beach', 'umbrella')

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

        path('canopy',(4,28),[((44,28),20,20,True),((34,28),5,5,False),((24,28),5,5,False),((14,28),5,5,False),((4,28),5,5,False)],True)
        self.add_line('pole',(24,28),(24,40));self.relate('connect','pole','canopy')
        self.add_polyline('sand',(4,40),(24,40),(44,40));self.relate('connect','pole','sand')

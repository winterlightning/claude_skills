'Handshake Agreement.\nPlan: Clasped hands between two angled wrists, with a crossing thumb and rounded fingers.\nConstruction reference: Lucide handshake: interlocked central thumb, angled wrists, and one unified lower finger contour.\nReduction: Individual knuckle divisions merged for clearance.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '868a7716-d4f7-4888-920c-c73290bf6c57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_19/fists crashing conflict_868a7716-d4f7-4888-920c-c73290bf6c57.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clasped-handshake'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('clasped', 'handshake')

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

        self.add_polyline('left-wrist',(4,24),(14,8),(24,14))
        self.add_polyline('right-wrist',(44,24),(34,8),(24,14))
        self.relate('connect','left-wrist','right-wrist')
        path('clasp',(24,14),[(16,22),((22,28),4,4,False),(28,22),(36,30),(36,34),((30,40),6,6,True),(26,40),(10,38),(4,24)])
        self.relate('connect','clasp','left-wrist');self.relate('connect','clasp','right-wrist')
        self.add_line('right-palm',(44,24),(36,30));self.relate('connect','right-palm','clasp');self.relate('connect','right-palm','right-wrist')

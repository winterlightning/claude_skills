'Hanging Leafy Branch.\nPlan: Arched hanging branch and two broad pointed leaves around a descending central stem.\nConstruction reference: Lucide wheat: broad leaf contours and shared stem nodes.\nReduction: Four leaves reduced to a single pair to preserve the hanging botanical silhouette at 48.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5a1907a8-d849-42eb-8ab1-4dba897daeb9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wisteria_5a1907a8-d849-42eb-8ab1-4dba897daeb9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hanging-leafy-branch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hanging', 'leafy', 'branch')

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

        path('branch',(8,44),[(8,20),((24,4),16,16,True),(40,4)])
        self.add_polyline('stem',(28,4),(28,20),(28,44));self.relate('connect','stem','branch')
        path('leaf-left',(28,20),[((18,36),10,16,False),((28,20),10,16,False)],True)
        path('leaf-right',(28,20),[((40,36),12,16,True),((28,20),12,16,True)],True)
        self.relate('connect','stem','leaf-left');self.relate('connect','stem','leaf-right')

'Tropical Island Palm Tree.\nPlan: A palm tree with four arching fronds rises from a low island.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Leaf outlines and trunk width reduced to strokes; island retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e7cfd73-e25b-4de2-adf5-0bafae1a1fea'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tree palm_3e7cfd73-e25b-4de2-adf5-0bafae1a1fea.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'island-palm-tree'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('island', 'palm', 'tree')

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

        path('frond-ul',(4,18),[((24,18),10,10,True)])
        path('frond-ur',(24,18),[((44,18),10,10,True)])
        path('frond-ll',(4,28),[((24,18),20,10,True)])
        path('frond-lr',(24,18),[((44,28),20,10,True)])
        self.add_line('trunk',(24,18),(24,32))
        names=['frond-ul','frond-ur','frond-ll','frond-lr','trunk']
        for j,a in enumerate(names):
         for b in names[j+1:]:self.relate('connect',a,b)
        path('island',(4,40),[((24,32),20,8,True),((44,40),20,8,True)])
        self.relate('connect','trunk','island')
        self.add_line('base',(4,40),(44,40));self.relate('connect','base','island')

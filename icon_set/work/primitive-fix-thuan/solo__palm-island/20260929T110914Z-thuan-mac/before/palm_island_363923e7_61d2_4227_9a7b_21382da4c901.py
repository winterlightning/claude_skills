'Tropical Island with Palm Tree.\nPlan: Palm tree on a low island with water to either side.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Five fronds reduced to four; water shown at the sides instead of across the island base.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '363923e7-61d2-4227-9a7b-21382da4c901'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/island_363923e7-61d2-4227-9a7b-21382da4c901.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'palm-island'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('palm', 'island')

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
        path('frond-ll',(4,27),[((24,18),20,9,True)])
        path('frond-lr',(24,18),[((44,27),20,9,True)])
        self.add_line('trunk',(24,18),(24,32))
        names=['frond-ul','frond-ur','frond-ll','frond-lr','trunk']
        for j,a in enumerate(names):
         for b in names[j+1:]:self.relate('connect',a,b)
        path('island',(10,38),[((24,32),14,6,True),((38,38),14,6,True)])
        self.relate('connect','trunk','island')
        path('water-left',(4,38),[((10,38),3,2,False)])
        path('water-right',(38,38),[((44,38),3,2,False)])
        self.relate('connect','water-left','island');self.relate('connect','water-right','island')

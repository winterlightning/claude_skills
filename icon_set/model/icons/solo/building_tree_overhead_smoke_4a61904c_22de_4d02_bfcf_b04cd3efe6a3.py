'Urban Building with Smoke Cloud.\nPlan: City scene: smoke above rectangular building and pointed tree on shared ground. Bounds6..42.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Omit short internal smoke curl and incomplete roof detail; retain building, tree, ground and overhanging smoke.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4a61904c-22de-4d02-bfcf-b04cd3efe6a3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/air pollution city_4a61904c-22de-4d02-bfcf-b04cd3efe6a3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'building-tree-overhead-smoke'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('building', 'tree', 'overhead', 'smoke')

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

        self.add_polyline('building',(6,42),(6,24),(22,24),(22,42));self.add_line('ground',(6,42),(42,42));self.relate('connect','building','ground')
        
        path('tree',(36,22),[(42,28),((30,28),6,6,True),(36,22)],True)
        self.add_line('trunk',(36,34),(36,42));self.relate('connect','tree','trunk');self.relate('connect','trunk','ground')
        path('smoke',(6,6),[((16,11),8,8,False),((30,14),10,10,False),((42,6),10,10,False)])

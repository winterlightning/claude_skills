'Tall Reeds in Water.\nPlan: Five reeds of varied heights above a bank and separate water ripple.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: One minor curved shoot omitted.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2540bed0-e5b0-4da8-843a-385b2235cda0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/swamp_2540bed0-e5b0-4da8-843a-385b2235cda0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'waterside-reed-stems'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('waterside', 'reed', 'stems')

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

        self.add_polyline('bank',(4,29),(12,29),(20,29),(28,29),(36,29),(44,29))
        for j,x in enumerate((12,20,28,36)):
         y=(20,14,8,12)[j];self.add_line(f'reed-{j}',(x,29),(x,y));self.relate('connect',f'reed-{j}','bank')
        path('shoot',(36,29),[((44,22),16,16,True)]);self.relate('connect','shoot','bank');self.relate('connect','shoot','reed-3')
        path('water',(6,39),[((18,39),6,1,True),((30,39),6,1,False),((42,39),6,1,True)])

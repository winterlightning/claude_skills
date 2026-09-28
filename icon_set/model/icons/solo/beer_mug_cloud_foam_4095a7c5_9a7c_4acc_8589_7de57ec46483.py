'Beer Mug with Foam.\nPlan: Rounded mug with foam crown, one face groove and a genuinely attached loop handle.\nConstruction reference: Lucide beer: lobed foam and rounded mug with attached handle.\nReduction: Two grooves reduced to one; foam small scallops omitted.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4095a7c5-9a7c-4acc-8589-7de57ec46483'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/ale_4095a7c5-9a7c-4acc-8589-7de57ec46483.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'beer-mug-cloud-foam'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('beer', 'mug', 'cloud', 'foam')

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

        path('body',(8,18),[(30,18),(30,26),(30,36),(30,40),((26,44),4,4,True),(12,44),((8,40),4,4,True),(8,18)],True)
        path('foam',(8,18),[(8,14),((12,10),4,4,True),(14,10),((26,10),6,6,True),((30,14),4,4,True),(30,18),(8,18)],True)
        self.relate('connect','body','foam')
        path('handle',(30,26),[(36,26),((40,30),4,4,True),(40,32),((36,36),4,4,True),(30,36)])
        self.relate('connect','body','handle')
        self.add_line('groove',(19,27),(19,35))

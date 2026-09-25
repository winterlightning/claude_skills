'Three Jaw Lathe Chuck.\nPlan: Circular lathe chuck with three broad inward jaws and an open center.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Transverse jaw seams omitted; three jaws and clear center retained.\nKeyshape: CIRCLE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b6181c28-b0ba-43c0-a780-8573246ca4d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/lathe chuck_b6181c28-b0ba-43c0-a780-8573246ca4d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-jaw-lathe-chuck'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('three', 'jaw', 'lathe', 'chuck')

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

        path('rim',(12,8),[((24,4),20,20,True),((36,8),20,20,True),((44,24),20,20,True),((36,40),20,20,True),((24,44),20,20,True),((12,40),20,20,True),((4,24),20,20,True),((12,8),20,20,True)],True)
        path('top-jaw',(12,8),[(20,12),(20,14),((28,14),4,4,False),(28,12),(36,8)])
        path('left-jaw',(4,24),[(12,24),((16,32),4,8,True),(12,40)])
        path('right-jaw',(44,24),[(36,24),((32,32),4,8,False),(36,40)])
        for n in ('top-jaw','left-jaw','right-jaw'):self.relate('connect','rim',n)

'Three People Wearing Balaclavas.\nPlan: Three hooded heads with a complete foreground eye opening and two joined rear brows.\nConstruction reference: No useful exact local Lucide match; geometric arcs and coherent contours preserve the supplied subject.\nReduction: Rear lower face curves omitted; the foreground mask retains its full eye opening and neck tails.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b87e413a-6c06-4509-b808-28f85d67c2a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/terrorists 1_b87e413a-6c06-4509-b808-28f85d67c2a6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-balaclava-wearers'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'balaclava', 'wearers')

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

        path('left',(8,20),[(8,12),((24,12),8,8,True)])
        path('right',(40,20),[(40,12),((24,12),8,8,False)])
        self.relate('connect','left','right')
        for name,x in [('left',8),('right',24)]:
         self.add_line('eyes-'+name,(x,12),(x+16,12));self.relate('connect','eyes-'+name,name)
        self.relate('connect','eyes-left','eyes-right');self.relate('connect','eyes-left','right');self.relate('connect','eyes-right','left')
        circle('front',24,32,8)
        self.add_line('front-eyes',(16,32),(32,32));self.relate('connect','front-eyes','front')
        for x in (16,32):
         self.add_line(f'neck-{x}',(x,32),(x,44));self.relate('connect',f'neck-{x}','front');self.relate('connect',f'neck-{x}','front-eyes')

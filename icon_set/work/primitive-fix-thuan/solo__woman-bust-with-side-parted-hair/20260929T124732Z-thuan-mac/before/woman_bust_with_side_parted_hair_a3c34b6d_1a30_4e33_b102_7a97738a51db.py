'Woman Profile Avatar Icon.\nPlan: Side-parted hair around circular lower face, above broad curved shoulders. Jaw24,20 r8; bodytop32 means zero ink gap.\nConstruction reference: human_ref/user.svg circular jaw and rounded shoulders; source asymmetric hair part retained.\nReduction: Omit narrow neck, blouse base and fine hair tips.\nKeyshape: VRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3c34b6d-1a30-4e33-b102-7a97738a51db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/ex wife_a3c34b6d-1a30-4e33-b102-7a97738a51db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'woman-bust-with-side-parted-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('woman', 'bust', 'with', 'side', 'parted', 'hair')

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

        path('hair',(8,26),[(8,20),((40,20),16,16,True),(40,26)])
        self.add_arc('jaw',(32,20),(16,20),radius_x=8)
        self.add_bezier('fringe',(16,20),((22,20),(25,16),(28,12)),((28,16),(30,18),(32,20)))
        self.relate('connect','fringe','jaw')
        for side,x in [('left',8),('right',32)]:
         self.add_line('temple-'+side,(x,20),(x+8,20));self.relate('connect','temple-'+side,'hair');self.relate('connect','temple-'+side,'jaw');self.relate('connect','temple-'+side,'fringe')
        self.add_arc('body-left',(8,44),(20,32),radius_x=12)
        self.add_line('body-top',(20,32),(28,32))
        self.add_arc('body-right',(28,32),(40,44),radius_x=12)
        self.add_contour('body','body-left','body-top','body-right');self.relate('connect','jaw','body')

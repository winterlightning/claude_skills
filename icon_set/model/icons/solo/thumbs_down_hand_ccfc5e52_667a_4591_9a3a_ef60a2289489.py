'Thumb Pointing Down Icon.\nPlan: Raised or lowered thumb, curved palm, closed fingers and left wrist.\nConstruction reference: Lucide thumbs-up and thumbs-down: coherent thumb/palm contour and separate cuff junction.\nReduction: Four tiny finger creases reduced to one central crease; thumb direction and cuff distinction retained.\nKeyshape: HRECT_L; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ccfc5e52-667a-4591-9a3a-ef60a2289489'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/thumbs down_ccfc5e52-667a-4591-9a3a-ef60a2289489.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'thumbs-down-hand'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('thumbs', 'down', 'hand')

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

        def point(x,y):return (x,48-y) if True else (x,y)
        def handpath(name,start,steps,closed=False):
         out=[]
         for step in steps:
          if len(step)==2:out.append(point(*step))
          else:out.append((point(*step[0]),step[1],step[2],not step[3] if True else step[3]))
         path(name,point(*start),out,closed)
        handpath('hand',(14,24),[(20,18),(22,8),(26,8),((30,12),4,4,True),(28,22),(38,22),((44,28),6,6,True),(44,31),(44,34),((38,40),6,6,True),(14,40)])
        self.add_line('finger-crease',point(35,31),point(44,31));self.relate('connect','finger-crease','hand')

        handpath('cuff',(14,24),[(6,24),((4,26),2,2,False),(4,38),((6,40),2,2,False),(14,40),(14,24)],True);self.relate('connect','hand','cuff')

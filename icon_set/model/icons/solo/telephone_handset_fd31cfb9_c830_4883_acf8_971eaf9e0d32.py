'Telephone Handset Receiver.\nPlan: Diagonal telephone receiver with broad rounded ends and a narrower curved grip.\nConstruction reference: Lucide phone: broad terminal blocks connected by one continuous curved receiver.\nReduction: No omitted identifying parts.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd31cfb9-c830-4883-acf8-971eaf9e0d32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/tty_fd31cfb9-c830-4883-acf8-971eaf9e0d32.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'telephone-handset'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('telephone', 'handset')

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

        path('phone',(6,12),[((12,6),6,6,True),(18,6),((22,10),4,4,True),(22,16),(16,20),((28,32),18,18,False),(32,26),(38,26),((42,30),4,4,True),(42,36),((36,42),6,6,True),((6,12),30,30,True)],True)

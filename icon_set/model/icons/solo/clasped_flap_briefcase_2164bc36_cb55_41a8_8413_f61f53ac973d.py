'Clasped Flap Briefcase\nPlan: Rounded briefcase body and drooping flap interrupted by central clasp.\nReference: Lucide briefcase-business: rounded body and broad curved flap.\nReduction: Retain plain clasp; supplied clutch has no handle, so none added.\nKeyshape: HRECT_M; exact SOLO48 contract envelope.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2164bc36-cb55-41a8-8413-f61f53ac973d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clutch_2164bc36-cb55-41a8-8413-f61f53ac973d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clasped-flap-briefcase'
    keyshape = Keyshape.HRECT_M
    category = "objects"
    keywords = ('clasped', 'flap', 'briefcase')

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
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        box('body',4,10,44,38,4)
        self.add_bezier('flap-left',(4,19),((4,23),(12,20),(20,20)))
        self.add_bezier('flap-right',(28,20),((36,20),(44,23),(44,19)))
        path('clasp',(20,20),[(20,24),((28,24),4,4,False),(28,20)])
        for p in ['flap-left','flap-right']:self.relate('connect',p,'body');self.relate('connect',p,'clasp')

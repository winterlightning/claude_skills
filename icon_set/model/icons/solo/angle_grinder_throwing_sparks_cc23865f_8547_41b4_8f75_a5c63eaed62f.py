'A horizontal motor housing meets a cutting disc with two sparks below. HRECT_L reserves width for the motor and height for sparks. Motor shell and exposed disc share the two real guard endpoints; sparks remain detached. Retain a single spindle dot; omit the separate guard seam. Source defines tool layout; no useful Lucide grinder match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc23865f-8547-41b4-8f75-a5c63eaed62f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_03/angle grinder_cc23865f-8547-41b4-8f75-a5c63eaed62f.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'angle-grinder-throwing-sparks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Angle Grinder Throwing Sparks',)
    keywords = ('grinder', 'tool', 'disc', 'cutting', 'sparks', 'power tool', 'workshop')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[];point=start
            for j,step in enumerate(steps):
                member=f"{name}-{j}"
                if len(step)==2:self.add_line(member,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('motor',(34,8),[(14,8),((4,18),10,10,False),((14,28),10,10,False),(34,28)])
        path('disc',(34,8),[((34,28),10,10,True),((34,8),10,10,True)],True)
        self.relate('connect','motor','disc')
        self.add_dot('spindle',(34,18))
        self.add_line('spark-right',(40,36),(44,40))
        self.add_line('spark-left',(28,36),(26,40))

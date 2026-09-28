'Dripping Wax Pot.\nPlan and review: Retained rounded pot and wax layer with two unequal drips.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd17ea3f7-3c72-47c7-a0c5-d88e0cf7a4aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/wax_d17ea3f7-3c72-47c7-a0c5-d88e0cf7a4aa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dripping-wax-pot'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('dripping', 'wax', 'pot')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        path('wax',(10,8),[(38,8),((44,14),6,6,True),((38,20),6,6,True),(30,20),(30,28),((22,28),4,4,True),(22,20),(14,20),(14,24),((6,24),4,4,True),(6,20),(4,20),(4,14),((10,8),6,6,True)],True)
        path('pot',(6,28),[(6,34),((12,40),6,6,False),(34,40),((40,34),6,6,False),(40,20)])
        self.relate('connect','pot','wax')

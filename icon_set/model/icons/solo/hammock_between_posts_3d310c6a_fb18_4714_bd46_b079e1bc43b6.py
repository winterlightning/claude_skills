'Relaxing Hammock Between Posts.\nPlan and review: Retained two posts and sagging hammock edges, with shared suspension anchors.\nKeyshape: HRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3d310c6a-fb18-4714-bd46-b079e1bc43b6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hammock_3d310c6a-fb18-4714-bd46-b079e1bc43b6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hammock-between-posts'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hammock', 'between', 'posts')

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

        self.add_polyline('post-left',(4,8),(4,16),(4,40));self.add_polyline('post-right',(44,8),(44,16),(44,40))
        curve('edge',(4,16),((14,26),(34,26),(44,16)))
        curve('sling',(4,16),((14,44),(34,44),(44,16)))
        for a in ('edge','sling'):
         for b in ('post-left','post-right'):self.relate('connect',a,b)

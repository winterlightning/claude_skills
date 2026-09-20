'Simple Fishing Hook.\nPlan and review: Retained round attachment eye, long shank, broad J curve and short barb.\nKeyshape: VRECT_M, exact SOLO48 envelope.\nConstruction reference: Lucide fishing-hook: round eye, connected shank and curved barbed hook.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c7a6c633-99f0-442a-8fff-3b4f5f38507c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_37/tackle_c7a6c633-99f0-442a-8fff-3b4f5f38507c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-eye-fishing-hook'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'eye', 'fishing', 'hook')

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

        path('eye',(32,16),[((32,4),6,6,True),((32,16),6,6,True)],True)
        path('hook',(32,16),[(32,33),((10,33),11,11,True),(10,26),(16,32)])
        self.relate('connect','eye','hook')

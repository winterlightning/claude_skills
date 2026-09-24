'Round Hat Box with Handle.\nPlan and review: Retained cylindrical box, oval lid and arched handle. Omitted doubled lid band and increased handle-to-lid clearance.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd694669-154a-40d8-b638-21a45768cc05'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hatbox_cd694669-154a-40d8-b638-21a45768cc05.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-hatbox-with-loop-handle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('round', 'hatbox', 'with', 'loop', 'handle')

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

        path('lid',(8,24),[((40,24),16,8,True),((8,24),16,8,True)],True)
        path('body',(8,24),[(8,36),((40,36),16,8,False),(40,24)]);self.relate('connect','body','lid')
        path('handle',(18,18),[(18,10),((30,10),6,6,True),(30,18)]);self.relate('connect','handle','lid')

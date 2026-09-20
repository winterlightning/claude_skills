'Curvy Winding Road Path.\nPlan and review: Retained two open winding banks and alternating turns; repaired the turn spacing and removed a retraced run.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9241789e-a5ea-4981-8e17-8dadce4a7803'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/trail_9241789e-a5ea-4981-8e17-8dadce4a7803.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curvy-winding-road-path'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('curvy', 'winding', 'road', 'path')

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

        path('bank-left',(42,6),[(16,6),((6,16),10,10,False),((16,25),10,9,False),(28,25),((28,33),4,4,True),(14,33),((6,42),8,9,False)])
        path('bank-right',(20,16),[(30,16),((42,28),12,12,True),((28,42),14,14,True),(18,42)])

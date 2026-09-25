'Dizzy Hypnotized Face.\nPlan and review: UNRESOLVED: readable spiral eyes exceed face/eye and inter-eye clearance. A smaller candidate passed numeric checks but lost its spiral identity; it was rejected visually. The recognizable larger draft remains unapproved.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this subject.\nConstruction reference: Source spiral construction; Lucide circular face vocabulary.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf969d29-b35a-425d-bec1-f3067a6600b5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/face spiral eyes_cf969d29-b35a-425d-bec1-f3067a6600b5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dizzy-hypnotized-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('dizzy', 'hypnotized', 'face')

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

        circle('head',24,24,20)
        # Preserve visible spirals in this unresolved draft instead of collapsing their openings.
        for j,x in enumerate((14,34)):
         curve(f'spiral-{j}',(x-8,22),((x-8,11),(x+8,11),(x+8,22)),((x+8,30),(x-4,30),(x-4,22)),((x-4,18),(x+2,18),(x+2,22)))
        self.add_line('mouth',(20,35),(28,35))

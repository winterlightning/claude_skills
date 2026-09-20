'Rectangular Aftershave Bottle.\nPlan and review: Retained rectangular bottle, short rectangular cap and blank label. Omitted narrow neck seam.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '078b15ae-a8b0-46f7-9d70-ae907f416879'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/aftershave_078b15ae-a8b0-46f7-9d70-ae907f416879.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'aftershave-rectangular-label-bottle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('aftershave', 'rectangular', 'label', 'bottle')

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

        box('bottle',8,16,40,44,4)
        path('cap',(18,16),[(18,4),(30,4),(30,16)]);self.relate('connect','cap','bottle')
        box('label',17,25,31,35,2)

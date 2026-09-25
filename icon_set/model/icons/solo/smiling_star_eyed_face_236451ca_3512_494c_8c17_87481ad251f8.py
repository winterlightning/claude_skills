'Excited Face With Star Eyes.\nPlan and review: UNRESOLVED: both the larger and reduced five-point star eyes failed spacing. Smaller stars also create undersized trapped holes and lose their outlined identity at 48px. Preserved the smaller diagnostic draft; it is not an accepted icon.\nKeyshape: CIRCLE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '236451ca-3512-494c-8c17-87481ad251f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face awesome_236451ca-3512-494c-8c17-87481ad251f8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smiling-star-eyed-face'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('smiling', 'star', 'eyed', 'face')

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
        for n,x in enumerate((17,31)):
         path(f'star-{n}',(x,15),[(x+1,18),(x+4,18),(x+2,21),(x+3,24),(x,22),(x-3,24),(x-2,21),(x-4,18),(x-1,18),(x,15)],True)
        self.add_arc('smile',(18,31),(30,31),radius_x=6,radius_y=4,sweep=False)

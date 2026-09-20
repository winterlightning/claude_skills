'Simple House with Arched Doorway.\nPlan and review: Retained steep roof, rectangular body and rounded arched doorway. Corrected the first square-door draft so it remains distinct from neighboring houses.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide house: continuous roof/wall silhouette and centered doorway.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fcbed669-2d73-47b0-926c-d41e6f39bf36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/hut_fcbed669-2d73-47b0-926c-d41e6f39bf36.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hut-with-arched-doorway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('hut', 'with', 'arched', 'doorway')

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

        path('house',(18,42),[(10,42),(10,22),(6,22),(24,6),(42,22),(38,22),(38,42),(30,42),(30,34),((18,34),6,6,False),(18,42)])

        self.add_line('baseline',(18,42),(30,42));self.relate('connect','baseline','house')

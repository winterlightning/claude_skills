'Face with Cowboy Hat.\nPlan and review: Retained pinched cowboy crown, broad curved brim and blank circular lower face. Brim and jaw have touching painted edges.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7a439e2-504d-4cce-bf79-ba911a657a41'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face cowboy hat_e7a439e2-504d-4cce-bf79-ba911a657a41.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blank-face-wearing-cowboy-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('blank', 'face', 'wearing', 'cowboy', 'hat')

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

        path('crown',(14,20),[(17,8),(24,12),(31,8),(34,20)])
        curve('brim',(4,14),((4,20),(8,24),(12,24)),((20,24),(28,24),(36,24)),((40,24),(44,20),(44,14)))
        self.relate('connect','crown','brim')
        self.add_arc('jaw',(12,28),(36,28),radius_x=12,sweep=False)
        self.relate('connect','jaw','brim')

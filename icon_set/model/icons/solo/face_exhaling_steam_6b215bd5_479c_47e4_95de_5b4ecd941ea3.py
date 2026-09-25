'Face Exhaling Breath.\nPlan and review: Retained open-bottom face, closed-eye strokes and descending breath curls. Reduced three breath strokes to two and omitted the small nose; opened the lower side outline for clearance.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6b215bd5-479c-47e4-95de-5b4ecd941ea3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_17/face nose steam_6b215bd5-479c-47e4-95de-5b4ecd941ea3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'face-exhaling-steam'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('face', 'exhaling', 'steam')

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

        path('head',(8,28),[(8,20),((40,20),16,16,True),(40,28)])
        self.add_line('eye-left',(17,20),(20,21));self.add_line('eye-right',(28,21),(31,20))
        curve('breath-left',(19,30),((15,35),(21,39),(17,44)))
        curve('breath-right',(31,30),((27,35),(33,39),(29,44)))

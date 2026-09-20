'Five Leaf Plant Sprig.\nPlan and review: Retained all five leaves: two opposite pairs and a terminal leaf. Rebalanced leaf bands and stem spacing; simplified the top leaf to a rounded outline.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '06808980-71a3-47b2-b2d9-3755a6f8a361'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/alfalfa_06808980-71a3-47b2-b2d9-3755a6f8a361.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'five-leaf-upright-sprig'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('five', 'leaf', 'upright', 'sprig')

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

        self.add_polyline('stem',(24,12),(24,28),(24,44))
        curve('leaf-top',(24,4),((18,4),(18,12),(24,12)),((30,12),(30,4),(24,4)))
        self.relate('connect','stem','leaf-top')
        for row,y in enumerate((20,36)):
         for side,s in enumerate((-1,1)):
          name=f'leaf-{row}-{side}';curve(name,(24,y+8),((24+s*12,y+8),(24+s*16,y+4),(24+s*16,y)),((24+s*4,y),(24,y+4),(24,y+8)))
          self.relate('connect',name,'stem')

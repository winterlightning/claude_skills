'Simple House Home Building.\nPlan and review: Retained peaked roof, projecting eaves and rectangular doorway open through the lower edge.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide house: continuous roof/wall silhouette and centered doorway.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '501d4799-3e29-48d7-ac79-d02739b401cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/townhouse_501d4799-3e29-48d7-ac79-d02739b401cb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-open-doorway'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('house', 'with', 'open', 'doorway')

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

        path('house',(18,42),[(10,42),(10,22),(6,22),(24,6),(42,22),(38,22),(38,42),(30,42),(30,30),(18,30),(18,42)])

'Simple Standing Chicken Icon.\nPlan and review: Retained left-facing hen, comb, small beak, broad belly, raised right tail and two legs. Integrated comb and beak into the silhouette to remove tiny overlaps.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Lucide bird: body/leg structure, source left-facing hen and raised tail retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '325e54cb-8d70-4bde-86ba-e15543964464'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_22/hen_325e54cb-8d70-4bde-86ba-e15543964464.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'standing-hen-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('standing', 'hen', 'profile')

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

        curve('crown',(10,14),((10,8),(10,6),(16,6)),((16,8),(18,8),(20,8)),((20,12),(20,14),(22,18)),((26,26),(34,20),(42,14)))
        curve('belly',(42,14),((42,28),(34,32),(24,32)),((12,32),(8,28),(10,20)))
        path('beak',(10,20),[(6,18),(10,14)])
        for a,b in [('crown','belly'),('crown','beak'),('belly','beak')]:self.relate('connect',a,b)
        for j,x in enumerate((16,32)):
         path(f'leg-{j}',(x,31),[(x-2,42),(x-6,42)]);self.relate('connect',f'leg-{j}','belly')

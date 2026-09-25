'Falcon Head Profile.\nPlan and review: Retained left-facing hooked falcon beak, rounded crown, eye and neck profile. Omitted separate brow and lower feather detail; intentional asymmetry follows the source.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '731770b0-068a-4e6d-8736-2a503b462801'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_18/falcon_731770b0-068a-4e6d-8736-2a503b462801.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'falcon-head-facing-left'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('falcon', 'head', 'facing', 'left')

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

        curve('crown',(12,18),((12,2),(34,2),(38,18)),((40,26),(40,32),(42,38)))
        curve('neck-back',(42,38),((28,30),(22,38),(14,42)))
        curve('neck-front',(14,42),((14,30),(24,24),(18,22)))
        curve('beak',(12,18),((6,18),(6,22),(6,26)),((9,22),(15,22),(18,22)))
        for a,b in [('crown','neck-back'),('neck-back','neck-front'),('neck-front','beak'),('crown','beak')]:self.relate('connect',a,b)
        self.add_dot('eye',(26,16))

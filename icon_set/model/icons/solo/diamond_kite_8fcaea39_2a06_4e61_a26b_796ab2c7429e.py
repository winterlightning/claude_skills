'Flying Kite with Tail.\nPlan and review: Retained asymmetric diamond kite, crossing spars and short winding tail. All spar intersections share an exact node.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8fcaea39-2a06-4e61-a26b-796ab2c7429e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/kite_8fcaea39-2a06-4e61-a26b-796ab2c7429e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diamond-kite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('diamond', 'kite')

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

        path('kite',(18,6),[(42,6),(42,30),(12,36),(18,6)],True)
        path('spar-one',(18,6),[(28,20),(42,30)]);path('spar-two',(42,6),[(28,20),(12,36)])
        for s in ('spar-one','spar-two'):self.relate('connect','kite',s)
        self.relate('connect','spar-one','spar-two')
        curve('tail',(12,36),((12,40),(10,42),(6,42)));self.relate('connect','tail','kite');self.relate('connect','tail','spar-two')

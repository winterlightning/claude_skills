'Faceted Diamond Gemstone.\nPlan and review: Retained gemstone silhouette, horizontal girdle and lower triangular facets. Omitted the small upper facet divisions.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide gem: horizontal girdle and converging lower facets.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '373b0263-1111-4887-aef2-953edca21fe4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gem_373b0263-1111-4887-aef2-953edca21fe4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'faceted-diamond-solo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('faceted', 'diamond', 'solo')

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

        path('gem',(4,20),[(14,8),(34,8),(44,20),(24,40),(4,20)],True)
        self.add_polyline('girdle',(4,20),(16,20),(32,20),(44,20));self.relate('connect','gem','girdle')
        path('facets',(16,20),[(24,40),(32,20)]);self.relate('connect','gem','facets');self.relate('connect','girdle','facets')

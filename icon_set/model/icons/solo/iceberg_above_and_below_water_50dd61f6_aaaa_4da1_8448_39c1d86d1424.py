'Floating Iceberg in the Sea.\nPlan and review: Retained uneven upper iceberg peaks, horizontal waterline and pointed submerged mass. Omitted small facets; replaced a too-regular initial diamond outline after native-size review.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '50dd61f6-aaaa-4da1-8448-39c1d86d1424'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/iceberg_50dd61f6-aaaa-4da1-8448-39c1d86d1424.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'iceberg-above-and-below-water'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('iceberg', 'above', 'and', 'below', 'water')

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

        path('ice',(4,24),[(16,8),(24,18),(34,10),(44,24),(28,40),(4,24)],True)
        self.add_line('water',(4,24),(44,24));self.relate('connect','ice','water')

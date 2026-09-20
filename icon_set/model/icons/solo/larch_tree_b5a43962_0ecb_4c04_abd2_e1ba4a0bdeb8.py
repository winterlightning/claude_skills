'Evergreen Pine Tree.\nPlan and review: Retained conifer silhouette, straight trunk and ground line. Reduced three branch tiers to two to eliminate tight notches.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide tree-pine: mirrored tiered silhouette and central trunk.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b5a43962-0ecb-4c04-abd2-e1ba4a0bdeb8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/larch_b5a43962-0ecb-4c04-abd2-e1ba4a0bdeb8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'larch-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('larch', 'tree')

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

        path('tree',(24,4),[(34,18),(29,18),(40,36),(24,36),(8,36),(19,18),(14,18),(24,4)],True)
        self.add_line('trunk',(24,36),(24,44));self.add_polyline('ground',(16,44),(24,44),(32,44));self.relate('connect','tree','trunk');self.relate('connect','ground','trunk')

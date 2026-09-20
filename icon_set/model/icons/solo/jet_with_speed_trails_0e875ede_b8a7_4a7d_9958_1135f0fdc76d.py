'Flying Jet Airplane.\nPlan and review: Retained diagonal jet with swept wings and tail. Omitted the small speed streaks; widened wing and tail openings. Directional asymmetry follows the source.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide plane: coherent diagonal swept-wing silhouette.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e875ede-b8a7-4a7d-9958-1135f0fdc76d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/jet_0e875ede-b8a7-4a7d-9958-1135f0fdc76d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'jet-with-speed-trails'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('jet', 'with', 'speed', 'trails')

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

        path('jet',(6,16),[(10,10),(26,14),(36,6),((42,12),6,6,True),(35,28),(40,38),(32,42),(24,30),(18,36),(16,42),(10,38),(6,32),(12,30),(18,24),(6,16)],True)

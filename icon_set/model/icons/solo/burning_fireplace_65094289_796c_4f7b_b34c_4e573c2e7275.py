'Fireplace with Burning Flame.\nPlan and review: Retained rectangular fireplace surround, hearth and asymmetric flame. Omitted inner flame and doubled mantel/hearth bands.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Source silhouette; no useful local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '65094289-796c-4f7b-b34c-4e573c2e7275'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/inglenook_65094289-796c-4f7b-b34c-4e573c2e7275.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'burning-fireplace'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('burning', 'fireplace')

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

        path('surround',(6,42),[(6,6),(42,6),(42,42)])
        self.add_polyline('hearth',(6,42),(24,42),(42,42));self.relate('connect','surround','hearth')
        curve('flame',(24,42),((10,38),(22,26),(24,18)),((34,26),(38,38),(24,42)))
        self.relate('connect','flame','hearth')

'Foggy Cloud Weather Icon.\nPlan and review: Retained rounded open cloud outline and two horizontal fog strokes, lower shorter. Rebuilt the lobe extrema and increased vertical clearance.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide cloud-fog: open cloud contour with two horizontal fog strokes.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ea1561a-0ad1-4359-8da5-b2d62f6fc199'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather cloud wind 1_3ea1561a-0ad1-4359-8da5-b2d62f6fc199.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'foggy-cloud'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('foggy', 'cloud')

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

        curve('cloud',(12,23),((2,23),(2,12),(12,12)),((12,8),(16,8),(20,8)),((27,8),(30,12),(30,16)),((40,12),(44,18),(44,23)))
        self.add_line('fog-upper',(4,32),(36,32));self.add_line('fog-lower',(10,40),(26,40))

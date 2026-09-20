'Cloud and Fog Weather.\nPlan and review: Retained cloud and two fog strokes, shorter lower line; rebalanced vertical spacing.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cloud: rounded lobes; wind: separate horizontal runs.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'def8556d-9454-4886-97b3-c3d444ead259'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_40/weather cloud wind 3_def8556d-9454-4886-97b3-c3d444ead259.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-and-fog-weather'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cloud', 'and', 'fog', 'weather')

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

        curve('cloud-top',(12,24),((7,24),(4,21),(4,17)),((4,12),(9,10),(14,12)),((16,8),(20,8),(24,8)),((30,8),(34,10),(34,14)),((40,12),(44,16),(44,20)),((44,22),(42,24),(40,24)))
        self.add_line('cloud-base',(40,24),(12,24));self.add_contour('cloud','cloud-top','cloud-base',closed=True)
        self.add_line('fog-upper',(4,32),(44,32));self.add_line('fog-lower',(14,40),(34,40))

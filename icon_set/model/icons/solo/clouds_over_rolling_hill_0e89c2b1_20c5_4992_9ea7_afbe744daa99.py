'Clouds over Rolling Hill.\nPlan and review: Retained all three clouds and the hill. Upper clouds use simplified lobes; smallest cloud becomes a dome; hill is shallower for clearance.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide cloud: simplified domed cloud contours; source three-cloud arrangement retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e89c2b1-20c5-4992-9ea7-afbe744daa99'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_39/veldt_0e89c2b1-20c5-4992-9ea7-afbe744daa99.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clouds-over-rolling-hill'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('clouds', 'over', 'rolling', 'hill')

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

        curve('cloud-large-top',(4,16),((4,14),(6,12),(8,12)),((8,10),(10,8),(12,8)),((14,8),(16,10),(16,12)),((18,12),(20,14),(20,16)))
        self.add_line('cloud-large-base',(20,16),(4,16));self.add_contour('cloud-large','cloud-large-top','cloud-large-base',closed=True)
        curve('cloud-right-top',(30,16),((30,14),(31,12),(33,12)),((33,10),(35,8),(37,8)),((39,8),(41,10),(41,12)),((43,12),(44,14),(44,16)))
        self.add_line('cloud-right-base',(44,16),(30,16));self.add_contour('cloud-right','cloud-right-top','cloud-right-base',closed=True)
        path('cloud-small',(19,30),[((31,30),6,6,True),(19,30)],True)
        curve('hill',(4,40),((18,38),(28,38),(44,40)))

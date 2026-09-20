'Deployed Vehicle Airbag.\nPlan and review: Retained inflated airbag and partly occluded steering wheel. Spoke attaches at exact circle nodes (33,30) and (40,38); preserved the natural overlap as a visible occlusion.\nKeyshape: SQUARE, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '895a3dac-de4f-448f-9d6f-3902541a35c6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/airbag_895a3dac-de4f-448f-9d6f-3902541a35c6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'deployed-vehicle-airbag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('deployed', 'vehicle', 'airbag')

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

        path('airbag',(6,21),[((21,6),15,15,True),((36,21),15,15,True),((33,30),15,15,True),((21,36),15,15,True),((6,21),15,15,True)],True)
        path('wheel',(36,21),[((42,32),6,11,True),((40,38),10,10,True),((32,42),10,10,True),((21,36),11,6,True)])
        self.relate('connect','airbag','wheel')
        self.add_line('spoke',(33,30),(40,38));self.relate('connect','spoke','wheel');self.relate('connect','spoke','airbag')

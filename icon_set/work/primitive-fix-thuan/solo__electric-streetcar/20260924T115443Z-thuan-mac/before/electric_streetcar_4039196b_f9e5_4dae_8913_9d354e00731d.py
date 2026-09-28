'Electric Streetcar Tram.\nPlan and review: Retained overhead contact arm, rounded side-view tram, glazing band and two wheels. Replaced the two small windows with one broad shared band.\nKeyshape: HRECT_L, exact SOLO48 envelope selected for this silhouette.\nConstruction reference: Lucide train-front: rounded body, broad glazing and two wheel cues; source side view.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4039196b-f9e5-4dae-8913-9d354e00731d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_38/trolley_4039196b-f9e5-4dae-8913-9d354e00731d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'electric-streetcar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('electric', 'streetcar')

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

        path('body',(10,32),[(4,32),(4,18),((8,14),4,4,True),(40,14),((44,18),4,4,True),(44,32),(38,32)])
        circle('wheel-left',14,36,4);circle('wheel-right',34,36,4)
        self.add_line('sill',(19,32),(29,32))
        for w in ('wheel-left','wheel-right'):self.relate('connect','body',w);self.relate('connect','sill',w)
        self.add_line('window-band',(4,23),(44,23));self.relate('connect','body','window-band')
        self.add_line('pantograph',(24,14),(34,8));self.relate('connect','body','pantograph')

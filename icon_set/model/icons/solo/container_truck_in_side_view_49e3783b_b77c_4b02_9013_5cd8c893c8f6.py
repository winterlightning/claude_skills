"""container-truck-in-side-view.
Plan: Rounded closed cargo box, separated rib series, coherent cab, two equal wheels on a shared axle.
Keyshape: HRECT_L, exact SOLO48 inset envelope.
Reference construction: Lucide truck: rounded cargo corners and circular wheels.
Omissions: Two of four cargo ribs; small cab window.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '49e3783b-b77c-4b02-9013-5cd8c893c8f6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_34/shipping logistic free shipping delivery container_49e3783b-b77c-4b02-9013-5cd8c893c8f6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'container-truck-in-side-view'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('shipping', 'logistic', 'free', 'shipping', 'delivery', 'container')

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

        box('cargo',4,8,28,24,2)
        for x in (12,20):
            self.add_line(f'rib-{x}',(x,8),(x,16));self.relate('connect',f'rib-{x}','cargo')
        path('cab',(28,16),[(35,16),(44,27),(44,36),(40,36)])
        self.relate('connect','cab','cargo')
        circle('rear',12,36,4);circle('front',36,36,4)
        self.add_line('axle',(16,36),(32,36));self.relate('connect','axle','rear');self.relate('connect','axle','front');self.relate('connect','cab','front')

        path('rear-chassis',(4,22),[(4,36),(8,36)])
        self.relate('connect','rear-chassis','cargo');self.relate('connect','rear-chassis','rear')

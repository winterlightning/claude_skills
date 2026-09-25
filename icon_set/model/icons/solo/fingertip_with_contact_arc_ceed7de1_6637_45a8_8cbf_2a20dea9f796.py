'Single Finger Tap Gesture.\nPlan and review: Retained complete upright fingertip and surrounding open contact arc with both long legs.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Human reference rounded hand vocabulary; Lucide hand rounded finger ends. Source contact arc retained.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ceed7de1-6637-45a8-8cbf-2a20dea9f796'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/gesture tap_ceed7de1-6637-45a8-8cbf-2a20dea9f796.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'fingertip-with-contact-arc'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('fingertip', 'with', 'contact', 'arc')

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

        path('finger',(18,44),[(18,24),((30,24),6,6,True),(30,44)])
        path('contact',(8,34),[(8,20),((40,20),16,16,True),(40,34)])

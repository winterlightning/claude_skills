'Closed Security Padlock.\nPlan and review: Retained blank rounded lock body and closed arched shackle.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: Lucide lock: U-shaped shackle and rounded body.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58d29d8e-4e2e-4825-b7c1-1cf9a0df7833'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/keep_58d29d8e-4e2e-4825-b7c1-1cf9a0df7833.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-security-padlock'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('closed', 'security', 'padlock')

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

        path('body',(16,24),[(32,24),(36,24),((40,28),4,4,True),(40,40),((36,44),4,4,True),(12,44),((8,40),4,4,True),(8,28),((12,24),4,4,True),(16,24)],True)
        path('shackle',(16,24),[(16,12),((32,12),8,8,True),(32,24)])
        self.relate('connect','body','shackle')

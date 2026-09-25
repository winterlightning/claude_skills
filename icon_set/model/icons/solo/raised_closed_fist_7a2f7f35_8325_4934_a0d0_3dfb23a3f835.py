'Raised Clenched Fist.\nPlan and review: Retained four rounded knuckles, crossing thumb and wrist. Omitted the finger crease hidden behind the thumb.\nKeyshape: VRECT_L, exact SOLO48 envelope.\nConstruction reference: Lucide hand-fist: rounded knuckles and crossing thumb; human_ref hand vocabulary.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a2f7f35-8325-4934-a0d0-3dfb23a3f835'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_21/grip_7a2f7f35-8325-4934-a0d0-3dfb23a3f835.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'raised-closed-fist'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('raised', 'closed', 'fist')

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

        path('fist',(12,44),[(12,36),((8,24),4,12,True),(8,12),((16,12),4,4,True),(16,8),((24,8),4,4,True),((32,8),4,4,True),((40,8),4,4,True),(40,24),((36,36),4,12,True),(36,44),(12,44)],True)
        path('thumb',(40,20),[(28,20),((28,28),4,4,False),(32,28)])
        self.relate('connect','thumb','fist');self.relate('connect','thumb','finger-1')
        for j,x in enumerate((16,32)):self.add_line(f'finger-{j}',(x,12),(x,20));self.relate('connect',f'finger-{j}','fist')

'Cupcake With Creamy Frosting Swirl.\nPlan and review: Retained tapered wrapper, rim and curled frosting peak. Reduced three frosting tiers to one coherent curl and base.\nKeyshape: VRECT_L, exact SOLO48 envelope selected for this subject.\nConstruction reference: No useful Lucide subject match; source render guides construction.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '910ac0b1-76b7-40fa-93a3-5477bd94b248'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_20/frosting_910ac0b1-76b7-40fa-93a3-5477bd94b248.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cupcake-with-creamy-frosting-swirl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cupcake', 'with', 'creamy', 'frosting', 'swirl')

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

        path('wrapper',(8,30),[(12,40),((16,44),4,4,False),(32,44),((36,40),4,4,False),(40,30)])
        curve('frosting',(8,30),((8,18),(26,22),(26,12)),((26,8),(28,8),(28,4)),((36,8),(40,12),(40,18)),((40,18),(36,18),(32,18)))
        self.add_line('right-edge',(40,18),(40,30));self.add_line('rim',(8,30),(40,30))
        self.relate('connect','wrapper','rim');self.relate('connect','frosting','rim');self.relate('connect','right-edge','rim');self.relate('connect','frosting','right-edge')

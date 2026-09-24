"""dripping-wax-pot.
Plan: Wax pot with a rounded lip and two smoothly rounded drips; long central drip and shorter left drip retain the reference hierarchy.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'd17ea3f7-3c72-47c7-a0c5-d88e0cf7a4aa'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dripping-wax-pot/20260924T105711Z-thuan-mac/reference/wax_d17ea3f7-3c72-47c7-a0c5-d88e0cf7a4aa.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'dripping-wax-pot'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('wax',)

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

        path('wax',(6,14),[((14,6),8,8,True),(34,6),((42,14),8,8,True),((38,18),4,4,True),(30,18),(30,30),((22,30),4,4,True),(22,18),(14,18),(14,24),((6,24),4,4,True),(6,14)],True)
        path('pot',(6,24),[(6,34),((14,42),8,8,False),(34,42),((42,34),8,8,False),(42,14)])
        self.relate('connect','pot','wax')

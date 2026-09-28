"""cupcake-with-creamy-frosting-swirl.
Plan: Two flowing frosting tiers above a tapered paper cup; smooth shared swirl junction and balanced base.
Keyshape: VRECT_L, exact SOLO48 inset envelope.
Reference construction: Lucide cake: coherent rounded outline with a separate icing division.
Omissions: Fine paper ridges.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '910ac0b1-76b7-40fa-93a3-5477bd94b248'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cupcake-with-creamy-frosting-swirl/20260924T105711Z-thuan-mac/reference/frosting_910ac0b1-76b7-40fa-93a3-5477bd94b248.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cupcake-with-creamy-frosting-swirl'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('frosting',)

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

        curve('frosting',(8,32),((8,23),(11,22),(16,20)),((24,17),(25,11),(24,4)),((30,7),(37,12),(34,20)),((40,23),(40,26),(40,32)))
        self.add_line('rim',(8,32),(40,32));self.relate('connect','rim','frosting')
        curve('swirl',(34,20),((33,23),(29,24),(24,24)));self.relate('connect','swirl','frosting')
        curve('cup',(8,32),((10,38),(10,44),(16,44)),((20,44),(28,44),(32,44)),((38,44),(38,38),(40,32)))
        self.relate('connect','cup','rim');self.relate('connect','cup','frosting')

"""cylindrical-marshmallow-on-slanted-stick.
Plan: Diagonal cylinder with a smooth elliptical top rim, rounded lower end and stick attached to the lower silhouette.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '51eb3863-a02f-4624-ba65-ff48208cd5b7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cylindrical-marshmallow-on-slanted-stick/20260924T105711Z-thuan-mac/reference/marshmallow_51eb3863-a02f-4624-ba65-ff48208cd5b7.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'cylindrical-marshmallow-on-slanted-stick'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('marshmallow',)

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

        curve('top',(22,6),((30,6),(42,16),(42,22)),((42,26),(40,28),(36,28)),((28,28),(16,18),(16,12)),((16,8),(18,6),(22,6)))
        curve('body',(16,12),((12,18),(8,24),(8,28)),((8,32),(10,34),(14,36)),((18,38),(22,40),(26,36)),((30,32),(32,30),(36,28)))
        self.relate('connect','top','body')
        self.add_line('stick',(14,36),(6,42));self.relate('connect','stick','body')

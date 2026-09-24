"""curved-larva.
Plan: Curled segmented larva with a broad round head, smooth concave back and convex underside. Two bands share exact outline nodes.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: Lucide worm: smooth inner and outer body contours.
Omissions: Two smallest tail segmentation bands.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '26443253-e3d6-433d-8f28-747729ca34c3'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__curved-larva/20260924T105711Z-thuan-mac/reference/larva_26443253-e3d6-433d-8f28-747729ca34c3.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'curved-larva'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('larva',)

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

        curve('outline',(6,34),((6,29),(9,28),(14,26)),((20,24),(24,21),(24,16)),((24,10),(26,6),(32,6)),((38,6),(42,10),(42,16)),((42,23),(39,29),(34,34)),((28,39),(20,42),(14,42)),((8,42),(6,39),(6,34)))
        curve('head-band',(24,16),((28,19),(36,19),(42,16)))
        curve('body-band',(14,26),((18,32),(25,35),(34,34)))
        for n in ('head-band','body-band'):self.relate('connect',n,'outline')

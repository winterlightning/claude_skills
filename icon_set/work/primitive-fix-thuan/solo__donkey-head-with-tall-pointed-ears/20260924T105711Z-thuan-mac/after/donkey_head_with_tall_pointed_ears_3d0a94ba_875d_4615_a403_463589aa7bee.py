"""donkey-head-with-tall-pointed-ears.
Plan: Donkey profile with two tall leaf-like ears, elongated rounded muzzle and open neck strokes. Ear endpoints share actual head nodes.
Keyshape: SQUARE, exact SOLO48 inset envelope.
Reference construction: No useful Lucide subject match.
Omissions: Small muzzle separation line omitted.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3d0a94ba-875d-4615-a403-463589aa7bee'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__donkey-head-with-tall-pointed-ears/20260924T105711Z-thuan-mac/reference/donkey_3d0a94ba-875d-4615-a403-463589aa7bee.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'donkey-head-with-tall-pointed-ears'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('donkey',)

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

        curve('face',(6,34),((6,32),(8,30),(10,28)),((12,25),(15,22),(18,20)),((20,19),(22,18),(24,18)),((27,18),(31,19),(34,20)),((37,24),(40,29),(42,32)))
        curve('muzzle',(6,34),((6,39),(9,42),(14,42)),((16,42),(17,41),(18,40)),((20,38),(22,37),(24,36)),((29,35),(32,34),(32,28)))
        self.relate('connect','face','muzzle')
        curve('ear-left',(18,20),((12,18),(12,10),(12,6)),((20,8),(24,12),(24,18)))
        curve('ear-right',(24,18),((24,12),(29,7),(34,6)),((36,12),(35,17),(34,20)))
        for n in ('ear-left','ear-right'):self.relate('connect',n,'face')
        self.relate('connect','ear-left','ear-right')
        self.add_line('neck',(24,36),(32,42));self.relate('connect','neck','muzzle')

        curve('muzzle-divider',(10,28),((16,30),(18,35),(18,40)))
        self.relate('connect','muzzle-divider','face');self.relate('connect','muzzle-divider','muzzle')

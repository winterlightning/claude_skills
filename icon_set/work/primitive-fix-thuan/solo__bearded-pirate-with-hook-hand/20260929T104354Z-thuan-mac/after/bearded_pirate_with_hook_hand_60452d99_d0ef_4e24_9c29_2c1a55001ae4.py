'Reversed the hook into a lower J-shaped curl and opened the hat brim, keeping the pointed beard and pirate hat.\nOriginal/current comparison: The rejected hook points downward from an inverted arch, whereas the original has an upright shaft and a lower curled hook; the hat brim is pinched.\nPlan: SQUARE, bounds (4, 4, 44, 44); shared circles, mirrored pairs and explicit joined nodes.\nReference: human_ref/user.svg for circular face; original supplies hat, beard and asymmetric hook.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '60452d99-d0ef-4e24-9c29-2c1a55001ae4'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bearded-pirate-with-hook-hand/20260929T104354Z-thuan-mac/reference/pirate_60452d99-d0ef-4e24-9c29-2c1a55001ae4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-pirate-with-hook-hand'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('bearded', 'pirate', 'with', 'hook', 'hand')
    human_construction = 'bust'

    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def bez(n,a,*segments): self.add_bezier(n,a,*segments)
        def poly(n,*points,closed=False): self.add_polyline(n,*points,closed=closed)
        def con(n,*members,closed=False): self.add_contour(n,*members,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j,(a,b) in enumerate(zip(pts,pts[1:])):arc(n+str(j),a,b,r)
            con(n,*(n+str(j) for j in range(4)),closed=True)
        def path(n,start,steps,closed=False):
            here=start; members=[]
            for i,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{i}';members.append(m)
                if kind=='L': line(m,here,end)
                elif kind=='A': arc(m,here,end,*args)
                elif kind=='C': bez(m,here,(args[0],args[1],end))
                here=end
            con(n,*members,closed=closed)
        def rect(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad),('L',(r,b-rad)),('A',(r-rad,b),rad),('L',(l+rad,b)),('A',(l,b-rad),rad),('L',(l,t+rad)),('A',(l+rad,t),rad)],True)

        bez('hat',(6,18),((6,14),(9,12),(12,12)),((12,8),(14,6),(18,6)),((22,6),(24,8),(24,12)),((27,12),(30,14),(30,18)))
        poly('brim',(30,18),(26,20),(10,20),(6,18));join('hat','brim')
        arc('face',(26,20),(10,20),8);join('face','brim')
        path('beard',(10,20),[('L',(10,32)),('C',(18,42),(10,37),(14,40)),('C',(26,32),(22,40),(26,37)),('L',(26,20))]);join('beard','face');join('beard','brim')
        line('hook-shaft',(34,28),(34,36))
        arc('hook-curl',(34,36),(42,36),4,s=False);join('hook-shaft','hook-curl')
        line('hook-tip',(42,36),(42,32));join('hook-curl','hook-tip')

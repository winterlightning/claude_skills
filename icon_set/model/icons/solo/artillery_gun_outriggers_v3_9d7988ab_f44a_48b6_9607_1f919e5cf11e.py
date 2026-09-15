"""A long elevated gun tube terminates in a separate muzzle block. The central wheel and two outward legs make the wheeled artillery silhouette explicit.
Reference: Supplied elevated artillery reference; same round wheel and minimal structural strokes
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9d7988ab-f44a-48b6-9607-1f919e5cf11e'
SOURCE_PATH = 'pictographic-primitives/war/tank machine gun_9d7988ab-f44a-48b6-9607-1f919e5cf11e.svg'
AUTHOR = 'gpt-6'

class ArtilleryGunOutriggersVariant3(Solo48):
    icon_id = 'artillery-gun-outriggers-v3'
    variant_of = 'artillery-gun-outriggers-v2'
    variant_label = 'Revised after specific drawing feedback, 16 September'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    aliases = ()
    keywords = ('artillery', 'gun', 'outriggers')

    def build(self):
        # Symbol plan: A long elevated gun tube terminates in a separate muzzle block. The central wheel and two outward legs make the wheeled artillery silhouette explicit.

        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        circle('wheel',18,36,8)
        line('barrel',(18,28),(30,14));join('wheel','barrel')
        poly('muzzle',(26,10),(32,4),(40,12),(34,18),closed=True);join('barrel','muzzle')
        line('left-outrigger',(10,36),(8,44));line('right-outrigger',(26,36),(40,44));join('wheel','left-outrigger');join('wheel','right-outrigger')

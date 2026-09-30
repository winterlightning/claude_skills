"""The rejected pirate had a straight brim and no smile. Restore a curved straw-hat brim, rounded crown, a wink and a small smiling mouth.
Symbol plan: Original straw hat and wink; curved brim and balanced circular-looking jaw. Smile added in a later spacing pass if room permits.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '89ee4b36-d26f-440c-9a51-5ee98f5d876c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__winking-straw-hat-pirate/20260929T124732Z-thuan-mac/reference/pirate luffy onepiece_89ee4b36-d26f-440c-9a51-5ee98f5d876c.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'winking-straw-hat-pirate'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('winking', 'straw', 'hat', 'pirate')

    def build(self):

        def path(n,start,steps,closed=False):
            point=start; members=[]
            for j,(kind,end,*args) in enumerate(steps):
                m=f'{n}-{j}'
                if kind=='L': self.add_line(m,point,end)
                elif kind=='A': self.add_arc(m,point,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,point,(args[0],args[1],end))
                point=end; members.append(m)
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

        path('crown',(10,18),[('A',(24,8),14,10,True),('A',(38,18),14,10,True)])
        path('brim',(4,18),[('C',(24,22),(8,22),(16,22)),('C',(44,18),(32,22),(40,22))]);join('crown','brim')
        path('jaw',(8,21),[('C',(24,40),(8,32),(14,40)),('C',(40,21),(34,40),(40,32))]);join('jaw','brim')
        self.add_dot('eye',(18,30));line('wink',(29,30),(32,29))

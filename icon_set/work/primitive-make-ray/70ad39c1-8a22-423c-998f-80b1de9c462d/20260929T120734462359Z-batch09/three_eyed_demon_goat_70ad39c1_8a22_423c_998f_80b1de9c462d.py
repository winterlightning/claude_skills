"""Goat: rejected horns are short hooks, face is broad and the third eye a dot. Restore curling horns, tapered muzzle and a distinct third eye. Restore long curved horns and taper the brow and muzzle around three separated eyes.
Symbol plan: No useful exact Lucide match; original reference and geometric curves.
Keyshape HRECT_L: exact SOLO48 envelope. Intentional directional asymmetry follows original.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '70ad39c1-8a22-423c-998f-80b1de9c462d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-eyed-demon-goat/20260929T115456Z-thuan-mac/reference/demon hunter goat head eye_70ad39c1-8a22-423c-998f-80b1de9c462d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'three-eyed-demon-goat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('three', 'eyed', 'demon', 'goat')

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

        path('head',(16,12),[('C',(24,8),(18,8),(21,8)),('C',(32,12),(27,8),(30,8)),('C',(37,22),(34,16),(37,19)),('L',(37,28)),('C',(31,35),(37,32),(31,32)),('A',(17,35),7,5,True),('C',(11,28),(17,32),(11,32)),('L',(11,22)),('C',(16,12),(11,19),(14,16))],True)
        for side in [-1,1]:
         p=lambda x,y:(24+side*x,y)
         path(f'horn-{side}',p(8,12),[('C',p(20,14),p(15,6),p(20,8)),('L',p(20,18))]);join('head',f'horn-{side}')
        self.add_dot('third-eye',(24,17));self.add_dot('eye-l',(20,26));self.add_dot('eye-r',(28,26))

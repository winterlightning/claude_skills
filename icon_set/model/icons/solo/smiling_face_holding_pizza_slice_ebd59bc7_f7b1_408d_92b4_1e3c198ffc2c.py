"""Happy face holding a pizza slice, with round facial contour and matching curved eyes.
Plan: Happy face holding a pizza slice, with round facial contour and matching curved eyes.
Construction: Lucide heart circular lobe vocabulary; source sets happy face and held pizza.
Omissions: Mouth and topping marks omitted in the occupied lower face; happy eyes retained."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'ebd59bc7-f7b1-408d-92b4-1e3c198ffc2c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_16/emoji food eating lover hug_ebd59bc7-f7b1-408d-92b4-1e3c198ffc2c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='smiling-face-holding-pizza-slice'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('smiling', 'face', 'holding', 'pizza', 'slice')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('face',(6,24),[('A',(24,6),18,18,True),('A',(42,24),18,18,True)])
        for i,x in enumerate((18,30)):
         path('eye-'+str(i),(x-2,19),[('C',(x+2,19),(x-2,17),(x+2,17))])
        path('pizza',(14,32),[('L',(33,28)),('L',(29,42)),('C',(14,32),(22,42),(18,37))],True)
        path('hand',(14,32),[('C',(6,36),(10,32),(6,32)),('C',(14,42),(6,40),(10,42)),('L',(20,42))]);join('hand','pizza')

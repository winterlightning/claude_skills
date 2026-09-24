"""Cupped hands have gently curved thumb and palm strokes around a paired-leaf sprout. Lucide hand-heart and sprout informed the construction; shared human reference full_body_ref.png informed rounded limb strokes. No head is present. Third tiny leaf omitted; leaf pair and hands mirror x=24."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bf61d88d-d269-4a85-955c-a411e11583cd'
SOURCE_PATH = 'pictographic-primitives/logos/treehouse logo_bf61d88d-d269-4a85-955c-a411e11583cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'treehouse-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'brands/logos'
    aliases = ()
    keywords = ('treehouse', 'logo')

    def build(self):
        # Plan: Cupped hands have gently curved thumb and palm strokes around a paired-leaf sprout. Lucide hand-heart and sprout informed the construction; shared human reference full_body_ref.png informed rounded limb strokes. No head is present. Third tiny leaf omitted; leaf pair and hands mirror x=24.
        def path(n, start, steps, closed=False):
            p=start; ids=[]
            for i,s in enumerate(steps):
                name=f'{n}-{i}'; kind,end,*args=s
                if kind=='L': self.add_line(name,p,end)
                elif kind=='A': self.add_arc(name,p,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(name,p,(args[0],args[1],end))
                ids.append(name); p=end
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        def join(a,b): self.relate('connect',a,b)
        for j in range(2):
            def p(x,y):return (x,y) if j==0 else (48-x,y)
            path(f'hand-{j}',p(6,24),[('L',p(6,30)),('L',p(6,34)),('C',p(8,42),p(6,38),p(8,38))])
            path(f'thumb-{j}',p(6,30),[('C',p(18,38),p(10,30),p(18,34)),('L',p(18,42))]);join(f'hand-{j}',f'thumb-{j}')
            path(f'leaf-{j}',p(10,6),[('A',p(24,20),14,14,j==0),('A',p(10,6),14,14,j==0)],True)
        line('stem',(24,20),(24,30));join('leaf-0','leaf-1')
        for j in range(2):join(f'leaf-{j}','stem')

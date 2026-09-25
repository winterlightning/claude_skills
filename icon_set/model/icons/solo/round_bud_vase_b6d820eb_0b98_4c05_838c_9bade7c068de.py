'round-bud-vase-v2: Rebalanced the three buds and deepened the vase. Keyshape VRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b6d820eb-0b98-4c05-838c-9bade7c068de'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/cherry blossom vase_b6d820eb-0b98-4c05-838c-9bade7c068de.svg'
AUTHOR = 'gpt-6'

class RoundBudVase(Solo48):
    icon_id = 'round-bud-vase'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'decoration'
    aliases = ()
    keywords = ('vase', 'buds', 'flowers', 'stems', 'bouquet', 'plant', 'decor')

    def build(self):
        # Removed the lower-right branch and rebalanced the vase width to retain the profile envelope.

        def path(n, start, commands, closed=False):
            names=[];here=start
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                names.append(ident);here=end
            self.add_contour(n,*names,closed=closed)
        def ellipse(n,x,y,rx,ry):
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        poly('mouth',(8,30),(24,30),(40,30))
        path('vase',(40,30),[('A',(24,44),16,14,True),('A',(8,30),16,14,True)]);join('mouth','vase')
        for name,x,y in [('left',11,15),('top',24,7)]:
         ellipse(name,x,y,3,3);line(name+'-stem',(x,y+3),(24,30));join(name,name+'-stem');join(name+'-stem','mouth')
        join('left-stem','top-stem')

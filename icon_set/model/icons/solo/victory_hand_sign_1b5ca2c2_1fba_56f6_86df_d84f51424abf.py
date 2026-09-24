"""Peace/victory hand with two rounded raised fingertips, a clear V opening and curved palm/knuckle outline. Lucide hand informed round fingertips; shared human full_body_ref.png supplied the rounded limb vocabulary. No head is present. Minor folded-finger creases omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1b5ca2c2-1fba-56f6-86df-d84f51424abf'
SOURCE_PATH = 'pictographic-primitives/wayfinding/two fingers_1b5ca2c2-1fba-56f6-86df-d84f51424abf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'victory-hand-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/wayfinding'
    aliases = ()
    keywords = ('victory', 'hand', 'sign')

    def build(self):
        # Plan: Peace/victory hand with two rounded raised fingertips, a clear V opening and curved palm/knuckle outline. Lucide hand informed round fingertips; shared human full_body_ref.png supplied the rounded limb vocabulary. No head is present. Minor folded-finger creases omitted.
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
        path('hand',(16,30),[('L',(6,10)),('A',(14,10),4,4,True),('L',(24,28)),('L',(34,10)),('A',(42,10),4,4,True),('L',(32,30)),('C',(36,36),(34,32),(36,33)),('A',(30,42),6,6,True),('L',(18,42)),('C',(8,32),(12,42),(8,37)),('L',(8,30)),('C',(16,30),(8,26),(12,28))],True)
        path('thumb',(16,30),[('L',(27,33)),('C',(28,36),(29,34),(29,35))]);join('thumb','hand')

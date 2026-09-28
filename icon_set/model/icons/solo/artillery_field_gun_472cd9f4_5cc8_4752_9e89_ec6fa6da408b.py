"""A long horizontal cannon barrel with a clear muzzle band sits on a visible mounting post, wheel and rear carriage. Omit small mechanical details.
Reference: Supplied field-gun silhouette; local Lucide circle construction for the wheel
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '472cd9f4-5cc8-4752-9e89-ec6fa6da408b'
SOURCE_PATH = 'pictographic-primitives/war/symbol artillery_472cd9f4-5cc8-4752-9e89-ec6fa6da408b.svg'
AUTHOR = 'gpt-6'

class ArtilleryFieldGun(Solo48):
    icon_id = 'artillery-field-gun'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'war'
    categories = ('war', 'primitives')
    aliases = ()
    keywords = ('artillery', 'field', 'gun')

    def build(self):
        # Symbol plan: A long horizontal cannon barrel with a clear muzzle band sits on a visible mounting post, wheel and rear carriage. Omit small mechanical details.

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
        path('barrel',(14,8),[('L',(44,8)),('L',(44,18)),('L',(14,18)),('A',(14,8),5,5,True)],True)
        line('muzzle-band',(36,8),(36,18));join('muzzle-band','barrel')
        circle('wheel',16,33,7)
        line('mount',(16,18),(16,26));join('mount','barrel');join('mount','wheel')
        line('left-leg',(9,33),(4,40));line('trail',(23,33),(44,40));join('wheel','left-leg');join('wheel','trail')

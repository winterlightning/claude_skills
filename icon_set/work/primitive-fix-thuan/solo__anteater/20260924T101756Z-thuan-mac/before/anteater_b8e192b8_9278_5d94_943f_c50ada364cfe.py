"""A long down-sloping snout leads into a low body, while a broad sweeping tail takes up the rear silhouette. Keep two near legs and one eye; omit the far legs and fur texture.
Reference: Naturalist Journeys giant anteater photograph: long snout, low body and large tail; no close Lucide animal match. https://www.naturalistjourneys.com/tours/2026/02/12/guyana-unspoiled-wilderness
Authored directly on SOLO48, with prior revision preserved."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b8e192b8-9278-5d94-943f-c50ada364cfe'
SOURCE_PATH = 'pictographic-primitives/animals/anteater_b8e192b8-9278-5d94-943f-c50ada364cfe.svg'
AUTHOR = 'gpt-6'

class Anteater(Solo48):
    icon_id = 'anteater'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('anteater',)

    def build(self):
        # Symbol plan: A long down-sloping snout leads into a low body, while a broad sweeping tail takes up the rear silhouette. Keep two near legs and one eye; omit the far legs and fur texture.

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
        path('animal',(4,24),[('L',(14,18)),('C',(18,12),(16,16),(16,12)),('L',(26,12)),('C',(32,20),(30,12),(32,16)),('C',(38,22),(34,18),(36,18)),('C',(42,32),(40,24),(42,28)),('C',(30,30),(38,34),(34,32)),('L',(18,30)),('L',(12,26)),('L',(4,24))],True)
        dot('eye',(22,21))
        line('front-leg',(18,30),(14,38));line('rear-leg',(28,30),(28,38));join('animal','front-leg');join('animal','rear-leg')

"""A five-pointed star outline leans slightly, with a curved shooting trail sweeping in from the lower left to its lower left point.

Symbol plan: Leaning five-point star with one curved lower-left shooting trail. Extremes (4,8)-(44,40).
Review notes: Retains the shooting-star outline and curved trail. Lucide star informs coherent joined points. Its lean and lower-left tail deliberately preserve the source direction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6ff8f7f-3ad0-4a2b-bc15-6241e3ec037a'
SOURCE_PATH = 'pictographic-primitives/logos/meta cafe logo_a6ff8f7f-3ad0-4a2b-bc15-6241e3ec037a.svg'
AUTHOR = 'gpt-6'

class MetacafeLogo(Solo48):
    icon_id = 'metacafe-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    categories = ("logos", "primitives")
    aliases = ()
    keywords = ('metacafe', 'video', 'shooting-star', 'logo', 'brand', 'entertainment', 'star')

    def build(self):

        def chain(name, *points):
            for i,(start,end) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{i}',start,end)
        def ring(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)
        def rounded(name, left, top, right, bottom, r):
            points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for i,start in enumerate(points):
                end=points[(i+1)%8]; ident=f'{name}-{i}'
                if start==end: continue
                if i%2:self.add_arc(ident,start,end,radius_x=r)
                else:self.add_line(ident,start,end)
                members.append(ident)
            self.add_contour(name,*members,closed=True)
        self.add_polyline('star',(30,8),(34,20),(44,20),(36,27),(39,40),(28,32),(18,40),(19,26),(8,18),(24,18),closed=True)
        self.add_bezier('trail',(4,40),((4,36),(10,30),(19,26)))
        self.relate('connect','trail','star-7');self.relate('connect','trail','star-8')

"""A tall capital N built from two vertical bars and a diagonal ribbon that crosses from the top left to the bottom right, drawn as outlines.

Symbol plan: Tall folded N ribbon with broad vertical strips; extremes (8,4)-(40,44).
Review notes: Retains the tall outlined N with broad vertical strips; removes redundant overlapping seam strokes so the diagonal ribbon has open space. No useful local Lucide brand match; diagonal direction remains unchanged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e4ec3d36-beab-461c-8e7e-d49d1ebd98b1'
SOURCE_PATH = 'pictographic-primitives/logos/netflix logo_e4ec3d36-beab-461c-8e7e-d49d1ebd98b1.svg'
AUTHOR = 'gpt-6'

class NetflixLogo(Solo48):
    icon_id = 'netflix-logo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('netflix', 'streaming', 'letter-n', 'movies', 'logo', 'brand', 'tv')

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
        self.add_polyline('outline',(8,44),(8,4),(18,4),(30,26),(30,4),(40,4),(40,44),(30,44),(18,22),(18,44),closed=True)

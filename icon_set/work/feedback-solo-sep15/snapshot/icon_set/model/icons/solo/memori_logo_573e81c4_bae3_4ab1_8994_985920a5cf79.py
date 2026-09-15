"""A five-pointed star with softly rounded points sits at the centre of a large circle.

Symbol plan: Radius20 circle enclosing a five-point star mirrored about x24. Radial maximum20.
Review notes: Lucide star informs the five alternating points and valleys; circle informs the enclosure. All five points remain; round joins soften them without extra tiny arcs.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '573e81c4-bae3-4ab1-8994-985920a5cf79'
SOURCE_PATH = 'pictographic-primitives/logos/memori logo_573e81c4-bae3-4ab1-8994-985920a5cf79.svg'
AUTHOR = 'gpt-6'

class MemoriLogo(Solo48):
    icon_id = 'memori-logo'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('memori', 'star', 'circle', 'logo', 'brand', 'favorites', 'memories')

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
        ring('frame',24,24,20)
        self.add_polyline('star',(24,13),(27,20),(35,21),(29,26),(31,33),(24,29),(17,33),(19,26),(13,21),(21,20),closed=True)

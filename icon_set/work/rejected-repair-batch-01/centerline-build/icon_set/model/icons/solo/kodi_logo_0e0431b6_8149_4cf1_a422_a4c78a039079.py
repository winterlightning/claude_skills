"""Four separate shapes arranged like a diamond: a tall slanted quadrilateral at the top, small diamonds at the right and bottom, and a small triangle at the left.

Symbol plan: Four detached angular shapes arranged in a diamond. Common axis x=24; extremes (6,6)-(42,42).
Review notes: Preserves all four pieces and deliberate unequal shapes. No useful local Lucide logo match. Native-size holes and separation require review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0e0431b6-8149-4cf1-a422-a4c78a039079'
SOURCE_PATH = 'pictographic-primitives/logos/kodi logo_0e0431b6-8149-4cf1-a422-a4c78a039079.svg'
AUTHOR = 'gpt-6'

class KodiLogo(Solo48):
    icon_id = 'kodi-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "brands/logos"
    aliases = ()
    keywords = ('kodi', 'media-center', 'player', 'logo', 'brand', 'open-source', 'tv')

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
        self.add_polyline('upper',(18,23),(18,12),(24,6),(30,12),closed=True)
        self.add_polyline('right',(30,24),(36,18),(42,24),(36,30),closed=True)
        self.add_polyline('bottom',(18,36),(24,30),(30,36),(24,42),closed=True)
        self.add_polyline('left',(10,20),(6,24),(10,28))

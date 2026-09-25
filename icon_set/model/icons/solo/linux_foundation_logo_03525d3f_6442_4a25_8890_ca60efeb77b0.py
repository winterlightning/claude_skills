"""A square frame broken at the top left and bottom right holds a smaller L-shaped bracket inside, the gaps offset like interlocking corners.

Symbol plan: Two interlocking open-corner brackets, derived from common outer and inner rails. Extremes (6,6)-(42,42).
Review notes: Keeps both offset bracket outlines; angular geometry is intrinsic, so Lucide square contributes only enclosure planning, not rounding.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '03525d3f-6442-4a25-8890-ca60efeb77b0'
SOURCE_PATH = 'pictographic-primitives/logos/linux foundation logo_03525d3f-6442-4a25-8890-ca60efeb77b0.svg'
AUTHOR = 'gpt-6'

class LinuxFoundationLogo(Solo48):
    icon_id = 'linux-foundation-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('linux-foundation', 'linux', 'open-source', 'square', 'logo', 'brand', 'foundation')

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
        self.add_polyline('upper-right',(6,16),(6,6),(42,6),(42,42),(32,42),(32,16),(6,16))
        self.add_polyline('lower-left',(6,26),(16,26),(16,32),(24,32),(24,42),(6,42),closed=True)

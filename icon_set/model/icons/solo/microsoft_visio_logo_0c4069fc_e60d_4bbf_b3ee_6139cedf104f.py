"""A rounded square with a capital V overlaps the left side of a diagram group: a tilted diamond at the top, a rectangle at the right and a circle beneath.

Symbol plan: V beside a diamond, rectangle and circle; extremes (4,8)-(44,40).
Review notes: Drops the V tile border and separates the three diagram shapes. The lower circle becomes small to preserve space beside the rectangle. Lucide circle/square construction informs the shapes; the three-shape group remains recognizable.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c4069fc-e60d-4bbf-b3ee-6139cedf104f'
SOURCE_PATH = 'pictographic-primitives/logos/microsoft visio logo_0c4069fc-e60d-4bbf-b3ee-6139cedf104f.svg'
AUTHOR = 'gpt-6'

class MicrosoftVisioLogo(Solo48):
    icon_id = 'microsoft-visio-logo'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "logos"
    aliases = ()
    keywords = ('visio', 'microsoft', 'diagram', 'office', 'logo', 'brand', 'letter-v')

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
        self.add_polyline('v',(4,16),(10,32),(16,16))
        self.add_polyline('diamond',(30,8),(36,14),(30,20),(24,14),closed=True)
        self.add_polyline('rectangle',(36,28),(44,28),(44,36),(36,36),closed=True)
        ring('circle',26,38,2)

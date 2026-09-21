"""American Football Ball.

Plan: Broad diagonal football with two end bands and two transverse laces; explicit band attachment nodes. Square extrema 6,6–42,42.
Construction reference: circle (local original and atomic-debug inspected).
Simplification: Four source laces reduced to two; end bands retained and openings enlarged.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a9f0b51b-1232-4e6f-922b-648cbe4c0f54'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_03/american football ball 1_a9f0b51b-1232-4e6f-922b-648cbe4c0f54.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'diagonal-american-football'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/sports'
    aliases = ()
    keywords = ('american', 'football', 'ball')

    def build(self):
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, left, top, right, bottom, r=2):
            pts=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
            members=[]
            for j,a in enumerate(pts):
                b=pts[(j+1)%8]; eid=f'{name}-{j}'; members.append(eid)
                if j%2: self.add_arc(eid,a,b,radius_x=r)
                else: self.add_line(eid,a,b)
            self.add_contour(name,*members,closed=True)

        # Each end-band meets two explicit outline nodes. The tips have enough
        # depth for a visible opening; two central laces remain 8+ units apart.
        self.add_line('side-low',(6,32),(7,27))
        self.add_arc('outline-upper',(7,27),(27,7),radius_x=26)
        self.add_line('side-high',(27,7),(32,6))
        self.add_arc('cap-upper',(32,6),(42,16),radius_x=10)
        self.add_line('side-right',(42,16),(41,21))
        self.add_arc('outline-lower',(41,21),(21,41),radius_x=26)
        self.add_line('side-bottom',(21,41),(16,42))
        self.add_arc('cap-lower',(16,42),(6,32),radius_x=10)
        self.add_contour('outline','side-low','outline-upper','side-high','cap-upper','side-right','outline-lower','side-bottom','cap-lower',closed=True)
        self.add_line('seam',(20,28),(28,20))
        for j,c in enumerate((20,28)):
            self.add_polyline(f'lace-{j}',(c-2,48-c-2),(c,48-c),(c+2,48-c+2))
            self.relate('connect','seam',f'lace-{j}')
        self.add_line('end-band-low',(7,27),(21,41))
        self.add_line('end-band-high',(27,7),(41,21))
        self.relate('connect','outline','end-band-low')
        self.relate('connect','outline','end-band-high')

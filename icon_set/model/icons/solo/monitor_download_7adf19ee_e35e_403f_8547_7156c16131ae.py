"""A desktop monitor displays a downward download arrow.
Symbol plan: Centered rounded screen with common radius 4; shared lower midpoint supports the stand and symmetric foot; arrow shaft and chevron share a real tip.
Keyshape visible bounds: (4, 4, 44, 44).
Construction references: Lucide monitor-down: screen, stand and centered download arrow; supplied reference: wide screen and open bottom foot..
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7adf19ee-e35e-403f-8547-7156c16131ae'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/monitor download_7adf19ee-e35e-403f-8547-7156c16131ae.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-download'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    categories = ("computers", "primitives")
    aliases = ()
    keywords = ('monitor', 'download')
    def build(self):
        # Screen lower edge is split at the stand attachment.
        self.add_line('screen-top',(10,6),(38,6))
        self.add_arc('screen-tr',(38,6),(42,10),radius_x=4)
        self.add_line('screen-right',(42,10),(42,30))
        self.add_arc('screen-br',(42,30),(38,34),radius_x=4)
        self.add_line('screen-bottom-r',(38,34),(24,34))
        self.add_line('screen-bottom-l',(24,34),(10,34))
        self.add_arc('screen-bl',(10,34),(6,30),radius_x=4)
        self.add_line('screen-left',(6,30),(6,10))
        self.add_arc('screen-tl',(6,10),(10,6),radius_x=4)
        self.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')
        self.add_line('arrow-shaft',(24,15),(24,25))
        self.add_polyline('arrow-head',(18,19),(24,25),(30,19))
        self.relate('connect','arrow-shaft','arrow-head')

    def circle(self, name, cx, cy, r):
        self.add_arc(name+"-top", (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc(name+"-bottom", (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour(name, name+"-top", name+"-bottom", closed=True)

    def box(self, name, left, top, right, bottom, r=3):
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,a in enumerate(points):
            b=points[(i+1)%8]; part=f"{name}-{i}"
            if i%2: self.add_arc(part,a,b,radius_x=r)
            else: self.add_line(part,a,b)
            members.append(part)
        self.add_contour(name,*members,closed=True)

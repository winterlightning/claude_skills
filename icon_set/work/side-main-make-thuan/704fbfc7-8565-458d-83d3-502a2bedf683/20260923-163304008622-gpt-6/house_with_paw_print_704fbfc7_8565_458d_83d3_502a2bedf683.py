"""House with Paw Print.

Symbol plan: House outline encloses three round toe loops and triangular central paw pad; mirrored about x=24. SQUARE extremes (6,6)-(42,42). Full source topology retained; fit may remain crowded.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '704fbfc7-8565-458d-83d3-502a2bedf683'
SOURCE_PATH = 'pictographic-primitives/other/house paw print_704fbfc7-8565-458d-83d3-502a2bedf683.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'house-with-paw-print'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'other'
    aliases = ()
    keywords = ('house', 'with', 'paw', 'print')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-a', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-b', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-a', name+'-b', closed=True)

    def rounded_box(self, name, left, top, right, bottom, r):
        self.add_line(name+'-top', (left+r,top), (right-r,top))
        self.add_arc(name+'-tr', (right-r,top), (right,top+r), radius_x=r)
        self.add_line(name+'-right', (right,top+r), (right,bottom-r))
        self.add_arc(name+'-br', (right,bottom-r), (right-r,bottom), radius_x=r)
        self.add_line(name+'-bottom', (right-r,bottom), (left+r,bottom))
        self.add_arc(name+'-bl', (left+r,bottom), (left,bottom-r), radius_x=r)
        self.add_line(name+'-left', (left,bottom-r), (left,top+r))
        self.add_arc(name+'-tl', (left,top+r), (left+r,top), radius_x=r)
        self.add_contour(name, *(name+'-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

    def build(self):
        axis=24
        self.add_line('roof-walls-1',(6, 38),(6, 16))
        self.add_line('roof-walls-2',(6, 16),(24, 6))
        self.add_line('roof-walls-3',(24, 6),(42, 16))
        self.add_line('roof-walls-4',(42, 16),(42, 38))
        self.add_arc('corner-right',(42,38),(38,42),radius_x=4)
        self.add_line('bottom',(38,42),(10,42))
        self.add_arc('corner-left',(10,42),(6,38),radius_x=4)
        self.add_contour('house','roof-walls-1','roof-walls-2','roof-walls-3','roof-walls-4','corner-right','bottom','corner-left',closed=True)
        # Three complete circular toes preserve the source rather than becoming dots.
        self.circle('toe-top',axis,17,3)
        for side,x in [('left',16),('right',32)]:
            self.circle('toe-'+side,x,25,3)
        self.add_polyline('pad',(axis,29),(31,36),(17,36),closed=True)

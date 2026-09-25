"""Spreadsheet with two orthogonal double expansion arrows.
Plan: Separate table and arrow bands. Both ends of both arrows are legible at native size.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f210946c-cdf6-4570-9689-058b554c18ac'
SOURCE_PATH = 'pictographic-primitives/interface-essential/resize expand spreadsheet_f210946c-cdf6-4570-9689-058b554c18ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'resize-expand-spreadsheet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('resize', 'expand', 'spreadsheet')

    def build(self):
        self.add_polyline('table',(6,6),(16,6),(26,6),(26,16),(26,26),(16,26),(6,26),(6,16),closed=True)
        self.add_polyline('vertical',(16,6),(16,16),(16,26))
        self.add_polyline('horizontal',(6,16),(16,16),(26,16))
        for a in ('vertical-1','vertical-2'):
            for b in ('horizontal-1','horizontal-2'):self.relate('connect',a,b)
        for a,bs in [('vertical-1',['table-1','table-2']),('vertical-2',['table-5','table-6']),('horizontal-1',['table-7','table-8']),('horizontal-2',['table-3','table-4'])]:
            for b in bs:self.relate('connect',a,b)
        self.arrow('right',(6,38),(30,38),(26,34),(26,42))
        self.add_polyline('left-head',(10,34),(6,38),(10,42))
        self.relate('connect','right-shaft','left-head-1');self.relate('connect','right-shaft','left-head-2')
        self.arrow('up',(38,30),(38,6),(34,10),(42,10))
        self.add_polyline('down-head',(34,26),(38,30),(42,26))
        self.relate('connect','up-shaft','down-head-1');self.relate('connect','up-shaft','down-head-2')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(name+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, l, t, r, b, rad=2):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        for i in range(8):
            a,z=pts[i],pts[(i+1)%8]
            if i%2:self.add_arc(f'{name}-{i}',a,z,radius_x=rad)
            else:self.add_line(f'{name}-{i}',a,z)
        self.add_contour(name,*(f'{name}-{i}' for i in range(8)),closed=True)

    def arrow(self, name, start, tip, wing1, wing2):
        self.add_line(name+'-shaft',start,tip)
        self.add_polyline(name+'-head',wing1,tip,wing2)
        for i in (1,2):self.relate('connect',name+'-shaft',f'{name}-head-{i}')

    def heart(self, name, x, top, half, bottom):
        # Mirrored lobes share dimensions and meet the pointed lower silhouette.
        self.add_bezier(name+'-left',(x,top+2),((x-half,top-5),(x-half-3,top+4),(x-half,top+7)),((x-half+2,top+10),(x, bottom),(x,bottom)))
        self.add_bezier(name+'-right',(x,bottom),((x,bottom),(x+half-2,top+10),(x+half,top+7)),((x+half+3,top+4),(x+half,top-5),(x,top+2)))
        self.add_contour(name,name+'-left',name+'-right',closed=True)

PLAN = 'Spreadsheet with two orthogonal double expansion arrows. Separate table and arrow bands.'
OMISSIONS = 'Grid reduced to two rows and two columns.'
CONSTRUCTION_REFERENCES = ['icon_set/references/lucide/original/expand.svg', 'icon_set/references/lucide/atomic-debug/expand.svg']
PARENT_SOURCE = 'icon_set/model/icons/solo/resize_expand_spreadsheet_f210946c_cdf6_4570_9689_058b554c18ac.py'

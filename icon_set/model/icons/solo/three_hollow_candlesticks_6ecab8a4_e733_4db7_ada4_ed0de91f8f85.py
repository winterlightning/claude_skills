"""Three financial candlesticks have rectangular hollow bodies and thin wicks extending above and below. Their heights and levels vary, and the left candle contains a diagonal interior division.
Symbol plan: Three hollow rectangular bodies share width 8 and 16-unit horizontal pitch. Independently varied levels and wick lengths retain the data. Omit the left internal diagonal division.
Keyshape: HRECT_L; centerline extremes (4,8)-(44,40).
Construction reference: chart-candlestick; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6ecab8a4-e733-4db7-ada4-ed0de91f8f85'
SOURCE_PATH = 'pictographic-primitives/business/hollow candles chart_6ecab8a4-e733-4db7-ada4-ed0de91f8f85.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'three-hollow-candlesticks'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('three', 'hollow', 'candlesticks')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        for j,(x,t,b,wt,wb) in enumerate([(8,18,34,8,40),(24,12,24,8,32),(40,16,32,8,38)]):
         self.add_polyline(f'body-{j}',(x-4,t),(x,t),(x+4,t),(x+4,b),(x,b),(x-4,b),closed=True)
         self.add_line(f'wick-top-{j}',(x,wt),(x,t));self.add_line(f'wick-bottom-{j}',(x,b),(x,wb))
         self.relate('connect',f'body-{j}',f'wick-top-{j}');self.relate('connect',f'body-{j}',f'wick-bottom-{j}')

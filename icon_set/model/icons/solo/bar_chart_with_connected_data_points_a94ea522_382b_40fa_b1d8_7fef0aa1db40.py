"""Four bars rise from a shared baseline beneath a connected line of four circular data points. The overall trend climbs rightward, with a small dip in the line before its final high point.
Symbol plan: Four bars share a baseline, trend has four round-cap data nodes. Replace hollow markers with stroke-sized nodes and bars with single strokes.
Keyshape: SQUARE, centerline extremes (6,6)-(42,42).
Construction reference: chart-no-axes-combined; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'a94ea522-382b-40fa-b1d8-7fef0aa1db40'
SOURCE_PATH = 'pictographic-primitives/business/graph bar_a94ea522-382b-40fa-b1d8-7fef0aa1db40.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'bar-chart-with-connected-data-points'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    categories = ('primitives', 'business')
    aliases = ()
    keywords = ('bar', 'chart', 'with', 'connected', 'data', 'points')

    def build(self):

        def segments(name, *points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name, cx, cy, r):
            self.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
            self.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        def rect(name, l,t,r,b, radius=0):
            if not radius:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            q=radius
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z: continue
                part=f'{name}-{j}'
                if j%2: self.add_arc(part,a,z,radius_x=q)
                else: self.add_line(part,a,z)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        def axes():
            self.add_line('axis-y',(6,6),(6,38))
            self.add_arc('axis-corner',(6,38),(10,42),radius_x=4,sweep=False)
            self.add_line('axis-x',(10,42),(42,42))
            self.add_contour('axes','axis-y','axis-corner','axis-x')

        self.add_polyline('trend',(6,20),(18,12),(30,16),(42,6))
        self.add_polyline('baseline',(6,42),(18,42),(30,42),(42,42))
        for j,(x,y) in enumerate([(6,32),(18,28),(30,30),(42,20)]):
         self.add_line(f'bar-{j}',(x,42),(x,y))
         self.relate('connect',f'bar-{j}','baseline')

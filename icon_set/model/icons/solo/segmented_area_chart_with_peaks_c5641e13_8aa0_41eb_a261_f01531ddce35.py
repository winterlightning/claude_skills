"""A jagged area-chart boundary climbs through several sharp peaks and valleys above a flat baseline. Vertical dividers descend from two valleys, separating the outlined area into adjoining sections.
Symbol plan: Jagged area silhouette, two shared valley dividers, common baseline. Drop redundant exterior axes.
Keyshape: SQUARE, centerline extremes (6,6)-(42,42).
Construction reference: chart-area; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c5641e13-8aa0-41eb-a261-f01531ddce35'
SOURCE_PATH = 'pictographic-primitives/business/graph segmented area null values_c5641e13-8aa0-41eb-a261-f01531ddce35.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'segmented-area-chart-with-peaks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'business'
    aliases = ()
    keywords = ('segmented', 'area', 'chart', 'with', 'peaks')

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

        self.add_polyline('area',(6,42),(6,22),(16,30),(24,6),(32,26),(42,10),(42,42),(32,42),(16,42),closed=True)
        for x,y in [(16,30),(32,26)]:
         self.add_line(f'divider-{x}',(x,y),(x,42))
         self.relate('connect',f'divider-{x}','area')

"""A tall rectangular pitch is divided into two halves by a vertical line. A circular centre marking sits on the halfway line, with the remaining field interior left empty.
Symbol plan: Tall field outline; central circle and split vertical halfway line. Circle stays open inside; omit the line through the circle to retain clear marking.
Keyshape: VRECT_L, centerline extremes (8,4)-(40,44).
Construction reference: workflow; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f896baac-1667-54c7-a59b-5dde70cb1c82'
SOURCE_PATH = 'pictographic-primitives/building/football field_f896baac-1667-54c7-a59b-5dde70cb1c82.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'football-pitch-with-centre-circle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('football', 'pitch', 'with', 'centre', 'circle')

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

        self.add_polyline('pitch',(8,4),(24,4),(40,4),(40,44),(24,44),(8,44),closed=True)
        self.add_arc('centre-right',(24,16),(24,32),radius_x=8)
        self.add_arc('centre-left',(24,32),(24,16),radius_x=8)
        self.add_contour('centre','centre-right','centre-left',closed=True)
        for n,a,b in [('top',(24,4),(24,16)),('bottom',(24,32),(24,44))]:
         self.add_line(n,a,b)
         self.relate('connect',n,'pitch')
         self.relate('connect',n,'centre')

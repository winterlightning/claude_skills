"""A bungalow with a broad peaked roof and arched doorway stands on long posts above water. A rectangular deck spans its front, with a row of curved waves below.
Symbol plan: Mirrored roof and stilt posts, open arched doorway, split floor and two waves. Remove duplicate deck edges and roof chord to open the interior.
Keyshape: SQUARE, centerline extremes (6,6)-(42,42).
Construction reference: house; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd4aeb0ca-0e11-48b7-be86-0aebbc5e8bfa'
SOURCE_PATH = 'pictographic-primitives/building/floating bungalow_d4aeb0ca-0e11-48b7-be86-0aebbc5e8bfa.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'stilt-bungalow-above-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    aliases = ()
    keywords = ('stilt', 'bungalow', 'above', 'waves')

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

        self.add_polyline('roof',(6,18),(9,16),(24,6),(39,16),(42,18))
        for x in (9,39):
         self.add_polyline(f'post-{x}',(x,16),(x,30),(x,32))
         self.relate('connect',f'post-{x}','roof')
        self.add_line('deck-left',(9,30),(20,30))
        self.add_line('deck-right',(28,30),(39,30))
        self.relate('connect','deck-left','post-9')
        self.relate('connect','deck-right','post-39')
        self.add_line('door-l',(20,30),(20,26))
        self.add_arc('door-a',(20,26),(28,26),radius_x=4)
        self.add_line('door-r',(28,26),(28,30))
        self.add_contour('door','door-l','door-a','door-r')
        self.relate('connect','door','deck-left')
        self.relate('connect','door','deck-right')
        self.add_arc('water-l',(6,40),(24,40),radius_x=9,radius_y=2,sweep=False)
        self.add_arc('water-r',(24,40),(42,40),radius_x=9,radius_y=2,sweep=False)
        self.add_contour('water','water-l','water-r')

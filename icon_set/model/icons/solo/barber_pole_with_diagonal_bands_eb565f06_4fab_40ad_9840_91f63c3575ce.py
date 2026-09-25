"""A vertical barber pole has a narrow cylindrical body between rounded top and bottom caps. Several diagonal stripes cross the central shaft, wrapping visually around its length.
Symbol plan: Symmetric pole with rounded cap ends and two diagonal stripes. One broad shaft between shared cap boundaries.
Keyshape: VRECT_L, centerline extremes (8,4)-(40,44).
Construction reference: paint-roller; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb565f06-4fab-40ad-9840-91f63c3575ce'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress barber_eb565f06-4fab-40ad-9840-91f63c3575ce.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'barber-pole-with-diagonal-bands'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('barber', 'pole', 'with', 'diagonal', 'bands')

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

        self.add_line('cap-top',(16,4),(32,4))
        self.add_arc('cap-tr',(32,4),(40,12),radius_x=8)
        segments('cap-bottom',(40,12),(32,12),(16,12),(8,12))
        self.add_arc('cap-tl',(8,12),(16,4),radius_x=8)
        self.add_contour('top-cap','cap-top','cap-tr','cap-bottom-1','cap-bottom-2','cap-bottom-3','cap-tl',closed=True)
        self.add_polyline('shaft-left',(16,12),(16,24),(16,36))
        self.add_polyline('shaft-right',(32,12),(32,24),(32,36))
        segments('bottom-top',(8,36),(16,36),(32,36),(40,36))
        self.add_arc('cap-br',(40,36),(32,44),radius_x=8)
        self.add_line('bottom-base',(32,44),(16,44))
        self.add_arc('cap-bl',(16,44),(8,36),radius_x=8)
        self.add_contour('bottom-cap','bottom-top-1','bottom-top-2','bottom-top-3','cap-br','bottom-base','cap-bl',closed=True)
        for s in ('shaft-left','shaft-right'):
         self.relate('connect',s,'top-cap');self.relate('connect',s,'bottom-cap')
        for j,y in enumerate((24,36)):
         self.add_line(f'stripe-{j}',(16,y),(32,y-12))
         self.relate('connect',f'stripe-{j}','shaft-left');self.relate('connect',f'stripe-{j}','shaft-right')

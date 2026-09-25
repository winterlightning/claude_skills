"""A wide rectangular garage door hangs beneath a projecting top rail. Two horizontal seams divide the door into three broad sections above a straight ground line.
Symbol plan: Symmetric rectangular rolling door with projecting rail and repeated section seams, all shared endpoints.
Keyshape: HRECT_L, centerline extremes (4,8)-(44,40).
Construction reference: warehouse; original and atomic geometry inspected when Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8cdf3f7f-a05b-585c-bc1b-60e8dd63c214'
SOURCE_PATH = 'pictographic-primitives/building/garage door closed_8cdf3f7f-a05b-585c-bc1b-60e8dd63c214.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'closed-sectional-garage-door'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'building'
    categories = ('building', 'primitives')
    aliases = ()
    keywords = ('closed', 'sectional', 'garage', 'door')

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

        self.add_polyline('rail',(4,8),(8,8),(40,8),(44,8))
        for x in (8,40):
         self.add_polyline(f'side-{x}',(x,8),(x,16),(x,24),(x,32),(x,40))
         self.relate('connect',f'side-{x}','rail')
        for y in (16,24,32,40):
         self.add_line(f'seam-{y}',(8,y),(40,y))
         for x in (8,40): self.relate('connect',f'seam-{y}',f'side-{x}')

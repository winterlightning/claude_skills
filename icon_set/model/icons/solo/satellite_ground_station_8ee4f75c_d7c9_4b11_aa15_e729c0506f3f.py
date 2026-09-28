"""Upright satellite dish, receiver, legs and radio arc. Square envelope; Lucide satellite-dish bowl/receiver relationship. One broad signal arc replaces repeated waves."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8ee4f75c-d7c9-4b11-aa15-e729c0506f3f'
SOURCE_PATH = 'pictographic-primitives/technology/ground station_8ee4f75c-d7c9-4b11-aa15-e729c0506f3f.svg'
AUTHOR = 'gpt-6'

class SatelliteGroundStation(Solo48):
    icon_id = 'satellite-ground-station'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('ground-station', 'satellite-dish', 'antenna', 'signal', 'receiver', 'broadcast', 'communication')

    def build(self):
        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,sweep=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=sweep)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def chain(n,*p):
            for i,(a,b) in enumerate(zip(p,p[1:]),1): line(f'{n}-{i}',a,b)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def connect(a,b): self.relate("connect",a,b)
        def circle(n,x,y,r):
            arc(n+'a',(x,y-r),(x,y+r),r)
            arc(n+'b',(x,y+r),(x,y-r),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,rad=4):
            line(n+'t',(l+rad,t),(r-rad,t)); arc(n+'tr',(r-rad,t),(r,t+rad),rad)
            line(n+'r',(r,t+rad),(r,b-rad)); arc(n+'br',(r,b-rad),(r-rad,b),rad)
            line(n+'b',(r-rad,b),(l+rad,b)); arc(n+'bl',(l+rad,b),(l,b-rad),rad)
            line(n+'l',(l,b-rad),(l,t+rad)); arc(n+'tl',(l,t+rad),(l+rad,t),rad)
            contour(n,*[n+s for s in ('t','tr','r','br','b','bl','l','tl')],closed=True)
        chain('rim',(8,28),(24,28),(40,28))
        arc('bowl-right',(40,28),(30,38),10)
        chain('bowl-base',(30,38),(18,38))
        arc('bowl-left',(18,38),(8,28),10)
        contour('dish','rim-1','rim-2','bowl-right','bowl-base-1','bowl-left',closed=True)
        circle('receiver',24,17,2)
        line('stem',(24,19),(24,28));connect('stem','receiver');connect('stem','dish')
        for x in (18,30):
            line(f'leg-{x}',(x,38),(x,42));connect(f'leg-{x}','dish')
        arc('signal-left',(6,10),(24,6),18,4)
        arc('signal-right',(24,6),(42,10),18,4);contour('signal','signal-left','signal-right')

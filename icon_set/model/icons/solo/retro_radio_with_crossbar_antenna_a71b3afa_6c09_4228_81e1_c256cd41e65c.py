"""Retro Radio with Crossbar Antenna.

Symbol plan: Rounded retro radio with one horizontal tuning line and a crossbar antenna. Omit short feet and fine tuner marks.
SQUARE centerline extremes (6,6)-(42,42); exact envelope selected for the subject's proportions.
Construction reference: Lucide radio-receiver original and atomic-debug also informed tangent quarter-circle casing corners during final review. Supplied radio layout; shared rounded rectangles and exact attachment points keep the body and antenna coherent.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a71b3afa-6c09-4228-81e1-c256cd41e65c'
SOURCE_PATH = 'pictographic-primitives/audio/radio retro_a71b3afa-6c09-4228-81e1-c256cd41e65c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'retro-radio-with-crossbar-antenna'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('radio', 'broadcast', 'audio', 'receiver', 'antenna', 'speaker', 'signal', 'tuning')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def path(n,*pts,closed=False): self.add_polyline(n,*pts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)

        def casing(n,x,y,w,h,ax,r=4):
            line(n+'-top-left',(x+r,y),(ax,y));line(n+'-top-right',(ax,y),(x+w-r,y))
            arc(n+'-ne',(x+w-r,y),(x+w,y+r),r)
            line(n+'-right',(x+w,y+r),(x+w,y+h-r));arc(n+'-se',(x+w,y+h-r),(x+w-r,y+h),r)
            line(n+'-bottom',(x+w-r,y+h),(x+r,y+h));arc(n+'-sw',(x+r,y+h),(x,y+h-r),r)
            line(n+'-left',(x,y+h-r),(x,y+r));arc(n+'-nw',(x,y+r),(x+r,y),r)
            edges=[n+'-'+suffix for suffix in ('top-left','top-right','ne','right','se','bottom','sw','left','nw')]
            for a,b in zip(edges,edges[1:]+edges[:1]):connect(a,b)

        casing('body',6,18,36,24,14)
        line('tuner',(14,30),(34,30))
        path('antenna',(14,18),(14,10),(14,6));connect('antenna','body-top-left');connect('antenna','body-top-right')
        path('crossbar',(6,10),(14,10),(22,10));connect('crossbar','antenna')

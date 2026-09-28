"""Stereo Radio with Two Speakers.

Symbol plan: Stereo radio with two identical circular speakers and a slanted antenna. Remove the narrow tuning line above the speaker pair.
HRECT_L centerline extremes (4,8)-(44,40); exact envelope selected for the subject's proportions.
Construction reference: Lucide radio-receiver original and atomic-debug also informed tangent quarter-circle casing corners during final review. Lucide radio original and atomic-debug inform circular audio elements; source supplies the paired speaker layout.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = 'a96b28b8-00ab-5cbb-b161-a2a2cd2026d0'
SOURCE_PATH = 'pictographic-primitives/audio/radio stereo_a96b28b8-00ab-5cbb-b161-a2a2cd2026d0.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stereo-radio-with-two-speakers'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    categories = ('audio', 'primitives')
    aliases = ()
    keywords = ('radio', 'broadcast', 'audio', 'receiver', 'antenna', 'speaker', 'signal', 'tuning')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,x,y,r):
            pts=[(x,y-r),(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
            for j in range(4): arc(n+str(j),pts[j],pts[j+1],r)
            join(n,*(n+str(j) for j in range(4)),closed=True)

        def casing(n,x,y,w,h,ax,r=4):
            line(n+'-top-left',(x+r,y),(ax,y));line(n+'-top-right',(ax,y),(x+w-r,y))
            arc(n+'-ne',(x+w-r,y),(x+w,y+r),r)
            line(n+'-right',(x+w,y+r),(x+w,y+h-r));arc(n+'-se',(x+w,y+h-r),(x+w-r,y+h),r)
            line(n+'-bottom',(x+w-r,y+h),(x+r,y+h));arc(n+'-sw',(x+r,y+h),(x,y+h-r),r)
            line(n+'-left',(x,y+h-r),(x,y+r));arc(n+'-nw',(x,y+r),(x+r,y),r)
            edges=[n+'-'+suffix for suffix in ('top-left','top-right','ne','right','se','bottom','sw','left','nw')]
            for a,b in zip(edges,edges[1:]+edges[:1]):connect(a,b)

        casing('body',4,16,40,24,24)
        for j,x in enumerate((16,32)):circle('speaker-'+str(j),x,28,4)
        line('antenna',(24,16),(36,8));connect('antenna','body-top-left');connect('antenna','body-top-right')

"""Person Recording with Headphones.

Symbol plan: Side-profile head with circular earcup and headset band; separate microphone capsule and stand. Omit grille ticks.
HRECT_L centerline extremes (4,8)-(44,40); envelope follows the subject's proportions.
Construction reference: human_ref/user.svg: rounded human contours; Lucide mic: capsule. Head and neck are continuous.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '5b2c44e7-50f9-4419-b47a-177cfdb3636d'
SOURCE_PATH = 'pictographic-primitives/audio/microphone podcast person_5b2c44e7-50f9-4419-b47a-177cfdb3636d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-recording-with-headphones'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'audio'
    aliases = ()
    keywords = ('person', 'recording', 'with', 'headphones')

    def build(self) -> None:

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def join(n,*parts,closed=False): self.add_contour(n,*parts,closed=closed)
        def connect(a,b): self.relate('connect',a,b)
        def circle(n,cx,cy,r):
            pts=[(cx,cy-r),(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
            for j in range(4): arc(n+'-'+str(j),pts[j],pts[j+1],r)
            join(n,*(n+'-'+str(j) for j in range(4)),closed=True)
        def box(n,x,y,w,h,r=2):
            pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for i in range(8):
                a,b=pts[i],pts[(i+1)%8]
                if a==b: continue
                if i%2: arc(n+str(i),a,b,r)
                else: line(n+str(i),a,b)
            join(n,*(n+str(i) for i in range(8) if pts[i]!=pts[(i+1)%8]),closed=True)

        arc('skull-l',(20,20),(32,8),12)
        arc('skull-r',(32,8),(44,20),12)
        line('skull-right',(44,20),(44,30))
        arc('back',(44,30),(38,36),6)
        pts=[(38,36),(38,40),(24,40),(24,34),(20,34),(20,28),(18,28),(20,24),(20,20)]
        for j,(a,b) in enumerate(zip(pts,pts[1:])): line('neck-'+str(j),a,b)
        join('profile','skull-l','skull-r','skull-right','back',*(f'neck-{j}' for j in range(len(pts)-1)))
        circle('earphone',32,24,3)
        line('headband',(32,8),(32,21))
        connect('headband','profile');connect('headband','earphone')
        box('mic',4,10,8,12,4)
        line('stem',(8,22),(8,40));connect('mic','stem')

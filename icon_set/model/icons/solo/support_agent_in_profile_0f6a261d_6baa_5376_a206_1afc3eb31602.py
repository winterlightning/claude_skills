"""Support Agent in Profile — batch 50."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0f6a261d-6baa-5376-a206-1afc3eb31602'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/headphones customer support human_0f6a261d-6baa-5376-a206-1afc3eb31602.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'support-agent-in-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('support', 'agent', 'in', 'profile')

    def build(self):
        # Plan: left-facing continuous profile, circular ear cup, band and curved boom.
        # SQUARE extremes (6,6)-(42,42). Lucide headset; human user.svg for simplification.
        # Continuous neck in source, so no detached head/body gap applies.
        self.add_arc('crown',(10,22),(26,6),radius_x=16)
        self.add_arc('crown-right',(26,6),(42,22),radius_x=16)
        self.add_line('back-upright',(42,22),(42,28))
        self.add_arc('back',(42,28),(34,36),radius_x=8)
        self.add_line('neck-back',(34,36),(34,42))
        self.add_line('face-bottom',(18,42),(14,42))
        self.add_arc('chin',(14,42),(10,38),radius_x=4)
        self.add_polyline('nose',(10,38),(10,30),(6,30),(10,22))
        self.contours.clear()
        self.add_contour('profile','face-bottom','chin','nose-1','nose-2','nose-3','crown','crown-right','back-upright','back','neck-back')
        self.circle('earpiece',26,22,4)
        self.add_line('band',(26,6),(26,18));self.relate('connect','band','earpiece');self.relate('connect','band','profile')
        self.add_arc('boom',(26,26),(20,32),radius_x=6)
        self.add_dot('microphone',(20,32));self.relate('connect','boom','microphone');self.relate('connect','boom','earpiece')


    def circle(self,n,x,y,r):
        pts=[(x+r,y),(x,y+r),(x-r,y),(x,y-r)]
        for j in range(4): self.add_arc(f'{n}-{j}',pts[j],pts[(j+1)%4],radius_x=r)
        self.add_contour(n,*[f'{n}-{j}' for j in range(4)],closed=True)

    def box(self,n,x,y,w,h,attachments=()):
        corners=[(x,y),(x+w,y),(x+w,y+h),(x,y+h)];nodes=[]
        for a,z in zip(corners,corners[1:]+corners[:1]):
            dx,dy=z[0]-a[0],z[1]-a[1]
            inside=[p for p in attachments if (p[0]-a[0])*dy==(p[1]-a[1])*dx and 0<(p[0]-a[0])*dx+(p[1]-a[1])*dy<dx*dx+dy*dy]
            inside.sort(key=lambda p:(p[0]-a[0])*dx+(p[1]-a[1])*dy);nodes.extend([a]+inside)
        self.add_polyline(n,*nodes,closed=True)


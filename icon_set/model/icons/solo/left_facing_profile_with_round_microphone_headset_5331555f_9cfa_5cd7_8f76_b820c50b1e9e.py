"""Human Profile wearing Communication Headset.

Symbol plan: Left-facing human profile, circular earpiece and curved microphone boom with round mouthpiece. Human reference user.svg/full_body_ref.png supports minimal anatomy; source supplies continuous profile/neck so detached-head gap does not apply. Lucide headset informs band and boom. Omit hollow band and tiny mouthpiece hole.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5331555f-9cfa-5cd7-8f76-b820c50b1e9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable headset_5331555f-9cfa-5cd7-8f76-b820c50b1e9e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'left-facing-profile-with-round-microphone-headset'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'devices'
    categories = ('primitives', 'devices')
    aliases = ()
    keywords = ('human', 'profile', 'wearing', 'communication', 'headset')

    def build(self):
        self.add_arc('crown',(10,22),(42,22),radius_x=16)
        self.add_line('back-upright',(42,22),(42,28))
        self.add_arc('back',(42,28),(34,36),radius_x=8)
        self.add_line('neck-back',(34,36),(34,42))
        self.run('face',(18,42),(14,42))
        self.add_arc('chin',(14,42),(10,38),radius_x=4)
        self.run('nose',(10,38),(10,30),(6,30),(10,22))
        self.add_contour('profile','face-1','chin','nose-1','nose-2','nose-3','crown','back-upright','back','neck-back')
        self.circle('earpiece',28,22,4)
        self.add_line('band',(32,22),(42,22));self.relate('connect','band','earpiece');self.relate('connect','band','profile')
        self.add_arc('boom',(28,26),(20,32),radius_x=8,radius_y=6)
        self.add_dot('mouthpiece',(20,32));self.relate('connect','boom','mouthpiece');self.relate('connect','boom','earpiece')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f"{name}-{i}",a,b)

"""Human Wearing Virtual Reality Headset.

Symbol plan: Left-facing continuous human profile with broad projecting visor and round earpiece. Human user.svg/full_body_ref.png informs circular skull and simple neck; Lucide headset informs attachments. Omit tiny visor inset and duplicate band edge. Asymmetry preserves facing direction.
Keyshape SQUARE; exact visible bounds (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a4ab06e-b066-4124-a4d4-2845bcd8c4bc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/devices/wearable vr goggles_8a4ab06e-b066-4124-a4d4-2845bcd8c4bc.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'left-facing-profile-wearing-broad-vr-visor'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/devices'
    aliases = ()
    keywords = ('human', 'wearing', 'virtual', 'reality', 'headset')

    def build(self):
        self.add_arc('crown',(10,15),(42,23),radius_x=17)
        self.run('back',(42,23),(42,28))
        self.add_arc('back-curve',(42,28),(34,36),radius_x=8)
        self.add_line('neck',(34,36),(34,42))
        self.add_contour('back-profile','crown','back-1','back-curve','neck')
        self.run('face',(18,42),(14,42))
        self.add_arc('chin',(14,42),(10,38),radius_x=4)
        self.run('nose',(10,38),(10,36),(6,36),(10,28))
        self.add_contour('front-profile','face-1','chin','nose-1','nose-2','nose-3')
        self.run('visor-top',(10,15),(23,15))
        self.add_arc('visor-bl',(10,28),(6,24),radius_x=4)
        self.add_line('visor-left',(6,24),(6,19))
        self.add_arc('visor-tl',(6,19),(10,15),radius_x=4)
        self.add_arc('visor-tr',(23,15),(28,20),radius_x=5)
        self.run('visor-bottom',(28,28),(10,28))
        self.add_contour('visor','visor-bottom-1','visor-bl','visor-left','visor-tl','visor-top-1','visor-tr')
        self.circle('ear',28,24,4)
        self.relate('connect','visor','ear');self.relate('connect','visor','back-profile');self.relate('connect','visor','front-profile')

    def circle(self,name,cx,cy,r):
        points=[(cx+r,cy),(cx,cy+r),(cx-r,cy),(cx,cy-r)]
        names=[]
        for i,start in enumerate(points):
            part=f'{name}-{i}';self.add_arc(part,start,points[(i+1)%4],radius_x=r);names.append(part)
        self.add_contour(name,*names,closed=True)

    def run(self,name,*points):
        for i,(a,b) in enumerate(zip(points,points[1:]),1):self.add_line(f'{name}-{i}',a,b)

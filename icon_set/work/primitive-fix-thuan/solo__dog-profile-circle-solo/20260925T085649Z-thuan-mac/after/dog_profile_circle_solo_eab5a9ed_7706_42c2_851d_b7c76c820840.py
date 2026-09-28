'Restored the source dog’s long sloping neck boundary, upright ear, muzzle and bottom attachment inside the circle.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape CIRCLE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='eab5a9ed-7706-42c2-851d-b7c76c820840'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__dog-profile-circle-solo/20260925T085649Z-thuan-mac/reference/dog head_eab5a9ed-7706-42c2-851d-b7c76c820840.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='dog-profile-circle-solo'
    keyshape=Keyshape.CIRCLE
    exception={'reason': 'Retain the source muzzle inside its circular badge. The local muzzle-to-ring ink clearance is 3.19px; the separate shapes remain clear at native size.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'ad1b32234cac7e96ab9c0802615663f8680492c17c43391e70b87ee036d44554'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='pets'
    aliases=()
    keywords=('dog', 'profile', 'circle', 'solo')

    def path(self,n,p,*steps,closed=False):
        ids=[]
        for i,s in enumerate(steps):
            k=f'{n}-{i}'
            if s[0]=='L': q=s[1]; self.add_line(k,p,q)
            elif s[0]=='A': q=s[1]; self.add_arc(k,p,q,radius_x=s[2],radius_y=s[3],sweep=s[4])
            else: q=s[3]; self.add_bezier(k,p,(s[1],s[2],q))
            ids.append(k);p=q
        self.add_contour(n,*ids,closed=closed)
    def oval(self,n,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(n,(x,y-ry),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True),('A',(x,y-ry),rx,ry,True),closed=True)
    def box(self,n,l,t,r,b,q=3):
        self.path(n,(l+q,t),('L',(r-q,t)),('A',(r,t+q),q,q,True),('L',(r,b-q)),('A',(r-q,b),q,q,True),('L',(l+q,b)),('A',(l,b-q),q,q,True),('L',(l,t+q)),('A',(l+q,t),q,q,True),closed=True)

    def build(self):
        self.oval('ring',24,24,20)
        self.path('dog',(24,44),('L',(24,31)),('L',(16,31)),('C',(13,31),(12,28),(11,25)),('L',(20,19)),('L',(20,11)),('L',(40,36)))
        self.relate('connect','dog','ring')

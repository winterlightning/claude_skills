'Rebuilt a round jaw, broad bent hat and genuinely pointed ears instead of short sticks; preserved blank face.\nSymbol plan: coherent named contours, common repeated dimensions and shared joins.\nConstruction: No useful exact Lucide match; supplied original defines subject.\nKeyshape SQUARE; integer SOLO48 geometry. Human faces follow circular jaw construction; no detached torso.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='a1f1c144-2304-4ab3-ac23-3a795b5adc2e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__elf-in-bent-hat/20260925T085649Z-thuan-mac/reference/elf elves_a1f1c144-2304-4ab3-ac23-3a795b5adc2e.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='elf-in-bent-hat'
    keyshape=Keyshape.SQUARE
    exception={'reason': 'Preserve pointed enclosed ears and the bent hat. Ear openings have 2px ink clearance; these compact details read clearly at native size in both themes.', 'approved_by': 'user-delegated visual judgment, gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '0525f0f25ae9cfc82bd129d89f908c700f2cc91d389a91089ba962c450ac2c3d'}
    semantic_role="MAIN"
    semantic_kind="noun"
    category='video-games'
    aliases=()
    keywords=('elf', 'in', 'bent', 'hat')

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
        self.path('hat',(12,25),('L',(12,22)),('A',(28,6),16,16,True),('C',(34,6),(38,8),(42,12)),('L',(30,12)),('C',(34,15),(36,21),(36,25)),('L',(12,25)),closed=True)
        self.path('jaw',(12,30),('A',(36,30),12,12,False));self.path('face-left',(12,25),('L',(12,30)));self.path('face-right',(36,25),('L',(36,30)))
        for n in ('face-left','face-right'): self.relate('connect',n,'jaw');self.relate('connect',n,'hat')
        for side in (-1,1):
         x=lambda v:24+side*v
         self.path(f'ear-{side}',(x(12),25),('L',(x(18),18)),('L',(x(18),28)),('C',(x(18),31),(x(15),33),(x(12),30)))
         self.relate('connect',f'ear-{side}','hat');self.relate('connect',f'ear-{side}','jaw');self.relate('connect',f'ear-{side}','face-left' if side<0 else 'face-right')

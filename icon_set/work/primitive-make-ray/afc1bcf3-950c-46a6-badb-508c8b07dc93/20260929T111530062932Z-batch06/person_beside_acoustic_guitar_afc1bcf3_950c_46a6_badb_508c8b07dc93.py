"""The rejected figure has one leg and the instrument has no acoustic soundhole. No written feedback. Broadened the guitar body for a visible soundhole, straightened its neck and gave the person two legs.
Construction: Lucide guitar: waisted body and soundhole. Human full_body_ref.png: round head and two legs with exact 4-unit gap.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'afc1bcf3-950c-46a6-badb-508c8b07dc93'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-beside-acoustic-guitar/20260929T110914Z-thuan-mac/reference/concert guitarist_afc1bcf3-950c-46a6-badb-508c8b07dc93.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'person-beside-acoustic-guitar'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('person', 'beside', 'acoustic', 'guitar')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)

        circle('head',10,11,5)
        line('torso',(10,24),(10,33));poly('arms',(6,29),(10,24),(16,26));join('arms','torso')
        poly('legs',(6,42),(10,33),(14,42));join('legs','torso')
        path('guitar',(34,42),[('C',(23,34),(27,42),(23,40)),('C',(27,26),(23,30),(26,30)),('C',(25,21),(24,25),(25,22)),('C',(34,18),(26,18),(29,18)),('C',(42,24),(41,18),(42,20)),('C',(39,29),(42,26),(39,27)),('C',(42,35),(41,31),(42,32)),('C',(34,42),(42,40),(39,42))],True)
        line('neck',(34,18),(34,6));line('headstock',(30,6),(38,6));join('neck','headstock','guitar')
        self.add_dot('soundhole',(33,31))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

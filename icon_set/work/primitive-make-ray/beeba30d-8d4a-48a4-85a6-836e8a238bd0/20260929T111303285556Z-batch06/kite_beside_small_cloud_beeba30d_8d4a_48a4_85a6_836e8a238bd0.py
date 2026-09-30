"""The current kite is a parallelogram with a flattened tail, and the cloud is cramped. No written feedback. Rebuilt a pointed kite and curling tail beside an open, larger cloud; omitted internal spars.
Construction: Lucide cloud: broad rounded lobe and coherent open contour.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'beeba30d-8d4a-48a4-85a6-836e8a238bd0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__kite-beside-small-cloud/20260929T110914Z-thuan-mac/reference/outdoors kite flying cloud_beeba30d-8d4a-48a4-85a6-836e8a238bd0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'kite-beside-small-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('kite', 'beside', 'small', 'cloud')
    
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

        path('cloud',(17,18),[('L',(11,18)),('A',(11,8),5),('C',(21,11),(11,4),(20,5))])
        poly('kite',(33,17),(42,26),(31,36),(23,26),closed=True)
        bez('tail',(31,36),((29,42),(37,42),(42,42)));join('tail','kite')

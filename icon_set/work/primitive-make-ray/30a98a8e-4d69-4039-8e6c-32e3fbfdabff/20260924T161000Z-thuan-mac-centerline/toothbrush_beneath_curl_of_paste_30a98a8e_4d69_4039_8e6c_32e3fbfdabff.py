"""A smooth paste curl floats above a brush. Three evenly spaced bristle strokes join a continuous handle with tangent bend transitions.
Construction: No useful exact Lucide match; source arrangement and geometric primitives.
Omissions: Individual fine bristles reduced to three equal strokes; paste curl retained.
Keyshape HRECT_L: exact contract extremes, stroke 4.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='30a98a8e-4d69-4039-8e6c-32e3fbfdabff'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__toothbrush-beneath-curl-of-paste/20260924T160711Z-thuan-mac/reference/brush toothpaste 1_30a98a8e-4d69-4039-8e6c-32e3fbfdabff.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='toothbrush-beneath-curl-of-paste'
    keyshape=Keyshape.HRECT_L
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects"
    aliases=()
    keywords=('toothbrush', 'beneath', 'curl', 'of', 'paste')
    def build(self):
        self.path('paste',(20,8),[('C',(28,16),(16,14),(24,16)),('A',(28,24),4,4,True),('L',(12,24)),('C',(20,8),(0,24),(7,11))],True)
        self.path('brush',(4,40),[('L',(26,40)),('C',(32,36),(28,40),(30,38)),('C',(38,32),(34,34),(36,32)),('L',(44,32))])
        for j,x in enumerate((4,12,20)):
         self.line('bristle'+str(j),(x,32),(x,40));self.join('bristle'+str(j),'brush')

    def path(self,n,p,steps,closed=False):
        ids=[]
        for j,step in enumerate(steps):
            k,q,*v=step; uid=f'{n}-{j}'
            if k=='L': self.add_line(uid,p,q)
            elif k=='A': self.add_arc(uid,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif k=='C': self.add_bezier(uid,p,(v[0],v[1],q))
            ids.append(uid);p=q
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=2):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def line(self,n,a,b): self.add_line(n,a,b)
    def poly(self,n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
    def join(self,a,b): self.relate('connect',a,b)

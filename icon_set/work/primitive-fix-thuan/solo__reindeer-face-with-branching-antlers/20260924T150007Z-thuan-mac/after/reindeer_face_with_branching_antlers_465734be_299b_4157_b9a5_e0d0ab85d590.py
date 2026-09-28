"""reindeer. Revision: Round mirrored ears and long muzzle, separate the branching antlers and use an outlined nose. Omit tiny eyes.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape VRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='465734be-299b-4157-b9a5-e0d0ab85d590'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__reindeer-face-with-branching-antlers/20260924T150007Z-thuan-mac/reference/reindeer_465734be-299b-4157-b9a5-e0d0ab85d590.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='reindeer-face-with-branching-antlers'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('reindeer',)

    def build(self):
        # Each contour owns its shape. Repeated parts share dimensions and axes.
        def path(n,start,steps,closed=False):
            p=start; members=[]
            for j,s in enumerate(steps):
                k=f'{n}-{j}';kind,q,*v=s
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=v[0],radius_y=v[1],sweep=v[2])
                elif kind=='C': self.add_bezier(k,p,(v[0],v[1],q))
                members.append(k);p=q
            self.add_contour(n,*members,closed=closed)
        def line(n,a,b):self.add_line(n,a,b)
        def poly(n,*p):self.add_polyline(n,*p)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def join(a,b):self.relate('connect',a,b)

        path('head',(13,24),[('C',(8,18),(10,24),(8,22)),('C',(17,19),(8,13),(13,16)),('C',(31,19),(21,16),(27,16)),('C',(40,18),(35,16),(40,13)),('C',(35,24),(40,22),(38,24)),('L',(35,33)),('A',(24,44),11,11,True),('A',(13,33),11,11,True),('L',(13,24))],True)
        for sign,label in [(-1,'left'),(1,'right')]:
            p=lambda x,y:(24+sign*x,y)
            path('antler-'+label,p(7,19),[('C',p(11,11),p(8,15),p(10,13)),('C',p(15,4),p(14,8),p(15,6))])
            poly('branch-'+label,p(11,11),p(7,8),p(7,4))
            join('antler-'+label,'head')
        circle('nose',24,32,2)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

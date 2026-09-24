"""cleaning vacuum 2. Revision: Restore low canister with large visible wheel, flexible hose and rounded floor nozzle. Omit wheel hub.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='73b9d387-6248-460f-a92b-023ea2dc33b8'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__low-vacuum-with-tall-curved-hose/20260924T142504Z-thuan-mac/reference/cleaning vacuum 2_73b9d387-6248-460f-a92b-023ea2dc33b8.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='low-vacuum-with-tall-curved-hose'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('cleaning', 'vacuum', '2')

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

        path('body',(6,36),[('L',(6,29)),('A',(11,24),5,5,True),('L',(17,24)),('A',(29,36),12,12,True),('L',(29,38)),('L',(18,38))])
        circle('wheel',12,36,6);join('body','wheel')
        path('hose',(17,24),[('C',(24,13),(27,24),(24,18)),('L',(24,12)),('A',(36,12),6,6,True),('L',(36,34))]);join('hose','body')
        path('nozzle',(36,34),[('L',(38,34)),('A',(42,38),4,4,True),('L',(42,42)),('L',(32,42))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

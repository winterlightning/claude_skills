"""redux logo. Revision: Restore three distinct circular nodes and three broad orbital sweeps in triangular arrangement. Preserve open sweep ends.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='eb47004b-f404-423b-86db-835fad7f0bcb'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__redux-three-lobed-emblem/20260924T150007Z-thuan-mac/reference/redux logo_eb47004b-f404-423b-86db-835fad7f0bcb.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='redux-three-lobed-emblem'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('redux', 'logo')

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

        circle('node-top',22,18,3);circle('node-left',14,30,3);circle('node-right',30,31,3)
        path('orbit-top',(14,27),[('C',(10,19),(10,25),(10,21)),('C',(23,6),(10,10),(17,6)),('C',(32,8),(27,6),(30,6))])
        path('orbit-right',(25,18),[('C',(42,32),(35,18),(42,23)),('L',(42,34))])
        path('orbit-left',(30,34),[('C',(19,42),(29,41),(24,42)),('C',(6,40),(12,42),(6,42))])

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

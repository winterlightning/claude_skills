"""Threaded sewing needle with smooth eye and a flowing loose thread.
Plan: Threaded sewing needle with smooth eye and a flowing loose thread.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Fine filament tail extension omitted; eye, taper and trailing thread retained."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='132f47bc-4c0e-4882-9b9d-93439d0723ca'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__threaded-sewing-needle/20260924T163448Z-thuan-mac/reference/needle_132f47bc-4c0e-4882-9b9d-93439d0723ca.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='threaded-sewing-needle'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('threaded', 'sewing', 'needle')

    def build(self):
        def path(name,start,steps,closed=False):
            p=start; members=[]
            for j,(kind,q,*args) in enumerate(steps):
                n=f'{name}-{j}'
                if p==q: continue
                if kind=='L': self.add_line(n,p,q)
                elif kind=='A': self.add_arc(n,p,q,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(n,p,(args[0],args[1],q))
                p=q;members.append(n)
            self.add_contour(name,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False):self.add_polyline(n,*p,closed=closed)
        def join(a,b):self.relate('connect',a,b)
        path('needle',(6,42),[('L',(26,14)),('A',(34,6),8,8,True),('A',(42,14),8,8,True),('L',(34,22)),('L',(6,42))],True)
        path('thread',(30,14),[('C',(34,22),(31,17),(31,20)),('C',(36,34),(40,26),(40,28)),('C',(28,42),(32,38),(28,38))]);join('thread','needle')

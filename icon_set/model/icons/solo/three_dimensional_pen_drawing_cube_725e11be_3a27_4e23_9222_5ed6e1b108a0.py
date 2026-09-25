"""A 3D pen drawing an isometric cube, with a rounded pen cap and straight cube edges.
Plan: A 3D pen drawing an isometric cube, with a rounded pen cap and straight cube edges.
Construction: No useful exact local Lucide match; source silhouette rebuilt from coherent curves.
Omissions: Small pen button and trailing filament omitted."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '725e11be-3a27-4e23-9222-5ed6e1b108a0'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_01/3 d pen box_725e11be-3a27-4e23-9222-5ed6e1b108a0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='three-dimensional-pen-drawing-cube'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('three', 'dimensional', 'pen', 'drawing', 'cube')

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
        poly('cube',(6,26),(18,20),(30,26),(30,36),(18,42),(6,36),closed=True)
        poly('faces',(6,26),(18,32),(30,26));line('front',(18,32),(18,42));join('faces','cube');join('front','cube');join('front','faces')
        path('pen',(30,26),[('L',(28,18)),('L',(34,8)),('C',(38,6),(35,6),(36,6)),('A',(42,10),4,4,True),('C',(40,16),(42,12),(41,14)),('L',(38,20)),('L',(30,26))],True);join('pen','cube');join('pen','faces')

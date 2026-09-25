"""oatmeal. Revision: Replace plain food dome with soft oatmeal lobes and rounded spoon end; add short bowl foot. Omit individual grains.
Construction: Lucide soup: coherent bowl and spoon, with source-specific oatmeal mound. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '683a2acb-7114-4e54-a1d8-6e9238c88f36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/oatmeal_683a2acb-7114-4e54-a1d8-6e9238c88f36.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='oatmeal-bowl-spoon'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('oatmeal',)

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

        path('bowl',(6,25),[('L',(42,25)),('C',(24,42),(42,35),(34,42)),('C',(6,25),(14,42),(6,35))],True)
        path('oatmeal',(9,25),[('A',(16,17),7,8,True),('A',(30,17),7,7,True),('A',(35,25),5,8,True)])
        line('spoon',(35,25),(41,6))
        join('oatmeal','bowl');join('spoon','bowl');join('spoon','oatmeal')

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

"""primitive symbols bull. Revision: Restore two left-swept horns, rounded long body and angled legs. Retain cave-art profile; omit facial detail.
Construction: No useful direct Lucide match; supplied source silhouette. Preserve source-facing direction and arrangement.
Keyshape HRECT_L; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '14947e0c-fbe9-4a62-8be2-bfa1ad2a4321'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/primitive symbols bull_14947e0c-fbe9-4a62-8be2-bfa1ad2a4321.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='primitive-bull-profile'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('primitive', 'symbols', 'bull')

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

        path('body',(14,16),[('C',(7,17),(11,14),(8,14)),('L',(4,23)),('C',(10,24),(4,26),(8,24)),('C',(17,30),(13,23),(12,28)),('C',(24,32),(20,31),(22,32)),('C',(32,31),(27,32),(30,32)),('C',(44,23),(40,31),(44,29)),('C',(37,16),(44,16),(41,15)),('C',(14,16),(29,19),(23,15))],True)
        path('horn-upper',(14,16),[('C',(4,8),(14,10),(8,11))])
        path('horn-lower',(7,17),[('C',(4,16),(5,18),(4,17))])
        poly('front-leg',(17,30),(13,40));poly('second-leg',(24,32),(22,40));join('second-leg','body')
        poly('back-leg',(32,31),(35,35),(31,40));poly('far-leg',(44,23),(44,35),(44,40))

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

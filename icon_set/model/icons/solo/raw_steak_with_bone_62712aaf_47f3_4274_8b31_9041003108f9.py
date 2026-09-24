"""steak. Revision: Enlarge the bone opening, smooth the irregular steak outline and keep an even depth band. Omit marbling.
Construction: Lucide beef: irregular steak outline with circular bone and curved depth band. Preserve source-facing direction and arrangement.
Keyshape SQUARE; exact contract extremes, stroke four. No validation exceptions.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '62712aaf-47f3-4274-8b31-9041003108f9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/steak_62712aaf-47f3-4274-8b31-9041003108f9.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='raw-steak-with-bone'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('steak',)

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

        path('top',(6,29),[('C',(16,17),(6,23),(13,22)),('C',(29,6),(18,9),(23,6)),('C',(42,20),(38,6),(42,12)),('C',(27,33),(42,27),(35,31)),('C',(6,29),(18,36),(9,34))],True)
        path('side',(6,29),[('C',(24,42),(6,40),(15,42)),('C',(42,20),(36,42),(42,32))])
        circle('bone',29,19,4)

        # Declare actual shared endpoints only; no proximity-based exemptions.
        for i,a in enumerate(self.primitives):
            if not hasattr(a,'start'):continue
            for b in self.primitives[i+1:]:
                if hasattr(b,'start') and {a.start,a.end}&{b.start,b.end}:
                    self.relate('connect',a.element_id,b.element_id)

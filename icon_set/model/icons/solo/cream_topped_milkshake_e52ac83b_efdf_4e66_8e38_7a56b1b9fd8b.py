'Cream Topped Milkshake.\nSymbol plan: A tapered milkshake cup holds a high swirl of whipped cream above its flat rim. A bent straw rises at the right, and a wavy liquid line crosses the cup.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: Flatten liquid line; retain the whipped peak and bent straw.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e52ac83b-efdf-4e66-8e38-7a56b1b9fd8b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bubble tea wipcream_e52ac83b-efdf-4e66-8e38-7a56b1b9fd8b.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'cream-topped-milkshake'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('milkshake', 'cream', 'cup', 'straw', 'drink', 'dessert', 'beverage')
    def build(self):


        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry,sweep=s)
        def bez(n,a,*s): self.add_bezier(n,a,*s)
        def con(n,*p,closed=False):
            self.contours[:] = [c for c in self.contours if not set(c.members)&set(p)]
            self.add_contour(n,*p,closed=closed)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            con(n,n+'a',n+'b',closed=True)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            ps=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
            for j in range(8):
                if j%2: arc(n+str(j),ps[j],ps[(j+1)%8],r)
                else: line(n+str(j),ps[j],ps[(j+1)%8])
            con(n,*(n+str(j) for j in range(8)),closed=True)
        poly('cup',(8,24),(12,44),(36,44),(40,24),(8,24))
        bez('cream',(12,24),((12,12),(24,16),(24,4)),((32,8),(34,16),(34,24)))
        poly('straw',(34,24),(40,8),(40,4))
        line('liquid',(10,32),(38,32))
        self.relate('connect','cup','cream');self.relate('connect','straw','cream');self.relate('connect','straw','cup');self.relate('connect','liquid','cup')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

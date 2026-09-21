# Final reduction: Four ticks replace five to maintain 8-unit centerline spacing.
'Plain Ruler with Five Short Ticks.\nSymbol plan: A horizontal rectangular ruler has a straight outline and five short upright tick marks spaced along its upper interior. The remaining surface is blank, with no visible numbers or labels.\nConstruction: Lucide ruler: one enclosing contour with a regular tick series.\nReduction: Retain the source parts and arrangement.\nKeyshape HRECT_M: ink extremes (2, 8, 46, 40).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4f0fb3b4-1180-4752-8068-66bf7a72b105'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/millimeter_4f0fb3b4-1180-4752-8068-66bf7a72b105.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'plain-ruler-with-four-short-ticks'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('ruler', 'measurement', 'ticks', 'scale', 'tool', 'length', 'rectangle')
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
        rect('ruler',4,10,40,28)
        for i,x in enumerate((12,20,28,36)): line('tick'+str(i),(x,18),(x,24))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

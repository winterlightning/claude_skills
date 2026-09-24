'Looped Treble Clef.\nSymbol plan: A treble clef has a tall upright stem looping at the top and curling at the bottom. A broad central spiral crosses the stem and ends inward.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One continuous treble-clef line retains the tall loop and central spiral.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0bb5de88-a86b-409b-a1eb-82ac6ee78932'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clef_0bb5de88-a86b-409b-a1eb-82ac6ee78932.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'looped-treble-clef-0bb5de88'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('treble', 'clef', 'music', 'symbol', 'notation', 'spiral', 'staff')
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
        # Three coherent gestures: upper loop, descending stem, and open central spiral.
        arc('loop-left',(24,20),(24,4),6,8)
        arc('loop-right',(24,4),(24,20),6,8)
        con('upper-loop','loop-left','loop-right',closed=True)
        bez('stem',(24,20),((24,25),(30,33),(30,38)),((30,44),(22,44),(18,44)),((14,44),(12,41),(12,38)))
        bez('spiral',(24,20),((8,22),(8,26),(8,30)),((8,32),(40,34),(40,24)))
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

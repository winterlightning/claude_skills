'Arched Mine Entrance with Forward Tracks.\nSymbol plan: A mine entrance has a broad horizontal lintel above two thick side supports and a rounded arch. Two rails spread toward the foreground, crossed by short horizontal sleepers beneath the opening.\nConstruction: No useful exact Lucide match; coherent contours and shared parameters.\nReduction: One broad track sleeper replaces closely spaced repetitions.\nKeyshape SQUARE: ink extremes (4, 4, 44, 44).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0fd69e68-9ff9-4d73-b98d-a511b3470bfb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mineshaft_0fd69e68-9ff9-4d73-b98d-a511b3470bfb.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'arched-mine-entrance-with-forward-tracks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('mine', 'entrance', 'tracks', 'rails', 'arch', 'tunnel', 'mining')
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
        rect('lintel',6,6,36,8)
        poly('left-post',(10,14),(10,34),(18,34),(18,30))
        arc('arch',(18,30),(30,30),6)
        poly('right-post',(30,30),(30,34),(38,34),(38,14))
        con('entrance','left-post-1','left-post-2','left-post-3','arch','right-post-1','right-post-2','right-post-3')
        poly('rail-left',(18,34),(14,42));poly('rail-right',(30,34),(34,42));line('sleeper',(14,42),(34,42))
        self.relate('connect','lintel','entrance');self.relate('connect','sleeper','rail-left');self.relate('connect','sleeper','rail-right')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

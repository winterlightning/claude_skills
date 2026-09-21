# Final reduction: Single broad visor rule; omit small eye cutout and vents to preserve clearance.
'Knight with Closed Visor.\nSymbol plan: A front-facing knight wears a domed helmet with a small plume above a broad visor. A narrow eye opening crosses the faceplate, with three vertical vents below and rounded shoulders beneath.\nConstruction: human_ref/user.svg: broad smooth shoulder silhouette.\nReduction: Reduce visor vents and plume detail.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7c142919-17a3-41f7-8e72-c4a49761d7ba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paladin_7c142919-17a3-41f7-8e72-c4a49761d7ba.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'knight-closed-visor'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('knight', 'helmet', 'visor', 'armor', 'medieval', 'bust')
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
        arc('helmet-top',(12,20),(36,20),12,12)
        line('brow',(12,20),(36,20))
        arc('jaw',(36,20),(12,20),12,14)
        con('helmet','helmet-top','jaw',closed=True)
        # Brow itself is the simplified visor; no duplicate overlapping eye stroke.
        bez('shoulders',(8,44),((8,37),(14,34),(20,34)))
        bez('shoulders-right',(28,34),((34,34),(40,37),(40,44)))
        line('bottom',(8,44),(40,44))
        line('plume',(24,4),(24,8))
        self.relate('connect','brow','helmet');self.relate('connect','plume','helmet');self.relate('connect','shoulders','helmet');self.relate('connect','shoulders-right','helmet')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

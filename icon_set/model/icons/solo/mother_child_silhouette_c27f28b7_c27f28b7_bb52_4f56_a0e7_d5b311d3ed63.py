'Mother with Child Silhouette.\nSymbol plan: A large figure has an oval head with short outward-curving hair above a broad flared body. A small stick-figure child stands centered within the body, with outstretched arms and spread legs.\nConstruction: human_ref/full_body_ref.png: circular heads and broad parent silhouette.\nReduction: Child arms retained; short lower torso must remain legible.\nKeyshape VRECT_L: ink extremes (6, 2, 42, 46).'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c27f28b7-bb52-4f56-a0e7-d5b311d3ed63'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/primitive symbols mother_c27f28b7-bb52-4f56-a0e7-d5b311d3ed63.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'mother-child-silhouette-c27f28b7'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('mother', 'child', 'family', 'figures', 'parent', 'people')
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
        circle('mother-head',24,8,4)
        bez('mother-body',(8,44),((8,27),(10,20),(24,20)),((38,20),(40,27),(40,44)))
        circle('child-head',24,31,2)
        line('child-torso',(24,41),(24,42))
        line('child-arms',(18,41),(30,41))
        poly('child-legs',(21,44),(24,42),(27,44))
        self.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
        # Only genuine shared endpoints are automatically declared as contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

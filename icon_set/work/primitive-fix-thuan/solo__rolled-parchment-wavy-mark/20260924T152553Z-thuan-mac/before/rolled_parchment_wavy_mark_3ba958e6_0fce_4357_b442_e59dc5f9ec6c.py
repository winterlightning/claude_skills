'Rolled Parchment with Wavy Mark.\nSymbol plan: An upright parchment sheet curls backward at its upper left and forward across the bottom. A short wavy mark sits in the otherwise blank center, between the long straight sides of the scroll.\nConstruction: Lucide scroll: rolled ends and long sheet edges.\nReduction: One short center mark replaces the fine wave.\nKeyshape VRECT_L.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3ba958e6-0fce-4357-b442-e59dc5f9ec6c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/parchment_3ba958e6-0fce-4357-b442-e59dc5f9ec6c.svg'
AUTHOR = 'gpt-6'

class BatchIcon(Solo48):
    icon_id = 'rolled-parchment-wavy-mark'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/reference"
    aliases = ()
    keywords = ('parchment', 'scroll', 'paper', 'rolled', 'document', 'manuscript')
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
        arc('top',(8,8),(16,8),4,s=True);line('top-edge',(12,4),(36,4));poly('sheet',(36,4),(36,36),(40,36),(40,40));arc('bottom-roll',(40,40),(32,40),4)
        line('bottom',(36,44),(16,44));arc('left-bottom',(16,44),(12,40),4);line('left',(12,40),(12,20));line('roll-lip',(8,8),(8,20));line('lip',(8,20),(16,20));line('return',(16,20),(16,8));line('mark',(22,26),(28,26))
        self.relate('connect','top-edge','top');self.relate('connect','left','lip');self.relate('connect','bottom','bottom-roll')
        # Declare only real, shared endpoints as automatic contacts.
        for i,a in enumerate(self.primitives):
            for b in self.primitives[i+1:]:
                if {a.start,a.end}&{b.start,b.end}: self.relate('connect',a.element_id,b.element_id)

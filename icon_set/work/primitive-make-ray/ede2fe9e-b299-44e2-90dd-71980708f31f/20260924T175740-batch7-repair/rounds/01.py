from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'ede2fe9e-b299-44e2-90dd-71980708f31f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/people conflict 1_ede2fe9e-b299-44e2-90dd-71980708f31f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """Two heads facing away with conflict sparks overhead.
    Plan: Mirror-related continuous head/neck profiles; three separate lightning strokes.
    Reference: No useful Lucide match; the source defines paired continuous profile silhouettes.
    """
    icon_id = 'people-conflict-1'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('people', 'conflict', '1')
    # Shared human_ref/user.svg reviewed for head scale. Continuous head/neck silhouettes have no detached head-body gap.

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rounded(self,n,l,t,r,b,k=4):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        members=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];name=f'{n}-{i}';members.append(name)
            if i%2:self.add_arc(name,p,q,radius_x=k)
            else:self.add_line(name,p,q)
        self.add_contour(n,*members,closed=True)

    def dollar(self):
        self.add_line('s-top',(29,16),(24,16))
        self.add_arc('s-left',(24,16),(24,24),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,24),(24,32),radius_x=4)
        self.add_line('s-bottom',(24,32),(19,32))
        self.add_contour('dollar','s-top','s-left','s-right','s-bottom')
        self.add_line('stem-top',(24,12),(24,16));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,32),(24,36));self.relate('connect','stem-bottom','dollar')

    def bust(self,n,x,y,r,width,body_y,body_ry):
        # Detached head bottom = y+r; shoulder apex = body_y-body_ry.
        # Author parameters require their difference to be exactly eight.
        self.circle(n+'-head',x,y,r)
        self.add_arc(n+'-shoulders',(x-width,body_y),(x+width,body_y),radius_x=width,radius_y=body_ry)

    def build(self):

        for i,cx in enumerate((13,35)):
            self.add_arc(f'skull-{i}',(cx-7,30),(cx+7,30),radius_x=7)
        self.add_polyline('left-front',(6,30),(4,34),(8,34),(8,38),(14,38),(14,40))
        self.add_line('left-back',(20,30),(20,40))
        self.add_polyline('right-front',(42,30),(44,34),(40,34),(40,38),(34,38),(34,40))
        self.add_line('right-back',(28,30),(28,40))
        for a,b in [('skull-0','left-front'),('skull-0','left-back'),('skull-1','right-front'),('skull-1','right-back')]:self.relate('connect',a,b)
        for i,x in enumerate((8,24,40)):self.add_polyline(f'spark-{i}',(x-3,8),(x+3,11),(x-1,14))

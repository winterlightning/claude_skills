"""Hand holding a tablet showing an upward trend arrow.
Plan: SQUARE fits tablet, hand and chart arrow.
Reduction: Three small bars omitted; the defining trend arrow remains. Hand and thumb spacing rebalanced.
Construction: tablet: coherent device boundary; trending-up: rising arrow. Intentional right-hand occlusion.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '2db6cf72-5f8c-42a8-a787-67d6ad07a91f'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_30/performance tablet increase_2db6cf72-5f8c-42a8-a787-67d6ad07a91f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'performance-tablet-increase'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('performance', 'tablet', 'increase')
    # Shared human_ref/user.svg reviewed; this is a hand and does not have a head/body gap.

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
        # Tablet and hand share exact occlusion nodes; the rising arrow is the chart's dominant mark.
        self.add_polyline('tablet',(24,42),(6,42),(6,6),(34,6),(34,20),(34,26))
        self.add_line('trend',(14,26),(26,14))
        self.add_polyline('arrow',(18,14),(26,14),(26,21));self.relate('connect','trend','arrow')
        self.add_polyline('hand',(34,20),(40,28),(40,34),(42,42));self.relate('connect','hand','tablet')
        self.add_arc('thumb-top',(30,30),(34,26),radius_x=4)
        self.add_polyline('thumb',(30,30),(32,36),(32,40),(34,42));self.relate('connect','thumb','thumb-top');self.relate('connect','thumb-top','tablet')

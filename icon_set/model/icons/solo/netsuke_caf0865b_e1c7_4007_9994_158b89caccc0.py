"""netsuke: standalone SOLO48 repair.
Plan: Round-headed netsuke figure with looping arms.
Keyshape: VRECT_M; shared dimensions and nodes own repeated elements.
Reduction: Enlarged arm loop into a circle and reduced head size; simplified the crossed-hand contours.
Lucide originals and atomic-debug construction reference: none.
human_ref/user.svg and full_body_ref.png: touching bust construction, circular head centered (24,9), radius 5, bottom y=14; shoulder crest y=18 gives exactly 4 centerline units and zero ink gap. Scoped actual touching relationship retained; detached-head rule does not apply.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='caf0865b-e1c7-4007-9994-158b89caccc0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/netsuke_caf0865b-e1c7-4007-9994-158b89caccc0.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='netsuke'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('netsuke',)
    human_construction='bust'

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):

        self.circle('head',24,9,5)
        self.add_arc('shoulders',(10,32),(38,32),radius_x=14,radius_y=14)
        self.add_line('right-side',(38,32),(38,40));self.add_arc('right-bottom',(38,40),(34,44),radius_x=4)
        self.add_line('right-base',(34,44),(28,44))
        self.add_contour('right-body','shoulders','right-side','right-bottom','right-base')
        self.add_line('left-side',(10,32),(10,40));self.add_arc('left-bottom',(10,40),(14,44),radius_x=4,sweep=False)
        self.add_contour('left-body','left-side','left-bottom');self.relate('connect','right-body','left-body')
        self.relate('connect','head','right-body')
        self.circle('hand-loop',24,31,4)
        self.add_bezier('arms',(14,44),((20,44),(20,35),(24,35)))
        self.relate('connect','arms','left-body')
        self.relate('connect','arms','hand-loop')


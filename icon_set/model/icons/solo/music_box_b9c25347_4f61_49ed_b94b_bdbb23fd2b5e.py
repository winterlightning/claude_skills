"""music box: standalone SOLO48 repair.
Plan: Box and crank below a shared pair of music notes.
Keyshape: SQUARE; shared dimensions and nodes own repeated elements.
Reduction: Removed the second beam and lid divider to open the note spacing.
Lucide originals and atomic-debug construction reference: music.

"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='b9c25347-4f61-49ed-b94b-bdbb23fd2b5e'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/music box_b9c25347-4f61-49ed-b94b-bdbb23fd2b5e.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='music-box'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    aliases=()
    keywords=('music', 'box')

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

        self.add_polyline('box',(6,34),(34,34),(34,38),(34,42),(6,42),closed=True)
        self.add_polyline('crank',(34,38),(42,38),(42,28))
        self.relate('connect','box','crank')
        self.circle('note-left',16,22,3);self.circle('note-right',32,22,3)
        self.add_polyline('beam',(19,22),(19,6),(35,6),(35,22))
        self.relate('connect','beam','note-left')
        self.relate('connect','beam','note-right')


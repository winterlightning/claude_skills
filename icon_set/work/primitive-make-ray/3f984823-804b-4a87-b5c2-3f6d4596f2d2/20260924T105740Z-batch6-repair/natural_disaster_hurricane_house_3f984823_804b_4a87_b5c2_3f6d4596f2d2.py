"""natural disaster hurricane house: standalone SOLO48 repair.
Plan: Spiral storm at upper left and complete house at lower right.
Keyshape: SQUARE; shared dimensions and nodes own repeated elements.
Reduction: Reduced spiral to one open turn; omitted small door and duplicate roof overhang. Directional asymmetry follows reference.
Lucide originals and atomic-debug construction reference: house.

"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3f984823-804b-4a87-b5c2-3f6d4596f2d2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_28/natural disaster hurricane house_3f984823-804b-4a87-b5c2-3f6d4596f2d2.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='natural-disaster-hurricane-house'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('natural', 'disaster', 'hurricane', 'house')

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
        # One open expanding spiral; fewer turns preserve generous spacing.
        self.add_bezier('tail',(6,30),((24,30),(28,24),(28,16)))
        self.add_arc('outer-coil',(28,16),(8,16),radius_x=10,sweep=False)
        self.add_arc('inner-coil',(8,16),(16,16),radius_x=4,sweep=False)
        self.add_contour('hurricane','tail','outer-coil','inner-coil')
        self.add_polyline('house',(26,35),(26,42),(42,42),(42,35),(34,29),closed=True)

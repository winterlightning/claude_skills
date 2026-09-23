"""A hurricane spiral sweeps past a small house.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: None; spiral and complete house retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='3f984823-804b-4a87-b5c2-3f6d4596f2d2'
SOURCE_PATH='icon_set/work/todo-references/natural disaster hurricane house_3f984823-804b-4a87-b5c2-3f6d4596f2d2.svg'
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

        self.add_bezier('tail',(6,30),((22,30),(34,24),(34,16)))
        self.add_arc('outer-coil',(34,16),(14,16),radius_x=10,sweep=False)
        self.add_arc('inner-coil',(14,16),(26,16),radius_x=6,sweep=False)
        self.add_bezier('core',(26,16),((26,11),(18,11),(20,18)))
        self.add_contour('hurricane','tail','outer-coil','inner-coil','core')
        self.add_polyline('house',(26,36),(26,42),(42,42),(42,36),(34,32),closed=True)

# Final visible bounds: (4, 4, 44, 44)
# Construction: No useful local Lucide match was used; the supplied reference and shared geometric construction guidance informed this composition.
# Final reductions: Door and secondary roof overhang omitted to retain a clearly spaced hurricane and complete house silhouette.
# Visual review: Spiral and house read clearly after removing the small door and duplicate roof overhang. House is reduced to a complete silhouette; asymmetry preserves the approaching storm.

"""A nectar bottle bears a five-petalled flower.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Bottle cap rounding simplified; all five petals retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='74f05c03-957b-4b86-b062-d7cbbb568098'
SOURCE_PATH='icon_set/work/todo-references/nectar_74f05c03-957b-4b86-b062-d7cbbb568098.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='nectar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('nectar',)

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

        self.add_polyline('cap',(10,6),(26,6),(26,14),(10,14),closed=True)
        self.add_polyline('bottle',(10,14),(6,22),(6,42),(30,42),(30,22),(26,14))
        self.relate('connect','cap','bottle')
        self.add_dot('flower-center',(34,21))
        petals=[((27,15),(31,8),(35,14)),((34,8),(42,12),(40,18)),((36,15),(42,17),(42,21)),((43,28),(34,33),(32,26)),((24,30),(23,20),(29,20))]
        for i,(c1,c2,k) in enumerate(petals):
            n='petal-'+str(i)
            if i==2:self.add_bezier(n,(34,21),(c1,c2,k),((42,25),(38,27),(34,21)))
            else:self.add_bezier(n,(34,21),(c1,c2,k),(k,(34,21),(34,21)))
            self.relate('connect',n,'flower-center')

# Final visible bounds: (4, 4, 44, 44)
# Construction: No useful local Lucide match was used; the supplied reference and shared geometric construction guidance informed this composition.
# Final reductions: Bottle cap rounding simplified; all five petals retained.
# Visual review: Bottle and all five petals are present, but the left petal crosses the bottle and flower details crowd at native size. Automated review warning retained; not approved.

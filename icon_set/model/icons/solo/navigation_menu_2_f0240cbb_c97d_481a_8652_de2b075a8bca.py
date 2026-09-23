"""Three rounded horizontal menu bars decrease in length.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 VRECT_L; omissions: Arrangement made taller so all three hollow bars keep eight-unit spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='f0240cbb-c97d-481a-8652-de2b075a8bca'
SOURCE_PATH='icon_set/work/todo-references/navigation menu 2_f0240cbb-c97d-481a-8652-de2b075a8bca.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='navigation-menu-2'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('navigation', 'menu', '2')

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

        for n,y,w in [('top',4,32),('middle',20,24),('bottom',36,16)]:self.box(n,8,y,w,8,4)

# Final visible bounds: (6, 2, 42, 46)
# Construction: No useful local Lucide match was used; the supplied reference and shared geometric construction guidance informed this composition.
# Final reductions: Arrangement made taller so all three hollow bars keep eight-unit spacing.
# Visual review: Three hollow rounded bars remain distinct. Composition is taller than the source to preserve minimum spacing. Repeated bars use equal height8 and corner radius4.

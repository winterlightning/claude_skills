"""The Next.js N mark sits within a circle with its diagonal extending to the rim.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 CIRCLE; omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='1a66325c-742a-4e29-a0c9-efc19aef9e9c'
SOURCE_PATH='icon_set/work/todo-references/nextjs logo_1a66325c-742a-4e29-a0c9-efc19aef9e9c.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='nextjs-logo'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'Uncategorized'
    aliases=()
    keywords=('nextjs', 'logo')

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

        self.add_arc('ring-a',(12,8),(36,40),radius_x=20);self.add_arc('ring-b',(36,40),(12,8),radius_x=20)
        self.add_contour('ring','ring-a','ring-b',closed=True)
        self.add_polyline('n',(16,32),(16,16),(28,30),(36,40))
        self.add_line('n-right',(28,16),(28,30));self.relate('connect','n','n-right');self.relate('connect','ring','n')

# Final visible bounds: (2, 2, 46, 46)
# Construction: No useful local Lucide match was used; the supplied reference and shared geometric construction guidance informed this composition.
# Final reductions: None.
# Visual review: N and circular border read clearly. Diagonal extends to the rim at an exact shared node; intentional asymmetry retains the logo.

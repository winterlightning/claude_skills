"""A hooded necromancer has a featureless skull-like face and robe.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 VRECT_L; omissions: Small jaw corners simplified; faceless hooded composition retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='253b2d2a-0938-4224-b01e-f0cf978b4d22'
SOURCE_PATH='icon_set/work/todo-references/necromancer_253b2d2a-0938-4224-b01e-f0cf978b4d22.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='necromancer'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('necromancer',)

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

        self.add_bezier('hood-left',(24,4),((13,4),(7,16),(12,30)))
        self.add_line('hood-bottom-1',(12,30),(24,36))
        self.add_line('hood-bottom-2',(24,36),(36,30))
        self.add_bezier('hood-right',(36,30),((41,16),(35,4),(24,4)))
        self.add_contour('hood','hood-left','hood-bottom-1','hood-bottom-2','hood-right',closed=True)
        # Hood opening: circular crown with a short squared jaw, not a detached stick head.
        self.add_arc('face-crown',(19,18),(29,18),radius_x=5)
        self.add_bezier('face-right',(29,18),((29,21),(28,21),(28,22)))
        self.add_line('jaw-right',(28,22),(28,24))
        self.add_line('jaw-base',(28,24),(20,24))
        self.add_line('jaw-left',(20,24),(20,22))
        self.add_bezier('face-left',(20,22),((20,21),(19,21),(19,18)))
        self.add_contour('face','face-crown','face-right','jaw-right','jaw-base','jaw-left','face-left',closed=True)
        self.add_bezier('robe-left',(8,44),((8,36),(8,32),(12,30)))
        self.add_bezier('robe-right',(36,30),((40,32),(40,36),(40,44)))
        self.add_line('robe-seam',(24,36),(24,44))
        self.relate('connect','hood','robe-left');self.relate('connect','hood','robe-right');self.relate('connect','hood','robe-seam')

# Final visible bounds: (6, 2, 42, 46)
# Construction: Shared human references supplied round heads, broad shoulders and coherent pose construction. Analytical head/body spacing is recorded in the visual review.
# Final reductions: Hood opening uses a circular crown and abbreviated squared jaw; no facial features added.
# Visual review: Widened hood and small circular-crown/squared-jaw face opening preserve the hooded figure. The face is an opening within an integrated hood, not a detached stick-figure head. Jaw and robe are simplified. Visual meaning remains a generic hooded figure.

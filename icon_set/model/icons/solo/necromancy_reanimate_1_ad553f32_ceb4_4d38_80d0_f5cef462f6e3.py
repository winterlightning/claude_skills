"""Crossed magic strokes float above a skull.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Skull jaw fillets simplified; eyes and two tooth divisions retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ad553f32-ceb4-4d38-80d0-f5cef462f6e3'
SOURCE_PATH='icon_set/work/todo-references/necromancy reanimate 1_ad553f32-ceb4-4d38-80d0-f5cef462f6e3.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='necromancy-reanimate-1'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('necromancy', 'reanimate', '1')

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
        self.add_polyline('magic-one',(6,6),(24,9),(42,12))
        self.add_polyline('magic-two',(6,12),(24,9),(42,6))
        self.relate('connect','magic-one','magic-two')
        self.add_arc('skull-top',(11,31),(37,31),radius_x=13)
        self.add_polyline('jaw',(37,31),(37,34),(32,36),(32,42),(24,42),(16,42),(16,36),(11,34),(11,31))
        self.relate('connect','skull-top','jaw')
        self.add_dot('eye-left',(20,29));self.add_dot('eye-right',(28,29))
        self.add_line('tooth',(24,38),(24,42));self.relate('connect','tooth','jaw')

# Final visible bounds: (4, 4, 44, 44)
# Construction: Rounded cranium, paired eye marks and minimal jaw/teeth construction.
# Final reductions: Eye outlines reduced to solid circular marks and two tooth divisions reduced to one to open the skull interior.
# Visual review: Skull and crossed magic strokes are clear. Eyes reduced to solid dots and tooth divisions to one; skull remains symmetric.

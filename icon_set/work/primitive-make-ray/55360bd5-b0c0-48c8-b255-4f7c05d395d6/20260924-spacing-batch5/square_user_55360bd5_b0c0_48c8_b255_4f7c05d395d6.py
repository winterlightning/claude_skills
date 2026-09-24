"""square user. Rounded frame, circular head and open smooth shoulders. Removed shoulder baseline. Head bottom21 to shoulders29 gives exact 4 ink gap; frame clearance9.
Symbol plan: shared circle/rounded-frame parameters; meaningful joints reuse endpoints.
Reference: supplied SVG; Lucide shopping-basket and square-user construction inspected.
Human construction uses human_ref/user.svg where applicable.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='55360bd5-b0c0-48c8-b255-4f7c05d395d6'
SOURCE_PATH='pictographic-primitives/_uncategorized_36/square user_55360bd5-b0c0-48c8-b255-4f7c05d395d6.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='square-user'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('square user',)
    def build(self):
        self.box('frame',6,6,42,42,4)
        self.circle('head',24,18,3)
        self.add_arc('torso',(24,29),(15,33),radius_x=9,radius_y=4,sweep=False)
        self.add_arc('shoulder-right',(33,33),(24,29),radius_x=9,radius_y=4,sweep=False)
        self.add_contour('shoulders','shoulder-right','torso')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

    def circle(self,n,x,y,r):
        pts=[(x-r,y),(x,y-r),(x+r,y),(x,y+r),(x-r,y)]
        for i in range(4): self.add_arc(f'{n}-{i}',pts[i],pts[i+1],radius_x=r)
        self.add_contour(n,*(f'{n}-{i}' for i in range(4)),closed=True)
    def box(self,n,l,t,r,b,q=4):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        for i in range(8):
            if i%2:self.add_arc(f'{n}-{i}',pts[i],pts[(i+1)%8],radius_x=q)
            else:self.add_line(f'{n}-{i}',pts[i],pts[(i+1)%8])
        self.add_contour(n,*(f'{n}-{i}' for i in range(8)),closed=True)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i):self.relate('connect',f'{n}-{i}',f'{n}-{j}')

# Contract keyshape visible bounds: (4, 4, 44, 44).

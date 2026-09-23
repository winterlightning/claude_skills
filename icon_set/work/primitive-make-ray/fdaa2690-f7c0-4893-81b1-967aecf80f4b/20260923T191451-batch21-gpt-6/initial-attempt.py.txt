"""Two sperm cells and a detached oval are shown in a circular laboratory view.
Construction reference: none.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'fdaa2690-f7c0-4893-81b1-967aecf80f4b'
SOURCE_PATH = 'icon_set/work/todo-references/laboratory sperm_fdaa2690-f7c0-4893-81b1-967aecf80f4b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'laboratory-sperm'
    keyshape = Keyshape.CIRCLE
    # Visible ink extremes: (2, 2, 46, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('laboratory', 'sperm')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: round observation field; diagonal ovals and flowing tails inside.
        self.circle('field',24,24,20)
        self.add_bezier('head-left',(16,19),((12,17),(17,10),(20,12)),((24,14),(20,21),(16,19)))
        self.add_bezier('tail-left',(16,19),((11,21),(16,26),(11,29)))
        self.add_bezier('head-right',(30,24),((26,22),(31,15),(34,17)),((38,19),(34,26),(30,24)))
        self.add_bezier('tail-right',(30,24),((25,28),(32,30),(26,35)))
        self.add_bezier('oval',(17,35),((13,33),(18,28),(20,30)),((23,32),(20,37),(17,35)))
        self.relate('connect','head-left','tail-left')
        self.relate('connect','head-right','tail-right')

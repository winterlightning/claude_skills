"""Remove both ears. A continuous rounded cheek and jaw outline connects directly to the original bow, retaining the eyes and smile.
Reference: Existing baby face with bow; shared rounded human face vocabulary
Authored directly on SOLO48, with prior revision preserved."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '724c83b9-dfbc-417a-b236-a8b1fd9f3b71'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__baby-face-with-bow/20260926T073831Z-thuan-mac/reference/baby girl_724c83b9-dfbc-417a-b236-a8b1fd9f3b71.svg'
AUTHOR = 'claude-opus-5-5'

class BabyFaceWithBow(Solo48):
    icon_id = 'baby-face-with-bow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'babies'
    categories = ('babies', 'state')
    aliases = ()
    keywords = ('baby', 'face', 'with', 'bow')

    def build(self):
        # Symbol plan: Remove both ears. A continuous rounded cheek and jaw outline connects directly to the original bow, retaining the eyes and smile.

        def path(n,start,commands,closed=False):
            here=start;members=[]
            for j,c in enumerate(commands):
                kind,end,*a=c;ident=f'{n}-{j}'
                if kind=='L':self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        # Revision per review: the face is a full circle (r15 about (24, 29)) and a bow sits on top
        # of the head - two closed loops (ellipses rx 8, ry 3 about (16, 7) and (32, 7)) tied at
        # (24, 7) and joined to the crown (24, 14) by a short knot. Dot eyes (19, 26)/(29, 26) and a
        # small smile (22, 34)-(26, 34) keep 8+ from each other and from the face.
        circle('face', 24, 29, 15)
        self.add_arc('bow-left-top', (8, 7), (24, 7), radius_x=8, radius_y=3)
        self.add_arc('bow-left-bottom', (24, 7), (8, 7), radius_x=8, radius_y=3)
        self.add_contour('bow-left', 'bow-left-top', 'bow-left-bottom', closed=True)
        self.add_arc('bow-right-top', (24, 7), (40, 7), radius_x=8, radius_y=3)
        self.add_arc('bow-right-bottom', (40, 7), (24, 7), radius_x=8, radius_y=3)
        self.add_contour('bow-right', 'bow-right-top', 'bow-right-bottom', closed=True)
        line('knot', (24, 7), (24, 14))
        join('bow-left', 'bow-right'); join('bow-left', 'knot'); join('bow-right', 'knot'); join('knot', 'face')
        dot('eye-left', (19, 26)); dot('eye-right', (29, 26))
        self.add_arc('smile', (22, 34), (26, 34), radius_x=2, radius_y=1, sweep=False)

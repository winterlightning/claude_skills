"""Two mirrored open pages with a central fold and short text lines; shared centre keeps page angles equal."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '710c81fd-6fdd-45a1-b7ed-cc8825ddf0d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__book-open-710c81fd/20260925T060624Z-thuan-mac/reference/book open_710c81fd-6fdd-45a1-b7ed-cc8825ddf0d9.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'book-open-710c81fd'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('book open',)

    def build(self):
        # Plan: Two mirrored open pages with a central fold and short text lines; shared centre keeps page angles equal.
        # Construction reference: book-open: matched page contours around one gutter

        def path(name, start, commands, closed=False):
            members=[]; here=start
            for index, command in enumerate(commands):
                ident=f'{name}-{index}'; kind,end,*args=command
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            path(name,(cx-r,cy),[('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        poly('outline',(4,8),(24,14),(44,8),(44,34),(24,40),(4,34),closed=True)
        line('gutter',(24,14),(24,40));join('gutter','outline')
        for n,x,s in [('left',13,1),('right',35,-1)]:
         line('text-'+n,(x,23),(x+s*3,24))

"""Flat rounded parcel with an attached rectangular tape tab, preserving the unbroken top edge."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '25bec113-9501-56df-8f1c-88dce76cb03d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__box-25bec113/20260925T060624Z-thuan-mac/reference/box_25bec113-9501-56df-8f1c-88dce76cb03d.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'box-25bec113'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('box',)

    def build(self):
        # Plan: Flat rounded parcel with an attached rectangular tape tab, preserving the unbroken top edge.
        # Construction reference: package: attached seam construction; front-view reference retained

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

        rounded('box',6,6,42,42,4)
        poly('tape',(18,6),(18,18),(30,18),(30,6));join('tape','box')

"""Closed book with a clean front cover and curved lower page block; no invented vertical spine stripe."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '3591871b-5aae-4c39-9571-b421f21c9a22'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__book-close-1/20260925T060624Z-thuan-mac/reference/book close 1_3591871b-5aae-4c39-9571-b421f21c9a22.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'book-close-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('book close 1',)

    def build(self):
        # Plan: Closed book with a clean front cover and curved lower page block; no invented vertical spine stripe.
        # Construction reference: book: rounded bound edge and lower page block

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

        path('cover',(8,38),[('L',(8,10)),('A',(14,4),6,6,True),('L',(40,4)),('L',(40,32)),('L',(14,32)),('A',(8,38),6,6,False)])
        path('pages',(8,38),[('A',(14,44),6,6,False),('L',(40,44)),('C',(40,32),(38,40),(38,36))]);join('cover','pages')

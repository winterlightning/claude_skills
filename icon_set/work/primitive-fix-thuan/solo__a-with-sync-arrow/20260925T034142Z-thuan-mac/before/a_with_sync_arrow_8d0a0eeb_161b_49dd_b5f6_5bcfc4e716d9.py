"""a-with-sync-arrow: Capital A inside two opposed smooth sync arcs; the A has straight symmetric legs and a horizontal crossbar, with equal paired arrow wings.
Lucide construction: refresh-cw; original and atomic-debug inspected.
Omissions: Arrowhead wings kept compact to preserve the central A.
Keyshape SQUARE: exact contract envelope; 4-unit stroke.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__a-with-sync-arrow/20260924T172457Z-thuan-mac/reference/a with sync arrow_8d0a0eeb-161b-49dd-b5f6-5bcfc4e716d9.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'a-with-sync-arrow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('a', 'with', 'sync', 'arrow')
    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,start,end)
                elif kind=='A': self.add_arc(ident,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,start,(args[0],args[1],end))
                members.append(ident);start=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx,cy-ry),[('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True),('A',(cx,cy-ry),rx,ry,True)],True)
        def rect(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('upper',(6,19),[('A',(42,19),18,13,True)])
        poly('upper-head',(39,16),(42,19),(42,13));join('upper','upper-head')
        path('lower',(42,29),[('A',(6,29),18,13,True)])
        poly('lower-head',(9,32),(6,29),(6,35));join('lower','lower-head')
        poly('letter',(17,31),(18,29),(24,17),(30,29),(31,31));line('bar',(18,29),(30,29));join('bar','letter')

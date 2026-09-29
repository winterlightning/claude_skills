"""Restore four equal circular vector nodes and three distinct spokes with deliberate node-edge attachments.
Plan: Preserve the reference arrangement; own continuous contours, repeated dimensions and real joins.
Before: The anchor nodes were tall ovals and the diagonal connectors merged into one heavy arrow-like shape.
Construction: spline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'eb962df2-7d7e-4704-b588-8cea12d18d62'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__vectors-add-anchor/20260928T175901Z-thuan-mac/reference/vectors add anchor_eb962df2-7d7e-4704-b588-8cea12d18d62.svg'
AUTHOR = 'gpt-6'

class RevisedIcon(Solo48):
    icon_id = 'vectors-add-anchor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('vectors', 'add', 'anchor')

    def build(self):

        def path(name,start,commands,closed=False):
            members=[]; here=start
            for i,(kind,end,*a) in enumerate(commands):
                if end==here and kind=='L':continue
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A':self.add_arc(ident,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
                elif kind=='C':self.add_bezier(ident,here,(a[0],a[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        L=lambda end:('L',end)
        C=lambda end,c1,c2:('C',end,c1,c2)
        A=lambda end,rx,ry,sweep:('A',end,rx,ry,sweep)
        line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        circle('hub',10,24,4)
        path('upper',(28,14),[A((28,6),4,4,True),A((28,14),4,4,True)],True)
        path('lower',(28,34),[A((28,42),4,4,True),A((28,34),4,4,True)],True)
        circle('right',38,24,4)
        line('horizontal',(14,24),(34,24));join('hub','horizontal');join('right','horizontal')
        line('upper-spoke',(14,24),(28,14));join('hub','upper-spoke');join('upper','upper-spoke');join('horizontal','upper-spoke')
        line('lower-spoke',(14,24),(28,34));join('hub','lower-spoke');join('lower','lower-spoke');join('horizontal','lower-spoke');join('upper-spoke','lower-spoke')

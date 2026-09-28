"""Equal-angle inward chevrons with a clear central gap.
Plan: coherent named contours and repeated dimensions. VRECT_L natural subject envelope.
Construction reference: Lucide chevrons-down-up: paired open angles.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a44a1df3-4ccd-4137-a15d-3cccc3022c7a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__chevron-inward-vertical/20260925T070532Z-thuan-mac/reference/move shrink vertical_a44a1df3-4ccd-4137-a15d-3cccc3022c7a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'chevron-inward-vertical'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('move', 'shrink', 'vertical')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for j,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                here=end;members.append(ident)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad=3):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        axis=24
        for name,edge,tip in [('down',4,20),('up',44,28)]:
            poly(name,(axis-16,edge),(axis,tip),(axis+16,edge))

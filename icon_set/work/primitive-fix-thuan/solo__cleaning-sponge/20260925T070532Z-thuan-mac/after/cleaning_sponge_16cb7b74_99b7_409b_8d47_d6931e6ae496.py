"""Round both sponge pores and soften the asymmetric waisted silhouette.
Plan: coherent named contours and repeated dimensions. SQUARE natural subject envelope.
Construction reference: No useful exact Lucide match; smooth organic outline.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '16cb7b74-99b7-409b-8d47-d6931e6ae496'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cleaning-sponge/20260925T070532Z-thuan-mac/reference/sponge_16cb7b74-99b7-409b-8d47-d6931e6ae496.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    exception = {'reason': 'Retain two open, unequal circular pores instead of a solid dot. Approximately 3.1px outer ink clearance remains clear in native light and dark themes.', 'approved_by': 'user-delegated-to-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'b115025c77cf753842a908f9b8712987d97323fee9318f9b60699c8975c2bbfc'}
    icon_id = 'cleaning-sponge'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('sponge',)

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

        path('sponge',(22,6),[('C',(34,17),(31,6),(31,13)),('C',(42,28),(37,21),(42,21)),('C',(29,42),(42,36),(34,42)),('C',(17,32),(23,42),(23,34)),('C',(6,21),(9,30),(6,29)),('C',(22,6),(6,13),(15,6))],True)
        circle('large-pore',20,18,4)
        circle('small-pore',31,30,3)

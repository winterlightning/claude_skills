"""Top View Lettuce Head."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3ffe86dd-4408-431e-8c39-6faf212715aa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/lettuce top_3ffe86dd-4408-431e-8c39-6faf212715aa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'top-view-lettuce'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('top', 'view', 'lettuce')

    def build(self):
        # Plan: Top-view lettuce with a lobed outer leaf cluster and two large inner folds. Interlacing tiny loops reduced to broad leaf arcs. Natural slight asymmetry retained; Lucide leaf informs smooth contours.
        # Envelope: SQUARE; visible ink (4, 4, 44, 44) on SOLO48.

        def path(name, start, commands, closed=False):
            members=[]
            here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f"{name}-{i}"
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx+rx,cy),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)

        path('head',(24,6),[('C',(34,13),(31,6),(34,8)),('C',(42,24),(42,13),(42,17)),('C',(36,34),(42,30),(40,34)),('C',(24,42),(36,42),(28,42)),('C',(12,34),(20,42),(12,42)),('C',(6,24),(8,34),(6,30)),('C',(14,13),(6,17),(6,13)),('C',(24,6),(14,8),(17,6))],True)
        path('fold-left',(14,13),[('C',(24,32),(20,14),(14,32)),('C',(36,34),(29,32),(32,34))]);join('fold-left','head')
        path('fold-right',(34,13),[('C',(24,32),(28,14),(34,26))]);join('fold-right','head');join('fold-right','fold-left')

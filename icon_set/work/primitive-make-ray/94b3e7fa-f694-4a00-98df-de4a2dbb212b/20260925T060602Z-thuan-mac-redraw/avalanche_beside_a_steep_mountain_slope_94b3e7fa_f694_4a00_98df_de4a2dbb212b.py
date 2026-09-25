"""Steep mountain with curved summit and snow contour, falling snowballs and motion."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '94b3e7fa-f694-4a00-98df-de4a2dbb212b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__avalanche-beside-a-steep-mountain-slope/20260925T060602Z-thuan-mac/reference/avalanche 1_94b3e7fa-f694-4a00-98df-de4a2dbb212b.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'avalanche-beside-a-steep-mountain-slope'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('avalanche 1',)

    def build(self):
        # Symbol plan: Steep mountain with curved summit and snow contour, falling snowballs and motion.
        # Construction reference: Lucide mountain; original supplied subject controls meaning.

        def path(name, start, commands, closed=False):
            ids=[]; here=start
            for i,c in enumerate(commands):
                kind,end,*args=c
                if kind == 'L' and here==end: continue
                eid=f'{name}-{i}'
                if kind=='L': self.add_line(eid,here,end)
                elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
                ids.append(eid);here=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line
        poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
        path('slope',(6,18),[('C',(14,10),(8,4),(10,4)),('L',(20,26)),('L',(26,42))])
        path('snow',(8,32),[('C',(14,28),(10,28),(12,27)),('C',(20,26),(17,30),(18,28))]);join('snow','slope')
        circle('large-snow',36,26,6);circle('small-snow',39,9,3)
        line('motion',(24,6),(26,10))

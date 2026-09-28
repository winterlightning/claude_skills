"""Broad inverted ribbon meets the shoulders of an enlarged circular medal."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '319fc61d-077f-5c65-942b-278d5d4da881'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__award-medal-rewards/20260925T060602Z-thuan-mac/reference/award medal_319fc61d-077f-5c65-942b-278d5d4da881.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'award-medal-rewards'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('award medal',)

    def build(self):
        # Symbol plan: Broad inverted ribbon meets the shoulders of an enlarged circular medal.
        # Construction reference: Lucide medal; original supplied subject controls meaning.

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
        circle('medal',24,32,12)
        poly('ribbon',(16,23),(8,4),(40,4),(32,23));join('ribbon','medal')

"""Regular data ticks and mirrored right U loops surround a horizontal arrow."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e886dcde-7af5-41c6-a333-6a6ddf119555'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arrow-right-data-flow/20260925T060602Z-thuan-mac/reference/coding apps website big data arrow_e886dcde-7af5-41c6-a333-6a6ddf119555.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'arrow-right-data-flow'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('coding apps website big data arrow',)

    def build(self):
        # Symbol plan: Regular data ticks and mirrored right U loops surround a horizontal arrow.
        # Construction reference: Lucide move-down-right; original supplied subject controls meaning.

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
        for x in (6,14,22):
         line(f'top-{x}',(x,6),(x,10));line(f'bottom-{x}',(x,38),(x,42))
        path('upper',(30,6),[('L',(30,8)),('A',(42,8),6,6,False),('L',(42,6))])
        path('lower',(30,42),[('L',(30,40)),('A',(42,40),6,6,True),('L',(42,42))])
        line('shaft',(6,24),(34,24));poly('head',(26,19),(34,24),(26,29));join('shaft','head')

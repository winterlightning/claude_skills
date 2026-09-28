"""Upright rounded battery and rounded terminal share shoulder nodes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '9ad9cd5c-98cd-452e-ad18-784b9bd66c4d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__battery/20260925T060602Z-thuan-mac/reference/battery_9ad9cd5c-98cd-452e-ad18-784b9bd66c4d.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'battery'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('battery',)

    def build(self):
        # Symbol plan: Upright rounded battery and rounded terminal share shoulder nodes.
        # Construction reference: Lucide battery; original supplied subject controls meaning.

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
        path('body',(14,12),[('L',(18,12)),('L',(30,12)),('L',(34,12)),('A',(38,16),4,4,True),('L',(38,40)),('A',(34,44),4,4,True),('L',(14,44)),('A',(10,40),4,4,True),('L',(10,16)),('A',(14,12),4,4,True)],True)
        path('terminal',(18,12),[('L',(18,8)),('A',(22,4),4,4,True),('L',(26,4)),('A',(30,8),4,4,True),('L',(30,12))]);join('terminal','body')

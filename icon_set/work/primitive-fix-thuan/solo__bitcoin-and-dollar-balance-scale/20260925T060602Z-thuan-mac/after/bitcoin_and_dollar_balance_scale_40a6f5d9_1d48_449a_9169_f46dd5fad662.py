"""Distinct bitcoin and dollar symbols sit above a level beam and closed triangular fulcrum."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '40a6f5d9-1d48-449a-9169-f46dd5fad662'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bitcoin-and-dollar-balance-scale/20260925T060602Z-thuan-mac/reference/crypto currency bitcoin dollar equal_40a6f5d9-1d48-449a-9169-f46dd5fad662.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'bitcoin-and-dollar-balance-scale'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('crypto currency bitcoin dollar equal',)

    def build(self):
        # Symbol plan: Distinct bitcoin and dollar symbols sit above a level beam and closed triangular fulcrum.
        # Construction reference: Lucide scale; original supplied subject controls meaning.

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
        path('bitcoin',(8,6),[('L',(16,6)),('A',(16,14),4,4,True),('A',(16,22),4,4,True),('L',(8,22)),('L',(8,14)),('L',(8,6))],True)
        line('bitcoin-bar',(8,14),(16,14));join('bitcoin-bar','bitcoin')
        line('bitcoin-tick',(12,4),(12,6));join('bitcoin-tick','bitcoin')
        line('bitcoin-foot',(12,22),(12,24));join('bitcoin-foot','bitcoin')
        dy=0
        path('dollar',(40,6+dy),[('L',(34,6+dy)),('C',(34,14+dy),(26,6+dy),(26,13+dy)),('C',(34,22+dy),(42,15+dy),(42,22+dy)),('L',(28,22+dy))])
        line('dollar-top',(34,4+dy),(34,6+dy));join('dollar-top','dollar')
        line('dollar-bottom',(34,22+dy),(34,24+dy));join('dollar-bottom','dollar')
        poly('beam',(8,32),(24,32),(40,32))
        poly('fulcrum',(24,32),(16,44),(32,44),closed=True);join('beam','fulcrum')

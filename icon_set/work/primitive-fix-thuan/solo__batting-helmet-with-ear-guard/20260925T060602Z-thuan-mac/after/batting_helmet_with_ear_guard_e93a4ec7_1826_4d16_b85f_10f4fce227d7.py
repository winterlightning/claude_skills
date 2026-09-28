"""Round batting shell, projecting brim and smooth ear guard with visible circular vent."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e93a4ec7-1826-4d16-b85f-10f4fce227d7'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__batting-helmet-with-ear-guard/20260925T060602Z-thuan-mac/reference/baseball helmet_e93a4ec7-1826-4d16-b85f-10f4fce227d7.svg'
AUTHOR = 'gpt-6'

class Revision(Solo48):
    icon_id = 'batting-helmet-with-ear-guard'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('baseball helmet',)

    def build(self):
        # Symbol plan: Round batting shell, projecting brim and smooth ear guard with visible circular vent.
        # Construction reference: Lucide moon; original supplied subject controls meaning.

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
        path('shell',(40,26),[('A',(4,26),18,18,False),('C',(18,40),(4,34),(8,40)),('C',(29,29),(32,40),(34,34)),('C',(28,26),(27,27),(27,26)),('L',(40,26))],True)
        line('brim',(40,26),(44,26));join('brim','shell')
        circle('ear-vent',18,28,3)

# Exact-drawing visual exception authorized by user; automatic findings remain in validation.txt.
Revision.exception = {'reason': 'Preserve the identifying helmet ear vent and inward cheek guard. The vent keeps 2.45px visible separation from the smooth guard; the enclosed dot opening remains visible at 48px in both themes.', 'approved_by': 'user: delegated visual exception judgment in this request', 'approved_on': '2026-09-25', 'svg_sha256': 'b73490c0921a0f50f07f387f173bdbd249c47e1068411de927aaf3c0f6d55fcc'}

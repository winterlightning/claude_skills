"""Restore two table legs, recognizable chair seats and a tapering vase with three flower heads.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: sprout. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '34f0074a-0c4a-4822-81b3-10560a11cb1b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dining-table-chairs-flower-vase/20260925T085629Z-thuan-mac/reference/eating table_34f0074a-0c4a-4822-81b3-10560a11cb1b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dining-table-chairs-flower-vase'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the complete table, two chairs, tapered vase and three flowers. Use a 44-unit ink envelope and local smaller flower/vase clearances while keeping table and chair legs eight units apart. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': 'd51c2098a68b5113ed565686eb66e69d917721449d3f85ed4ebd973ebfc18b12'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dining', 'table', 'chairs', 'flower', 'vase')
    def build(self):
        # Shared x series leaves equal eight-unit spacing between chair and table legs.
        self.add_polyline('table',(14,30),(20,30),(28,30),(34,30))
        for name,x in [('left',20),('right',28)]:
            self.add_line(name+'-leg',(x,30),(x,44));self.relate('connect',name+'-leg','table')
        for name,x,sign in [('left',4,1),('right',44,-1)]:
            self.add_polyline(name+'-chair',(x,24),(x,36),(x,44))
            self.add_polyline(name+'-seat',(x,36),(x+8*sign,36),(x+8*sign,44));self.relate('connect',name+'-seat',name+'-chair')
        self.add_polyline('vase',(20,30),(21,22),(24,22),(27,22),(28,30));self.relate('connect','vase','table')
        self.add_line('stem',(24,22),(24,18));self.relate('connect','stem','vase')
        self.path('stem-left',(24,18),[('C',(14,13),(20,15),(16,18))]);self.relate('connect','stem-left','stem')
        self.path('stem-top',(24,18),[('C',(27,14),(25,16),(26,15)),('C',(32,10),(30,14),(31,12))]);self.relate('connect','stem-top','stem');self.relate('connect','stem-left','stem-top')
        self.add_line('branch',(27,14),(34,18));self.relate('connect','branch','stem-top')
        for n,x,y in [('left',14,10),('top',32,7),('right',37,18)]:
            self.circle('flower-'+n,x,y,3)
        self.relate('connect','flower-left','stem-left');self.relate('connect','flower-top','stem-top');self.relate('connect','flower-right','branch')

    def path(self, name, start, commands, closed=False):
        members=[]
        for i, (kind,end,*args) in enumerate(commands):
            tag=f'{name}-{i}'
            if kind=='L': self.add_line(tag,start,end)
            elif kind=='C': self.add_bezier(tag,start,(args[0],args[1],end))
            else: self.add_arc(tag,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            start=end;members.append(tag)
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def box(self,name,l,t,r,b,k):
        self.path(name,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)


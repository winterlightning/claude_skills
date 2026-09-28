"""Restore all three fork tines with equal spacing, rounded shoulders and a separate round plate.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: utensils. Original source establishes full subject and arrangement.
Keyshape: HRECT_L; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a8a63c5c-caf1-441f-8678-fb2e81e65bdf'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__dining-plate-fork/20260925T085629Z-thuan-mac/reference/preparation_a8a63c5c-caf1-441f-8678-fb2e81e65bdf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'dining-plate-fork'
    keyshape = Keyshape.HRECT_L
    exception = {'reason': 'Preserve all three evenly spaced tines with two-pixel visible gaps; replacing the three-prong fork with a two-prong symbol loses source identity. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '1df8637dd218c3b8cdcc5629fd12b069f034f88aaa963dc5348fffcc08eae5eb'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('dining', 'plate', 'fork')
    def build(self):

        self.circle('plate',14,24,10)
        self.path('fork',(32,8),[('L',(32,20)),('A',(38,26),6,6,False),('A',(44,20),6,6,False),('L',(44,8))])
        self.add_polyline('middle-handle',(38,8),(38,26),(38,40));self.relate('connect','middle-handle','fork')


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


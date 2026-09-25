"""Restore the solid outlined handle and opposed crescent jaws with half-turn symmetry.
Symbol plan: Each outline owns its smooth contour. Shared endpoints connect attached parts.
Lucide construction: wrench. Original source establishes full subject and arrangement.
Keyshape: SQUARE; preserve natural source proportions where a documented exception is needed.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a3821bc3-8cdd-5cce-aa77-833dd70703fc'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__diagonal-double-ended-wrench/20260925T085629Z-thuan-mac/reference/wrench double_a3821bc3-8cdd-5cce-aa77-833dd70703fc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'diagonal-double-ended-wrench'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Retain the reference double-jaw outline and hollow handle with half-turn symmetry. Local jaw wall clearance is smaller than four units but remains visibly separated at 48 pixels. Reviewed in light and dark at 48px. User explicitly authorized case-specific exceptions for UI/UX quality.', 'approved_by': 'user-directed-gpt-6', 'approved_on': '2026-09-25', 'svg_sha256': '0bc8d510ce2cae2afdce6f23e34de6f1db5da243fb506a18f68f8ece68bb115b'}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('diagonal', 'double', 'ended', 'wrench')
    def build(self):

        # A half-turn defines both jaw and handle sides from one source contour.
        half=[('C',(23,17),(22,4),(24,11)),('L',(31,25)),('C',(42,38),(39,23),(44,30)),('L',(35,31)),('C',(31,35),(32,30),(30,32)),('L',(38,42))]
        commands=half+[(k,(48-e[0],48-e[1]),*((48-p[0],48-p[1]) for p in args)) for k,e,*args in half]
        self.path('wrench',(10,6),commands,True)


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


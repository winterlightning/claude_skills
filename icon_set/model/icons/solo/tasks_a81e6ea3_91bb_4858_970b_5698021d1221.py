"""Tasks, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='a81e6ea3-91bb-4858-970b-5698021d1221'
SOURCE_PATH='icon_set/work/todo-references/tasks_a81e6ea3-91bb-4858-970b-5698021d1221.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='tasks'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'content'
    aliases=()
    keywords=('tasks',)

    # Keyshape visible extremes: (4, 4, 44, 44); centerline extremes: (6, 6, 42, 42).
    def build(self):
        # Clipboard, rounded clip crown, two checked rows and two diagonal text strokes.
        self.path('board',(16,14),[('L',(10,14)),('A',(6,18),4,False),('L',(6,38)),
            ('A',(10,42),4,False),('L',(38,42)),('A',(42,38),4,False),
            ('L',(42,18)),('A',(38,14),4,False),('L',(32,14))])
        self.path('clip',(16,14),[('L',(16,10)),('L',(20,10)),('A',(28,10),4),
            ('L',(32,10)),('L',(32,14)),('L',(32,18)),('L',(16,18)),('L',(16,14))],True)
        self.relate('connect','board','clip')
        for i,y in enumerate((26,35)):
            self.add_polyline(f'check-{i}',(14,y),(17,y+2),(23,y-3))
            self.add_line(f'text-{i}',(31,y+1),(34,y-2))


    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)

    def rect(self,n,l,t,r,b,k=4,top=(),right=(),bottom=(),left=()):
        # One rounded rectangle owns paired radii, extents, and connection splits.
        seg=[('L',(x,t)) for x in sorted(set(top)) if l+k<x<r-k]
        seg += [('L',(r-k,t)),('A',(r,t+k),k)]
        seg += [('L',(r,y)) for y in sorted(set(right)) if t+k<y<b-k]
        seg += [('L',(r,b-k)),('A',(r-k,b),k)]
        seg += [('L',(x,b)) for x in sorted(set(bottom),reverse=True) if l+k<x<r-k]
        seg += [('L',(l+k,b)),('A',(l,b-k),k)]
        seg += [('L',(l,y)) for y in sorted(set(left),reverse=True) if t+k<y<b-k]
        seg += [('L',(l,t+k)),('A',(l+k,t),k)]
        self.path(n,(l+k,t),seg,True)

    def suitcase(self):
        # SQUARE: ink (4,4)-(44,44); centerlines (6,6)-(42,42).
        self.rect('case',6,14,42,42,4,top=(16,32))
        self.path('handle',(16,14),[('L',(16,10)),('A',(20,6),4),
            ('L',(28,6)),('A',(32,10),4),('L',(32,14))])
        self.relate('connect','case','handle')

    def check(self,n,x,y):
        self.add_polyline(n,(x,y),(x+3,y+3),(x+9,y-3))


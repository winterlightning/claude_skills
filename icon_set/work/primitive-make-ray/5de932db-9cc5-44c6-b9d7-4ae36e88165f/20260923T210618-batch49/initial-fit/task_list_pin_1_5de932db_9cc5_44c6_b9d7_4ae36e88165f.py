"""Task list pin 1, drawn from its complete supplied reference.
Symbol plan: preserve the subject, nested symbols, repeats and intentional overlaps.
Each repeated part and rounded rectangle owns its parameters and attachment nodes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='5de932db-9cc5-44c6-b9d7-4ae36e88165f'
SOURCE_PATH='icon_set/work/todo-references/task list pin 1_5de932db-9cc5-44c6-b9d7-4ae36e88165f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='task-list-pin-1'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('task', 'list', 'pin', '1')

    def build(self):
        # Folded note with three lines and a round-headed diagonal pin.
        self.path('paper',(26,14),[('L',(10,14)),('A',(6,18),4,False),
            ('L',(6,42)),('L',(30,42)),('L',(38,34)),('L',(38,22))])
        self.path('fold',(30,42),[('L',(30,38)),('A',(34,34),4),('L',(38,34))])
        self.relate('connect','paper','fold')
        self.add_arc('pin-a',(34,15),(40,7),radius_x=5)
        self.add_arc('pin-b',(40,7),(34,15),radius_x=5)
        self.add_contour('pin-head','pin-a','pin-b',closed=True)
        self.add_line('pin-stem',(34,15),(26,23))
        self.relate('connect','pin-head','pin-stem')
        for i,(y,end) in enumerate(((24,29),(30,29),(36,22))):
            self.add_line(f'text-{i}',(13,y),(end,y))


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


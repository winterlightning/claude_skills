"""messages bubble text.
Plan: Circular badge with rounded speech bubble, tail and one text stroke. Reduce two text lines to one because nested 24-unit bubble cannot support three 8-unit vertical gaps. No useful exact Lucide match.
Keyshape CIRCLE: visible bounds (2, 2, 46, 46); centerlines inset 2 from these bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b43ae04a-1ea7-48c8-9d78-6d2f1fe1a195'
SOURCE_PATH='pictographic-primitives/_uncategorized_27/messages bubble text_b43ae04a-1ea7-48c8-9d78-6d2f1fe1a195.svg'
AUTHOR="gpt-6"

class Drawing(Solo48):
    icon_id='messages-bubble-text'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('messages', 'bubble', 'text')
    def build(self):
        self.circle('badge',24,24,20)
        self.path('bubble',(18,14),[('L',(30,14)),('A',(34,18),4,4,True),('L',(34,28)),('A',(30,32),4,4,True),('L',(26,32)),('L',(18,34)),('L',(18,30)),('A',(14,26),4,4,True),('L',(14,18)),('A',(18,14),4,4,True)],True)
        self.add_line('text',(23,23),(25,23))

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,ops,closed=False):
        at=start; members=[]
        for i,op in enumerate(ops):
            eid=f'{n}-{i}';kind,end,*args=op
            if end==at:continue
            if kind=='L':self.add_line(eid,at,end)
            elif kind=='A':self.add_arc(eid,at,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            at=end;members.append(eid)
        self.add_contour(n,*members,closed=closed)

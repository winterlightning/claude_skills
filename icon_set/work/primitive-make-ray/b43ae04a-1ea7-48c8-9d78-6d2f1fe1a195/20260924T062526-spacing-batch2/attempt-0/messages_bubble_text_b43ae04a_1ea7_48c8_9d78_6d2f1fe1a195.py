"""messages bubble text.
Plan: Round badge around a rounded speech bubble with two text lines and lower-left tail. No useful exact Lucide match. Preserve badge, bubble and text as complete composition.
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
        self.path('bubble',(16,14),[('L',(32,14)),('A',(34,16),2,2,True),('L',(34,30)),('A',(32,32),2,2,True),('L',(24,32)),('L',(17,36)),('L',(18,32)),('L',(16,32)),('A',(14,30),2,2,True),('L',(14,16)),('A',(16,14),2,2,True)],True)
        self.add_line('text-top',(22,21),(26,21))
        self.add_line('text-bottom',(22,29),(26,29))

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

"""Restored a four-cell arithmetic calculator with plus, minus, multiply and equals in front of a house.
Plan and comparison: The calculator became a generic device with a display and two dots, losing the arithmetic operators.
Construction reference: calculator: rounded body and aligned keypad; operators follow the supplied reference
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='110df7d0-d83c-4e1f-a771-57b0adb39e09'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__real-estate-market-calculator-house/20260929T043142Z-thuan-mac/reference/real estate market calculator house_110df7d0-d83c-4e1f-a771-57b0adb39e09.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='real-estate-market-calculator-house'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def path(self, name, start, commands, closed=False):
        members=[]
        at=start
        for n,c in enumerate(commands):
            ident=f"{name}-{n}"
            if c[0]=='L':
                end=c[1]; self.add_line(ident,at,end)
            else:
                _,end,rx,ry,sweep,*large=c
                self.add_arc(ident,at,end,radius_x=rx,radius_y=ry,sweep=sweep,large_arc=bool(large and large[0]))
            members.append(ident); at=end
        self.add_contour(name,*members,closed=closed)

    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)

    def box(self,name,l,t,r,b,rad=2):
        self.path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):

        # The calculator occludes the lower-left house; its 2x2 series owns the four operators.
        self.add_polyline('roof',(20,14),(32,4),(44,14))
        self.add_polyline('house',(42,19),(42,29),(37,29))
        self.box('calculator',4,17,32,44,3)
        self.add_line('vertical',(18,17),(18,44)); self.relate('connect','vertical','calculator')
        self.add_line('horizontal',(4,30),(32,30)); self.relate('connect','horizontal','calculator'); self.relate('connect','horizontal','vertical')
        self.add_line('plus-h',(8,24),(14,24)); self.add_line('plus-v',(11,21),(11,27)); self.relate('connect','plus-h','plus-v')
        self.add_line('minus',(23,24),(28,24))
        self.add_line('times-a',(9,35),(13,39)); self.add_line('times-b',(13,35),(9,39)); self.relate('connect','times-a','times-b')
        for n,y in enumerate((35,40)): self.add_line(f'equals-{n}',(23,y),(28,y))

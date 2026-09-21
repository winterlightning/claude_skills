'A backward baseball cap sits above paired sunglasses. This is a natural accessory group, not a modifier combination. SQUARE balances dome and eyewear. Dome and rear opening share x24; lenses share a mirrored rounded bowl definition. Source supplies cap opening and broad glasses; Lucide hat-glasses supplies vertical spacing and glasses bridge. Omit the tiny top button to preserve the dome.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '264814f3-8ffa-45e9-be4e-00194dae68c2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_09/cap sunglasses_264814f3-8ffa-45e9-be4e-00194dae68c2.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'backward-cap-above-sunglasses'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Baseball Cap and Sunglasses',)
    keywords = ('baseball', 'cap', 'and', 'sunglasses')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('cap',(6,24),[(18,24),((30,24),6,6,True),(42,24),((6,24),18,18,False)],True)
        for name,l in [('left',6),('right',28)]:
            r=l+14
            path(name,(l,34),[(r,34),(r,38),((r-4,42),4,4,True),(l+4,42),((l,38),4,4,True),(l,34)],True)
        self.add_line('bridge',(20,34),(28,34));self.relate('connect','bridge','left');self.relate('connect','bridge','right')

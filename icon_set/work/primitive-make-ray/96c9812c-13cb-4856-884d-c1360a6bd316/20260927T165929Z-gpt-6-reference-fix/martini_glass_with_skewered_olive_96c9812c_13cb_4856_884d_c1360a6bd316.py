'A triangular martini glass holds a skewered olive. SQUARE balances broad bowl and slender stem, extremes 6,6,42,42. Open upper rim lets the physical garnish remain readable. Stem and split foot share true nodes. Lucide martini supplies the V bowl, stem and base; source supplies olive and diagonal pick. Omit the rim across the garnish opening.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '96c9812c-13cb-4856-884d-c1360a6bd316'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__martini-glass-with-skewered-olive/20260927T165437Z-thuan-mac-1/reference/appetizer_96c9812c-13cb-4856-884d-c1360a6bd316.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'martini-glass-with-skewered-olive'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ('Martini Glass with Skewered Olive',)
    keywords = ('martini', 'glass', 'olive', 'cocktail', 'pick', 'drink', 'bar')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[];point=start
            for j,step in enumerate(steps):
                member=f"{name}-{j}"
                if len(step)==2:self.add_line(member,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        self.add_polyline('bowl',(6,6),(24,30),(42,6))
        self.add_line('rim',(6,6),(42,6))
        self.add_line('stem',(24,30),(24,42))
        self.add_polyline('foot',(14,42),(24,42),(34,42))
        self.relate('connect','bowl','rim');self.relate('connect','bowl','stem');self.relate('connect','stem','foot')
        # The olive hangs within the bowl, pierced by a diagonal cocktail pick.
        self.add_line('olive',(21,16),(24,16))
        self.add_line('pick',(24,16),(26,6))
        self.relate('connect','olive','pick');self.relate('connect','pick','rim')

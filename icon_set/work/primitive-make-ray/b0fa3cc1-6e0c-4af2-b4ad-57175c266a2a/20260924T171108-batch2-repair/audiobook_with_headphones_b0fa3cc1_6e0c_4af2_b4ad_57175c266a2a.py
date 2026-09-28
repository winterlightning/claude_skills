"""An open book surrounded by headphones.
Plan: HRECT_L balances the headphone arch and central book.
Reduction: Removed the inner earcup closure seams to open spacing around the book.
Construction: Lucide headphones: arch and paired cups; book-open: central fold and paired pages.
Layout: Mirrored earcups and book pages."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'b0fa3cc1-6e0c-4af2-b4ad-57175c266a2a'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/audio book headphones_b0fa3cc1-6e0c-4af2-b4ad-57175c266a2a.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'audiobook-with-headphones'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('audiobook', 'with', 'headphones')

    def circle(self, name, x, y, r):
        self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, x, y, w, h, r=0):
        if not r:
            self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            part=f'{name}-{i}'; ids.append(part)
            if i%2: self.add_arc(part,pts[i],pts[(i+1)%8],radius_x=r)
            else: self.add_line(part,pts[i],pts[(i+1)%8])
        self.add_contour(name,*ids,closed=True)

    def build(self):
        # HRECT_L extremes (4,8)-(44,40). Shared book axis; open ear pads
        # remove the crowded inner seams while retaining headphones around book.
        self.add_arc('headband',(6,26),(42,26),radius_x=18)
        for side,x,sweep in [('left',6,False),('right',42,True)]:
            self.add_arc(side+'-cup',(x,26),(x,38),radius_x=2,radius_y=6,sweep=sweep)
            self.relate('connect','headband',side+'-cup')
        self.add_polyline('book',(15,25),(24,29),(33,25),(33,36),(24,40),(15,36),closed=True)
        self.add_line('fold',(24,29),(24,40))
        self.relate('connect','book','fold')

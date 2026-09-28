'Apple with Honey Jar and Dipper.\nPlan: Apple below-right of honey dipper, with one hanging drip and diagonal handle.\nConstruction reference: Lucide apple: lobe-based fruit contour; source dipper and dripping honey retained.\nReduction: Dipper grooves reduced to a bold head and one drip.\nKeyshape: SQUARE; use exact SOLO48 centerline extremes from the contract.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'efb1f8f3-2844-4c28-87ad-415937bd4b08'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__apple-with-dripping-honey-dipper/20260927T160114Z-thuan-mac-1/reference/honey apple_efb1f8f3-2844-4c28-87ad-415937bd4b08.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'apple-with-dripping-honey-dipper'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('apple', 'with', 'dripping', 'honey', 'dipper')

    def build(self):
        # Apple at lower right; oval dipper head and one curled honey drip at upper left.
        def oval(name,cx,cy,rx,ry):
            self.add_arc(name+'-a',(cx-rx,cy),(cx+rx,cy),radius_x=rx,radius_y=ry)
            self.add_arc(name+'-b',(cx+rx,cy),(cx-rx,cy),radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-a',name+'-b',closed=True)
        self.add_bezier('apple',(30,27),
            ((25,24),(20,25),(18,30)),((14,36),(20,42),(25,42)),
            ((28,40),(28,40),(30,41)),((32,40),(33,42),(36,42)),
            ((43,41),(45,32),(40,28)),((37,25),(33,25),(30,27)))
        self.add_contour('fruit','apple',closed=True)
        self.add_line('stem',(30,27),(34,20))
        self.relate('connect','stem','fruit')
        oval('dipper',12,12,5,6)
        self.add_line('handle',(17,10),(34,6))
        self.relate('connect','handle','dipper')
        self.add_bezier('honey',(9,18),((8,22),(9,26),(8,31)))
        self.relate('connect','honey','dipper')

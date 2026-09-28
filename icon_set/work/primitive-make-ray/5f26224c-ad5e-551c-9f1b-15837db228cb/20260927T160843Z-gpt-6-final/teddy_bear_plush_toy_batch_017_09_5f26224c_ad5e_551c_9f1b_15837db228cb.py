from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5f26224c-ad5e-551c-9f1b-15837db228cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__teddy-bear-plush-toy-batch-017-09/20260927T155415Z-thuan-mac-1/reference/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
AUTHOR = 'gpt-6'
EXPORTED_REFERENCE = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/references/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
BRIEF_PATH = 'work/brief-exports/20260917-all-todo-batches-15/batches/batch-017/09-teddy-bear-plush-toy--5f26224c-ad5e-551c-9f1b-15837db228cb.md'
DESIGN_PLAN = 'Mirrored round ears above a broad head; rounded side arms and forward feet.'
DESIGN_NOTES = ['Blank face and belly preserve the plush toy’s uncluttered appearance; feet merge into the lower silhouette.']
CONSTRUCTION_REFERENCE = 'No useful exact Lucide match; geometric contour construction.'

class BatchIcon(Solo48):
    icon_id = 'teddy-bear-plush-toy-batch-017-09'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "kids"
    categories = ("primitives", "kids")
    keywords = ('teddy', 'bear', 'plush', 'toy', 'animal', 'seated', 'childhood', 'soft')

    def build(self):
        # Four round masses follow the source: paired ears, a circular head,
        # and a seated body with separate rounded arms and feet.
        def circle(name, x, y, r):
            self.add_arc(name+'-a', (x,y-r), (x,y+r), radius_x=r, radius_y=r, sweep=True)
            self.add_arc(name+'-b', (x,y+r), (x,y-r), radius_x=r, radius_y=r, sweep=True)
            self.add_contour(name, name+'-a', name+'-b', closed=True)
        circle('ear-left', 12, 10, 4)
        circle('ear-right', 36, 10, 4)
        circle('head', 24, 17, 10)
        points = [
            ((20,25), (12,25), (6,27), (6,31)),
            ((6,31), (6,35), (9,37), (12,36)),
            ((12,36), (10,40), (11,42), (15,42)),
            ((15,42), (19,42), (20,38), (24,38)),
            ((24,38), (28,38), (29,42), (33,42)),
            ((33,42), (37,42), (38,40), (36,36)),
            ((36,36), (39,37), (42,35), (42,31)),
            ((42,31), (42,27), (36,25), (28,25)),
        ]
        members=[]
        for j,(start,c1,c2,end) in enumerate(points):
            n=f'body-{j}'
            self.add_bezier(n,start,(c1,c2,end))
            members.append(n)
        self.add_line('body-top',(28,25),(20,25))
        self.add_contour('body',*members,'body-top',closed=True)
        for a,b in [('head','ear-left'),('head','ear-right'),('head','body')]:
            self.relate('connect',a,b)

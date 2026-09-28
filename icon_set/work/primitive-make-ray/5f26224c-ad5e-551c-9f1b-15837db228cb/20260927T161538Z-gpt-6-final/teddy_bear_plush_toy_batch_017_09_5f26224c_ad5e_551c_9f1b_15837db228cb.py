from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '5f26224c-ad5e-551c-9f1b-15837db228cb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__teddy-bear-plush-toy-batch-017-09/20260927T155415Z-thuan-mac-1/reference/toys teddy bear_5f26224c-ad5e-551c-9f1b-15837db228cb.svg'
AUTHOR = "gpt-6"
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
        # One continuous mirrored silhouette keeps round ears and distinct feet
        # without the overlapping loops that collapse into tiny white holes.
        right = [
            ((24,8),(28,8),(31,9),(32,11)),
            ((32,11),(32,8),(33,6),(36,6)),
            ((36,6),(40,6),(42,10),(40,14)),
            ((40,14),(39,16),(36,17),(35,16)),
            ((35,16),(36,21),(34,25),(30,26)),
            ((30,26),(38,26),(42,29),(42,32)),
            ((42,32),(42,36),(39,38),(35,36)),
            ((35,36),(38,40),(37,42),(33,42)),
            ((33,42),(29,42),(29,38),(24,38)),
        ]
        def mirror(point): return (48-point[0],point[1])
        whole = right + [(mirror(end),mirror(c2),mirror(c1),mirror(start))
                         for start,c1,c2,end in reversed(right)]
        members=[]
        for j,(start,c1,c2,end) in enumerate(whole):
            name=f'outline-{j}'
            self.add_bezier(name,start,(c1,c2,end))
            members.append(name)
        self.add_contour('bear',*members,closed=True)

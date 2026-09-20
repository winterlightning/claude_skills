"""User-authorized 32px exceptions: 4px frame and smaller 2px shared characters."""
import sys,json,ast,textwrap
from pathlib import Path
W=Path(__file__).resolve().parent;ROOT=W.parents[2];sys.path.insert(0,str(ROOT));sys.path.insert(0,str(W.parent/'sub-fidelity-repair-32'))
from glyph_native import fit
from icon_set.scripts.create_variant import prepare_variant
from icon_set.model.icons.registry import create
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/sub-fidelity-repair-32/accepted.json'
AUTHOR='gpt-6'
rows=[r for r in json.loads((W.parent/'sub-fidelity-repair-32/accepted.json').read_text()) if r['number'] in (3,11,17)]
frame="""self.add_bezier('top-left',(16,2),((8,2),(2,7),(2,14)))
self.add_bezier('lower-left',(2,14),((2,19),(4,22),(8,24)))
self.add_line('tail-left',(8,24),(4,30))
self.add_line('tail-right',(4,30),(11,26))
self.add_bezier('bottom',(11,26),((20,29),(30,24),(30,14)))
self.add_bezier('top-right',(30,14),((30,7),(24,2),(16,2)))
self.add_contour('frame','top-left','lower-left','tail-left','tail-right','bottom','top-right',closed=True)
"""
bodies={
3:frame+fit('symbol-bitcoin',14,16,14,'glyph')[0]+"\nself.add_line('serif-top',(10,10),(11,10))\nself.add_line('serif-bottom',(10,18),(11,18))\n",
11:frame+fit('letter-h-uppercase',10,12,14,'h')[0]+"\nself.add_line('plain-i',(21,9),(21,19))\n",
17:"""self.add_arc('circle-top',(2,16),(30,16),radius_x=14)
self.add_arc('circle-bottom',(30,16),(2,16),radius_x=14)
self.add_contour('frame','circle-top','circle-bottom',closed=True)
self.add_arc('o-top',(7,14),(15,14),radius_x=4)
self.add_arc('o-bottom',(15,14),(7,14),radius_x=4)
self.add_contour('o','o-top','o-bottom',closed=True)
self.add_bezier('two-head',(20,15),((22,13),(25,15),(24,17)))
self.add_polyline('two-foot',(24,17),(20,22),(25,22))
"""}
out=[]
for r in rows:
 dst,uid,source=prepare_variant(r['candidate'],'sub','User-approved compact 32px with smaller inner glyph')
 dst=dst.with_name(dst.stem+'_'+r['source_id'].replace('-','_')+'.py')
 # Independent module, compact geometry authored directly in final coordinates.
 content='"""Compact source composition. User allows stroke and spacing exceptions for the inner characters."""\nfrom ._base import Sub32\nfrom ...keyshapes import Keyshape\n'
 content+=f'SOURCE_ICON_ID={r["source_id"]!r}\nSOURCE_PATH={r["source_path"]!r}\nAUTHOR="gpt-6"\n'
 parent=create(r['candidate']);mod=__import__(parent.__module__,fromlist=['TYPEFACE_GLYPH_IDS'])
 content+=f'TYPEFACE_GLYPH_IDS={getattr(mod,"TYPEFACE_GLYPH_IDS",())!r}\n'
 content+='COMPACT_EXCEPTION = "User requested smaller inner symbols, allowing sub stroke/grid/spacing exceptions instead of enlargement."\n'
 content+=f'class Drawing(Sub32):\n    icon_id={uid!r}\n    variant_of={r["candidate"]!r}\n    variant_label="Compact inner symbol"\n    keyshape=Keyshape.SQUARE\n    STROKE_WIDTH=2\n    PATH_STROKE_WIDTHS={{"frame":4}}\n    semantic_role="SUB"\n    semantic_kind="modifier"\n    category="primitives/mark"\n    def build(self):\n'+textwrap.indent(bodies[r['number']],'        ')+'\n'
 content+='    def to_record(self):\n        record=super().to_record()\n        record["style"]["path_stroke_widths"]=dict(self.PATH_STROKE_WIDTHS)\n        record["compact_exception"]=COMPACT_EXCEPTION\n        return record\n'
 ast.parse(content);dst.write_text(content)
 out.append(dict(r,parent=r['candidate'],compact=uid,compact_python=str(dst.relative_to(ROOT))))
(W/'candidates.json').write_text(json.dumps(out,indent=2))
print('Created three independent compact models.')

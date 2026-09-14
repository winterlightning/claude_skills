"""Final per-symbol corrections after visual and release QA."""
SOURCE_ICON_ID = None
SOURCE_PATH = 'selection.json'
AUTHOR = 'gpt-6'
from pathlib import Path
import json
W=Path(__file__).parent;ROOT=W.resolve().parents[2];s=json.loads((W/'selection.json').read_text())
def change(n,pairs):
 p=ROOT/s[n-1]['file'];t=p.read_text()
 for a,b in pairs:
  assert a in t,(n,a)
  t=t.replace(a,b)
 p.write_text(t)
change(8,[
 ("((22, 42), None), ((24, 40), None), ((36, 28), None)","((24, 42), None), ((26, 40), None), ((40, 26), None)"),
 ("((38, 26), None), ((22, 10), None), ((20, 12), None)","((24, 10), None), ((10, 24), None)"),
 ("((8, 24), None), ((6, 26), None)","((6, 28), None)"),
 ("contour('bottle', (6, 26)","contour('bottle', (6, 28)"),
 ("contour('teat', (22, 10)","contour('teat', (24, 10)"),
 ("((42, 14), None), ((38, 26), None)","((42, 14), None), ((40, 26), None)"),
 ("        contour('handle-left', (8, 24), [\n            ((6, 16), (2, 8, True)), ((14, 8), (8, 8, True)),\n            ((20, 12), (6, 4, True))])\n        contour('handle-right', (36, 28), [\n            ((42, 34), (6, 6, True)), ((34, 42), (8, 8, True)),\n            ((24, 40), (10, 2, True))])",
 "        # Radius-10 circles use exact 6-8-10 attachment vectors.\n        self.add_arc('handle-left', (10, 24), (24, 10), radius_x=10, large_arc=True)\n        self.add_arc('handle-right', (40, 26), (26, 40), radius_x=10, large_arc=True)"),
])
change(25,[
 ("run('upper-body',(4, 21),(12,19),(16,24),(20,22),(29,18),(35,16))", "run('upper-body',(4, 21),(12,19),(16,24),(20,22),(9,10),(18,8),(29,18),(35,16))"),
 ("        self.add_polyline('far-wing',(20,22),(9,10),(18,8),(29,18))\n        self.relate('connect','outline','far-wing')", "        # The far wing is part of the silhouette; its redundant crossing seam\n        # is omitted so the tail/wing junction does not create tiny counters."),
])
change(46,[('(24, 12)','(24, 14)'),('radius_x=16, radius_y=8','radius_x=16, radius_y=10')])
# Human pose: preserve the kneeling backbend and make its head gap exact.
change(21,[
 ("(34, 7), (40, 7), radius_x=3, radius_y=3", "(28, 10), (40, 10), radius_x=6, radius_y=6"),
 ("(40, 7), (34, 7), radius_x=3, radius_y=3", "(40, 10), (28, 10), radius_x=6, radius_y=6"),
 ('(30, 19)', '(34, 24)'), ('(30, 44)', '(34, 44)'),
 ('radius_x=22, radius_y=22', 'radius_x=26, radius_y=17'),
 ("        # Envelope repair:","        # Human reference: human_ref/full_body_ref.png, kneeling pose.\n        # Head center (34,10), radius 6; body top (34,24): ink gap exactly 4.\n        # Envelope repair:"),
])

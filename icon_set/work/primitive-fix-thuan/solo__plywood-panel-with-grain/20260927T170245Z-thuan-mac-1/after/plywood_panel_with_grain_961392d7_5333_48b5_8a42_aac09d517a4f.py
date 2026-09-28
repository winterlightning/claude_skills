"""Plywood panel with two sweeping wood-grain curves.
Plan: rounded square frame contains two independent flowing grain strokes; tiny corner fixings are omitted so the grain reads at 48 pixels.
Keyshape SQUARE centerline (6,6)-(42,42). No useful Lucide wood pattern; the reference governs the organic grain.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "961392d7-5333-48b5-8a42-aac09d517a4f"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__plywood-panel-with-grain/20260927T170245Z-thuan-mac-1/reference/plywood_961392d7-5333-48b5-8a42-aac09d517a4f.svg"
AUTHOR = "gpt-6"
class PlywoodPanelWithGrain(Solo48):
 icon_id = "plywood-panel-with-grain"
 keyshape = Keyshape.SQUARE
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "materials"
 aliases = ("plywood",)
 keywords = ("wood", "plywood", "panel", "grain")
 def build(self):
  pts=((10,6),(38,6),(42,10),(42,38),(38,42),(10,42),(6,38),(6,10))
  parts=[]
  for j,a in enumerate(pts):
   b=pts[(j+1)%8];n=f"panel-{j}";parts.append(n)
   if j%2:self.add_arc(n,a,b,radius_x=4,sweep=True)
   else:self.add_line(n,a,b)
  self.add_contour("panel",*parts,closed=True)
  self.add_bezier("grain-upper",(15,19),(((19,17),(27,15),(33,15))))
  self.add_bezier("grain-lower",(15,30),(((20,28),(27,25),(33,27))))

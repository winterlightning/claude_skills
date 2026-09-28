"""Banded planet with two vertical stripes and a hollow central spot.
Plan: eight shared-radius arcs form one sphere; the bands meet four named circle nodes. The spot stays open at SOLO48.
Keyshape CIRCLE radius20 about (24,24). No direct Lucide match; circular construction informed by Lucide globe.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "4b501896-39ae-4d0f-82d0-50f8cd6f897d"
SOURCE_PATH = "icon_set/work/primitive-fix-thuan/solo__planet-with-vertical-bands-and-a-spot/20260927T170245Z-thuan-mac-1/reference/astronomy planet neptune_4b501896-39ae-4d0f-82d0-50f8cd6f897d.svg"
AUTHOR = "gpt-6"
class BandedPlanet(Solo48):
 icon_id = "planet-with-vertical-bands-and-a-spot"
 keyshape = Keyshape.CIRCLE
 semantic_role = "MAIN"
 semantic_kind = "noun"
 category = "astronomy"
 aliases = ("neptune",)
 keywords = ("planet", "neptune", "band", "spot")
 def build(self):
  points=((24,4),(36,8),(44,24),(36,40),(24,44),(12,40),(4,24),(12,8))
  parts=[]
  for j,a in enumerate(points):
   b=points[(j+1)%len(points)];n=f"planet-{j}";parts.append(n)
   self.add_arc(n,a,b,radius_x=20,sweep=True)
  self.add_contour("planet",*parts,closed=True)
  for x in (12,36):
   n=f"band-{x}";self.add_line(n,(x,8),(x,40));self.relate("connect","planet",n)
  self.add_arc("spot-upper",(21,24),(27,24),radius_x=3,sweep=True)
  self.add_arc("spot-lower",(27,24),(21,24),radius_x=3,sweep=True)
  self.add_contour("spot","spot-upper","spot-lower",closed=True)

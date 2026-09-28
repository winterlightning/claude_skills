Generate icon by codex frompt giving prmot
exepected output: clean icons and can be display within 48x48 pixel in production


Vectorize (pictocon vectorize)

Cleaning/Redrawn - Opus -> from vectorize svg element path -> redrawn them in opus

Metrics (svg_metrics.py) -> after vectorize, before the Opus redraw
  /opt/homebrew/bin/python3 new-pipeline-test/svg_metrics.py <run>/<slug>_raw.svg
  writes <slug>_metrics.json, <slug>_fitted.svg, <slug>_fitted-48.png in the run folder:
  keyshape suggestion + fit, every part's segments on the 48 grid, junctions,
  clearances (8), holes (6 inscribed), human head gap (exactly 8), and an issues list.

Redraw (/icon-solo) -> give the agent the raw svg + metrics json; it rebuilds the
  icon as a Solo48 model and repairs each issue in the metrics it can, reporting any it cannot.

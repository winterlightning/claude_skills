# Notes for prompt.md (do not paste)

## NEGATIVE (if the model has a negative field)

fill, silhouette, gradient, shadow, 3D, perspective, sketch, hand drawn, thin line, varying width, text, frame, background tile, app icon, multiple icons

## OPTIONAL PRE-STEP: let an agent choose the parts

Ask any text agent this, then replace the second sentence of the prompt with its answer:

"For a 48 px line icon of {{SUBJECT}}, Lucide / Feather style, name its 2 to 4 most recognizable parts in one sentence, and say whether the overall shape is tall, wide, square or round. No decoration. Answer as: Show only ..., nothing else. Shape: ..."

Example for "coffee mug":
Show only a rounded cup open at the top, a C-shaped handle on the right, two short steam lines above, nothing else. Shape: square.

## WHY THESE NUMBERS

- 1/12 stroke and margin = 4 of 48 units, the SOLO48 stroke width and ink clearance.
- One stroke width of gap = the 8-unit spacing the build gate enforces between separate contours.
- Half a stroke width for holes = the 6-unit opening minimum.
- Black on white, uniform width, round caps: the vectorizer traces one clean path per stroke, so the Opus redraw gets simple geometry.
- Six strokes is about what survives at 48 px.

## IF THE OUTPUT IS WRONG

- Filled shapes: move "outline strokes only, hollow interior" to the first line.
- Uneven line width: lower "at most 6 strokes" to 4.
- Drawn on a rounded tile: add "on a plain white page, not on a button".
- Lines too thin to trace: change the stroke to "about 1/10 of the icon size".
- Wrong parts chosen: run the pre-step and paste its sentence.
- Tall or wide subject came back squashed into a square: put the shape word first, e.g. "tall portrait icon of a pencil".
- Person came back with a face, hands, clothes or a filled body: start the parts sentence with "a stick figure with" and add "no face, no hands" to the do-not-draw line.
- Always check the PNG downscaled to 48x48 before accepting it.

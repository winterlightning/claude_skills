# Main redraw import

Imported and verified 79 completed redraws; 12 use existing user-approved exceptions.

All exported SVG hashes and exception records match the prepared drawings. Ten tests passed.

The following three redraws were initially held; the user subsequently approved their exceptions and all three were imported successfully:
- Mobile Retail Shopping Cart
- Modern Two Wheeled Mountain Bike
- Open Palm Hand Stop Gesture

This is a local build. The live side-mains page mirrors production and requires deployment of these changes. No production reviews were cleared.

Detailed evidence: `report.json`, `verification.json`, `before/`, and `prepared/`.

## Live check

The live page changed from 82 to 7 Needs fix entries during this work. Only 1 of the 79 prepared SVG hashes currently matches the live catalog, so that count change is not proof this import has been deployed. Remaining entries: SE text, lowercase a, shopping cart, air purifier, mountain bike, open palm hand, and volume.

## Exception approval completed

User instruction: “exception approval them”. The shopping cart, mountain bike, and open palm hand now pass through drawing-bound exceptions, with original findings retained. See `../20260925-approved-three/applied/report.json`. This brings the imported total to 82, including 15 exceptions.

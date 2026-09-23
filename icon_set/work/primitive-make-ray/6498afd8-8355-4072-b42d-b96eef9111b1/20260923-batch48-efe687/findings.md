# street view

Standing person beside a map pin and short road line.

## Keyshape

SQUARE: The full composition uses a balanced 36 by 36 centerline envelope, visible ink (4,4)–(44,44).

## References

Input: `icon_set/work/todo-references/street view_6498afd8-8355-4072-b42d-b96eef9111b1.svg`.

Construction: human_ref/full_body_ref.png and map-pin: outlined head, connected limbs, pointed marker. Local Lucide original and atomic-debug geometry were inspected where used; the human construction reference owns anatomy.

## Reduction

- Outlined body reduced to shared stick-figure construction.
- Locator hole reduced to a solid center dot.

## Visual review

Person, locator and both street rules retained. Stick-figure reduction follows the shared full-body construction; the pin hole is represented by a dot. Reviewed at native 48px and enlarged size in both themes.

Head center (12,10), radius 4; actual torso starts (12,22) on vertical head axis. 22-(10+4)-4 = 4 units ink. human_figure flag is present.

## Validation

```text
status: valid
```

# Core Scripts Overview

The detailed command and module contracts now live in
[scripts.md](scripts.md). That inventory is the authoritative place to find:

- inputs, outputs, side effects, and exit behavior;
- `normal`, `sub`, and `container` support per tool;
- shared modules and the machine-readable profile registry;
- regression and repository checks; and
- top-level rework and upload orchestration.

Use [icon-pipeline.md](icon-pipeline.md) to decide when each command runs. The
pipeline has five tooling lanes:

| Lane | Purpose | Start in the inventory |
| --- | --- | --- |
| Intake | Stage a rework payload or analyze supplied SVG evidence | [Pipeline commands](scripts.md#pipeline-commands) |
| Build | Resolve atoms and emit the design/ship pair | [Pipeline commands](scripts.md#pipeline-commands) |
| Verify | Run structural, grid, overlap, keyshape, hole, pinch, and true-size checks | [Pipeline commands](scripts.md#pipeline-commands) |
| Maintain | Regenerate registry assets/examples or run a scoped migration | [Registry, compatibility, and migration commands](scripts.md#registry-compatibility-and-migration-commands) |
| Protect | Run unit tests plus documentation/inventory consistency checks | [Regression and repository checks](scripts.md#regression-and-repository-checks) |

Design values and exceptions do not belong in either scripts page. Keep them in
[icon-types.md](icon-types.md), [icon-rules.md](icon-rules.md), and
[atomic-shapes.md](atomic-shapes.md) so commands and rules cannot drift through
copy-pasted documentation.

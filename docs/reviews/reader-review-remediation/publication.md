# Publication and reviewed-tree identity

The local Git client had no GitHub push credentials, so publication used the connected GitHub Git-data API. That API assigns commit metadata, producing different commit IDs. Before moving `main`, each uploaded tree was checked against the local tree: identical tree IDs establish identical paths, file modes and content throughout that snapshot.

| Stage | Local commit | GitHub commit | Identical Git tree |
| --- | --- | --- | --- |
| Workflow repair and task records | `6355779341fc3eac541ef14ae8daeefb7be5af6b` | `63d8d88a085fa8cede067b2a0c8a0cd85f85e501` | `a2c94597801e9d844305267f59ddf5111174691b` |
| Documentation; independently reviewed snapshot | `823d1e261f6d4fa7d7baf6edad03e32e3d53b00d` | `e7c4b2ccf8d8ccf140bae1ffe5fd25761b98924c` | `6255943f01f19869f3309ef38e440638e4a0d95d` |
| Verbatim independent review and completion record | `d95d17bb18eea4eccb9f54bb17d8819eb7f1f32c` | `3e0788143a5d271cae525e2970b0fb82b747c281` | `eef78f441deec03ca06c4d13a7019e5793d2266d` |

The [independent review](review.md) retains the exact local commit IDs it examined. The corresponding public snapshot is `e7c4b2ccf8d8ccf140bae1ffe5fd25761b98924c`; its tree is byte-identical. This publication note and source-commit link clarification are documentation additions after acceptance. The tested workflow SHA-256 remains `7e8786f9a1321ce1c78756d6b6c970b9d32a00d87a030e5499e92bfcc6fe8d93`.

The branch update uses a non-forced fast-forward with expected prior head `1b6a8224ded9c25def1a86c97e58b0d2d07b4729`, preserving concurrent work if that head has changed. No release or tag is created by this repair; the changelog entry remains Unreleased.

# Submodule Policy

## urf-counterexamples
- Tracked as a Git submodule
- Pinned to an exact commit hash
- Updates require an explicit PR titled:
  "chore(submodule): bump urf-counterexamples to <short-sha>"

## Rules
1. No floating refs (no branches, no tags).
2. CI checks must use `submodules: recursive`.
3. Releases record the submodule SHA in release notes.


# Setting up a new spec repo from this template

1. Create the repo with **Use this template** on GitHub, then clone it next to your code repos.
2. Replace the placeholders everywhere:
   ```bash
   grep -rln '<project>\|<Project>\|<owner>' . --exclude-dir=.git
   ```
   `<project>` is the lowercase repo prefix, `<Project>` the product name, `<owner>` the GitHub handle that approves PRs.
3. Edit `scripts/spec_config.py`: list your parts (`PARTS`) and the platforms a person runs device cases on (`DEVICE_PLATFORMS`).
   Then match the part columns in `features/_template/validation.md`, `parity.md` and the `Parts affected:` lines in the templates.
4. Fill `constitution.md` and `glossary.md` (both start as `draft`).
5. Fill the repo table in `README.md` and `components/README.md`, and the contract list in `contracts/README.md`.
6. Set `.github/CODEOWNERS` to the owner, and add a branch ruleset on `main` that requires the `branch-name`, `source-branch` and `spec-check` checks.
7. Run `scripts/check`. It should print `OK (0 feature(s))`.
8. Delete this file.

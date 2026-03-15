# ADR-0011: Single-Maintainer GitHub Governance

- Date: 2026-03-15
- Status: Accepted

## Context

veri-graph already uses GitHub Actions, `verification-gates`, `CODEOWNERS`, a pull request template, and branch protection on `main`. Requiring one approving review is appropriate for a team, but it blocks a repository operated by a single maintainer with no second reviewer.

A mandatory approving review would therefore prevent routine protected-branch flow even when CI and conversation-resolution gates are already active.

## Decision

Use the following GitHub governance policy for a single-maintainer repository:

1. `main` remains a protected branch
2. changes still enter `main` through a branch plus pull request flow
3. `verify` remains a required status check with `strict=true`
4. `required_conversation_resolution=true` remains enabled
5. `enforce_admins=true` remains enabled
6. do not require `required_approving_review_count >= 1`
7. keep `CODEOWNERS` and `PULL_REQUEST_TEMPLATE` as structured PR guidance

## Consequences

### Positive

- the repository still uses a PR-based flow without a fake review gate
- `main` remains protected by CI and conversation resolution
- the maintainer can keep using the protected-branch workflow without creating an artificial second-reviewer dependency

### Negative

- the repository loses a mandatory human approval gate until more reviewers exist
- `CODEOWNERS` remains guidance rather than an enforced second-party review mechanism

## Follow-up

- if additional reviewers join, re-evaluate whether to require `required_approving_review_count >= 1`
- if ownership expands, split `CODEOWNERS` by real path owners or teams

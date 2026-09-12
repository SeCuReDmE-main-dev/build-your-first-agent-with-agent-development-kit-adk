---
name: synthia-handoff-orientation
description: Exercise skill for preparing source-grounded Synthia handoff packets from the ADK YAML lesson. Use only inside adk-workspace practice, not as production Synthia configuration.
---

# Synthia Handoff Orientation Skill

This skill belongs to the ADK exercise workspace. It is paired with the YAML exercise in `my_config_agent/root_agent.yaml`.

It must not modify the real Synthia repository.

## Purpose

Turn the Synthia-oriented YAML exercise into a skill-style handoff procedure:

- identify the real public Synthia source;
- avoid guessing Synthia state;
- separate stable contract, evidence, and working context;
- produce a small handoff packet for Codex/OpenAI or Antigravity/Gemini;
- keep the real Synthia repo outside the exercise.

## Required source anchors

- Public repository: `https://github.com/SeCuReDmE-main-dev/Synthia`
- Local checkout when available: `Z:\SecuredMe Education suite\Synthia`
- Organisation-only notes: `Z:\SecuredMe Education suite\Synthia\_organisation`
- Governance entrypoint: `AGENTS.md`
- Public entrypoints: `README.md`, `docs/public/index.md`, `docs/public/architecture.md`, `docs/public/interfaces.md`, `docs/public/operations.md`, `docs/public/webmcp.md`
- Adapter contracts when present:
  - `.codex/plugins/securedme-synthia-codex-adapter/skills/securedme-synthia-codex-adapter/SKILL.md`
  - `.antigravity/skills/securedme-synthia-antigravity-adapter/SKILL.md`

## Procedure

1. Verify which Synthia source files were actually read.
2. If not read, mark Synthia state as unverified.
3. Build a handoff packet with:
   - lane;
   - stable contract;
   - evidence paths;
   - uncertainty;
   - blocked actions;
   - next reversible action.
4. Keep the packet compact.
5. Do not copy the whole orchestrator context.

## Output

Return a concise handoff packet and a single next action that can be verified against the real Synthia repository later.


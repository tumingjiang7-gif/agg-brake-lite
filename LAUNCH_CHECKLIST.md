# AGG Brake Lite Launch Checklist

## Before Publish

- Set the final payment link in [README.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/README.md).
- Verify the package installs with `pip install -e .`.
- Run [examples/basic_usage.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/basic_usage.py).
- Confirm local log creation and anonymous export both work.
- Re-read the disclaimer text once before publishing.

## Repository Surface

- Keep the repository small:
  - [README.md](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/README.md)
  - [src/agg_brake_lite/core.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/src/agg_brake_lite/core.py)
  - [examples/basic_usage.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/basic_usage.py)
  - [examples/templates/langchain_example.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/templates/langchain_example.py)
  - [examples/templates/crewai_example.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/templates/crewai_example.py)
  - [examples/templates/autogpt_example.py](/mnt/e/agpt/automaton_unpacked/automaton-main/sdk/agg_brake_lite/examples/templates/autogpt_example.py)
- Do not add dashboards, cloud workers, or extra automation before first signal.

## Publish Window

- Day 0:
  - publish repository
  - publish one payment link
  - make one small announcement set
- Day 3:
  - check whether anyone paid, exported logs, or reported real integration use
- Day 14:
  - continue only if at least one real signal exists

## Real Signals

- Stranger paid
- Stranger exported anonymous logs
- Stranger shared a real integration use case

## Not Signals

- Stars only
- Downloads only
- Nice idea comments
- General curiosity without installation

#!/usr/bin/env python3
"""Wrapper for finalizing Codex session distillation metadata."""

from context_bridge import main


if __name__ == "__main__":
    raise SystemExit(main(["finalize-session-distillation", *(__import__("sys").argv[1:])]))

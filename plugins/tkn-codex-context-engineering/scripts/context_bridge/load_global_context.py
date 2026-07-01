#!/usr/bin/env python3
"""Wrapper for read-only loading selected user-global Codex context."""

from context_bridge import main


if __name__ == "__main__":
    raise SystemExit(main(["load", *(__import__("sys").argv[1:])]))


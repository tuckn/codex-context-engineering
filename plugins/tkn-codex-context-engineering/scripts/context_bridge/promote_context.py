#!/usr/bin/env python3
"""Wrapper for promoting repository context into user-global Codex context."""

from context_bridge import main


if __name__ == "__main__":
    raise SystemExit(main(["promote", *(__import__("sys").argv[1:])]))


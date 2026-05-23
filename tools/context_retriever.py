#!/usr/bin/env python3
import json
import os
import argparse
from pathlib import Path

MEMORY_DIR = Path("memory")

def ensure_dir():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

def load_json(filepath):
    if not filepath.exists():
        return {}
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def save_json(filepath, data):
    ensure_dir()
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def set_global_pref(key, value):
    filepath = MEMORY_DIR / "global_preferences.json"
    data = load_json(filepath)
    data[key] = value
    save_json(filepath, data)
    print(f"Set global preference: {key} = {value}")

def get_global_pref(key=None):
    filepath = MEMORY_DIR / "global_preferences.json"
    data = load_json(filepath)
    if key:
        val = data.get(key)
        print(json.dumps({key: val}, indent=2) if val else f"Preference '{key}' not found.")
    else:
        print(json.dumps(data, indent=2))

def add_course_context(course_id, key, value):
    filepath = MEMORY_DIR / f"{course_id}_context.json"
    data = load_json(filepath)
    data[key] = value
    save_json(filepath, data)
    print(f"Added context to {course_id}: {key} = {value}")

def get_course_context(course_id, key=None):
    filepath = MEMORY_DIR / f"{course_id}_context.json"
    data = load_json(filepath)
    if not data:
        print(f"No context found for course {course_id}.")
        return
    
    if key:
        val = data.get(key)
        print(json.dumps({key: val}, indent=2) if val else f"Context '{key}' not found in {course_id}.")
    else:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Memory and Context Retriever for OpenCode Swarm")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Global Prefs
    parser_set_pref = subparsers.add_parser("set_pref", help="Set a global user preference")
    parser_set_pref.add_argument("key", help="Preference key (e.g., default_citation_style)")
    parser_set_pref.add_argument("value", help="Preference value (e.g., APA)")

    parser_get_pref = subparsers.add_parser("get_pref", help="Get a global user preference")
    parser_get_pref.add_argument("--key", help="Specific preference key (optional)")

    # Course Context
    parser_add_ctx = subparsers.add_parser("add_context", help="Add context to a specific course")
    parser_add_ctx.add_argument("course_id", help="Course identifier (e.g., CS101)")
    parser_add_ctx.add_argument("key", help="Context key (e.g., syllabus_summary, professor_name)")
    parser_add_ctx.add_argument("value", help="Context value")

    parser_get_ctx = subparsers.add_parser("get_context", help="Get context for a specific course")
    parser_get_ctx.add_argument("course_id", help="Course identifier")
    parser_get_ctx.add_argument("--key", help="Specific context key (optional)")

    args = parser.parse_args()

    if args.command == "set_pref":
        set_global_pref(args.key, args.value)
    elif args.command == "get_pref":
        get_global_pref(args.key)
    elif args.command == "add_context":
        add_course_context(args.course_id, args.key, args.value)
    elif args.command == "get_context":
        get_course_context(args.course_id, args.key)

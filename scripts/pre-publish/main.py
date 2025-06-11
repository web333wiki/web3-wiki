#!/usr/bin/env python3
"""
main.py - Pre-publish validation orchestrator for Web3 Wiki

This script serves as the main entry point for all pre-publish validations.
It coordinates the execution of individual validation scripts to ensure
all cards meet the required standards before publication.

The script performs the following validations:
1. Card naming conventions
2. Category tag requirements

Exit codes:
- 0: All validations passed
- 1: One or more validations failed
"""

import sys
import os
import subprocess
from pathlib import Path
from typing import List, Tuple


def get_script_path(script_name: str) -> Path:
    """Get the full path to a validation script."""
    current_dir = Path(__file__).parent
    return current_dir / script_name


def run_validation_script(script_name: str, description: str) -> Tuple[bool, str]:
    """
    Run a validation script and return the result.
    
    Args:
        script_name: Name of the script file to run
        description: Human-readable description of what the script does
        
    Returns:
        Tuple of (success: bool, output: str)
    """
    script_path = get_script_path(script_name)
    
    if not script_path.exists():
        return False, f"Validation script '{script_name}' not found"
    
    try:
        print(f"\n{'='*60}")
        print(f"Running: {description}")
        print(f"Script: {script_name}")
        print(f"{'='*60}")
        
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            cwd=Path.cwd()  # Ensure we run from the project root
        )
        
        # Print the output regardless of success/failure
        if result.stdout.strip():
            print(result.stdout)
        if result.stderr.strip():
            print(result.stderr, file=sys.stderr)
        
        success = result.returncode == 0
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"\nStatus: {status}")
        
        return success, result.stdout + result.stderr
        
    except Exception as e:
        error_msg = f"Error executing {script_name}: {e}"
        print(f"❌ FAILED: {error_msg}", file=sys.stderr)
        return False, error_msg


def main() -> int:
    """
    Main validation orchestrator.
    
    Runs all validation scripts in the correct order and reports results.
    Returns 0 if all validations pass, 1 if any fail.
    """
    print("🚀 Starting Web3 Wiki Pre-publish Validation")
    print(f"Working directory: {Path.cwd()}")
    
    # Define validations in execution order
    validations = [
        ("check-tag.py", "Category Tag Validation"),
        ("check-card-name.py", "Card Name Convention Validation"),
    ]
    
    # Track results
    results: List[Tuple[str, bool, str]] = []
    all_passed = True
    
    # Run each validation
    for script_name, description in validations:
        success, output = run_validation_script(script_name, description)
        results.append((description, success, output))
        
        if not success:
            all_passed = False
    
    # Print summary
    print(f"\n{'='*60}")
    print("📊 VALIDATION SUMMARY")
    print(f"{'='*60}")
    
    for description, success, _ in results:
        status = "✅ PASSED" if success else "❌ FAILED"
        print(f"{status} {description}")
    
    if all_passed:
        print(f"\n🎉 All validations passed! Ready for publication.")
        return 0
    else:
        failed_count = sum(1 for _, success, _ in results if not success)
        print(f"\n💥 {failed_count} validation(s) failed. Please fix the issues above before publication.")
        return 1


if __name__ == "__main__":
    sys.exit(main())



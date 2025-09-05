#!/usr/bin/env python3
"""
Check required sections in PRP document
"""

import sys
import re
from pathlib import Path

def check_sections(file_path: str) -> bool:
    """Check that all required sections are present in the PRP"""
    
    required_sections = {
        "GOAL": r"##\s+GOAL",
        "WHY": r"##\s+WHY", 
        "WHAT": r"##\s+WHAT",
        "MUST READ": r"##\s+MUST READ",
        "IMPLEMENTATION": r"##\s+IMPLEMENTATION",
        "VALIDATION": r"##\s+VALIDATION"
    }
    
    optional_sections = {
        "Success Criteria": r"###?\s+Success Criteria",
        "Dependencies": r"##\s+DEPENDENCIES",
        "Rollback": r"##\s+ROLLBACK",
        "Notes": r"##\s+NOTES"
    }
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    missing_required = []
    found_sections = []
    missing_optional = []
    
    # Check required sections
    for section_name, pattern in required_sections.items():
        if re.search(pattern, content, re.IGNORECASE):
            found_sections.append(section_name)
        else:
            missing_required.append(section_name)
    
    # Check optional sections
    for section_name, pattern in optional_sections.items():
        if not re.search(pattern, content, re.IGNORECASE):
            missing_optional.append(section_name)
    
    # Print results
    print(f"\n📋 Section Check for: {Path(file_path).name}")
    print("="*50)
    
    if found_sections:
        print("\n✅ Required sections found:")
        for section in found_sections:
            print(f"   • {section}")
    
    if missing_required:
        print("\n❌ Missing REQUIRED sections:")
        for section in missing_required:
            print(f"   • {section}")
    
    if missing_optional:
        print("\n⚠️  Missing optional sections (consider adding):")
        for section in missing_optional:
            print(f"   • {section}")
    
    # Check section order
    print("\n📏 Section Order Check:")
    section_positions = {}
    for section_name, pattern in required_sections.items():
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            section_positions[section_name] = match.start()
    
    expected_order = ["GOAL", "WHY", "WHAT", "MUST READ", "IMPLEMENTATION", "VALIDATION"]
    actual_order = sorted(section_positions.keys(), key=lambda x: section_positions.get(x, float('inf')))
    
    if actual_order == expected_order[:len(actual_order)]:
        print("   ✅ Sections are in recommended order")
    else:
        print("   ⚠️  Sections are not in recommended order")
        print(f"   Expected: {' → '.join(expected_order)}")
        print(f"   Found:    {' → '.join(actual_order)}")
    
    print("\n" + "="*50)
    
    if missing_required:
        print("❌ FAILED: Missing required sections")
        return False
    else:
        print("✅ PASSED: All required sections present")
        return True


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python check_sections.py <prp-file.md>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    success = check_sections(file_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
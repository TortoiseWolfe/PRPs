#!/usr/bin/env python3
"""
Check markdown formatting and structure
"""

import sys
import re
from pathlib import Path

def check_markdown(file_path: str) -> bool:
    """Validate markdown formatting"""
    
    issues = []
    warnings = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            content = ''.join(lines)
    except Exception as e:
        print(f"Error reading file: {e}")
        return False
    
    print(f"\n📝 Markdown Check for: {Path(file_path).name}")
    print("="*50)
    
    # Check for title (H1)
    h1_lines = [i for i, line in enumerate(lines) if line.startswith('# ')]
    if len(h1_lines) == 0:
        issues.append("No H1 title found (should start with '# ')")
    elif len(h1_lines) > 1:
        issues.append(f"Multiple H1 headers found on lines: {h1_lines}")
    else:
        print(f"✅ Title found on line {h1_lines[0] + 1}")
    
    # Check header hierarchy
    header_pattern = r'^(#{1,6})\s+'
    headers = []
    for i, line in enumerate(lines):
        match = re.match(header_pattern, line)
        if match:
            level = len(match.group(1))
            headers.append((i + 1, level, line.strip()))
    
    # Check for skipped header levels
    prev_level = 1
    for line_num, level, header in headers[1:]:  # Skip H1
        if level > prev_level + 1:
            warnings.append(f"Line {line_num}: Skipped header level (H{prev_level} → H{level})")
        prev_level = level
    
    # Check for code blocks
    code_blocks = re.findall(r'```[\s\S]*?```', content)
    if code_blocks:
        print(f"✅ Found {len(code_blocks)} code block(s)")
        
        # Check for language specification
        unspecified = len(re.findall(r'```\n', content))
        if unspecified > 0:
            warnings.append(f"{unspecified} code block(s) without language specification")
    else:
        warnings.append("No code blocks found - consider adding examples")
    
    # Check for lists
    bullet_lists = len(re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE))
    numbered_lists = len(re.findall(r'^\s*\d+\.\s+', content, re.MULTILINE))
    checkbox_lists = len(re.findall(r'^\s*-\s*\[[x\s]\]', content, re.MULTILINE | re.IGNORECASE))
    
    if bullet_lists + numbered_lists + checkbox_lists > 0:
        print(f"✅ Lists found: {bullet_lists} bullet, {numbered_lists} numbered, {checkbox_lists} checkbox")
    else:
        warnings.append("No lists found - consider using lists for better organization")
    
    # Check for links
    markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    raw_urls = re.findall(r'(?<!\()https?://[^\s\)]+', content)
    
    if markdown_links:
        print(f"✅ Found {len(markdown_links)} formatted link(s)")
    
    if raw_urls:
        warnings.append(f"Found {len(raw_urls)} raw URL(s) - consider using markdown link format")
    
    # Check line length
    long_lines = []
    for i, line in enumerate(lines):
        # Skip code blocks and URLs
        if not line.strip().startswith('```') and 'http' not in line:
            if len(line.rstrip()) > 120:
                long_lines.append(i + 1)
    
    if long_lines[:5]:  # Show first 5
        warnings.append(f"Long lines (>120 chars) on lines: {long_lines[:5]}...")
    
    # Check for trailing whitespace
    trailing_spaces = [i + 1 for i, line in enumerate(lines) if line.rstrip() != line.rstrip('\n').rstrip('\r')]
    if trailing_spaces[:5]:
        warnings.append(f"Trailing whitespace on lines: {trailing_spaces[:5]}...")
    
    # Check for consistent list markers
    if '-' in content and '*' in content:
        different_markers = []
        for i, line in enumerate(lines):
            if re.match(r'^\s*[-*]\s+', line):
                different_markers.append(i + 1)
        if different_markers[:3]:
            warnings.append("Mixed list markers (- and *) - use consistent markers")
    
    # Check for empty sections
    for i in range(len(headers) - 1):
        current_line = headers[i][0]
        next_line = headers[i + 1][0]
        content_between = ''.join(lines[current_line:next_line - 1]).strip()
        if len(content_between) < 50:
            warnings.append(f"Section '{headers[i][2]}' appears to be empty or very short")
    
    # Print results
    print("\n📊 Results:")
    
    if issues:
        print("\n❌ Issues found:")
        for issue in issues:
            print(f"   • {issue}")
    
    if warnings:
        print("\n⚠️  Warnings:")
        for warning in warnings:
            print(f"   • {warning}")
    
    if not issues and not warnings:
        print("   ✅ Markdown formatting looks good!")
    
    print("\n" + "="*50)
    
    if issues:
        print("❌ FAILED: Markdown has formatting issues")
        return False
    else:
        print("✅ PASSED: Markdown is properly formatted")
        return True


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python check_markdown.py <prp-file.md>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    success = check_markdown(file_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
PRP Validation Script
Validates that a PRP follows Cole Medin's template structure and best practices
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple, Dict

class PRPValidator:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)
        self.content = ""
        self.lines = []
        self.errors = []
        self.warnings = []
        self.info = []
        
    def load_file(self) -> bool:
        """Load the PRP file content"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
                self.lines = self.content.split('\n')
            return True
        except FileNotFoundError:
            self.errors.append(f"File not found: {self.file_path}")
            return False
        except Exception as e:
            self.errors.append(f"Error reading file: {e}")
            return False
    
    def check_required_sections(self) -> None:
        """Check for all required PRP sections"""
        required_sections = [
            ("## GOAL", "GOAL section is missing"),
            ("## WHY", "WHY section is missing"),
            ("## WHAT", "WHAT section is missing"),
            ("## MUST READ", "MUST READ context section is missing"),
            ("## IMPLEMENTATION", "IMPLEMENTATION APPROACH section is missing"),
            ("## VALIDATION", "VALIDATION GATES section is missing")
        ]
        
        for section, error_msg in required_sections:
            if section not in self.content:
                self.errors.append(error_msg)
        
        # Check for Success Criteria
        if "Success Criteria" not in self.content and "### Success Criteria" not in self.content:
            self.warnings.append("Success Criteria subsection is recommended in WHAT section")
    
    def check_goal_section(self) -> None:
        """Validate GOAL section quality"""
        goal_match = re.search(r'## GOAL\n+(.*?)(?=\n##|\Z)', self.content, re.DOTALL)
        if goal_match:
            goal_content = goal_match.group(1).strip()
            
            # Check length
            if len(goal_content) < 50:
                self.warnings.append("GOAL section seems too short. Be more specific about what needs to be built")
            
            # Check for vague terms
            vague_terms = ['improve', 'enhance', 'better', 'optimize', 'somehow', 'maybe']
            for term in vague_terms:
                if term.lower() in goal_content.lower():
                    self.warnings.append(f"GOAL section contains vague term '{term}'. Be more specific")
    
    def check_why_section(self) -> None:
        """Validate WHY section quality"""
        why_match = re.search(r'## WHY\n+(.*?)(?=\n##|\Z)', self.content, re.DOTALL)
        if why_match:
            why_content = why_match.group(1).strip()
            
            # Check for business value
            if not any(word in why_content.lower() for word in ['value', 'benefit', 'improve', 'reduce', 'increase', 'save']):
                self.warnings.append("WHY section should clearly state business value or user benefit")
            
            # Check for metrics
            if not re.search(r'\d+[%$]?|\$\d+|percent|hours?|minutes?|days?', why_content):
                self.info.append("Consider adding specific metrics to WHY section (%, time, money)")
    
    def check_success_criteria(self) -> None:
        """Check for checkbox success criteria"""
        criteria_pattern = r'- \[ \].*'
        criteria_matches = re.findall(criteria_pattern, self.content)
        
        if len(criteria_matches) < 3:
            self.warnings.append(f"Only {len(criteria_matches)} success criteria found. Aim for at least 5 specific criteria")
        
        # Check for measurable criteria
        for criterion in criteria_matches:
            if not any(word in criterion.lower() for word in ['can', 'able', 'success', 'complete', 'pass', 'meet', 'achieve']):
                self.info.append("Success criteria should be measurable and testable")
                break
    
    def check_context_section(self) -> None:
        """Validate context section has proper structure"""
        context_match = re.search(r'## MUST READ.*?\n(.*?)(?=\n##|\Z)', self.content, re.DOTALL)
        if context_match:
            context_content = context_match.group(1)
            
            # Check for URLs
            url_pattern = r'https?://[^\s]+'
            urls = re.findall(url_pattern, context_content)
            if len(urls) < 1:
                self.info.append("Consider adding relevant documentation URLs to context")
            
            # Check for 'why' explanations
            if 'why:' not in context_content.lower():
                self.warnings.append("Context items should explain 'why' they're important")
            
            # Check for file references
            if 'file:' in context_content.lower() or 'path:' in context_content.lower():
                self.info.append("Good: File references found in context")
    
    def check_implementation_section(self) -> None:
        """Validate implementation approach"""
        impl_match = re.search(r'## IMPLEMENTATION.*?\n(.*?)(?=\n##|\Z)', self.content, re.DOTALL)
        if impl_match:
            impl_content = impl_match.group(1)
            
            # Check for phases
            phase_count = len(re.findall(r'Phase \d+|### Phase', impl_content, re.IGNORECASE))
            if phase_count < 2:
                self.warnings.append("Consider breaking implementation into multiple phases")
            
            # Check for action verbs
            action_verbs = ['CREATE', 'MODIFY', 'DELETE', 'IMPLEMENT', 'UPDATE', 'CONFIGURE', 'DEPLOY']
            has_action_verbs = any(verb in impl_content for verb in action_verbs)
            if not has_action_verbs:
                self.info.append("Use action verbs (CREATE, MODIFY, etc.) for clear implementation steps")
            
            # Check for error handling mention
            if 'error' not in impl_content.lower() and 'exception' not in impl_content.lower():
                self.warnings.append("Implementation should address error handling")
    
    def check_validation_section(self) -> None:
        """Check validation gates are executable"""
        validation_match = re.search(r'## VALIDATION.*?\n(.*?)(?=\n##|\Z)', self.content, re.DOTALL)
        if validation_match:
            validation_content = validation_match.group(1)
            
            # Check for code blocks with commands
            code_blocks = re.findall(r'```(?:bash|sh|shell)?\n(.*?)\n```', validation_content, re.DOTALL)
            if len(code_blocks) < 1:
                self.warnings.append("Validation section should include executable test commands")
            
            # Check for test types
            test_types = ['unit', 'integration', 'e2e', 'performance', 'security']
            mentioned_tests = [t for t in test_types if t in validation_content.lower()]
            if len(mentioned_tests) < 2:
                self.info.append("Consider adding more test types (unit, integration, e2e, performance)")
    
    def check_dependencies(self) -> None:
        """Check if dependencies are documented"""
        if 'dependencies' in self.content.lower() or 'requirements' in self.content.lower():
            self.info.append("Good: Dependencies section found")
        else:
            self.warnings.append("Consider adding a DEPENDENCIES section listing required libraries/services")
    
    def check_markdown_quality(self) -> None:
        """Check markdown formatting"""
        # Check for proper headers
        h1_count = len(re.findall(r'^# ', self.content, re.MULTILINE))
        h2_count = len(re.findall(r'^## ', self.content, re.MULTILINE))
        
        if h1_count != 1:
            self.warnings.append("Should have exactly one H1 (#) header for the PRP title")
        
        if h2_count < 6:
            self.warnings.append("Missing some H2 (##) section headers")
        
        # Check for code blocks
        if '```' not in self.content:
            self.info.append("Consider adding code examples or command blocks")
    
    def check_completeness_score(self) -> int:
        """Calculate overall completeness score"""
        score = 100
        score -= len(self.errors) * 15
        score -= len(self.warnings) * 5
        return max(0, score)
    
    def validate(self) -> bool:
        """Run all validation checks"""
        if not self.load_file():
            return False
        
        self.check_required_sections()
        self.check_goal_section()
        self.check_why_section()
        self.check_success_criteria()
        self.check_context_section()
        self.check_implementation_section()
        self.check_validation_section()
        self.check_dependencies()
        self.check_markdown_quality()
        
        return len(self.errors) == 0
    
    def print_results(self) -> None:
        """Print validation results"""
        print(f"\n{'='*60}")
        print(f"PRP Validation Report: {self.file_path.name}")
        print(f"{'='*60}\n")
        
        if self.errors:
            print("❌ ERRORS (must fix):")
            for error in self.errors:
                print(f"   • {error}")
            print()
        
        if self.warnings:
            print("⚠️  WARNINGS (should address):")
            for warning in self.warnings:
                print(f"   • {warning}")
            print()
        
        if self.info:
            print("ℹ️  SUGGESTIONS (consider):")
            for info in self.info:
                print(f"   • {info}")
            print()
        
        score = self.check_completeness_score()
        
        if len(self.errors) == 0:
            if len(self.warnings) == 0:
                print("✅ VALIDATION PASSED - Excellent PRP!")
                print(f"   Quality Score: {score}/100")
            else:
                print("✅ VALIDATION PASSED - Good PRP with minor issues")
                print(f"   Quality Score: {score}/100")
        else:
            print("❌ VALIDATION FAILED - Please fix errors")
            print(f"   Quality Score: {score}/100")
        
        print(f"\n{'='*60}")
        
        # Exit with appropriate code
        sys.exit(0 if len(self.errors) == 0 else 1)


def main():
    """Main entry point"""
    if len(sys.argv) != 2:
        print("Usage: python validate_prp.py <prp-file.md>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    validator = PRPValidator(file_path)
    validator.validate()
    validator.print_results()


if __name__ == "__main__":
    main()
#!/usr/bin/env python3
"""
Simple optimization script for the therapy site.
Validates HTML, checks CSS, and provides performance insights.
"""

import os
import subprocess
import sys
from pathlib import Path

def run_command(command, description):
    """Run a command and return success status."""
    print(f"\n🔍 {description}...")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ {description} passed")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"❌ {description} failed")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error running {description}: {e}")
        return False

def check_file_sizes():
    """Check file sizes for performance optimization."""
    print("\n📊 File Size Analysis:")
    
    files_to_check = [
        "index.html",
        "index_uk.html", 
        "css/styles.css",
        "images/profile.jpg"
    ]
    
    total_size = 0
    for file_path in files_to_check:
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            total_size += size
            size_kb = size / 1024
            status = "✅" if size_kb < 100 else "⚠️" if size_kb < 500 else "❌"
            print(f"{status} {file_path}: {size_kb:.1f} KB")
        else:
            print(f"❌ {file_path}: File not found")
    
    total_kb = total_size / 1024
    print(f"\n📦 Total size: {total_kb:.1f} KB")
    
    if total_kb < 500:
        print("✅ Excellent! Site is very lightweight")
    elif total_kb < 1000:
        print("✅ Good! Site size is reasonable")
    else:
        print("⚠️ Consider optimizing file sizes")

def validate_html():
    """Validate HTML files."""
    html_files = ["index.html", "index_uk.html"]
    all_valid = True
    
    for html_file in html_files:
        if os.path.exists(html_file):
            # Simple HTML validation (basic checks)
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Check for basic HTML structure
            checks = [
                ("<!DOCTYPE html>", "DOCTYPE declaration"),
                ("<html", "HTML tag"),
                ("<head>", "Head section"),
                ("<title>", "Title tag"),
                ("<meta charset=", "Character encoding"),
                ("<meta name=\"viewport\"", "Viewport meta tag"),
                ("</html>", "Closing HTML tag")
            ]
            
            print(f"\n🔍 Validating {html_file}:")
            for check, description in checks:
                if check in content:
                    print(f"✅ {description}")
                else:
                    print(f"❌ Missing {description}")
                    all_valid = False
        else:
            print(f"❌ {html_file} not found")
            all_valid = False
    
    return all_valid

def check_accessibility():
    """Check basic accessibility features."""
    print("\n♿ Accessibility Check:")
    
    with open("index.html", 'r', encoding='utf-8') as f:
        content = f.read()
    
    accessibility_checks = [
        ("skip-link", "Skip navigation link"),
        ("alt=", "Image alt attributes"),
        ("aria-label", "ARIA labels"),
        ("lang=", "Language attribute"),
        ("<h1>", "Heading structure (h1)"),
        ("<h2", "Heading structure (h2)"),
        ("role=", "ARIA roles"),
        ("aria-labelledby", "ARIA labelledby"),
        ("aria-hidden", "ARIA hidden"),
        ("loading=", "Image loading attributes")
    ]
    
    for check, description in accessibility_checks:
        if check in content:
            print(f"✅ {description} found")
        else:
            print(f"⚠️ {description} not found")

def check_seo():
    """Check SEO optimization."""
    print("\n🔍 SEO Check:")
    
    with open("index.html", 'r', encoding='utf-8') as f:
        content = f.read()
    
    seo_checks = [
        ("og:", "Open Graph tags"),
        ("twitter:", "Twitter Card tags"),
        ("canonical", "Canonical URL"),
        ("hreflang", "Language alternatives"),
        ("application/ld+json", "Structured data"),
        ("manifest.json", "PWA manifest"),
        ("description", "Meta description")
    ]
    
    for check, description in seo_checks:
        if check in content:
            print(f"✅ {description} found")
        else:
            print(f"⚠️ {description} not found")

def check_performance():
    """Check performance optimizations."""
    print("\n⚡ Performance Check:")
    
    with open("index.html", 'r', encoding='utf-8') as f:
        content = f.read()
    
    performance_checks = [
        ("preload", "Resource preloading"),
        ("loading=", "Image lazy loading"),
        ("rel=\"noopener\"", "Secure external links"),
        ("defer", "Script deferring"),
        ("async", "Async scripts")
    ]
    
    for check, description in performance_checks:
        if check in content:
            print(f"✅ {description} found")
        else:
            print(f"⚠️ {description} not found")
    
    # Check for external dependencies
    external_deps = ["googleapis.com", "cdnjs.cloudflare.com", "fonts.gstatic.com"]
    has_external = any(dep in content for dep in external_deps)
    
    if not has_external:
        print("✅ No external dependencies found")
    else:
        print("⚠️ External dependencies detected")

def main():
    """Main optimization and validation function."""
    print("🚀 Therapy Site Optimization & Validation")
    print("=" * 50)
    
    # Change to script directory
    os.chdir(Path(__file__).parent)
    
    # Run checks
    check_file_sizes()
    html_valid = validate_html()
    check_accessibility()
    check_seo()
    check_performance()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 Summary:")
    
    if html_valid:
        print("✅ HTML validation passed")
    else:
        print("❌ HTML validation failed")
    
    print("\n💡 Recommendations:")
    print("• Keep images optimized and under 100KB")
    print("• Ensure all images have alt text")
    print("• Test with screen readers")
    print("• Validate with real HTML5 validator")
    print("• Run Lighthouse performance audit")
    print("• Test dark mode functionality")
    print("• Verify PWA installation")
    
    print("\n🌐 Test your site:")
    print("• Local: http://localhost:8000")
    print("• HTML Validator: https://validator.w3.org/")
    print("• Accessibility: https://wave.webaim.org/")
    print("• PWA: Chrome DevTools > Application > Manifest")
    print("• Performance: Chrome DevTools > Lighthouse")

if __name__ == "__main__":
    main()
#!/bin/bash
# Auto-generated commit script - 2026-02-06 19:10:25

set -e  # Exit on any error

# Function to print colored output
print_info() { echo -e "\033[34m[INFO]\033[0m $1"; }
print_success() { echo -e "\033[32m[SUCCESS]\033[0m $1"; }
print_error() { echo -e "\033[31m[ERROR]\033[0m $1"; }

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    print_error "Not in a git repository!"
    exit 1
fi

# Get commit message from parameter
if [ $# -eq 0 ]; then
    print_error "Commit message required!"
    echo "Usage: $0 '<commit message>'"
    exit 1
fi

COMMIT_MSG="$1"

print_info "Starting commit process..."
print_info "Commit message: $COMMIT_MSG"

# Pre-commands
print_info "Running pre-commands..."
print_info "Running: python to_html.py beginner/*.md"
eval "python to_html.py beginner/*.md" || {
    print_error "Pre-command failed: $CMD"
    exit 1
}

# Add all changes
print_info "Adding all changes..."
git add .

# Check if there are changes to commit
if git diff --cached --quiet; then
    print_info "No changes to commit"
    exit 0
fi

# Commit changes
print_info "Committing changes..."
git commit -m "$COMMIT_MSG"
print_success "Changes committed successfully"

# Switch to branch: main
print_info "Switching to branch main..."
git checkout main

# Push to repositories
print_info "Pushing to https://github.com/bakedb/linux-transition-guide.git main..."
git push https://github.com/bakedb/linux-transition-guide.git main
print_info "Pushing to https://codeberg.org/bkd/linux-transition-guide.git main..."
git push https://codeberg.org/bkd/linux-transition-guide.git main
print_success "Push completed"

print_success "Commit script completed successfully!"
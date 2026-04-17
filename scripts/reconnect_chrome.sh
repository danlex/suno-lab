#!/bin/bash
# Reconnect Claude Chrome extension by restarting Chrome with claude.ai open
# Usage: ./scripts/reconnect_chrome.sh

echo "Restarting Chrome to reconnect Claude extension..."

# Gracefully quit Chrome
osascript -e 'tell application "Google Chrome" to quit' 2>/dev/null
sleep 2

# Reopen Chrome with claude.ai (triggers extension reconnection)
open -a "Google Chrome" "https://claude.ai"
sleep 5

echo "Chrome restarted with claude.ai open."
echo "The Claude extension should reconnect within 10-15 seconds."
echo "If it doesn't, check chrome://extensions and ensure the Claude extension is enabled."

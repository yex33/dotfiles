#!/bin/bash

# Set keyboard layout in X
$HOME/Documents/scripts/set_keymap.sh

# Start compositor for fancy visuals
picom &

# Unclutter to hide the mouse cursor
unclutter --jitter 10 --start-hidden --fork

# Nitrogen for wallpaper
nitrogen --set-zoom-fill "$HOME/Pictures/wallpaper.jpg" &

# flameshot for screenshots
flameshot &

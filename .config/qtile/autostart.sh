#!/bin/bash

# xrandr script for monitors config
# /home/joe/.screenlayout/dual0.sh

# Compositor
picom &

# Wallpaper
nitrogen --restore &

# keymap
/home/joe/Documents/scripts/set_keymap.sh

# hide cursor
unclutter &

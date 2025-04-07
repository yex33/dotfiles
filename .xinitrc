xrdb -merge ~/.Xresources

# Disable beep
xset -b

# Set keyboard layout in X
$HOME/Documents/scripts/set_keymap.sh

# xrandr script
$HOME/.screenlayout/dual.sh

# Start compositor for fancy visuals
picom &

# Unclutter to hide the mouse cursor
unclutter --jitter 10 --igonre-scrolling --start-hidden --fork

# Nitrogen for wallpaper
nitrogen --set-zoom-fill "$HOME/Pictures/wallpaper.jpg" &

# Start qtile window manage
qtile start

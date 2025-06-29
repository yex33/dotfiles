xrdb -merge ~/.Xresources

# Disable beep
xset -b

# xrandr script
$HOME/.screenlayout/dual.sh

# Start qtile window manage
exec qtile start

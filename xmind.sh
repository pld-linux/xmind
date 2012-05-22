#!/bin/sh
XMIND_CONFIG="${XDG_CONFIG_HOME:-$HOME/.config}/xmind"
if [ ! -d "$XMIND_CONFIG" ]; then
	install -d "$XMIND_CONFIG"
fi
exec @appdir@/XMind_Linux/xmind-bin -configuration $XMIND_CONFIG -data $XMIND_CONFIG "$@"

# PixCodeOS - Developed by [Your Name] with AI as Co-Developer
# AI tools (e.g., Grok) generated code based on my Sator Square equations and vision.

#!/bin/bash
echo "Starting PixCodeOS..."

# Activate virtual environment (adjust path as needed)
if [ -d "/home/bleak/myenv" ]; then
    source /home/bleak/myenv/bin/activate
else
    echo "Virtual environment not found. Installing dependencies..."
    pip3 install -r /usr/local/share/pixcodeos/requirements.txt
fi

# Start Docker if not running
if ! systemctl is-active docker >/dev/null 2>&1; then
    sudo systemctl start docker
    sudo systemctl enable docker
fi

# Launch PixCodeOS GUI
pixcodeos

# Keep the system running
echo "PixCodeOS is running. Press Ctrl+C to exit."
read -r

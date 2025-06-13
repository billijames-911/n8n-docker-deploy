# Start from the official n8n Alpine-based image
FROM n8nio/n8n:latest

# Switch to root user to install packages
USER root

# --- STEP 1: Install system dependencies AND build tools ---
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    chromium \
    chromium-chromedriver \
    build-base \
    python3-dev

# --- STEP 2: Create a virtual environment ---
RUN mkdir -p /home/node/venv && chown node:node /home/node/venv

# Switch back to the node user
USER node

# --- STEP 3: Create venv and install packages into it ---
RUN python3 -m venv /home/node/venv

# FIXED: Call pip directly from the venv's full path to avoid instability.
RUN /home/node/venv/bin/pip install --no-cache-dir pandas numpy openpyxl selenium

# --- STEP 4: Copy your Python scripts ---
COPY scripts/py-n8n.py /home/node/py-n8n.py
COPY scripts/facebook.py /home/node/facebook.py
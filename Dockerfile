# Start from the official n8n Alpine-based image
FROM n8nio/n8n:latest

# Switch to root user to install packages
USER root

# --- STEP 1: Install system dependencies AND build tools ---
# build-base and python3-dev are CRITICAL for installing numpy/pandas
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    chromium \
    chromium-chromedriver \
    build-base \
    python3-dev

# --- STEP 2: Create a virtual environment ---
# Note: We do not need the ENV VENV_PATH variable for this corrected version
# Create the venv directory and change its ownership to the 'node' user
RUN mkdir -p /home/node/venv && chown node:node /home/node/venv

# Switch back to the node user
USER node

# --- STEP 3: Create venv and install packages into it ---
RUN python3 -m venv /home/node/venv

# FIXED: Call pip directly from the venv's full path.
# This installs the packages correctly without changing the global PATH.
RUN /home/node/venv/bin/pip install --no-cache-dir pandas numpy openpyxl selenium


# --- STEP 4: Copy your Python scripts ---
# This can be done after the environment is fully set up
COPY scripts/py-n8n.py /home/node/py-n8n.py
COPY scripts/facebook.py /home/node/facebook.py

# The Dockerfile is now finished.
# It will inherit the default CMD from the base image to start n8n.
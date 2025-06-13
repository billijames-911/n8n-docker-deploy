# Start from the official n8n Alpine-based image
FROM n8nio/n8n:latest

# Switch to root user to install packages
USER root

# --- STEP 1: Install system dependencies ---
# We only need the base python3 and pip for this test
RUN apk update && apk add --no-cache python3 py3-pip

# --- STEP 2: Create a virtual environment ---
RUN mkdir -p /home/node/venv && chown node:node /home/node/venv

# Switch back to the node user
USER node

# --- STEP 3: Create the venv ---
# No additional packages will be installed for this test
RUN python3 -m venv /home/node/venv

# --- STEP 4: Copy a simple Python script for testing ---
COPY scripts/test_simple.py /home/node/test_simple.py

# The Dockerfile is now finished.
# It will inherit the default CMD from the base image to start n8n.
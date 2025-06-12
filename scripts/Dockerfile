FROM n8nio/n8n:latest

USER root

# Install Python, Chromium, and dependencies
RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
    py3-virtualenv \
    chromium \
    wget \
    unzip

# Create virtual environment
ENV VENV_PATH=/opt/venv
RUN python3 -m venv $VENV_PATH
ENV PATH="$VENV_PATH/bin:$PATH"

# Install Python packages
RUN pip install --no-cache-dir pandas numpy openpyxl selenium

# Install ChromeDriver that matches Chromium v136
RUN wget https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.113/linux64/chromedriver-linux64.zip && \
    unzip chromedriver-linux64.zip && \
    mv chromedriver-linux64/chromedriver /usr/bin/chromedriver && \
    chmod +x /usr/bin/chromedriver && \
    rm -rf chromedriver-linux64*

# Set environment variables for Chrome
ENV CHROME_BIN=/usr/bin/chromium-browser
ENV CHROMIUM_PATH=/usr/lib/chromium/chrome
ENV PATH=$PATH:/usr/lib/chromium/

USER node

# Copy Python scripts
COPY scripts/py-n8n.py /home/node/py-n8n.py
COPY scripts/facebook.py /home/node/facebook.py

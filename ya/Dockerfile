FROM python:3.12
WORKDIR /app/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY src .

# Setup an app user so the container doesn't run as the root user
RUN useradd house_pred_app
USER house_pred_app

CMD ["uvicorn", "fast_api_server:app", "--host", "0.0.0.0", "--port", "7844"]

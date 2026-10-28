FROM python:3.13.7-alpine3.22

WORKDIR /app

COPY requirements.txt .
RUN apk upgrade --no-cache \
    && pip install --no-cache-dir --upgrade -r requirements.txt \
    && pip uninstall --yes pip \
    && addgroup --system app \
    && adduser --system --ingroup app app

COPY app.py .

ARG APP_VERSION=dev
ENV APP_VERSION=${APP_VERSION}
USER app
EXPOSE 5000

CMD ["python", "app.py"]
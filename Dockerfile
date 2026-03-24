FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install \
    --no-cache-dir \
    --default-timeout=100 \
    -i https://pypi.tuna.tsinghua.edu.cn/simple \
    -r requirements.txt

COPY . .

EXPOSE 8000

# 0.0.0.0 is required in Docker so port publishing works; browse http://localhost:8000 on the host.
CMD sh -c "echo '' && echo '  >>> Open in browser: http://localhost:8000' && echo '' && python manage.py runserver 0.0.0.0:8000"
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# Flask 및 MySQL 연결 라이브러리 설치
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Flask 앱 파일 복사
COPY app.py .

# Flask 실행
CMD ["python", "app.py"]


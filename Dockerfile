FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

CMD ["streamlit", "run","streamlit.py" , "--host", "0.0.0.0", "--port", "80"] 
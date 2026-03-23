FROM python:3.11-slim

WORKDIR /app

RUN pip install flask --no-cache-dir

COPY income_tax_calculator.py .

EXPOSE 5000

CMD ["python", "income_tax_calculator.py"]

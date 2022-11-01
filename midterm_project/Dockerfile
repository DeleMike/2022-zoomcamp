FROM python:3.8.13-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["predict.py", "xgb_model_with_dv_eta=0.1_max_depth=6_min_child_weight=1.bin", "./"]

EXPOSE 9696

# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"] --- for linux/unix/Mac
# for Windows App
ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]  
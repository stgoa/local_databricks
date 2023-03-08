FROM jupyter/pyspark-notebook as base
WORKDIR /local_databricks
COPY pyproject.toml ./
ADD /pipeline ./pipeline
ADD /local ./local
ENV PYTHONPATH "${PYTHONPATH}:./"
RUN python -m pip install --upgrade pip 
RUN pip install poetry 
RUN poetry config virtualenvs.create false 
RUN poetry install --no-dev --no-interaction --no-ansi
RUN pip install numpy==1.23.1
# https://github.com/apache/spark/blob/v3.4.0-rc1/python/pyspark/sql/pandas/conversion.py#L301


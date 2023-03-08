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


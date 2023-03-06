FROM python:3.9 as base
WORKDIR /local_databricks
COPY pyproject.toml ./
ADD /local_databricks ./local_databricks
ENV PYTHONPATH "${PYTHONPATH}:./"
RUN python -m pip install --upgrade pip \
    && pip install poetry \
    &&poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
# Test image
FROM base as tester
COPY tests ./tests
RUN pip install pytest && pytest -s -vvv
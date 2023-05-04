FROM  3.10.4-alpine
WORKDIR /app
COPY ./pyproject.toml ./
RUN 
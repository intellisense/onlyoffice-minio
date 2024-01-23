Example of configuring [OnlyOffice DocumentServer](https://github.com/ONLYOFFICE/DocumentServer) Cache with S3-Like storage (e.g., [Minio](https://min.io/)).

## Prerequisites
- [Docker](https://www.docker.com/)

## Testing
1. Clone the repository
    ```bash
    git clone git@github.com:intellisense/onlyoffice-minio.git
    ```
2. Create a `.env` file with the following variables:
    ```
    AWS_ACCESS_KEY_ID=minio-access-key
    AWS_SECRET_ACCESS_KEY=minio-secret-key
    ENDPOINT_URL="http://minio:9000"
    BUCKET_NAME=onlyoffice
    ```
3. Run `docker compose up --build`
4. Allow some time for the OnlyOffice DocumentServer to fully start.
5. Open the browser and visit the OnlyOffice DocumentServer healthcheck URL at http://127.0.0.1/healthcheck; it should respond with `true`.
   - If it responds with `false` check `onlyoffice-documentserver` container logs.

## Validating connectivity with Minio
The `main.py` file includes a straightforward function to verify S3 storage connectivity by uploading a file and listing keys from an existing bucket (specified in `.env.BUCKET_NAME`). This script runs automatically, and the `test-app` container should exit with code `0`. Check the logs for validation by executing:

```bash
docker logs test-app
```

You should observe the following logs:

```bash
Uploading file "assets/sample.pdf" to S3 bucket "onlyoffice".
File "assets/sample.pdf" uploaded successfully to S3 bucket "onlyoffice".
Listing keys in S3 bucket "onlyoffice"
sample.pdf
```

To further confirm the successful upload, you can also check the Minio console:

1. Login to Minio console http://127.0.0.1:9001.
   - Use the `AWS_ACCESS_KEY_ID` value from the `.env` file as the username and the `AWS_SECRET_ACCESS_KEY` value as the password.
2. Visit the bucket at http://127.0.0.1:9001/browser/onlyoffice to ensure that the file `sample.pdf` is present.

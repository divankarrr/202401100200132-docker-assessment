# FestPass Docker and Container Security Assessment

## Personal values

- Name: **Divankar Singh**
- REGNO: **202401100200132**
- PORT: **8032**
- Docker Hub username: **devakarz2428**
- Docker Hub repository: `https://hub.docker.com/r/devakarz2428/fest-backend`

## Run locally

```bash
cp .env.example .env
# Set a strong local POSTGRES_PASSWORD in .env.
docker compose up -d --build
curl http://localhost:8032/api/health
```

The frontend is on `frontend-backend`; only the backend is also on the
`backend-db` network. PostgreSQL data is stored in the `postgres-data` named
volume.

## Security evidence

Run the following commands on the assessment machine and save their output in
the `reports/` and `screenshots/` directories:

```bash
mkdir -p reports
trivy image fest-backend:0.1 | tee reports/trivy-before.txt
trivy image fest-backend:0.2 | tee reports/trivy-after.txt
trivy image --severity CRITICAL --ignore-unfixed --exit-code 1 fest-backend:0.2
echo $?
```

| Image | CRITICAL | HIGH | Size |
|---|---:|---:|---:|
| `fest-backend:0.1` | 234 | 2,243 | 1,596,413,737 bytes |
| `fest-backend:0.2` | 0 | 0 | 110,307,495 bytes |

## Versioning, publishing, and signing

```bash
docker build --build-arg APP_VERSION=1.0.0 -t devakarz2428/fest-backend:1.0.0 backend
docker tag devakarz2428/fest-backend:1.0.0 devakarz2428/fest-backend:1.0
docker push devakarz2428/fest-backend:1.0.0
docker push devakarz2428/fest-backend:1.0

cosign generate-key-pair
cosign sign --key cosign.key devakarz2428/fest-backend@<digest-from-push>
cosign verify --key cosign.pub devakarz2428/fest-backend@<digest-from-push>
```

The private key, registry credentials, and `.env` must never be committed.
Record the pushed `1.0.0` digest here:

`1.0.0 digest: sha256:dcf7a70f2aa5415a864ed443dc7c0a79aaae3121eacd8ef1902479e320bb3b8f`

Build `1.0.1` without signing it and verify that `cosign verify` rejects it.
The unsigned `1.0.1` digest published during this setup is
`sha256:6d6bd19b278f3b4b824433f30f16416c231af8a9d30974f2be5d2decba2390d7`.

## AI tools

GitHub Copilot (Copilot SDK in VS Code) was used to help inspect the
assessment requirements, implement the container configuration, and review
the application changes. All commands, builds, scans, and release actions
must be run and verified by the student.

## Incomplete evidence

- Docker Hub screenshots and cosign verification still need to be captured
- locally after publishing and key generation. `cosign` is not installed in
  the current environment, so no signing key or signature was created.

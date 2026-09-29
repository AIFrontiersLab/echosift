# EchoSift

Convert passive meeting audio into structured, searchable action items and summaries without active bot participation.

# Simple Query MVP

A minimal FastAPI service that processes text queries.

## Usage

Run the server:
uvicorn main:app --reload

Test it:
pytest -q

## Architecture

![Architecture](docs/architecture.png)

<details>
<summary>Mermaid source</summary>

```mermaid
flowchart LR
    A[Client] --> B[FastAPI]
    B --> C{Validate Text}
    C -->|Empty| D[400 Error]
    C -->|Valid| E[Process Text]
    E --> F[Generate SHA-256]
    F --> G[Return Result & Hash]
```

</details>

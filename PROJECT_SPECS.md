# JobTracker AI — Engineering Specification & Sprint Roadmap

## 1. Overview
A cloud-native, AI-powered Job Application Tracker built with Python and Flask. Replaces manual spreadsheets with a relational database, pipeline analytics, and an automated (human-in-the-loop) AI email follow-up engine.

## 2. Tech Stack (Production-Grade)
- **Language & Framework**: Python 3.12+, Flask (Application Factory Pattern + Blueprints)
- **Database & ORM**: PostgreSQL 16, SQLAlchemy 2.0, Flask-Migrate (Alembic)
- **Validation & Config**: Pydantic / pydantic-settings (12-Factor App config)
- **Async Task Queue**: Celery + Redis (for daily follow-up checks & email scheduling)
- **AI & Email**: Google Gemini API (context-aware multilingual drafts) + SMTP / Gmail API
- **Frontend**: Jinja2 + HTMX + TailwindCSS (interactive UI without heavy SPA complexity)
- **Testing & Code Quality**: Pytest, Coverage, Ruff (Linter/Formatter), pre-commit
- **DevOps & Infrastructure**: Docker, Docker Compose, GitHub Actions (CI/CD), Kubernetes (Deployments, Services, ConfigMaps, Secrets, CronJobs)

## 3. Core Data Model
### `applications`
- `id` (UUID / Primary Key)
- `company` (String, required)
- `role` (String, required)
- `link` (URL String)
- `source` (Enum: LinkedIn, Company Site, Referral, Indeed, Other)
- `applied_date` (Date, default today)
- `cv_language` (Enum: EN, ES, PT, FR, DE, etc.)
- `status` (Enum: Wishlist, Applied, Screening, Technical, Final, Offer, Rejected, Ghosted)
- `work_mode` (Enum: Remote, Hybrid, Onsite)
- `salary_range` (String, optional)
- `job_description` (Text, optional — used as AI context)
- `follow_up_date` (Date, indexed)
- `follow_ups_sent` (Integer, default 0)
- `contact_name` (String, optional)
- `contact_email` (String, optional)
- `notes` (Text — interview notes used as AI context)
- `created_at` / `updated_at` (Timestamps)

### `email_drafts` (AI Follow-up Queue)
- `id` (UUID / Primary Key)
- `application_id` (Foreign Key -> `applications.id`)
- `email_type` (Enum: POST_APPLICATION, THANK_YOU, STATUS_CHECK)
- `subject` (String)
- `body` (Text)
- `status` (Enum: PENDING_APPROVAL, SENT, SKIPPED)
- `scheduled_for` (Date)
- `sent_at` (Timestamp, nullable)

## 4. Agile Sprint Roadmap
- **Sprint 1: Foundation, Git Workflow & Code Quality**
  - Git init, `.gitignore`, virtual environment, `pyproject.toml`, Ruff linter, pre-commit hooks, Flask App Factory skeleton, healthcheck endpoint, and first Pytest test.
- **Sprint 2: Database Layer & Migrations (PostgreSQL + Docker)**
  - Local Postgres via `docker-compose.yml`, SQLAlchemy 2.0 models, Alembic migrations, and CRUD repository/service layer with unit tests.
- **Sprint 3: Web UI & REST/HTMX Endpoints**
  - Dashboard with status filters, Add/Edit Application modals, status transitions (automatically calculating the next `follow_up_date` based on best-practice rules).
- **Sprint 4: AI Email Generator & Background Automation**
  - Prompt engineering service (using `company`, `role`, `cv_language`, `job_description`, and `notes`), Celery + Redis worker calculating due follow-ups, Approval Queue UI, and SMTP email sending.
- **Sprint 5: CI/CD Pipeline & Production Dockerization**
  - Multi-stage `Dockerfile` (non-root user, Gunicorn WSGI server), GitHub Actions workflow (Lint -> Pytest with Postgres container -> Build Docker image).
- **Sprint 6: Kubernetes Deployment & Portfolio Polish**
  - K8s manifests (`Deployment`, `Service`, `ConfigMap`, `Secret`, `CronJob`), running locally on Kind/Minikube, architecture diagram, and portfolio `README.md`.

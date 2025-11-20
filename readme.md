# OilQuest

OilQuest is a turn-based strategy game where players build an oil empire. The journey spans from acquiring acreage and conducting exploration to developing projects, producing oil, and trading with refineries. The game supports single-player and multiplayer modes and is played via a web browser.

## Project Structure

The project is a monorepo organized into the following components:

-   **`backend/`**: A Python FastAPI application.
    -   `main.py`: API entry points and server configuration.
    -   `models.py`: SQLAlchemy database models (Players, Acreage, GameState).
    -   `game_logic.py`: Core game mechanics (World generation, resource distribution).
    -   `database.py`: Database connection logic (handles Local, Docker, and Cloud Run environments).
-   **`frontend/`**: A React application built with Vite and TypeScript.
    -   `src/components/GameMap.tsx`: Interactive map using Leaflet.
    -   `src/App.tsx`: Main application layout and state management.
-   **Infrastructure**:
    -   `docker-compose.yml`: Local development orchestration (Frontend, Backend, PostgreSQL).
    -   `cloudbuild.yaml`: Google Cloud Build configuration for CI/CD.

## End Goals

The ultimate vision for OilQuest includes:

1.  **Exploration**: Identifying promising regions through seismic data, hiring geologists, and drilling exploration wells.
2.  **Appraisal**: Assessing discoveries to determine commercial viability and facility requirements.
3.  **Development**: Sanctioning and executing construction projects for production facilities.
4.  **Operations**: Managing oil production, maintaining facilities, and optimizing output.
5.  **Trading**: Selling crude oil to refineries and managing market fluctuations.
6.  **Multiplayer**: Competing with other players for acreage and resources.

## Implementation Plan & Roadmap

We are currently in the **Exploration & Appraisal** development cycle.

### Phase 1: Foundation (Completed)
-   [x] Basic project setup (FastAPI + React).
-   [x] Docker and Cloud Build integration.
-   [x] World generation (Grid-based map).
-   [x] Basic map visualization.

### Phase 2: Exploration & Appraisal (In Progress)
**Key Objectives:**
-   **Company Management**: Implement hiring of geologists and spies to improve data accuracy.
-   **Seismic Surveys**: Allow players to gather noisy data about acreage potential.
-   **Drilling**: Implement exploration drilling to reveal actual resources (Discovery vs. Dry Hole).
-   **Appraisal**: Add mechanics to study discoveries for reserves and development costs.

**Upcoming Tasks:**
1.  **Backend**:
    -   Update `models.py` with `SeismicSurvey`, `ExplorationWell`, and `Appraisal` tables.
    -   Implement logic for hiring staff and calculating seismic noise.
    -   Create API endpoints for `hire`, `seismic`, `drill`, and `appraise` actions.
2.  **Frontend**:
    -   Create a **Company Dashboard** for managing staff and finances.
    -   Build an **Action Panel** to perform operations on selected acreage.
    -   Visualize seismic data overlays on the map.

### Phase 3: Development & Production (Future)
-   Facility design and construction.
-   Production curves and decline rates.
-   Operational expenditure (OPEX) management.

## Getting Started

### Local Development
1.  Ensure Docker and Docker Compose are installed.
2.  Run the application:
    ```bash
    docker-compose up --build
    ```
3.  Access the frontend at `http://localhost:5173` and the backend docs at `http://localhost:8000/docs`.

### Deployment
The project is configured for Google Cloud Run via Cloud Build. Pushing to the repository triggers a build and deploy pipeline defined in `cloudbuild.yaml`.
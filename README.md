# Westonia

The WestoniaNetwork repository consists of multiple components including a backend API, a frontend web application, and various Docker configurations. This document provides an overview of the project structure, setup instructions, and usage guidelines.

## Backend: WestoniaAPI

The backend for the Westonia project is a RESTful API built with ASP.NET Core 8.0 and Entity Framework Core. It uses a MsSql database to store data and ASP.NET Identity and JWT for authentication.

### Projects

- **WestoniaAPI.Core**: Contains the business logic, data models, interfaces, and services.
- **WestoniaAPI.Infrastructure**: Contains the implementations for database access (via Entity Framework Core) and other external services.

### Getting Started

#### Prerequisites

1. Install the [.NET 8.0 SDK](https://dotnet.microsoft.com/download/dotnet/8.0)
2. Install a MsSQL instance, preferably via Docker

#### Installation

1. Clone the repository: `git clone https://github.com/your-username/WestoniaAPI.git`
2. Navigate to the project directory: `cd WestoniaAPI`
3. Restore the NuGet packages: `dotnet restore`
4. Build the solution: `dotnet build`

#### Configuration

1. Open the `appsettings.json` file in the `WestoniaAPI` project.
2. Update the connection string to point to your MsSQL instance.

#### Database Migration

1. Open a terminal and navigate to the `WestoniaAPI` project directory.
2. Run the following command to apply the database migrations: `dotnet ef database update`

#### Running the API

1. Open a terminal and navigate to the `WestoniaAPI` project directory.
2. Run the following command to start the API: `dotnet run`

## Frontend: WestoniaWeb

The frontend for the Westonia project is built with Vue.js and uses Vuetify for UI components.

### Getting Started

#### Prerequisites

1. Install [Node.js](https://nodejs.org/)
2. Install [Yarn](https://yarnpkg.com/)

#### Installation

1. Navigate to the `WestoniaWeb` directory: `cd WestoniaWeb`
2. Install the dependencies: `yarn install`

#### Running the Development Server

To start the development server with hot-reload, run the following command. The server will be accessible at [http://localhost:3000](http://localhost:3000):

```bash
npm run <configuration[dev, test, prod]>
```

#### Building for Production

To build your project for production, use:

```bash
npm run build<Configuration[Dev, Test, Prod]>
```

Once the build process is completed, your application will be ready for deployment in a production environment.

## Docker

This repository includes Docker configurations to facilitate development and deployment.

### Starting Docker Compose

To start the Docker Compose environment, use the provided batch script.

This script sets the environment file for Docker Compose and starts the services defined in `docker-compose.yaml`.

## License

This project is licensed under the [GPLv3](./LICENSE) license.

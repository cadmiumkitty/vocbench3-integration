# VocBench Integration

Example of VocBench API use to automate creation of users and projects, along with basic set up to run load tests using locust.

## Set up

Create python virtual environment, then install dependencies.

```
pip install -r requirements.txt
```

## Prerequisites

Assumes that you created and enabled an API user with a username and password, and that API user has appropriate permissions. For the load test and for assinging users to projects it assumes that SDG project is created with [Sustainable Development Goals Ontology](http://metadata.un.org/sdg/?lang=en).

## Usage

### Creating and Enabling Users

```
python3 create-users.py <api username> <api password> <VocBench host> <users.csv>
```

### Creating Projects

```
python3 create-projects.py <api username> <api password> <VocBench host> <users.csv>
```

### Assigning Users to Projects

```
python3 assign-users.py <api username> <api password> <VocBench host> <users.csv>
```

### Running Load Test

For a very basic set up, start `locust` and use its local web console at http://localhost:8089/.

```
locust
```
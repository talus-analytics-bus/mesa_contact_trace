mesa_contact_trace
========================

ABM model of infection and testing to determine trade-offs of quantity vs. turn-around time

Create a virtualenv and install requirements.txt, then you can run with `python run.py`
from project root.

or

You can build and run this Docker image with these commands:
*  `$ docker build . -t mesa_contact_trace_image`
*  `$ docker run --name mesa_contact_trace -p 8521:8521/tcp -it mesa_contact_trace_image`

View at http://127.0.0.1:8521


TODO:
* Implement workplace dynamics - create coworkers each agent is more likely than random/less likely than family to contact each day
* Allow for symptomatic-only testing if desired
* Contact tracing
* Quarantine Ignorers
* False positive/negative testing
* Impact from quarantining false positives (more ignorers?)
* Performance improvements

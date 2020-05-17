"""
Configure visualization elements and instantiate a server
"""

from .model import Contact_Trace_Model, Contact_Trace_Agent  # noqa

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import ChartModule
from mesa.visualization.UserParam import UserSettableParameter

percent_sick = ChartModule([{"Label": "Percent Sick", "Color": "Pink"},],)
num_infectious = ChartModule([{"Label": "Number Infectious", "Color": "Green"},],)

model_params = {
    "num_agents": UserSettableParameter("number", "Number of agents", value=1000),
    "num_sick": UserSettableParameter("number", "Number of initial sick", value=1),
    "infection_chance": UserSettableParameter(
        "slider",
        "Chance of infection from encountering infectious person",
        0.01,
        0,
        0.5,
        0.01,
    ),
    "random_contact_mean": UserSettableParameter(
        "slider", "Average number of random contacts per day", 3, 0, 25, 1
    ),
    "random_contact_sd": UserSettableParameter(
        "slider", "Standard deviation of random contacts per day", 1, 1, 5, 1
    ),
    "percent_tested_per_day": UserSettableParameter(
        "slider", "Percent of population tested each day", 0.05, 0, 1, 0.01
    ),
    "turn_around_time": UserSettableParameter(
        "slider", "Days to return test results", 2, 1, 10, 1
    ),
    "false_negative_rate": UserSettableParameter(
        "slider",
        "Percent of total tests that come back negative when agent is infected",
        0.05,
        0,
        1,
        0.01,
    ),
    "false_positive_rate": UserSettableParameter(
        "slider",
        "Percent of total tests that come back positive when agent is not infected",
        0.05,
        0,
        1,
        0.01,
    ),
}

server = ModularServer(
    Contact_Trace_Model,
    [percent_sick, num_infectious],
    "Contact_Trace_Mesa_Model",
    model_params,
)
server.port = 8521

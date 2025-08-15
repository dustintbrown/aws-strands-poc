from strands import Agent
import logging

logging.getLogger("strands").setLevel(logging.DEBUG)

# Sets the logging format and streams logs to stderr
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Create an agent with default settings
agent = Agent()

# Ask the agent a question
agent("Tell me about agentic AI")
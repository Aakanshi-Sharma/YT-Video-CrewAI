from crewai import Agent
from tools import channel_tool

# create a senior blog researcher

blog_researcher = Agent(
    role="Blog Researcher from youtube videos",
    goal="get the relevant video content for the topic {topic} from youtube channel",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI data science, Machine learning and GENAI"
    ),
    tools=[channel_tool],
    allow_delegation=True
)

#  create a senior blog writer agent

blog_writer = Agent(
    role="Blog Researcher from Youtube Videos",
    goal="get the relevant video content for the topic {topic} from youtube channel",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, Machine Learning and GenAI"
    ),
    tools=[channel_tool],
    allow_delegation=True
)

from crewai import Agent

# create a senior blog researcher

blog_researcher = Agent(
    role="Blog Researcher from youtube videos",
    goal="get the relevant video content for the topic {topic} from youtube channel",
    verboe=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI data science, Machine learning and GENAI"
    ),
    tools=[],
    allow_delegation=True
)

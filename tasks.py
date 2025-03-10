from crewai import Task
from tools import channel_tool
from agents import blog_researcher, blog_writer

research_task = Task(
    description=(
        "Identity the video {topic}.",
        "Get detailed information about the video from the channel."
    ),
    expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content',
    tools=[channel_tool],
    agent=blog_researcher
)

writer_task = Task(
    description=(
        "get the info from the youtube channel on the topic {topic}."
    ),
    expected_output="Summarize the info from the youtube channel video on the topic {topic}",
    tools=[channel_tool],
    agent=blog_writer,
    async_execution=False,
    output_file="new-blog-post.md"
)

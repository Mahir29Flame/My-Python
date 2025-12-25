import asyncio
from dotenv import load_dotenv
from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli, llm
from livekit.agents import MultimodalAgent
from livekit.plugins.google.beta import realtime 

load_dotenv()

async def entrypoint(ctx:JobContext):
    initial_ctx = llm.chat_context(
        role = "assistant",
        content = "You are a helpful assistant."
    )
    await ctx.connect(auto_subscribe=AutoSubscribe.Both)

    model = realtime.RealtimeModel(
        model="gemini-live-2.5-flash-native-audio", 
        voice="Puck", # Options: Puck, Kore, Charon, Fenrir, Aoede
    )
    
    assistant = MultimodalAgent(
        model=model,
        chat_ctx=initial_ctx,
    )

    assistant.start(ctx.room)
    await asyncio.sleep(1)
    await assistant.say("Hey, how can i help you today?", allow_interruptions=True)
    

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
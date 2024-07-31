# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from typing_extensions import override
from openai import AssistantEventHandler
from streamlit_extras.buy_me_a_coffee import button
button(username="simjoy", floating=True, width=221)

st.header("리뷰 제조기 🤖")
st.write("🍀 리뷰 업종과 별점을 입력하면 리뷰를 생성해드립니다. 🍀")

from openai import OpenAI
client = OpenAI()
  
assistant = client.beta.assistants.create(
  name="Review Generator",
  instructions="You are a review maker. Once you receive the industry and star rating, create a review according to that.",
  tools=[{"type": "code_interpreter"}],
  model="gpt-4o",
)

thread = client.beta.threads.create()

if 'messages' not in st.session_state:
    st.session_state.messages = []
 
class EventHandler(AssistantEventHandler):    
  @override
  def on_text_created(self, text) -> None:
    print(f"\nassistant > ", end="", flush=True)
      
  @override
  def on_text_delta(self, delta, snapshot):
    print(delta.value, end="", flush=True)
    st.session_state.messages.append(delta.value)
      
  def on_tool_call_created(self, tool_call):
    print(f"\nassistant > {tool_call.type}\n", flush=True)
  
  def on_tool_call_delta(self, delta, snapshot):
    if delta.type == 'code_interpreter':
      if delta.code_interpreter.input:
        print(f"delta.code : {delta.code_interpreter.input}", end="", flush=True)
      if delta.code_interpreter.outputs:
        print(f"\n\n output >", flush=True)
        for output in delta.code_interpreter.outputs:
          if output.type == "logs":
            print(f"\n logs : {output.logs}", flush=True)

with st.form("my_form"):
    upjong = st.text_input("업종을 입력하세요.")
    st.text("별점을 입력하세요.")
    sentiment_mapping = ["one", "two", "three", "four", "five"]
    star = st.feedback("stars")
    submitted = st.form_submit_button("리뷰 생성")
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="업종: " + upjong + ", 별점: " + str(star) + "점 이라고 입력했습니다. 리뷰를 생성해주세요. 그리고 이모지도 넣어서 리뷰를 마무리해주세요."
    )
    if submitted:
        with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant.id,
            instructions="이모지는 중간중간에 넣어주세요. 문장은 최대 4줄로 완성시켜줘.",
            event_handler=EventHandler(),
        ) as stream:
            stream.until_done()
        
        st.write_stream(st.session_state.messages)

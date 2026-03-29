import streamlit as st
from agents.schedule_agent import ScheduleAgent
from agents.notes_agent import NotesAgent
from agents.task_agent import TaskAgent

# Initialize agents
schedule_agent = ScheduleAgent()
notes_agent = NotesAgent()
task_agent = TaskAgent()

# Streamlit UI
st.title("🧠 Multi-Agent Productivity Assistant")
st.write("Starting Multi-Agent AI Assistant...")

st.subheader("📅 Schedule")
schedule_input = st.text_input("Add a Schedule Item")
if st.button("Add Schedule"):
    schedule_agent.add_schedule(schedule_input)
    st.success(f"Schedule added: {schedule_input}")

if st.button("View Schedule"):
    schedules = schedule_agent.get_schedules()
    st.write(schedules if schedules else "No schedules yet.")

st.subheader("📝 Notes")
note_input = st.text_area("Add a Note")
if st.button("Add Note"):
    notes_agent.add_note(note_input)
    st.success(f"Note added: {note_input}")

if st.button("View Notes"):
    all_notes = notes_agent.get_notes()
    st.write(all_notes if all_notes else "No notes yet.")

st.subheader("✅ Tasks")
task_input = st.text_input("Add a Task")
if st.button("Add Task"):
    task_agent.add_task(task_input)
    st.success(f"Task added: {task_input}")

if st.button("View Tasks"):
    tasks = task_agent.get_tasks()
    st.write(tasks if tasks else "No tasks yet.")
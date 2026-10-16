import streamlit as st

st.set_page_config(page_title="AI Email Reply Generator", page_icon="✉️")
st.title("✉️ Email Reply Generator")
st.write("Create a polite email reply from a message and a selected tone.")

message = st.text_area(
    "Paste the email or message you received",
    placeholder="Example: Please send your project report by Friday."
)
tone = st.selectbox("Choose reply tone", ["Professional", "Friendly", "Short and simple"])
purpose = st.text_input("What do you want to say? (optional)", placeholder="Example: I will send it tomorrow.")

def make_reply(original, selected_tone, purpose_text):
    if purpose_text.strip():
        main_point = purpose_text.strip()
    else:
        main_point = "Thank you for your message. I have received it and will get back to you soon."

    if selected_tone == "Professional":
        return f"Subject: Re: Your Message\n\nDear Sir/Madam,\n\nThank you for your email.\n\n{main_point}\n\nPlease let me know if any further information is required.\n\nBest regards,\n[Your Name]"
    if selected_tone == "Friendly":
        return f"Hi,\n\nThanks for reaching out!\n\n{main_point}\n\nThanks again,\n[Your Name]"
    return f"Hello,\n\nThank you for the message. {main_point}\n\nRegards,\n[Your Name]"

if st.button("Generate reply", type="primary"):
    if not message.strip():
        st.warning("Please paste the message you received first.")
    else:
        st.subheader("Generated reply")
        st.text_area("You can edit and copy this reply", value=make_reply(message, tone, purpose), height=220)
        st.caption("Demo note: This is a template-based prototype and does not call a GPT API.")

st.divider()
st.caption("Wipro CPPE AI Engineering demo project")

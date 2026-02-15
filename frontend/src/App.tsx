import { useEffect, useState } from "react";
import type { Message } from "./types/message";
import { fetchMessages, createMessage } from "./services/messageService";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);

  const loadMessages = async () => {
    const data = await fetchMessages();
    setMessages(data);
  };

  useEffect(() => {
    loadMessages();
  }, []);

  const handleSubmit = async () => {
    if (!message.trim()) return;

    await createMessage({ text: message });
    setMessage("");
    loadMessages();
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Messages</h1>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message"
      />

      <button onClick={handleSubmit}>Send</button>

      <ul>
        {messages.map((m, i) => (
          <li key={i}>{m.text}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

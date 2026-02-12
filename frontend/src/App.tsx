import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState<string[]>([]);

  const fetchMessages = () => {
    fetch("http://localhost:8000/messages")
      .then((res) => res.json())
      .then((data) => setMessages(data.messages ?? []));
  };

  useEffect(() => {
    fetchMessages();
  }, []);

  const submitMessage = async () => {
    await fetch("http://localhost:8000/messages", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: message }),
    });

    setMessage("");
    fetchMessages();
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Messages</h1>

      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Type a message"
      />

      <button onClick={submitMessage}>Send</button>

       <ul>
      {messages?.map((m, i) => (
          <li key={i}>{m}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

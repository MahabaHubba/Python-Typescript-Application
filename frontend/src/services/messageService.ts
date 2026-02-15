import type { Message } from "../types/message";

// Create a variable to allocate the URL required for our calls.
const API_URL = "http://localhost:8000";

// Fetch messages use to reutrn a string array in which this interacted badly with the front end.
// data.messages return string[]
// Now it returns text:" "
export async function fetchMessages(): Promise<Message[]> {
  const res = await fetch(`${API_URL}/messages`);
  const data = await res.json();

  return (data.messages ?? []).map((m: any) => ({
    text: m.text,
  }));
}

// utilises the POST method to create message with stringifies the json.
export async function createMessage(message: Message): Promise<void> {
  await fetch(`${API_URL}/messages`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(message),
  });
}

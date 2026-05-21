import { useState } from "react"
import socket from "./websocket"

export default function VoiceAgent() {

  const [messages, setMessages] = useState<string[]>([])

  const sendMessage = () => {

    socket.send("Book appointment tomorrow")
  }

  socket.onmessage = (event) => {

    const data = JSON.parse(event.data)

    setMessages(prev => [...prev, data.response])
  }

  return (
    <div>
      <h1>Voice AI Agent</h1>

      <button onClick={sendMessage}>
        Send Voice Message
      </button>

      {
        messages.map((m, i) => (
          <p key={i}>{m}</p>
        ))
      }
    </div>
  )
}

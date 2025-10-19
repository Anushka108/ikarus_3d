import React, {useState} from 'react'

function ChatPage(){
  const [messages, setMessages] = useState([{from: 'bot', text: 'Hi! Tell me what kind of furniture you need.'}])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)

  async function send(){
    if(!input.trim()) return
    const userMsg = {from: 'user', text: input}
    setMessages(m => [...m, userMsg])
    setInput('')
    setLoading(true)
    try{
      // Backend expects GET /recommend?query=... and returns { query, recommendations: [...] }
      const url = `http://localhost:8000/recommend?query=${encodeURIComponent(userMsg.text)}`
      const res = await fetch(url, { method: 'GET' })
      const data = await res.json()

      // Map backend recommendation objects to a simple display string.
      const botText = (data.recommendations || []).map(r => {
        const title = r.title || r.uniq_id || 'Unknown'
        const desc = r.description || ''
        return `${title} — ${desc}`
      }).join('\n\n')

      setMessages(m => [...m, {from: 'bot', text: botText || 'No recommendations found.'}])
    }catch(e){
      console.error('recommend error', e)
      setMessages(m => [...m, {from: 'bot', text: 'Sorry, something went wrong.'}])
    }finally{ setLoading(false) }
  }

  return (
    <div>
      <h3>Recommendation Chat</h3>
      <div className="card mb-3" style={{minHeight: 300}}>
        <div className="card-body" style={{whiteSpace: 'pre-wrap'}}>
          {messages.map((m,i)=> (
            <div key={i} className={m.from==='user'? 'text-end mb-2':'text-start mb-2'}>
              <span className={m.from==='user'? 'badge bg-primary':'badge bg-light text-dark'}>{m.from}</span>
              <div className="mt-1">{m.text}</div>
            </div>
          ))}
        </div>
      </div>

      <div className="input-group">
        <input className="form-control" value={input} onChange={e=>setInput(e.target.value)} placeholder="Ask for a chair, sofa, style..." />
        <button className="btn btn-primary" onClick={send} disabled={loading}>{loading? 'Loading...':'Send'}</button>
      </div>
    </div>
  )
}

export default ChatPage

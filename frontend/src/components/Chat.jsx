import React, { useState, useRef, useEffect } from 'react';
import '../styles/Chat.css';

const Chat = () => {
  const [messages, setMessages] = useState([
    { id: 1, text: 'Welcome to VAU-CS Academic Advisor! How can I help you today?', sender: 'bot' }
  ]);
  const [inputValue, setInputValue] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!inputValue.trim()) return;

    // Add user message
    const userMessage = {
      id: messages.length + 1,
      text: inputValue,
      sender: 'user'
    };

    setMessages(prev => [...prev, userMessage]);
    setInputValue('');
    setIsTyping(true);

    // Simulate bot response after a delay
    setTimeout(() => {
      const botResponse = {
        id: messages.length + 2,
        text: `I received: "${inputValue}"\n(This is a dummy response. The actual API will be integrated later.)`,
        sender: 'bot'
      };
      setMessages(prev => [...prev, botResponse]);
      setIsTyping(false);
    }, 1000);
  };

  const handleClearChat = () => {
    if (window.confirm('Are you sure you want to clear the chat history?')) {
      setMessages([
        { id: 1, text: 'Welcome to VAU-CS Academic Advisor! How can I help you today?', sender: 'bot' }
      ]);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <h1>VAU-CS Academic Advisor</h1>
      </div>
      
      <div className="messages-container">
        {messages.map((message) => (
          <div key={message.id} className={`message ${message.sender}`}>
            <div className="message-content">
              {message.text.split('\n').map((line, i) => (
                <p key={i}>{line}</p>
              ))}
            </div>
          </div>
        ))}
        {isTyping && (
          <div className="message bot">
            <div className="typing-indicator">
              <span></span>
              <span></span>
              <span></span>
            </div>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form onSubmit={handleSubmit} className="input-container">
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Type your message here..."
          aria-label="Type your message"
        />
        <div className="button-group">
          <button type="submit" className="send-button" disabled={!inputValue.trim()}>
            Send
          </button>
          <button type="button" className="clear-button" onClick={handleClearChat}>
            Clear
          </button>
        </div>
      </form>
    </div>
  );
};

export default Chat;

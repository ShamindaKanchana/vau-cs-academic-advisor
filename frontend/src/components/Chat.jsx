import React, { useState, useRef, useEffect } from 'react';
import ReactMarkdown from 'react-markdown';
import '../styles/Chat.css';

// Message component to handle both user and bot messages
const Message = ({ text, sender }) => {
  return (
    <div className={`message ${sender}`}>
      <div className="message-avatar">
        {sender === 'user' ? (
          <span className="material-icons">person</span>
        ) : (
          <span className="material-icons">smart_toy</span>
        )}
      </div>
      <div className="message-content">
        {sender === 'bot' ? (
          <ReactMarkdown>{text}</ReactMarkdown>
        ) : (
          <p>{text}</p>
        )}
      </div>
    </div>
  );
};

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

  const handleSubmit = async (e) => {
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

    try {
      const response = await fetch('http://localhost:5000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: inputValue })
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      
      if (data.status === 'success') {
        const botResponse = {
          id: messages.length + 2,
          text: data.response,
          sender: 'bot'
        };
        setMessages(prev => [...prev, botResponse]);
      } else {
        throw new Error(data.message || 'Failed to get a valid response from the server');
      }
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        id: messages.length + 2,
        text: `Sorry, I encountered an error: ${error.message}`,
        sender: 'bot',
        isError: true
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsTyping(false);
    }
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
          <Message key={message.id} text={message.text} sender={message.sender} />
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
            <span className="material-icons">send</span>
           
          </button>
          <button type="button" className="clear-button" onClick={handleClearChat}>
            <span className="material-icons">delete</span>
           
          </button>
        </div>
      </form>
    </div>
  );
};

export default Chat;

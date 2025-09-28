import React from 'react';
import './App.css';
import './styles/Chat.css';
import Chat from './components/Chat';

function App() {
  return (
    <div className="app">
      <Chat />
      <footer className="app-footer">
        <p>© {new Date().getFullYear()} Developed by <strong>Shaminda Kanchana</strong> for contribution to CS students</p>
      </footer>
    </div>
  );
}

export default App;

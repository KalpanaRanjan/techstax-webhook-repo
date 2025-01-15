import React, { useEffect, useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from 'axios';

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      const response = await axios.get('http://localhost:5000/webhook/gitaction');
      console.log(response.data.events);
      setEvents(response.data.events);
    };

    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
      <div className="container d-flex justify-content-center align-items-center">
        <div w-100>
          <h2 className="text-center mb-4">GitHub Repository Events</h2>
            <table className='table'>
              <tr>
                  <ul>
                  {events.map(event => (
                    <li key={event._id}>
                      {event.action === 'PUSH' &&
                        <span><i className='fw-bold'>{event.author}</i> pushed to <i className='fw-bold'>{event.from_branch}</i> on <i className='fw-bold'>{event.timestamp}</i></span>}
                      {event.action === 'PULL_REQUEST' &&
                        <span><i className='fw-bold'>{event.author}</i> submitted a pull request from <i className='fw-bold'>{event.from_branch}</i> to <i className='fw-bold'>{event.to_branch}</i> on <i className='fw-bold'>{event.timestamp}</i></span>}
                      {event.action === 'MERGE' &&
                        <span><i className='fw-bold'>{event.author}</i> merged branch <i className='fw-bold'>{event.from_branch}</i> to <i className='fw-bold'>{event.to_branch}</i> on <i className='fw-bold'>{event.timestamp}</i></span>}
                    </li>
                  ))}
                 </ul>
              </tr>
            </table>
        </div>
      </div>
    </>
  );
}

export default App;
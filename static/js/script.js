import { Calendar } from '@fullcalendar/core';
import dayGridPlugin from '@fullcalendar/daygrid';
import timeGridPlugin from '@fullcalendar/timegrid';
import listPlugin from '@fullcalendar/list';

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
  
    var calendar = new Calendar(calendarEl, {
      plugins: [ dayGridPlugin, timeGridPlugin, listPlugin ],
      initialView: 'dayGridMonth', // Initial view when calendar loads
      events: [
        // Your events data will go here
        {
          title: 'Event 1',
          start: '2024-07-01',
          end: '2024-07-02'
        },
        {
          title: 'Event 2',
          start: '2024-07-05T10:00:00',
          end: '2024-07-05T12:00:00'
        }
        // Add more events as needed
      ]
    });
  
    calendar.render(); // Renders the calendar
  });
  
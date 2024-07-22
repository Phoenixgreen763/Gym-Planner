document.addEventListener('DOMContentLoaded', function() {
    // Update the copyright year
    var currentYear = new Date().getFullYear();
    document.getElementById('year').textContent = currentYear;

    // Initialize FullCalendar
    var calendarEl = document.getElementById('calendar');

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        events: '/api/events', // Endpoint to fetch events
        editable: true, // Allow editing events
        selectable: true, // Allow selecting time slots to create events
        eventClick: function(info) {
            // Handle event click (e.g., edit or delete event)
            console.log(info.event);
        },
        eventDrop: function(info) {
            // Handle event drag and drop to update event on backend
            console.log(info.event);
        },
        eventResize: function(info) {
            // Handle event resize to update event on backend
            console.log(info.event);
        }
    });

    calendar.render();
});

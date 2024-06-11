import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

const displayMessage = (message, time) => {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    client.publish('holberton school channel', message);
  }, time);
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

displayMessage('Holberton Student #1 starts course', 100);
displayMessage('Holberton Student #2 starts course', 200);
displayMessage('KILL_SERVER', 300);
displayMessage('Holberton Student #3 starts course', 400);
